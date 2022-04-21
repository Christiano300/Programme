from turtle import *
speed(0)
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(165)
    if abs(pos()) < 1:
        break
end_fill()
exitonclick()
