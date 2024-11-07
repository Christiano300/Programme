# Christian Patzl 1BHIF
# Hangman
import getpass


def buchstabe_einlesen(text: str) -> str:
    """Liest einen Buchstaben vom Benutzer ein

    Args:
        text (str): Aufforderungstext

    Returns:
        str: Eingegebener Buchstabe
    """
    while True:
        b = input(text)
        if len(b) == 1 and b.isalpha():
            return b


wort = getpass.getpass('Wort: ').upper()
getippt = []

while True:
    while True:
        tipp = buchstabe_einlesen("> ").upper()
        if tipp in getippt:
            print("Ungültig, schon getippt")
            continue
        getippt.append(tipp)
        break

    tipps = [i if i in getippt else "_" for i in wort]
    print(tipps_str := "".join(tipps))
    if tipps_str == wort:
        print("Richtig!")
        break
    else:
        print("Getippt:", end=' ')
        print(*getippt, sep=", ")
