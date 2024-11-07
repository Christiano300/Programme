def find_function(options: list[str], param: str) -> str | None:
    option = None
    for o in options:
        if o.startswith(param):
            if option != None: # second match
                return None
            option = o
    return option
        

def inputInt(name):
    while True:
        try:
            return int(float(input(f"{name}: ")))
        except ValueError:
            print("you have to enter an integer")

lamps = []

while True:
    while True:
        mode = input("c: calculate position\nn: new lamp\n> ")
        if mode in ["c", "n"]:
            break
        print("you have to enter c or n")

    if mode == "n":
        print("enter lamp coordinates")
        x = inputInt("x")
        y = inputInt("y")
        z = inputInt("z")
        while True:
            upper = input("u: facing up\nd: facing down")
            if upper not in "ud":
                break
            print("you have to enter u or d")
        lamps.append()
    
    elif mode == "c":
        print("enter target coordinates: ")
        x = inputInt("x")
        y = inputInt("y")
        z = inputInt("z")
    
        
        
    