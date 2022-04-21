from copy import deepcopy
from math import sqrt
from sys import exit as closewindow
import pygame

pygame.init()
size = width, height = 320, 240
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def saturate(value, min_val=0, max_val=255):
    if value > max_val:
        return max_val
    elif value < min_val:
        return min_val
    return value


hmap = [[0 for i in range(width)] for j in range(height)]
pxarray = pygame.PixelArray(screen)


def change_heightmap(x: int, y: int, radius: int = 30) -> None:
    ratio = 255 / radius
    for i in range(-radius, radius + 1):
        for j in range(-radius, radius + 1):
            xpos = i + x
            ypos = j + y
            try:
                hmap[xpos][ypos] += max(0,
                                        ratio * (radius - sqrt(i**2 + j**2)))
            except IndexError:
                pass
            else:
                hmap[xpos][ypos] = saturate(hmap[xpos][ypos])


newmap = deepcopy(hmap)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            closewindow()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # indcrease height map at that position
            change_heightmap(event.pos[1], event.pos[0], 2)

    for y, row in enumerate(hmap):
        for x in range(width):
            sum = 0
            try:
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        sum += hmap[x + i][y + j]
                newmap[x][y] = saturate(sum // 9)
            except IndexError:
                pass
    hmap = newmap

    for y, row in enumerate(hmap):
        for x, pixel in enumerate(row):
            pxarray[x][y] = (pixel, 0, 0)
            # pxarray[x][y] = (255, 255- pixel, 255- pixel)

    pygame.display.update()