from math import cos, sin, pi

import pygame

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size)

NUM_POINTS = 500
RADIUS = 200

points = [(cos(i * 2 * pi / NUM_POINTS + pi) * RADIUS + 320,
           sin(i * 2 * pi / NUM_POINTS + pi) * RADIUS + 240)
          for i in range(NUM_POINTS)]
length = len(points)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), (320, 240), RADIUS + 2, 5)
    for i, point in enumerate(points):
        pygame.draw.aaline(screen, (0, 0, 0), point, points[(2 * i) % length])
    pygame.display.update()
