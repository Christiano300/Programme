"""
fix_jar_manifest.py
-------------------
Opens a .jar file, reads META-INF/MANIFEST.MF, recalculates any
incorrect file-entry digests (SHA-1, SHA-256, SHA-512, MD5, …) and
writes the corrected manifest back into the archive.

Usage:
    python fix_jar_manifest.py <path/to/file.jar>
"""

import base64
import hashlib
import os
import re
import shutil
import sys
import tempfile
import zipfile


# ---------------------------------------------------------------------------
# Manifest parsing / serialising
# ---------------------------------------------------------------------------

def _unfold(text: str) -> str:
    """Remove manifest line-continuation sequences (CRLF / LF followed by a space)."""
    return re.sub(r'\r?\n ', '', text)


def parse_manifest(text: str) -> list[tuple[dict[str, str], list[str]]]:
    """
    Parse a MANIFEST.MF into a list of sections.
    Each section is a tuple (attributes_dict, ordered_key_list).
    The first section is the main section (no 'Name' attribute).
    """
    sections: list[tuple[dict[str, str], list[str]]] = []
    attrs: dict[str, str] = {}
    order: list[str] = []

    for raw_line in _unfold(text).splitlines():
        if raw_line == '':
            if attrs:
                sections.append((attrs, order))
                attrs, order = {}, []
        elif ': ' in raw_line:
            key, _, value = raw_line.partition(': ')
            attrs[key] = value
            order.append(key)

    if attrs:
        sections.append((attrs, order))

    return sections


def _fold_line(line: str) -> str:
    """
    Encode a single 'Key: value' line with the JAR manifest 72-byte folding rule.
    Returns the folded text including CRLF line endings.
    """
    raw = line.encode('utf-8')
    if len(raw) <= 72:
        return line + '\r\n'

    chunks: list[bytes] = [raw[:72]]
    raw = raw[72:]
    while raw:
        chunks.append(raw[:71])
        raw = raw[71:]

    return '\r\n '.join(c.decode('utf-8') for c in chunks) + '\r\n'


def serialise_manifest(sections: list[tuple[dict[str, str], list[str]]]) -> bytes:
    """Reconstruct manifest bytes from parsed sections."""
    parts: list[str] = []
    for attrs, order in sections:
        for key in order:
            parts.append(_fold_line(f'{key}: {attrs[key]}'))
        parts.append('\r\n')
    return ''.join(parts).encode('utf-8')


# ---------------------------------------------------------------------------
# Digest helpers
# ---------------------------------------------------------------------------

# Map manifest attribute name → hashlib name
_ALGO_MAP: dict[str, str] = {
    'sha1':   'sha1',
    'sha256': 'sha256',
    'sha384': 'sha384',
    'sha512': 'sha512',
    'md5':    'md5',
}


def _manifest_key_to_algo(key: str) -> str | None:
    """'SHA-256-Digest' → 'sha256', 'SHA1-Digest' → 'sha1', …"""
    norm = key.removesuffix('-Digest').replace('-', '').lower()
    return _ALGO_MAP.get(norm)


def _digest_b64(data: bytes, algo: str) -> str:
    h = hashlib.new(algo)
    h.update(data)
    return base64.b64encode(h.digest()).decode('ascii')


# ---------------------------------------------------------------------------
# Main logic
# ---------------------------------------------------------------------------

def fix_jar_manifest(jar_path: str) -> None:
    print(f"Processing: {jar_path}")

    # ---- read manifest -------------------------------------------------------
    with zipfile.ZipFile(jar_path, 'r') as zf:
        names_in_jar = set(zf.namelist())
        if 'META-INF/MANIFEST.MF' not in names_in_jar:
            sys.exit("ERROR: No META-INF/MANIFEST.MF found in the JAR.")
        manifest_text = zf.read('META-INF/MANIFEST.MF').decode('utf-8')

    sections = parse_manifest(manifest_text)
    if not sections:
        sys.exit("ERROR: Manifest is empty or could not be parsed.")

    print(f"  Sections found: {len(sections)}  "
          f"(1 main + {len(sections) - 1} file entries)")

    # ---- check / fix digests -------------------------------------------------
    fixed = 0
    skipped = 0

    with zipfile.ZipFile(jar_path, 'r') as zf:
        for attrs, order in sections[1:]:          # skip main section
            name = attrs.get('Name')
            if not name:
                continue

            if name not in names_in_jar:
                print(f"  WARN  '{name}' not present in JAR – skipping")
                skipped += 1
                continue

            file_data = zf.read(name)

            for key in [k for k in order if k.endswith('-Digest')]:
                algo = _manifest_key_to_algo(key)
                if algo is None:
                    print(f"  WARN  Unknown algorithm for '{key}' in '{name}' – skipping")
                    continue

                correct = _digest_b64(file_data, algo)
                if attrs[key] != correct:
                    print(f"  FIX   {key} for {name}")
                    print(f"          old: {attrs[key]}")
                    print(f"          new: {correct}")
                    attrs[key] = correct
                    fixed += 1

    print(f"\n  Digests fixed : {fixed}")
    print(f"  Entries skipped: {skipped}")

    if fixed == 0:
        print("  All digests are already correct – JAR not modified.")
        return

    # ---- write fixed manifest back into a new archive -----------------------
    new_manifest_bytes = serialise_manifest(sections)

    jar_dir = os.path.dirname(os.path.abspath(jar_path))
    fd, tmp_path = tempfile.mkstemp(dir=jar_dir, suffix='.jar')
    os.close(fd)

    try:
        with zipfile.ZipFile(jar_path, 'r') as zin, \
             zipfile.ZipFile(tmp_path, 'w') as zout:

            for info in zin.infolist():
                if info.filename == 'META-INF/MANIFEST.MF':
                    # Preserve the ZipInfo metadata but replace content
                    info.compress_type = zipfile.ZIP_DEFLATED
                    zout.writestr(info, new_manifest_bytes)
                else:
                    # Preserve compression type of every other entry
                    zout.writestr(info, zin.read(info.filename),
                                  compress_type=info.compress_type)

        shutil.move(tmp_path, jar_path)
        print(f"\n  Saved: {jar_path}")

    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python fix_jar_manifest.py <file.jar>")
        sys.exit(1)

    path = sys.argv[1]
    if not os.path.isfile(path):
        sys.exit(f"ERROR: File not found: {path}")
    if not path.lower().endswith('.jar'):
        print(f"WARNING: '{path}' does not end with .jar – proceeding anyway.")

    fix_jar_manifest(path)
