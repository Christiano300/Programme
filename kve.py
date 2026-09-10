from time import perf_counter
from tqdm import tqdm
from numba import njit
import numpy as np
import pygame

pygame.init()
size = width, height = 400, 400
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

BANDWIDTH = 20
N_POINTS = 200
X = np.random.uniform(50, 350, N_POINTS)
Y = np.random.uniform(50, 350, N_POINTS)
VALUES = np.random.uniform(0, 255, N_POINTS).astype(np.uint8)
first = True


@njit
def kernel(x): return np.exp(-1 * x * x)
# @njit
# def kernel(x): return np.max(0, - np.abs(x) + 1)

@njit
def smoothstep(x): return x * x * (3 - 2 * x)


def kde(points, x, y):
    total = 0
    for point, _ in points:
        distance = point.distance_to(pygame.Vector2(x, y))
        total += kernel(distance / BANDWIDTH)
    total /= (BANDWIDTH * len(points))
    return total


@njit(error_model="numpy", fastmath=True)
def kve(points_x, points_y, values, x, y):
    distance = np.hypot(points_x - x, points_y - y)
    density = np.sum(kernel(distance / BANDWIDTH))

    value = np.sum(kernel(distance / BANDWIDTH) * values)

    return (density / (BANDWIDTH * len(points_x)), value / density if density > 0 else 0)


@njit(fastmath=True)
def cmap(value):
    return (193 + value * 62, 88 + value * 167, value * 255)


@njit(fastmath=True)
def cmult(color, mult):
    return (int(color[0] * mult), int(color[1] * mult), int(color[2] * mult))


@njit(fastmath=True, parallel=True)
def draw_kve(pxarray: np.ndarray, X: np.ndarray, Y: np.ndarray, VALUES: np.ndarray):
    densities = np.zeros((width, height), dtype=np.float32)
    values = np.zeros((width, height), dtype=np.float32)

    for x in range(width):
        for y in range(height):
            density, weight = kve(X, Y, VALUES, x, y)
            densities[x, y] = density
            values[x, y] = weight

    max_density = np.max(densities)

    for x in range(width):
        for y in range(height):
            density = densities[x, y]
            value = values[x, y]
            density = smoothstep(density / max_density) if max_density > 0 else 0
            color = cmap(value / 255)
            pxarray[x, y] = cmult(color, density)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if first:
                draw_kve(pygame.surfarray.pixels3d(screen), X, Y, VALUES)
                first = False
            start = perf_counter()
            draw_kve(pygame.surfarray.pixels3d(screen), X, Y, VALUES)
            end = perf_counter()
            print(f"Time taken: {end - start:.4f} seconds")
            X = np.random.uniform(50, 350, N_POINTS)
            Y = np.random.uniform(50, 350, N_POINTS)
            VALUES = np.random.uniform(0, 255, N_POINTS).astype(np.uint8)
            pygame.display.update()

    clock.tick(60)
