def get_int(msg):
    while True:
        try:
            zahl = int(input(msg))
            return zahl
        except ValueError:
            print("Keine Ganzzahl")
def ziff_in_zahl(ziffer, zahl):
    return str(zahl).count(str(ziffer))

# while True: ziffer = get_int("Ziffer: "); print("Darf nur Ziffer sein") if len(str(ziffer)) != 1
while True:
    print("Muss ziffer sein") if len(str(get_int("Ziffer: "))) != 1 else exec("break")


print(str(get_int("Zahl: ")).count(str(ziffer)))