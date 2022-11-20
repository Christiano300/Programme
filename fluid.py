from random import randint
from time import sleep
import pyautogui as pgui
distance = 200
sleep(5)
pgui.mouseDown()
for _ in range(20):
    x, y = pgui.position()
    pgui.move(75, randint(-50,50))
pgui.mouseUp()