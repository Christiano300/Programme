import time
import keyboard
time.sleep(5)
for i in range(100):
    keyboard.send('t')
    time.sleep(0.1)
    keyboard.write("/summon armor_stand")
    keyboard.send('enter')
