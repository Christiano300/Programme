from random import shuffle

import pygame
import pygame.gfxdraw

pygame.init()

size = width, height = 1920, 1080
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()

points = [(i * 30 + 15, j * 30 + 15) for i in range(round(width / 30)) for j in range(round(height / 30))]

while True:
    for c in [0xf00f0f, 0xff7f0f, 0xffff0f, 0x0fcf0f, 0x0fffff, 0x0070ff, 0xff5faf]:
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
            color = (c >> 16 & 0xff, c >> 8 & 0xff, c & 0xff)
            pygame.gfxdraw.filled_circle(screen, *i, 22, color)
            pygame.gfxdraw.aacircle(screen, *i, 22, color)
            pygame.display.update()
            clock.tick(300)
