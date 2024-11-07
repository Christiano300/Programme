# Christian Patzl 1BHIF
# Differenz zwischen zwei Zeiten berechnen


def zeitdiff(zeit1: list, zeit2: list) -> list:
    """Berechnet die Differenz zwischen zwei Zeiten

    Args:
        zeit1 (list): Erste Zeit
        zeit2 (list): Zweite Zeit

    Returns:
        list: Differenz zwischen den beiden Zeiten
    """
    s1 = zeit1[0] * 3600 + zeit1[1] * 60 + zeit1[2]
    s2 = zeit2[0] * 3600 + zeit2[1] * 60 + zeit2[2]
    s = s2 - s1
    m, s = divmod(s, 60)
    h, m = divmod(m, 60)
    return h, m, s

def ist_zeit_gueltig(z: list) -> bool:
    """Berechnet ob eine Zeit gültig ist

    Args:
        z (list): Zeit

    Returns:
        bool: Ob die Zeit gültig ist
    """
    return z[0] in range(24) and z[1] in range(60) and z[2] in range(60)

def zeit_eingeben(text: str) -> list:
    """Liest eine Zeit vom Benutzer ein

    Args:
        text (str): Die Eingabeaufforderung

    Returns:
        list: Die eingegebene Zeit
    """
    while True:
        eingabe = input(text)
        zeit = eingabe.split(":")
        if len(zeit) == 3 and "".join(zeit).isdecimal():
            zeit = [int(i) for i in zeit]
            if ist_zeit_gueltig(zeit):
                return zeit
        print("Ungültige Eingabe")

zeit1 = zeit_eingeben("Erste Zeit: ")
zeit2 = zeit_eingeben("Zweite Zeit: ")

print(f"Differenz: {':'.join([f'{i:02d}' for i in zeitdiff(zeit1, zeit2)])}")