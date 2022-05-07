# Christian Patzl 1BHIF
# Überprüfen ob Klammern gültig sind

def klammern_gueltig(s: str) -> bool:
    klammern = {"(": ")", "[": "]", "{": "}"}
    liste = []
    for i in s:
        if i in klammern:
            liste.append(i)
        elif i in klammern.values():
            if len(liste) and i == klammern[liste[-1]]:
                del liste[-1]
            else:
                return False
    return not bool(len(liste))

a = input("Klammern: ")
print("korrekt" if klammern_gueltig(a) else "falsch")