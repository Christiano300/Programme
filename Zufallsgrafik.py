from random import choice, randint
from turtle import *

colors = ["red", "green", "gold", "blue", "lime", "yellow", "salmon", "lime", "coral", "peru", "olive", "springgreen", "darkred",
          "deepskyblue", "cyan", "crimson", "magenta", "mediumblue", "dodgerblue", "orchid", "mediumspringgreen", "aqua", "aquamarine"]


def dreieck(l, w, x, y, c1, c2, dr):
    pu()
    width(w)
    color(c1, c2)
    setpos(x, y)
    seth(dr)
    pd()
    begin_fill()
    for i in range(3):
        fd(l)
        left(120)
    end_fill()


def viereck(l, w, x, y, c1, c2, dr):
    pu()
    width(w)
    color(c1, c2)
    setpos(x, y)
    seth(dr)
    pd()
    begin_fill()
    for i in range(4):
        fd(l)
        left(90)
    end_fill()


def kreis(r, w, x, y, c1, c2, dr):
    pu()
    width(w)
    color(c1, c2)
    setpos(x, y)
    seth(dr)
    pd()
    begin_fill()
    circle(r)
    end_fill()


speed(0)
ht()
for i in range(300):
    form = randint(1, 3)
    if form == 1:
        dreieck(randint(5, 100), randint(1, 10), randint(-300, 300),
                randint(-300, 300), choice(colors), choice(colors), randint(0, 360))
    elif form == 2:
        viereck(randint(5, 100), randint(1, 10), randint(-300, 300),
                randint(-300, 300), choice(colors), choice(colors), randint(0, 360))
    else:
        kreis(randint(2, 50), randint(1, 10), randint(-300, 300),
              randint(-300, 300), choice(colors), choice(colors), randint(0, 360))
done()
