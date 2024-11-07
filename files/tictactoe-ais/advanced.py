from copy import deepcopy
from random import choice

def ai_move_easy(grid: list):
    possible = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == " ":
                possible.append((i, j))
    return choice(possible)

def check_for_winner(grid: list):
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

def move(grid: list, spieler: str):
    spieler_l = ["X", "O"]
    not_lose_spots = []
    for i in range(3):
        for j in range(3):
            if grid[i][j] == " ":
                new = deepcopy(grid)
                for s in spieler_l:
                    new[i][j] = s
                    if (winner := check_for_winner(new)):
                        if winner == spieler:
                            return i, j
                        not_lose_spots.append((i, j))
    if not_lose_spots:
        i, j = choice(not_lose_spots)
        return i, j
    if grid[1][1] == " ":
        return 1, 1
    ecken = []
    for i in (0, 2):
        for j in (0, 2):
            if grid[i][j] == " ":
                ecken.append((i, j))
    if ecken:
        return choice(ecken)
    return ai_move_easy(grid)