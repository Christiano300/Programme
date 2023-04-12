from random import shuffle

import pygame

pygame.init()

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)

points = [(i * 30 + 15, j * 30 + 15) for i in range(round(width / 30)) for j in range(round(height / 30))]

while True:
    for c in [0xff0000, 0xff7f00, 0xffff00, 0x00ff00, 0x00ffff, 0x0000ff, 0xff00ff]:
        shuffle(points)
        for i in points:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    pygame.quit()
                    quit()

            # pygame.draw.circle(screen, c, i, randint(14, 22))
            pygame.draw.circle(screen, c, i, 22)
            pygame.display.update()
