from random import choice, randint
import pygame
pygame.init()
size = width, height = 75, 75
screen = pygame.display.set_mode(size, pygame.NOFRAME)

tiles = {0: [1, 1, 0, 0], 1: [0, 1, 1, 0], 2: [0, 0, 1, 1], 3: [1, 0, 0, 1]}
sides = {(-1, 0): 3, (1, 0): 1, (0, -1): 0, (0, 1): 2}


def find_lowest_entropy(grid: list) -> tuple:
    min = float("inf")
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if isinstance(cell, dict) and len(cell) < min:
                min = len(cell)
                pos = i, j
    if min == 4:
        pos = [randint(0, 4) for i in range(2)]
    return pos, min


def draw_tile(x: int, y: int, tile: int):
    pygame.draw.rect(screen, "0x303030", (x * 15, y * 15, 15, 15))
    if tile[0]:
        pygame.draw.rect(screen, "0xd0d010", (x * 15 + 5, y * 15 + 5, 5, 10))
    if tile[1]:
        pygame.draw.rect(screen, "0xd0d010", (x * 15 + 5, y * 15 + 5, 10, 5))
    if tile[2]:
        pygame.draw.rect(screen, "0xd0d010", (x * 15 + 5, y * 15, 5, 10))
    if tile[3]:
        pygame.draw.rect(screen, "0xd0d010", (x * 15, y * 15 + 5, 10, 5))


grid = [[tiles for i in range(5)] for j in range(5)]
screen.fill("0x303030")
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # one iteration
            (y, x), minimum = find_lowest_entropy(grid)
            if isinstance(tile, dict):
                grid[y][x] = choice(grid[y][x])
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if not (i and j) and (i or j):
                            this = sides[(i, j)]
                            other = (this + 2) % 4
                            for variant in [_ for _ in grid[y + j][x + i]]:
                                if variant[other] != grid[y][x][this]:
                                    grid[y + j].remove(variant)
                

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
    screen.fill("0x303030")
    for i, row in enumerate(grid):
        for j, tile in enumerate(row):
            if isinstance(tile, list):
                draw_tile(j, i, tile)
    pygame.display.update()
