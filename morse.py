import json
from time import sleep
from winsound import Beep

DIT = 40
DAH = DIT * 3
SYMBOL = DIT
LETTER = DIT * 3
SPACE = DIT * 7

with open("files/morse.json") as f:
    morsedict = json.load(f)

eingabe = input("Eingabe: ").lower()
for i in eingabe:
    if not i in morsedict:
        print(f"Invalid Character {i}")
        quit()

for i in eingabe:
    if i == " ":
        sleep(SPACE / 1000)
    else:
        for j, l in enumerate(morsedict[i]):
            Beep(600, DIT if l == "." else DAH)
            if j != len(morsedict[i]) - 1:
                sleep(SYMBOL / 1000)
        sleep(LETTER / 1000)
