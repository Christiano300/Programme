from math import ceil, sqrt
import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()


def random_from_pos(coords: list, chance: float = .2):
    h = hash(str(hash(tuple(coords))))
    return h % 100 < chance * 100

playerpos = [width // 2 - 10, height // 2 - 10]
campos = [0, 0]
mouse_pressed = False
boundary = pygame.Rect(50, 50, width - 100, height - 100)
MOVEMENT_SPEED = 3

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.size
            boundary = pygame.Rect(50, 50, width - 100, height - 100)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pressed = True
        
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False
    
    # spieler bewegen
    if mouse_pressed:
        # differenzvektor ausrechnen
        diff = [p - m for m, p in zip([width // 2, height // 2], pygame.mouse.get_pos())]
        # länge des vektors berechnen
        l = sqrt(sum((i ** 2 for i in diff)))
        # skalierung berechnen und vektor mit skalierung multiplizieren
        # ergebnis: vektor hat die selbe richtung aber die länge von MOVEMENT_SPEED
        scale = MOVEMENT_SPEED / l if l else 0
        norm = [i * scale for i in diff]
        new = [n + p for n, p in zip(norm, playerpos)]
        # wenn der spieler in der box ist spieler bewegen, ansonsten die Kamera
        if pygame.Rect.collidepoint(boundary, new):
            playerpos = new
        else:
            campos[0] += norm[0]
            campos[1] += norm[1]
    
    screen.fill(0x000000)
    
    for i in range(cx := int(campos[0] / 50) - 1, ceil(width / 50) + cx + 2):
        for j in range(cy := int(campos[1] / 50) - 1, ceil(height / 50) + cy + 2):
            if random_from_pos([i, j], .1):
                color = 0x009000
            elif random_from_pos([i, j], .9):
                color = 0x00c800
            else:
                color = 0xa8683e
            xs = i * 50 - campos[0]
            ys = j * 50 - campos[1]
            pygame.draw.rect(screen, color, (xs, ys, 50, 50))
                
        
    pygame.draw.rect(screen, 0xffc1bc,(playerpos[0] - 10, playerpos[1] - 10, 20, 20))
        
    pygame.display.update()
    clock.tick(60)
