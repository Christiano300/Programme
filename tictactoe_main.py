from copy import deepcopy
from importlib import import_module
import os
from typing import Union

S = ["X", "O"]


def print_grid(grid: list):
    print("\u250f{}\u2513".format(
        '\u2533'.join(['\u2501' * 3 for i in range(3)])))

    for i, row in enumerate(grid):
        print("\u2503{}\u2503".format('\u2503'.join([f" {i} " for i in row])))
        if i != 2:
            print("\u2523{}\u252b".format(
                '\u254b'.join(['\u2501' * 3 for i in range(3)])))

    print("\u2517{}\u251b".format(
        '\u253b'.join(['\u2501' * 3 for i in range(3)])))


def check_for_winner(grid: list) -> Union[str, None]:
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

def select_player(id):
    while True:
        print(f"\nVerfügbar: {', '.join(ais.keys())}. Leer lassen um selbst zu spielen")
        a = input(f"Spieler {id}: ")
        if a == "":
            return -1
        elif a in ais:
            return ais[a]
        else:
            print("Keine option!")

ai_names = [i for i in os.listdir("./files/tictactoe-ais") if i.endswith(".py")]
ais_list = [import_module("files.tictactoe-ais." + os.path.splitext(i)[0]) for i in ai_names]
ais = {os.path.splitext(name)[0]: i for i, name in zip(ais_list, ai_names) if hasattr(i, "move")}

spieler_ai = [select_player(i) for i in range(2)]
spielerbot = [i != -1 for i in spieler_ai]

# spieler = 0 heißt X, 1 heißt O


def game(startspieler: int, do_print: bool = True):
    feld = [[" " for i in range(3)] for j in range(3)]
    spieler = startspieler
    # Rundenschleife
    for i in range(9):
        if do_print:
            print_grid(feld)
        if spielerbot[spieler]:
            if do_print:
                print(f"Spieler {S[spieler]} ist dran\n")
            y, x = spieler_ai[spieler].move(deepcopy(feld), S[spieler])
            if feld[y][x] == " ":
                feld[y][x] = S[spieler]
            else:
                print(f"Spieler {S[spieler]} hat versucht auf ein besetztes Feld zu setzen ({y, x}). Spiel wird abgebrochen.")
                exit(1)
        else:
            y, x = input_field(feld, S[spieler])
            feld[y][x] = S[spieler]
        if (winner := check_for_winner(feld)):
            if do_print:
                print_grid(feld)
                print(f"Spieler {winner} hat gewonnen!\n\n")
            return spieler
        spieler = (spieler + 1) % 2
    else:
        if do_print:
            print_grid(feld)
            print("Unentschieden!\n\n")
        return -1

def contest(games: int, do_print: bool):
    x = y = u = start = 0
    for _ in range(games):
        erg = game(start, do_print)
        if erg == 0:
            x += 1
        elif erg == 1:
            y += 1
        elif erg -1:
            u += 1
        start = (start + 1) % 2
    print(f"Spieler 1: {x}, Spieler 2: {y}, Unentschieden: {u}")

contest(1000, False)