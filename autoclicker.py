import pyautogui
import keyboard
import time

mousex1 = 0
mousey1 = 0

doing = False

while True:
    if keyboard.is_pressed("feststell"):
        mousex1, mousey1 = pyautogui.position()
        print("Pos 1 set")
        time.sleep(1)
        break

while True:
    if keyboard.is_pressed("feststell"):
        doing = not doing
        if doing:
            print("Auto clicker started")
        else:
            print("Auto clicker stopped")
        time.sleep(1)

    if doing:
        pyautogui.click(mousex1, mousey1)
        
        

