import pygame
import pygame.gfxdraw
import typing
import numpy as np
from random import choice, randint, randrange
from math import sqrt
from numba import njit, jit, prange

BLOCK_SIZE = 30
POINT_SAMPLES = 3
SOFTMAX_TEMP = .05
INIT_GRID_SIZE = 20

pygame.init()
# Load image, set display to enable convert, convert image, transform image to block size, set display to new size
image = pygame.image.load(r"files/gits.jpg")
size = width, height = image.get_size()
screen = pygame.display.set_mode(size)
image = image.convert()

block_w = round(width / BLOCK_SIZE)
block_h = round(height / BLOCK_SIZE)
image = pygame.transform.smoothscale(
    image, (block_w * BLOCK_SIZE, block_h * BLOCK_SIZE))
size = width, height = image.get_size()
screen = pygame.display.set_mode(size)

canvas = pygame.Surface(size)

# canvas.fill((200, 200, 200))

def draw_circle(surf: pygame.Surface, color: pygame.Color, pos: tuple[int, int], radius: int, alpha: int):
    color.a = 255
    pygame.gfxdraw.filled_circle(surf, *pos, radius, color)
    pygame.gfxdraw.aacircle(surf, *pos, radius, color)


@jit(forceobj=True, looplift=True)
def surf_diff(surface1: pygame.Surface, surface2: pygame.Surface) -> int:
    return arr_diff(pygame.surfarray.pixels3d(surface1), pygame.surfarray.pixels3d(surface2))


@njit(fastmath=True, parallel=True)
def arr_diff(array1: np.ndarray, array2: np.ndarray) -> int:
    return np.sum(np.square((array1.astype(np.int16) - array2.astype(np.int16)).astype(np.int32)))


@njit(fastmath=True)
def byte_sat(value: int) -> int:
    return max(0, min(255, value))


@njit(fastmath=True)
def softmax_cumprob(x: np.ndarray, temp: float = 1.0) -> np.ndarray:
    x = np.log(x.astype(np.float64) + 1e-10) # add small value to avoid log(0)
    e_x = np.exp((x - np.max(x)) / temp)
    probabilities = e_x / e_x.sum()
    return np.cumsum(probabilities)


@njit(fastmath=True)
def multinomial(cumulative_probabilities: np.ndarray) -> int:
    r = np.random.rand()
    return (cumulative_probabilities < r).sum()


@jit(forceobj=True)
def color_vary(color: pygame.Color, amount: int) -> pygame.Color:
    return pygame.Color(*_color_vary(color.r, color.g, color.b, amount))


@njit(fastmath=True)
def _color_vary(r: int, g: int, b: int, amount: int) -> tuple[int, int, int]:
    return (byte_sat(r + randint(-amount, amount)),
            byte_sat(g + randint(-amount, amount)),
            byte_sat(b + randint(-amount, amount)))


def circle_bounds(pos: tuple[int, int], radius: int, surf_size: tuple[int, int]) -> pygame.Rect:
    x0 = max(0, pos[0] - radius)
    y0 = max(0, pos[1] - radius)
    x1 = min(surf_size[0], pos[0] + radius + 1)
    y1 = min(surf_size[1], pos[1] + radius + 1)
    return pygame.Rect(x0, y0, x1 - x0, y1 - y0)


@jit(forceobj=True, looplift=True)
def do_iteration(target: pygame.Surface, current: pygame.Surface, sample: pygame.Surface, current_diff: int, block_diffs: np.ndarray, block_probs: np.ndarray) -> typing.Union[int, bool]:
    # Generate random circle
    circles: list[tuple[tuple[int, int], int, pygame.Color]] = []
    scores = np.zeros(POINT_SAMPLES)
    # Choose a block weighted by diff, then random position in block
    flat_idx = multinomial(block_probs)

    # Choose the block with the highest diff
    bx = flat_idx // block_diffs.shape[1]
    by = flat_idx % block_diffs.shape[1]
    for i in range(POINT_SAMPLES):
        # radius = randint(1, int(sqrt(current_diff) / 150))

        radius = randint(1, int(sqrt(block_diffs[bx, by]) / 30) + 5)

        pos = (randrange(bx * BLOCK_SIZE, (bx + 1) * BLOCK_SIZE),
               randrange(by * BLOCK_SIZE, (by + 1) * BLOCK_SIZE))
        # color = pygame.Color(randint(0, 255), randint(0, 255), randint(0, 255))
        color = color_vary(sample.get_at(pos), 10)
        alpha = choice([64, 128, 192, 255])

        circles.append((pos, radius, color))

        rect = circle_bounds(pos, radius + 1, target.get_size())
        target_patch = target.subsurface(rect)
        current_patch = current.subsurface(rect)

        # Recompute the global score from only the changed region.
        old_patch_diff = surf_diff(target_patch, current_patch)
        test_patch = current_patch.copy()
        local_pos = (pos[0] - rect.x, pos[1] - rect.y)
        draw_circle(test_patch, color, local_pos, radius, alpha)
        new_patch_diff = surf_diff(target_patch, test_patch)
        scores[i] = current_diff - old_patch_diff + new_patch_diff

    best_idx = np.argmin(scores)
    score = scores[best_idx]
    pos, radius, color = circles[best_idx]

    if score <= current_diff * 1.0001:
        draw_circle(current, color, pos, radius, alpha)
        print(score, round((1 - score / start_diff) * 100, 2), "% \r", end="")
        return score
    return False


@njit(fastmath=True)
def diff_img(array1: np.ndarray, array2: np.ndarray) -> np.ndarray:
    return np.abs(array1.astype(np.int16) - array2.astype(np.int16))


@njit(fastmath=True, parallel=True)
def diff_by_block(array1: np.ndarray, array2: np.ndarray, block_size: int) -> np.ndarray:
    w_blocks = array1.shape[0] // block_size
    h_blocks = array1.shape[1] // block_size
    diffs = np.zeros((w_blocks, h_blocks), dtype=np.int32)
    diff_img = np.abs(
        (array1.astype(np.int16) - array2.astype(np.int16)).astype(np.int32))
    for by in prange(h_blocks):
        for bx in prange(w_blocks):
            diffs[bx, by] = np.sum(
                diff_img[bx*block_size:(bx+1)*block_size, by*block_size:(by+1)*block_size])
    return diffs


current_diff = surf_diff(image, canvas)
start_diff = current_diff


def main():
    # for x in range(0, width, INIT_GRID_SIZE):
    #     for y in range(0, height, INIT_GRID_SIZE):
    #         draw_circle(canvas, image.get_at((x, y)), (x, y), int(INIT_GRID_SIZE / 1.3))

    # for _ in range(width * height // 1000):
    #     x = randint(0, width-1)
    #     y = randint(0, height-1)
    #     draw_circle(canvas, image.get_at((x, y)),
    #                 (x, y), randint(5, 75))

    global current_diff
    show_diff = False
    iteration = 0
    block_diffs = diff_by_block(pygame.surfarray.pixels3d(
        image), pygame.surfarray.pixels3d(canvas), BLOCK_SIZE)
    probs = softmax_cumprob(block_diffs.flatten(), temp=SOFTMAX_TEMP)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                print()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    show_diff = not show_diff

        if iteration % 20 == 0:
            block_diffs = diff_by_block(pygame.surfarray.pixels3d(
                image), pygame.surfarray.pixels3d(canvas), BLOCK_SIZE)
            probs = softmax_cumprob(block_diffs.flatten(), temp=SOFTMAX_TEMP)

        res = do_iteration(target=image, current=canvas, sample=image,
                           current_diff=current_diff, block_diffs=block_diffs, block_probs=probs)
        iteration += 1
        if res:
            current_diff = res
            if show_diff:
                pygame.surfarray.blit_array(screen, diff_img(
                    pygame.surfarray.pixels3d(image), pygame.surfarray.pixels3d(canvas)))
            else:
                screen.blit(canvas, (0, 0))

            pygame.display.flip()


if __name__ == "__main__":
    main()
