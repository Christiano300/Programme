from turtle import *

def kurve(n, l):
    if n:
        kurve(n - 1, l / 3)
        left(60)
        kurve(n - 1, l / 3)
        right(120)
        kurve(n - 1, l / 3)
        left(60)
        kurve(n - 1, l / 3)
    else:
        fd(l)

speed(0)
tracer(0)

pu()
goto(-250, 130)
pd()
ht()
# begin_fill()
color("blue")
for i in range(3):
    kurve(4, 500)
    right(120)
# end_fill()
done()
