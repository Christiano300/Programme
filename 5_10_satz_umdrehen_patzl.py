# Christian Patzl 1BHIF
# Satz einlesen und umdrehen

def satz_umdrehen(s: str) -> str:
    """Bekommt einen Satz und dreht ihn um

    Args:
        s (str): Übergebener Satz

    Returns:
        str: Umgedrehter Satz
    """
    se = ".!?"
    sz = ",;"
    if s[-1] not in se:
        return "Fehler"
    ende = s[-1]
    s = s[:-1]
    for i in s:
        if i in se:
            return "Fehler"
    l = s.split()
    zeichen = {}
    for i, wort in enumerate(l):
        if wort[-1] in sz:
            zeichen[i] = wort[-1]
            l[i] = wort[:-1]
    l = l[::-1]
    for i, x in zeichen.items():
        l[i] += x
    return " ".join(l) + ende

a = input("Satz: ")
print(satz_umdrehen(a))