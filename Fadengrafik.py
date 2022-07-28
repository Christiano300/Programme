from turtle import *
from random import *

reset()
hideturtle()
color('green')
speed(0)
# n = int(input("Wiederholungen: "))
# l = int(input("Länge: "))
n = 100
l = 50
def grafik(n,l):
    if n >= 1:
        fd(l)
        if random() >= .3:
            left(30)
        else:
            right(30)
        grafik(n-1,l * 0.9)
grafik(n,l)
done()
