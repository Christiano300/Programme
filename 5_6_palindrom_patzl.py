# Christian Patzl 1BHIF
# Überprüfen ob ein String ein Palindrom ist


def ist_palindrom(s: str) -> bool:
    """Überürüft ob ein String ein Palindrom ist

    Args:
        s (str): Der übergebene String

    Returns:
        bool: Ob der String ein Palindrom ist
    """
    return s == s[::-1]


eingabe = input("Eingabe: ")
print("Palindrom" if ist_palindrom(eingabe) else "kein Palindrom")