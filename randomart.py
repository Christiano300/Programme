from numba.core.transforms import loop_lifting
from numba.core.typeinfer import ForceLiteralArg
import pygame
import pygame.gfxdraw
import typing
import numpy as np
from random import randint
from math import sqrt
from numba import njit, jit
import cProfile

pygame.init()
image = pygame.image.load(r"files/REFR.jpg")
size = width, height = image.get_size()
screen = pygame.display.set_mode(size)

canvas = pygame.Surface(size)
offsets = [(i, j) for i in (-3, 0, 3) for j in (-3, 0, 3)]

image = image.convert_alpha(screen)

def draw_circle(surf: pygame.Surface, color: pygame.Color, pos: tuple[int, int], radius: int):
    pygame.gfxdraw.filled_circle(surf, *pos, radius, color)
    pygame.gfxdraw.aacircle(surf, *pos, radius, color)

@jit(forceobj=True, looplift=True)
def surf_diff(surface1: pygame.Surface, surface2: pygame.Surface) -> int:
    return arr_diff(pygame.surfarray.pixels3d(surface1), pygame.surfarray.pixels3d(surface2))

@njit(fastmath=True, parallel=True)
def arr_diff(array1: np.ndarray, array2: np.ndarray) -> int:
    return np.sum(np.abs(array1.astype(np.int16) - array2.astype(np.int16)))

def byte_sat(value: int) -> int:
    return max(0, min(255, value))

def zero_sat(value: int, m: int) -> int:
    return max(0, min(m, value))

def color_vary(color: pygame.Color, amount: int) -> pygame.Color:
    return pygame.Color(byte_sat(color.r + randint(-amount, amount)),
        byte_sat(color.g + randint(-amount, amount)),
        byte_sat(color.b + randint(-amount, amount)))

@jit(forceobj=True, looplift=True)
def do_iteration(target: pygame.Surface, current: pygame.Surface, current_diff: int) -> typing.Union[int, bool]:
    # Generate random circle
    attempts = 20
    circles: list[tuple[tuple[int, int], int, pygame.Color]] = []
    scores = np.zeros(3)
    for i in range(3):
        radius = randint(1, int(sqrt(current_diff) / 150))
        pos = (randint(0, width - 1), randint(0, height - 1))
        # color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
        color = color_vary(target.get_at(pos), 20)

        circles.append((pos, radius, color))

        test = current.copy()
        draw_circle(test, color, pos, radius)
        new_diff = surf_diff(target, test)
        scores[i] = new_diff

    best_idx = np.argmin(scores)
    score = scores[best_idx]
    pos, radius, color = circles[best_idx]

    if score <= current_diff:
        draw_circle(current, color, pos, radius)
        print(score, round((1 - score / start_diff) * 100, 2), "% \r", end="")
        return score
    return False

current_diff = surf_diff(image, canvas)
start_diff = current_diff

def main():
    global current_diff
    show_diff = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    show_diff = not show_diff

        res = do_iteration(image, canvas, current_diff)
        if res:
            current_diff = res
            if show_diff:
                pygame.surfarray.blit_array(screen, np.abs(pygame.surfarray.pixels3d(image).astype(np.int16) - pygame.surfarray.pixels3d(canvas).astype(np.int16)))
            else:
                screen.blit(canvas, (0, 0))

            pygame.display.flip()

if __name__ == "__main__":
    main()
