# Christian Patzl 1BHIF
# IBAN überprüfen
from string import ascii_uppercase

def iban_gueltig(iban: str) -> bool:
    iban = iban.replace(' ', '')
    if len(iban) == 20 and iban[2:].isdecimal():
        iban = list(iban)
        if all(i in ascii_uppercase for i in iban[:2]):
            for i in range(2):
                iban[i] = str(ascii_uppercase.find(iban[i]) + 10)
            iban = iban[4:] + iban[:4]
            return int("".join(iban)) % 97 == 1
    return False

a = input("IBAN: ")
print("gültig" if iban_gueltig(a) else "ungültig")