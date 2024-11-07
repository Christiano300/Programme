import pyautogui
import keyboard
import time

mx1 = 0
my1 = 0
mx2 = 0
my2 = 0
mx3 = 0
my3 = 0

while True:
    if keyboard.is_pressed('f10'):
        mx1, my1 = pyautogui.position()
        print("Pos 1 set")
        time.sleep(1)
        break

while True:
    if keyboard.is_pressed('f9'):
        mx2, my2 = pyautogui.position()
        print("Pos 2 set")
        time.sleep(1)
        break


while True:
    while True:
        if keyboard.is_pressed('f10'):
            mx3, my3 = pyautogui.position()
            pyautogui.click(mx1, my1)
            time.sleep(0.1)
            pyautogui.moveTo(mx3, my3)
            break

        if keyboard.is_pressed('f9'):
            mx3, my3 = pyautogui.position()
            pyautogui.click(mx2, my2)
            time.sleep(0.1)
            pyautogui.moveTo(mx3, my3)
            break
        
        

