from random import randint, shuffle

import pygame
import pygame.gfxdraw

pygame.init()

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()

points = [(i * 30 + 10 - 15 * (j % 2), j * 30 + 10) for i in range(round(width / 30)) for j in range(round(height / 30))]
# points = [(i * 30 + 10, j * 30 + 10) for i in range(round(width / 30)) for j in range(round(height / 30))]
radius = 20

while True:
    for c in [0xf00f0f, 0xff7f0f, 0xffff0f, 0x0fcf0f, 0x0fffff, 0x0070ff, 0xBE63FF]:
        shuffle(points)
        for i in points:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.KEYDOWN and event.key in (pygame.K_q, pygame.K_ESCAPE):
                    pygame.quit()
                    quit()

            # pygame.draw.circle(screen, c, i, randint(14, 22))
            color = (c >> 16 & 0xff, c >> 8 & 0xff, c & 0xff)
            pygame.gfxdraw.filled_circle(screen, *i, radius, color)
            pygame.gfxdraw.aacircle(screen, *i, radius, color)
            pygame.display.update()
            clock.tick(300)
