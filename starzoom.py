from math import sqrt
from random import choice, randint
import pygame
pygame.init()

size = width, height = 1920, 1080
min_dist = sqrt((width / 2) ** 2 + (height / 2) ** 2) + 10
max_dist = 10
center = [width / 2, height / 2]
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

STAR_FREQUENCY = 0
WARP_DISTORTION = 1
STAR_SPEED = .98
cooldown = 0
stars = []
center = []

def approach_point(src: list, dst: list, factor: float) -> list:
    xnew = dst[0] - src[0] * factor
    ynew = dst[1] - src[1] * factor
    return [xnew + dst[0], ynew + dst[1]]

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

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button in (4, 5):
            s = [event.pos[0] - width / 2, event.pos[1] - height / 2, randint(-100, 100)]
            stars.append(s)

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
            stars.append([star[0] * ratio + center[0], star[1] * ratio + center[1], choice([0])])
            
    screen.fill((0, 0, 0))
    for i in stars:
        pos1 = i[0], i[1]
        # pos2 = approach_point(i, center, WARP_DISTORTION)
        if i[2] > 0:
            color = [255 - i[2], 255 - i[2], 255]
        else:
            color = [255, 255 + i[2], 255 + i[2]]
        pygame.draw.aaline(screen, color, pos1, pos1)
    
    # for i, star in enumerate(stars):
    #     stars[i] = [star[0] * STAR_SPEED, star[1] * STAR_SPEED, star[2]]
    
    for i, star in enumerate(stars):
        stars[i] = approach_point(star, center, STAR_SPEED)
        stars[i].append(star[2])
    
    i = 0
    while i < len(stars):
        if sqrt((stars[i][0] - center[0]) ** 2 + (stars[i][1] - center[1]) ** 2) < max_dist:
            del stars[i]
        else:
            i += 1
    pygame.display.update()
    clock.tick(60)