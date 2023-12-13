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

pu()
goto(-200, 200)
pd()
ht()
speed(0)
begin_fill()
color("blue")
for i in range(3):
    kurve(5, 500)
    right(120)
end_fill()
done()
