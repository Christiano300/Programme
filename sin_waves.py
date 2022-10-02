from math import radians, sin
import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

def wert(x):
    return sin(radians(x)) * 180 + 240

a = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(0xffffff)
    punkte = [[x * 50 + 25, wert(x * 50 - a)] for x in range(round(width / 50) + 1)]
    # pygame.draw.lines(screen, 0, False, punkte, 3)
    for i in punkte:
        pygame.draw.circle(screen, 0, i, 5.7)
    a += 1
    pygame.display.update()
    clock.tick(100)