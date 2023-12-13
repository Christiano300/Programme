import pygame
pygame.init()

size = width, height = pygame.display.get_desktop_sizes()[0]
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

    pygame.display.update()
    clock.tick(60)