# Christian Patzl 1BHIF
# Buchstaben Zählen

def zaehle_buchstaben(s: str) -> dict:
    """Zaehlt die Buchstaben in einem String

    Args:
        s (str): Der String

    Returns:
        dict: Dictionary mit Anzahl der Buchstaben
    """
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d

a = input("Eingabe: ")
print(zaehle_buchstaben(a))
