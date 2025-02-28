from turtle import *
from random import *

reset()
hideturtle()
color('green')
speed(0)
# n = int(input("Wiederholungen: "))
# l = int(input("Länge: "))
n = 30
l = 50
def grafik(n,l):
    if n >= 1:
        fd(l)
        if random() >= .3:
            left(60)
        else:
            right(60)
        grafik(n-1,l * 0.9)

while True:
    grafik(n,l)
    pu()
    goto(0,0)
    pd()
done()
