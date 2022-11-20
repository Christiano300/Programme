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


zahl = 1536
print("beginne primfaktorzerlegung...")
faktorliste = faktoren(zahl)
print("primfaktorzerlegung beendet\nstarte druckvorgang")

print("*".join([str(i) for i in faktorliste]))

print("programm beendet")
