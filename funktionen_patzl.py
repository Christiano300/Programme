# Christian Patzl 1BHIF
# Funktionsdefinitionen

def inputInt(text: str) -> int:
    """Liest einen Ganzzahl vom Benutzer ein

    Args:
        text (str): Aufforderungstext

    Returns:
        int: Eingegebene Zahl
    """
    while True:
        try:
            z = input(text)
            z = int(z)
            return z
        except ValueError:
            print(f"{z} ist keine Ganzzahl")

def inputFloat(text: str) -> int:
    """Liest einen Zahl vom Benutzer ein

    Args:
        text (str): Aufforderungstext

    Returns:
        int: Eingegebene Zahl
    """
    while True:
        try:
            z = input(text)
            z = float(z)
            return z
        except ValueError:
            print(f"{z} ist keine Zahl")
