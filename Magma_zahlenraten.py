import random
import time

def differenz(a, b):
    if a < b:
        return b - a
    else:
        return a - b

print("Zahl wurde ausgewählt.")

while True:
    zahl = random.randint(0, 50)
    while True:
        eingabe = int(input("Zahl eingeben: "))
        dif = differenz(eingabe, zahl)
        if dif == 0:
            print("Magma!\nNeue Zahl wurde ausgewählt.")
            break
        elif dif == 1:
            print("Lava")
        elif dif <= 5:
            print("Vulkan")
        elif dif <= 15:
            print("Feuer")
        elif dif <= 30:
            print("Wasser")
        else:
            print("Antarktis")
