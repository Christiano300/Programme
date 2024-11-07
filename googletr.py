from googletrans import Translator as Tr
from webbrowser import open_new_tab

tr = Tr()

def intput(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Thats not a whole number idiot")

inp = input("That thing to repeat: ")
n = intput("Maximum input letters: ")
mtabs = intput("Maximum number of tabs open at the same time (not including already opened tabs): ")

text = ""
length = len(inp)
translations = []
for i in range(n):
    text += inp[i % length]
    new = tr.translate(text, dest='en', src='auto').text
    if new != text:
        translations.append(text)


for i in range(0, len(translations), mtabs):
    input("Press enter to show next 10 translations...")
    for j in translations[i:i+mtabs]:
        open_new_tab(f"https://translate.google.at/?sl=auto&tl=en&text={j}&op=translate")