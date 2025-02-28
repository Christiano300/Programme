import pygame
import pygame.gfxdraw
import typing
import numpy as np
from random import randint
from math import sqrt

pygame.init()
image = pygame.image.load(r"files\colorfill\5b1028529b7ad12e10d9a149a1b9b81383374978a8a17a1bc0c7b25fed2a9313.png")
size = width, height = image.get_size()
screen = pygame.display.set_mode(size)
offsets = [(i, j) for i in (-3, 0, 3) for j in (-3, 0, 3)]

image = image.convert_alpha(screen)

def draw_circle(surf: pygame.Surface, color: pygame.Color, pos: tuple[int, int], radius: int):
    pygame.gfxdraw.filled_circle(surf, *pos, radius, color)
    pygame.gfxdraw.aacircle(surf, *pos, radius, color)

def surf_diff(surface1: pygame.Surface, surface2: pygame.Surface) -> int:
    array1 = pygame.surfarray.pixels3d(surface1).astype(np.int16)
    array2 = pygame.surfarray.pixels3d(surface2).astype(np.int16)
    return np.sum(np.abs(array1.astype(np.int16) - array2.astype(np.int16)))

def byte_sat(value: int) -> int:
    return max(0, min(255, value))

def zero_sat(value: int, m: int) -> int:
    return max(0, min(m, value))

def color_vary(color: pygame.Color, amount: int) -> pygame.Color:
    return pygame.Color(byte_sat(color.r + randint(-amount, amount)),
        byte_sat(color.g + randint(-amount, amount)),
        byte_sat(color.b + randint(-amount, amount)))


def do_iteration(target: pygame.Surface, current: pygame.Surface, current_diff: int) -> typing.Union[int, bool]:
    # Generate random circle
    circles = []
    scores = []
    for i in range(3):
        radius = randint(1, int(sqrt(current_diff) / 150))
        pos = (randint(0, width - 1), randint(0, height - 1))
        # color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
        color = color_vary(target.get_at(pos), 20)

        circles.append((pos, radius, color))

        test = current.copy()
        draw_circle(test, color, pos, radius)
        new_diff = surf_diff(target, test)
        scores.append(new_diff)

    best_idx = min(range(len(scores)), key=lambda x: scores[x])
    score = scores[best_idx]
    pos, radius, color = circles[best_idx]

    if score <= current_diff:
        draw_circle(current, color, pos, radius)
        print(score, "\r", end="")
        return score
    return False

current_diff = surf_diff(image, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print()
            quit()


    res = do_iteration(image, screen, current_diff)
    if res:
        current_diff = res

        pygame.display.flip()
