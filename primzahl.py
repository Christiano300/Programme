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

while True:
    zahl = int(input("Zahl: "))
    print(f"normal_for: {prim_normal_for(zahl)}")
    print(f"normal_while: {prim_normal_while(zahl)}")
    print(f"besser: {prim_besser(zahl)}")