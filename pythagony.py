# if, elif, for, while, return

from math import sqrt


a = int(input("Zahl 1: "))
b = int(input("Zahl 2: "))
# if a == b:
#     print("Zahl 1 = Zahl 2")
# elif a > b:
#     print("Zahl 2 > Zahl 1")
# else:
#     print("Zahl 1 < Zahl 2")

try:
    1 / (a - b)
except ZeroDivisionError:
    print("Zahl 1 == Zahl 2")
else:
    try:
        sqrt(a - b)
    except ValueError:
        print("Zahl 1 < Zahl 2")
    else:
        print("Zahl 1 > Zahl 2")