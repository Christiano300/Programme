from math import pi, sin, cos
from random import randint
import pygame
from dataclasses import dataclass, field
from typing import MutableSequence
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

base_image = pygame.image.load("files/firework.png").convert_alpha()
pxarray = pygame.PixelArray(base_image)

TWO_PI = 2 * pi
# n = 7
# print(pxarray[n, n])
# # print(base_image.unmap_rgb(pxarray[n, n]))
# p = pxarray[n, n]
# print(p >> 24 & 255, p >> 16 & 255, p >> 8 & 255, p & 255)
# exit(0)


@dataclass
class Firework:
    pos: MutableSequence[int]
    vel: MutableSequence[float]
    color: int
    distance: int
    size: int
    n: int
    image: pygame.Surface = field(default=None, init=False)
    time: int = field(default=None, init=False)

    def draw(self):
        for i in range(self.n):
            alpha = i / self.n * TWO_PI
            x = cos(alpha) * self.distance + self.pos[0]
            y = sin(alpha) * self.distance + self.pos[1]
            screen.blit(self.image, (x, y))

    def make_image(self):
        self.time = 0
        pxarray = pygame.PixelArray(base_image.copy())
        r = self.color >> 16 & 255
        g = self.color >> 8 & 255
        b = self.color & 255
        for i in range(pxarray.shape[0]):
            for j in range(pxarray.shape[1]):
                a = pxarray[i, j] >> 24 & 255
                test = r * a // 256, g * a // 256, b * a // 256, a
                pxarray[i, j] = test
        self.image = pygame.transform.smoothscale(
            pxarray.surface, (self.size, self.size))
        pxarray.close()


firework_list: list[Firework] = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button != 0:
                pos = list(event.pos)
                firework_list.append(Firework(pos, [0, 0], randint(
                    0, 0xffffff), 0, randint(20, 40), randint(5, 50)))
                firework_list[-1].make_image()

    screen.fill(0)
    
    for f in firework_list:
        f.draw()
        f.pos[0] += f.vel[0]
        f.pos[1] += f.vel[1]
        f.vel[1] += 0.01
        f.distance += .7
        f.time += 1


    pygame.display.update()
    clock.tick(60)
