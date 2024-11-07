# Christian Patzl 1BHIF
# Den ersten Buchstaben in einem String überall sonst zu einem $ machen


def erstes_zu_dollar(s: str) -> str:
    return s[0] + s[1:].replace(s[0].lower(), '$').replace(s[0].upper(), '$')


eingabe = input("Eingabe: ")
print(erstes_zu_dollar(eingabe))