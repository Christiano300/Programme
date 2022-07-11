from math import ceil
import random
import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()


def random_from_pos(coords: list, chance: float = .2):
    random.seed(coords[0])
    multi = random.randint(1, 200)
    mod = random.randint(1, 50)
    random.seed(coords[0] + coords[1] * multi % mod)
    return random.random() > chance


playerpos = [width // 2 - 10, height // 2 - 10]
camerpos = [0, 0]
keys_pressed = {i: False for i in "wasd"}
MOVEMENT_SPEED = 3
boundary = pygame.Rect(70, 70, width - 140, height - 140)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            elif event.unicode in "wasd":
                keys_pressed[event.unicode] = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys_pressed["w"] = False
            elif event.key == pygame.K_a:
                keys_pressed["a"] = False
            elif event.key == pygame.K_s:
                keys_pressed["s"] = False
            elif event.key == pygame.K_d:
                keys_pressed["d"] = False

    if pygame.Rect.collidepoint(boundary, playerpos):
        if keys_pressed["w"]:
            playerpos[1] -= MOVEMENT_SPEED
        if keys_pressed["a"]:
            playerpos[0] -= MOVEMENT_SPEED
        if keys_pressed["s"]:
            playerpos[1] += MOVEMENT_SPEED
        if keys_pressed["d"]:
            playerpos[0] += MOVEMENT_SPEED
    else:
        if keys_pressed["w"]: pass
    screen.fill(0x000000)
    
    for i in range(ceil(width / 50)):
        for j in range(ceil(height / 50)):
            if random_from_pos([i, j], .9):
                x = i * 50 + camerpos[0]
                y = j * 50 + camerpos[1]
                pygame.draw.rect(screen, 0x0050ff, (x, y, 50, 50))
        
    pygame.draw.rect(screen, 0xffc1bc,
                     (playerpos[0] - 10, playerpos[1] - 10, 20, 20))
        
    pygame.display.update()
    clock.tick(60)
