from random import randint
import pygame
pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

tiles = [{
    "id": 0,
    "faces": [1, 1, 0, 0]
}, {
    "id": 1,
    "faces": [0, 1, 1, 0]
}, {
    "id": 2,
    "faces": [0, 0, 1, 1]
}, {
    "id": 3,
    "faces": [1, 0, 0, 1]
}]

def find_lowest_entropy(grid: list) -> list:
    min = float("inf")
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if len(cell) < min:
                min = len(cell)
                pos = i, j
    if min == 4:
        i, j = [randint(0, 4) for i in "12"]
    return pos, min


grid = [[tiles[:] for i in range(5)] for j in range(5)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pass
            # one_iteration()