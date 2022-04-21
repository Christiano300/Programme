import pyautogui
import keyboard
import time

mousex1 = 0
mousey1 = 0
mousex2 = 0
mousey2 = 0

while True:
    if keyboard.is_pressed('anwendung'):
        mousex1, mousey1 = pyautogui.position()
        print("Pos 1 set")
        time.sleep(1)
        break

while True:    
    if keyboard.is_pressed('anwendung'):
        mousex2, mousey2 = pyautogui.position()
        print("Pos 2 set")
        time.sleep(1)
        break

while True:
    while True:
        if keyboard.is_pressed('anwendung'):
            keyboard.press('umschalt')
            print("hold_shift")
            pyautogui.click(mousex1, mousey1)
            print("click 1")
            time.sleep(0.6)
            print("sleep")
            pyautogui.click(mousex2, mousey2)
            print("click 2")
            keyboard.release('umschalt')
            print("release_shift")
            time.sleep(0.5)
            break
        
        

