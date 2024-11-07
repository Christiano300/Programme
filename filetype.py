import keyboard
import time

with open("files/type.txt") as f:
    text = f.read()


while True:
    if keyboard.is_pressed("rollen-feststell"):
        break
    time.sleep(.1)

keyboard.write(text, .01)