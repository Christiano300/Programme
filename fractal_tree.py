from random import randint
import pygame
pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

pxarray = pygame.surfarray.pixels3d(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    x = randint(0, 600)
    y = randint(0, 400)
    pxarray[x, round((x / 600) * (y / 400) * 400)] = (255, 255, 255)
    pygame.display.update()
