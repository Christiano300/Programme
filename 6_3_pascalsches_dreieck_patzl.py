# Christian Patzl 1BHIF
# Pascalsches Dreieck bis zu Benutzereingabe
from funktionen_patzl import inputInt


def print_pasc_line(zeile: list):
    """Gibt eine Zeile des Pascalschen Dreiecks aus

    Args:
        koeffizienten (list): die Koeffizienten in der Zeile
    """
    out = []
    l = len(zeile) - 1
    if l == 0:
        print(1)
        return
    elif l == 1:
        print("a + b")
        return
    for i, k in enumerate(zeile):
        if k == 1:
            out.append(f"{f'a^{l}' if i == 0 else f'b^{l}'}")
        else:
            out.append(
                f"{k}a{f'^{l-i} ' if l-i != 1 else ''}b{f'^{i}' if i != 1 else ''}")
    print(" + ".join(out))


dreieck = [0]
n = inputInt('(a+b)^n bis n = ')

for i in range(n):
    neu = []
    print_pasc_line(dreieck)
    for j in range(len(dreieck) + 1):
        if j in range(1, len(dreieck)):
            neu.append(dreieck[j - 1] + dreieck[j])
        else:
            neu.append(1)
    dreieck = neu[:]

print_pasc_line(dreieck)
