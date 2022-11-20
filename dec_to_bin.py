while True:
    try:
        n = float(input("Zahl: "))
        break
    except ValueError:
        print("Keine Zahl: ")

ganz = bin(int(n))[2:]
komma = ""
n %= 1
i = 1
while n != 0 and i < 200:
    if (aktuell := 1 / 2 ** i) <= n:
        komma += "1"
        n -= aktuell
    else:
        komma += "0"
    i += 1
print(f"{ganz}.{komma}")