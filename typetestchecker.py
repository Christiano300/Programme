from threading import Timer
import keyboard

def press_escape():
    keyboard.press_and_release('esc')
    print("Escape pressed")

timer = Timer(1, press_escape)

def on_key_press(event: keyboard.KeyboardEvent):
    if event.event_type == keyboard.KEY_UP:
        return
    global timer
    timer.cancel()
    if event.name != 'esc':
        timer = Timer(1, press_escape)
        timer.start()

keyboard.hook(on_key_press)
keyboard.wait("nach-unten")