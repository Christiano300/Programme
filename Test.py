from turtle import *
from random import randint, uniform
speed(0)
ht()
zahl = 90.1
color([uniform(0, 1) for i in range(3)], [uniform(0, 1) for i in range(3)])
begin_fill()
while True:
    forward(200)
    left(zahl)
    if abs(pos()) < .5:
        break
end_fill()
print(zahl)
done()
