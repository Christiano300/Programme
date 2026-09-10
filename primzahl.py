from math import sqrt


def prim_normal_for(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prim_normal_while(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def prim_besser(n):
    if n % 2 == 0:
        return False
    if (modsix := n % 6) != 1 and modsix != 5:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(100, 1000):
    if prim_besser(i) and all(prim_besser(int(k)) for k in str(i)):
        s = str(i)
        if prim_besser(int(s[:2])) and prim_besser(int(s[1:])):
            print(i)