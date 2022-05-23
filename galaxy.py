from math import cos, pi, sin, sqrt
from random import randint, random, uniform

import pygame

pygame.init()

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

stars = []
NUM_STARS = 2500
twopi = pi * 2
starcolor = "0x00ff00"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                stars = []
                for i in range(NUM_STARS):
                    r = sqrt(random()) * (min(size) - 100) / 2
                    stars.append([r, uniform(0, twopi), pi / (r + randint(-50, 50))])
            elif event.key == pygame.K_q:
                pygame.quit()
                quit()
            elif event.key == pygame.K_c:
                if starcolor == "0xffffff":
                    starcolor = "0x00ff00"
                else:
                    starcolor = "0xffffff"

    screen.fill("0x000000")
    for i, star in enumerate(stars):
        pygame.draw.rect(screen, starcolor, (cos(
            star[1]) * star[0] + width / 2, sin(star[1]) * star[0] + height / 2, 1, 1), 0)
        # pygame.display.update()
        stars[i][1] += star[2]
        stars[i][1] %= twopi
    pygame.display.update()

    pygame.display.update()
    clock.tick(60)
