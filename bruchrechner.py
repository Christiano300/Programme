#primfaktorzerlegung
def faktoren(n):
    faktoren = []
    n = abs(n)
    i = 2
    while i * i <= n:
        if  n % i == 0:
            faktoren.append(i)
            n //= i
        else: i += 1
    faktoren.append(n)
    return faktoren

#kgv
def kgv(zahl_1, zahl_2):
    faktoren_1 = faktoren(zahl_1)
    faktoren_2 = faktoren(zahl_2)
    kgv = 1

    for i in faktoren_1:
        if i in faktoren_2:
            faktoren_2.remove(i)
        kgv *= i

    for i in faktoren_2:
        kgv *= i
    return kgv

#ggt
def ggt(zahl_1, zahl_2):
    faktoren_1 = faktoren(zahl_1)
    faktoren_2 = faktoren(zahl_2)
    ggt = 1

    for i in faktoren_1:
        if i in faktoren_2:
            ggt *= i
            faktoren_2.remove(i)
    return ggt

#Bruch schön ausgeben
def print_results(zaehler, nenner, positiv):
    if positiv % 2 == 0:
        #positiv
        minus_zahl = ""
        minus_strich = ""
        
    else:
        minus_zahl = "  "
        minus_strich = "- "
        #negativ

    stellen_zaehler = len(str(zaehler))
    stellen_nenner = len(str(nenner))

    if stellen_zaehler >= stellen_nenner:
        print(f"{minus_zahl}{zaehler:^{stellen_zaehler + 2}d}")
        print(minus_strich + "-" * (stellen_zaehler + 2))
        print(f"{minus_zahl}{nenner:^{stellen_zaehler + 2}d}")

    else:
        print(f"{minus_zahl}{zaehler:^{stellen_nenner + 2}d}")
        print(minus_strich + "-" * (stellen_nenner + 2))
        print(f"{minus_zahl}{nenner:^{stellen_nenner + 2}d}")

#eingabe
try:
    zaehler_a = int(input("Zaehler A: "))

    nenner_a = int(input("Nenner A: "))

    operator = input("Operator: ")
    if operator not in ('+', '-', '*', '/', ':', 'k'):
        raise ValueError
    elif operator == 'k':
        raise IndexError

    zaehler_b = int(input("Zahler B: "))

    nenner_b = int(input("Nenner B: "))

except ValueError:
    print("Invalid input")

except IndexError:
    pass

#berechnung
else:
    if operator == '+':
        nenner_erg = kgv(nenner_a, nenner_b)
        zaehler_erg = zaehler_a * (nenner_erg // nenner_a) + zaehler_b * (nenner_erg // nenner_b)

    elif operator == "-":
        nenner_erg = kgv(nenner_a, nenner_b)
        zaehler_erg = zaehler_a * (nenner_erg // nenner_a) - zaehler_b * (nenner_erg // nenner_b)

    elif operator == "*":
        zaehler_erg = zaehler_a * zaehler_b
        nenner_erg = nenner_a * nenner_b
    
    elif operator == 'k':
        zaehler_erg = zaehler_a
        nenner_erg = nenner_a

    else:
        zaehler_erg = zaehler_a * nenner_b
        nenner_erg = nenner_a * zaehler_b
    
    #kürzen
    kuerzfaktor = ggt(zaehler_erg, nenner_erg)
    zaehler_erg //= kuerzfaktor
    nenner_erg //= kuerzfaktor
    positiv = 0
    if zaehler_erg < 0:
        positiv += 1
    if nenner_erg < 0:
        positiv += 1

    print_results(abs(zaehler_erg), abs(nenner_erg), positiv)