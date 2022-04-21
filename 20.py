def faktorielle(n):
    e = 1
    for i in range(1, n + 1):
        e *= i
    return e
gesamt = 0
zahl = str(faktorielle(100))
for i in str(zahl):
    gesamt += int(i)
print(gesamt)