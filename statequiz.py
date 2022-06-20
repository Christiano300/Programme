import csv
from random import choice, randint
with open("files/states.csv") as f:
    reader = csv.DictReader(f)
    states = {i['state']: i['capital'] for i in reader}


while True:
    # pick a state
    state = choice(list(states.keys()))
    capitals = []
    capitals.append(capital := states[state])
    while True:
        cap = states[choice(list(states.keys()))]
        if cap != capitals[0]:
            capitals.append(cap)
            break
    capitals = capitals if randint(0, 1) else capitals[::-1]
    print(f"\nWhats the capital of {state}?")
    print(f"A: {capitals[0]}, B: {capitals[1]}")
    while True:
        answer = input().lower()
        if answer == "a":
            if capitals[0] == capital:
                print("Correct")
            else:
                print(f"Wrong, the answer is {capitals[1]}")
            break
        elif answer == "b":
            if capitals[1] == capital:
                print("Correct")
            else:
                print(f"Wrong, the answer is {capitals[0]}")
            break
        else:
            print("Invalid Option")