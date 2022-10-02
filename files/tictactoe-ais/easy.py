from random import choice


def move(grid: list, _):
    possible = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == " ":
                possible.append((i, j))
    return choice(possible)
