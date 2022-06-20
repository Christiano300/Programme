import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.NOFRAME)
clock = pygame.time.Clock()



screen.fill("0xffffff")
pygame.draw.rect(screen, "0xf04f93", (100, 200, 365, 200), 200, 2000)
pygame.draw.circle(screen, "0xabcdef", (200, 100), 35.4, 20, True, False, True, False)
pygame.draw.ellipse(screen, "0xfedcab", (100, 150, 534, 260))
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.draw.rect(screen, "0xff7f05", (*event.pos, 5, 5))
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
        
        elif event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, "0xff7f05", (*event.pos, 5, 5))

            


    pygame.display.update()
    clock.tick(60)
