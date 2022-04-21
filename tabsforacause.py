import keyboard
import time
#start
while True:
    while True:
        if keyboard.is_pressed('rollen-feststell'):
            break
    time.sleep(0.5)
    while True:
        if keyboard.is_pressed('rollen-feststell'):
            break
        keyboard.send('f5')
        time.sleep(2.15)
        # time.sleep(3.15)
    time.sleep(5)
