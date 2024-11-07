import random
farben = ["Rot", "Gelb", "Grün", "Blau", "Pink", "Weiß"]
farben_kopie = farben[:]
code = []
print("Farbencode wurde ausgewählt")

def eingabe():
    while True:
        try:
            guess = input("Versuch: ").split(" ")
        except:
            print("Ungültige Eingabe. Bitte wiederholen")
        else:
            gueltig = True
            if len(guess) == 4:
                for i in guess:
                    if i not in farben:
                        gueltig = False
                        break
            if gueltig:
                break
            else:
                print("Ungültige Eingabe. Bitte wiederholen")
    return guess

def generate_code():
    return random.sample(["Rot", "Gelb", "Grün", "Blau", "Pink", "Weiß"], 4)
    

versuch = eingabe()
code = generate_code()

while versuch == code:
    code = generate_code()



geschafft = True
for i in range(10):
    
    pass

print(code)
print(farben)
print(farben_kopie)