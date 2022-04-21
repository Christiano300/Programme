from random import choice
from time import sleep

witze = ["Was ist braun und schwimmt unter Wasser?\nEin U-Brot",
"Was ist orange und geht den Berg hinauf?\nEine Wanderine",
'Der Schüler fragt: "Herr Lehrer sie wollten uns doch heute etwas über das Gehirn erzählen."\nSagt der Lehrer: "Später, im Moment habe ich etwas anderes im Kopf"',
"Was sagt eine Schnecke, die auf einer Schildkröte reitet?\nHuii ist das schnell!"
]

def command_line():
    eingabe = "mSinit"
    while True:
        eingabe = input("Command line input: ")
        if eingabe == "exSp":
            exit()
        elif eingabe.startswith("cgpassw"):
            print("There was an error while trying to get the password.")
        elif eingabe == "lmoSp":
            print("Please confirm with y")
            eingabe = input("")
            if eingabe == "y":
                break
        elif eingabe.startswith("cpdata"):
            print("No data found")
        elif eingabe == "but there should be data":
            print("no")
        elif eingabe == "yes":
            print("I SAID THERE IS NO DATA")
        else:
            print("Error")
            print("Command not aviable or spelled wrong")
            print("Please try again")

while True:
    eingabe = input("")
    if "witz" in eingabe.lower() or "witzig" in eingabe.lower():
        sleep(0.5)
        print(choice(witze))

    elif "hallo" in eingabe.lower():
        sleep(0.5)
        print("Hallo!")

    elif eingabe == "moSp":
        command_line()

    elif "wie geht es dir" in eingabe.lower():
        sleep(0.5)
        print("Danke gut.")
        sleep(0.5)
        print("Und dir?")
        ask = True

    elif ("schlecht" in eingabe.lower() or "nicht gut" in eingabe.lower()) and ask:
        sleep(0.5)
        print("Das ist schade.")
        ask = False

    elif (eingabe.lower() == "gut" or eingabe.lower() == "ausgezeichnet") and ask:
        sleep(0.5)
        print("Das freut mich.")
        ask = False

    else:
        sleep(0.5)
        print("Keine Ahnung was du meinst")
