from time import sleep
import keyboard

def transform():
    sleep(1)
    keyboard.send('del') # delete [
    for i in 'abcd':
        keyboard.send('del') # delete [
        keyboard.write(f"vec3 {i} = vec3(")
        
        for i in range(2):
            keyboard.press('ctrl')
            for i in range(3):
                keyboard.send('right')
            keyboard.release('ctrl')
            keyboard.write(',')
            keyboard.send('right')

        keyboard.press('ctrl')
        for i in range(3):
            keyboard.send('right')
        keyboard.release('ctrl')
        keyboard.send('del') # delete ]
        keyboard.send('del') # delete space
        
        keyboard.write(');\n')
        

keyboard.add_hotkey('ctrl+shift+alt+1', transform)
keyboard.wait('esc')