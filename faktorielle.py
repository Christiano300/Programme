while True:
    a = int(input("Zahl: "))
    erg = 1
    for i in range(2, a + 1):
        erg *= i
    print(erg)