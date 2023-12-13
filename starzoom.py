from math import sqrt
from random import choice, randint
import pygame
pygame.init()

size = width, height = 1920, 1080
min_dist = sqrt((width / 2) ** 2 + (height / 2) ** 2) + 10
max_dist = 2
center = [width / 2, height / 2]
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

STAR_FREQUENCY = 0
WARP_DISTORTION = 1.5
STAR_SPEED = .95
ROTATION_SPEED = 0
cooldown = 0
stars = []

def approach_point(point: list, anchor: list, factor: float) -> list:
    x = (anchor[0] - point[0]) * factor
    y = (anchor[1] - point[1]) * factor
    xnew = x + anchor[0]
    ynew = y + anchor[1]
    return [(point[i] - anchor[i]) * factor + anchor[i] for i in range(2)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size
            min_dist = sqrt((width / 2) ** 2 + (height / 2) ** 2) + 10
            center = [width / 2, height / 2]
            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            pygame.quit()
            quit()

    mousebuttons = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    if mousebuttons[0]:
        s = [mouse[0], mouse[1], 0]
        stars.append(s)
    elif mousebuttons[2]:
        center = list(pygame.mouse.get_pos())
        
    if cooldown:
        cooldown -= 1
    else:
        cooldown = STAR_FREQUENCY
        star = [randint(-50, 50), randint(-50, 50)]
        try:
            ratio = min_dist / sqrt(star[0] ** 2 + star[1] ** 2)
        except ZeroDivisionError:
            pass
        else:
            stars.append([star[0] * ratio + center[0], star[1] * ratio + center[1], 0])
            
    screen.fill((0, 0, 0))
    for i in stars:
        pos1 = i[:2]
        pos2 = approach_point(i, center, WARP_DISTORTION)
        if i[2] > 0:
            color = [255 - i[2], 255 - i[2], 255]
        else:
            color = [255, 255 + i[2], 255 + i[2]]
        pygame.draw.aaline(screen, color, pos1, pos2)
    # screen.blit(pygame.font.Font(None, 30).render(str(len(stars)), True, (0, 200, 0)), (100, 100))
    
    # for i, star in enumerate(stars):
    #     stars[i] = [star[0] * STAR_SPEED, star[1] * STAR_SPEED, star[2]]
    
    for i, star in enumerate(stars):
        stars[i] = approach_point(star, center, STAR_SPEED)
        stars[i].append(star[2])
    
    i = 0
    while i < len(stars):
        x = stars[i][0] - center[0]
        y = stars[i][1] - center[1]
        if sqrt(x ** 2 + y ** 2) < max_dist:
            del stars[i]
        else:
            x = stars[i][0] - center[0] + ROTATION_SPEED
            if sqrt(x ** 2 + y ** 2) < max_dist:
                del stars[i]
            else:
                i += 1
    
    center[0] = (center[0] + ROTATION_SPEED) % width
    # pygame.draw.aaline(screen, (255, 0, 0), (center[0] + 10, center[1] + 10), (center[0] - 10, center[1] - 10))
    # pygame.draw.aaline(screen, (255, 0, 0), (center[0] + 10, center[1] - 10), (center[0] - 10, center[1] + 10))
    pygame.display.update()
    clock.tick(60)