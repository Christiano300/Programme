from turtle import *
speed(0)
color('red', 'yellow')
while True:
    forward(400)
    left(180.2)
    if abs(pos()) < .5:
        break
exitonclick()
