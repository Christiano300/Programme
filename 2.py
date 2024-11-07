from functools import reduce


def faktoren(n):
    faktoren = []
    i = 2
    while i * i <= n:
        if n % i == 0:
            faktoren.append(i)
            n //= i
        else:
            i += 1
    faktoren.append(n)
    return faktoren

fkt = []
for i in range(1, 21):
    fakt = faktoren(i)
    for j in fkt:
        try:
            fakt.remove(j)
        except:
            pass
    fkt.extend(fakt)

print(reduce(lambda x, y: x * y, fkt))