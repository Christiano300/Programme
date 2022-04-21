def ist_schaltjahr(jahr):
    if jahr % 400 == 0 or (jahr % 4 == 0 and jahr % 100 != 0):
        return True
    else:
        return False

def wochentag(tag, jahr):
    a = jahr - 1
    w = (a + a // 4 - a // 100 + a // 400 + tag) % 7
    return w

monatstage = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
schaltjahrstage = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]

gesamt = 0

for jahr in range(1901, 2001):
    for monat in range(12):
        tag = 1
        if ist_schaltjahr(jahr):
            for i in range(monat):
                tag += schaltjahrstage[i + 1]
        else:
            for i in range(monat):
                tag += monatstage[i + 1]

        if wochentag(tag, jahr) == 0:
            gesamt += 1
print(gesamt)