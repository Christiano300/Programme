# Christian Patzl 1BHIF
# Primfaktorzerlegung mit Dictionaries
from funktionen_patzl import inputInt

def primfaktoren(n: int) -> dict:
    """Zerlegt eine Zahl in Primfaktoren

    Args:
        n (int): Die zu zerlegende Zahl

    Returns:
        dict: Dictionary mit Anzahl der Primfaktoren
    """
    d = {}
    i = 2
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            d[i] = d.get(i, 0) + 1
            n //= i
    d[i] = d.get(i, 0) + 1
    return d

zahl = inputInt("Zahl eingeben: ")
print(f"Primfaktoren: {primfaktoren(zahl)}")