from random import choice

poker_symbole = ["Herz", "Karo", "Pik", "Kreuz"]
poker_werte = ["2", "3", "4", "5", "6", "7", "8",
               "9", "10", "Bube", "Dame", "König", "As"]

poker_karten = [i + j for i in poker_symbole for j in poker_werte]

aktive_karten = poker_karten
spieler_liste = []
tischkarten = []
pot = 0

# regeln festlegen
mindesteinsatz = 1  # int(input("Mindesteinsatz: "))
startgeld = 50  # int(input("Wie viel hat jeder am Anfang? "))
spielerzahl = 3  # int(input("Anzahl der Spieler: "))

# spieler-klasse


class Spieler:
    def __init__(self, name, geld):
        self.handkarten = []
        self.name = name
        self.geld = geld
        self.gesetzt = 0
        self.hat_gepasst = False
        self.passwert = 0
        self.schon_erhöht = False

    def karte_nehmen(self, karte):
        self.handkarten.append(karte)

    def __str__(self):
        nachricht = self.name + " hat die Karten: "
        for i in self.handkarten:
            nachricht = nachricht + i + ", "
        nachricht = nachricht.strip(", ")
        return nachricht

    def setzen(self, menge):
        self.geld -= menge
        self.gesetzt += menge

    def passen(self):
        if self.gesetzt:
            self.passwert = self.gesetzt
            self.gesetzt = 0


"""def setzkampf(spieleranzahl,n,setzwert):
    for i in spieler_liste:
        if not i.has_passed:
            #nach Aktion fragen
            print(i.name + " ist and der Reihe. Bitte wähle eine Aktion.", end="")
            eingabe = input("\n")

            #gepasst
            if eingabe == "p":
                print(i.name + " hat gepasst.")
                global pot
                i.passen()
                pot += i.setzwert
                i.has_passed = True

            #erhöht
            elif eingabe.startswith("e") and i.schon_erhöht == False:
                wert = int(eingabe.lstrip("e "))
                print(i.name + " erhöht auf " + str(wert))
                i.setzen(wert)
                setzwert = wert
                i.schon_erhöht = True
                if n == spieleranzahl:
                    return 0
                else:
                    for j in spieler_liste:
                        print(i)
                        print(j)
                        if j.gesetzt != wert and (not i == j):
                            setzkampf(spieleranzahl,n+1,setzwert)
            #gecheckt
            else:
                print(i.name + " hat gecheckt.")
                i.setzen(setzwert - i.gesetzt)"""



def check_for_set_finish(setzwert):
    for i in spieler_liste:
        if i.gesetzt != setzwert:
            return False
    return True


def setzkampf():
    global pot
    for i in spieler_liste:
        if not i.has_passed:
            eingabe = input("Wähle eine Aktion: ")
            if eingabe == "p":
                print(i.name + " hat gepasst.")
                global pot
                i.passen()
                pot += i.setzwert
                i.has_passed = True

            elif eingabe.startswith("e"):
                wert = int(eingabe.lstrip("e "))
                print(f"{i.name} erhöht auf {wert}")
                i.setzen(wert)


# spieler initialisieren
for i in range(1, spielerzahl + 1):
    playername = input(f"Name von Spieler {i}: ")
    spieler_liste.append(Spieler(playername, startgeld))


def karte_geben():
    kartenname = choice(aktive_karten)
    aktive_karten.remove(kartenname)
    return kartenname


# karten ziehen
for i in spieler_liste:
    for j in range(2):
        i.karte_nehmen(karte_geben())

# karten zeigen
for i in spieler_liste:
    input(" ")
    print(i)
    input(" ")
    print("\n" * 75)

# flops audecken
for i in range(3):
    tischkarten.append(karte_geben())

print("Die Flops werden aufgedeckt.")
print(f"Es sind: {tischkarten[0]}, {tischkarten[1]} und {tischkarten[2]}")
for i in spieler_liste:
    print(f"{i.name}: {i.geld}, {i.gesetzt}")

# the turn und the river aufdecken
