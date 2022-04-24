while True:
    a = int(input("Zahl: "))
    erg = 1
    for i in range(2, a + 1):
        erg *= i
    with open("files/factorial.txt", "w") as f:
        print(erg, file=f)