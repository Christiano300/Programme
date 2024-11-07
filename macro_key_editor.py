import pygame
import pygaminter
pygame.init()

size = width, height = 1280, 720
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(60)