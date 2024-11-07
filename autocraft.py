import time

import keyboard
import pyautogui

while True:
    if keyboard.is_pressed('anwendung'):
        mousex1, mousey1 = pyautogui.position()
        print("Pos 1 set")
        time.sleep(1)
        break


while True:
    if keyboard.is_pressed('anwendung'):
        keyboard.press('shift')
        time.sleep(.3)
        for i in range(35):
            pyautogui.click()
            time.sleep(.09)
        keyboard.release('shift')
        keyboard.press("e")
        time.sleep(.2)
        keyboard.release('e')
        time.sleep(.5)
        pyautogui.moveTo(mousex1, mousey1)
        time.sleep(.1)
        keyboard.press("k")
        time.sleep(.2)
        keyboard.release('k')

        