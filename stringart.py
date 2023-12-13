import pygame
import numpy as np
from math import sin, cos, pi

pygame.init()

size = width, height = 500, 500
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

radius = min(width, height) // 2 - 20

NAILS = 100
POSITIONS = np.array([(int(width // 2 + radius * cos(2 * pi * i / NAILS)),
                       int(height // 2 + radius * sin(2 * pi * i / NAILS))) for i in range(NAILS)])

screen.fill(0xffffff)

mask = pygame.Surface(size)
mask.fill(0)
pygame.draw.circle(mask, 0xffffff, (width // 2, height // 2), radius)
mask = pygame.mask.from_surface(mask)

image = mask.to_surface(pygame.image.load(
    r"files\parallax\plx1.png").convert(screen))
new_image = pygame.Surface((radius * 2, radius * 2))
new_image.blit(image, (0, 0), (image.get_width() // 2 - radius,
               image.get_height() // 2 - radius, radius * 2, radius * 2))
image = new_image

current_nail = 0


MAX_VALUE = 0xffffff * width * height


def diff(surface1, surface2):
    pxarray1 = pygame.PixelArray(surface1)
    pxarray2 = pygame.PixelArray(surface2)
    return (sum(sum(i) for i in
                            pxarray1.compare(pxarray2, weights=(0.5, 0.5, 0.5))))  # type: ignore


cords = pygame.Surface(image.get_size())
screen_crop = pygame.Rect((screen.get_width() - cords.get_width()) // 2,
                          (screen.get_height() - cords.get_height()) // 2,
                          cords.get_width(), cords.get_height())

active = True
iteration = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    if active:
        best_value = -float("inf")
        best_nail = current_nail
        for i in range(NAILS):
            cords.blit(screen, (0, 0), screen_crop)
            pygame.draw.aaline(cords, 0, POSITIONS[current_nail], POSITIONS[i])
            value = diff(cords, image)
            if value < best_value:
                best_value = value
                best_nail = i
        if best_nail == current_nail:
            active = False
            print("something probably went wrong and this is the end at iteration " + str(iteration))
        else:
            pygame.draw.aaline(screen, 0, POSITIONS[current_nail], POSITIONS[best_nail])
            current_nail = best_nail
        iteration += 1

    pygame.display.update()
    clock.tick(60)
