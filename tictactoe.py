from copy import deepcopy
from random import choice
from typing import Union
from funktionen_patzl import inputInt


def print_grid(grid: list):
    """Gibt das Feld aus

    Args:
        grid (list): Feld als liste
    """
    print("\u250f{}\u2513".format('\u2533'.join(['\u2501' * 3 for i in range(3)])))

    for i, row in enumerate(grid):
        print("\u2503{}\u2503".format('\u2503'.join([f" {i} " for i in row])))
        if i != 2:
            print("\u2523{}\u252b".format('\u254b'.join(['\u2501' * 3 for i in range(3)])))
    
    print("\u2517{}\u251b".format('\u253b'.join(['\u2501' * 3 for i in range(3)])))


def check_for_winner(grid: list) -> Union[str, None]:
    """Schaut ob wer gewonnen hat

    Args:
        grid (list): Feld als Liste

    Returns:
        Union[str, None]: Wer gewonnen hat
    """
    for i in grid:
        if i[0] != " " and i[0] == i[1] == i[2]:
            return i[0]
    for i in range(3):
        if grid[0][i] != " " and grid[0][i] == grid[1][i] == grid[2][i]:
            return grid[0][i]
    if grid[0][0] != " " and grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]
    if grid[0][2] != " " and grid[0][2] == grid[1][1] == grid[2][0]:
        return grid[0][2]
    return None

def input_field(spieler: str, grid: list) -> tuple:
    """Liest koordinaten ein
    
    Args:
        spieler (str): Spieler der dran ist
        feld (list): aktuelles Spielfeld

    Returns:
        tuple: reihe, spalte
    """
    print(f"Spieler {spieler} ist dran")
    while True:
        eingabe = input("Koordinate mit Leerzeichen getrennt eingeben: ")
        if len(eingabe) == 3 and eingabe.count(" ") == 1:
            xs, ys = eingabe.split(" ")
            if xs.isdecimal() and ys.isdecimal and (x := int(xs)) in range(3) and (y := int(ys)) in range(3):
                if grid[x][y] == " ":
                    return x, y
                    print()
                else:
                    print("Da steht schon wer")
                    continue
        print("Ungültige Eingabe, probiers nochmal")

def ai_move_easy(spieler: str, grid: list):
    possible = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == " ":
                possible.append((i, j))
    y, x = choice(possible)
    grid[x][y] = spieler

def ai_move_advanced(spieler: str, grid: list):
    spieler_l = ["X", "O"]
    not_lose_spots = []
    for i in range(3):
        for j in range(3):
            new = deepcopy(grid)
            for s in spieler_l:
                new[i][j] = s
                if (winner := check_for_winner(new)):
                    if winner == spieler:
                        grid[i][j] = spieler
                        return
                    else:
                        not_lose_spots.append((i, j))
    if not_lose_spots:
        i, j = choice(not_lose_spots)
        grid[i][j] = spieler
        return
    if grid[1][1] == " ":
        grid[1][1] = spieler
        return
    ecken = []
    for i in (0, 2):
        for j in (0, 2):
            if grid[i][j] == " ":
                ecken.append((i, j))
    if ecken:
        i, j = choice(ecken)
        grid[i][j] = spieler
        return
    ai_move_easy(spieler, grid)
        
                

    
                    
anfangsspieler = "O"
spielstand = {"X": 0, "O": 0}
aktiv = True
while True:
    anzahl = inputInt("Anzahl der Spieler: ")
    if anzahl in range(1, 3):
        break
    else:
        print("Geht nicht!")

while aktiv:
    feld = [[" " for i in range(3)] for j in range(3)]
    anfangsspieler = "O" if anfangsspieler == "X" else "X"
    spieler = anfangsspieler
    # Rundenschleife
    for i in range(9):
        print_grid(feld)
        if anzahl == 1 and spieler == "O":
            ai_move_advanced(spieler, feld)
            print(f"Spieler {spieler} ist dran\n")
        else:
            reihe, spalte = input_field(spieler, feld)
            feld[reihe][spalte] = spieler
        if (winner := check_for_winner(feld)):
            print(f"Spieler {winner} hat gewonnen!\n\n")
            spielstand[winner] += 1
            print(f"{spielstand['X']} : {spielstand['O']}")
            break
        spieler = "O" if spieler == "X" else "X"
    else:
        print("Unentschieden!\n\n")
    for i in spielstand:
        if spielstand[i] == 3:
            print(f"Spielende! Spieler {i}")
            aktiv = False
            break
            
