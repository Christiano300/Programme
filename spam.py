from random import randint
import shutil
import time
a = []
while True:
    for j in range(shutil.get_terminal_size().columns - 1):
        a.append(randint(0, 1))
    print("".join(str(i) for i in a))
    a = []
    time.sleep(.05)
