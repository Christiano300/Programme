import pygame
from math import pi, sin, cos
pygame.init()

size = width, height = 640, 480
hwidth, hheight = width / 2, height / 2
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()


def deg_to_rad(deg: float):
    return deg / 180 * pi


planets = [[0xcec68a, 7, 100, 0, 3], [0xad3400, 12, 200, 50, 2.4],
           [0xe55220, 13, 400, 160, 1.6], [0x008fff, 14, 300, 200, 2]]
roty = 0.0
vroty = 0.0
rotx = 0.0
vrotx = 0.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size
            hwidth, hheight = width / 2, height / 2
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            elif event.key == pygame.K_UP:
                vroty += .25
            elif event.key == pygame.K_DOWN:
                vroty -= .25
            elif event.key == pygame.K_RIGHT:
                vrotx += .25
            elif event.key == pygame.K_LEFT:
                vrotx -= .25
    roty += vroty
    rotx += vrotx
    screen.fill(0)
    pygame.draw.circle(screen, 0xffffa0, (hwidth, hheight), 20)
    for idx, i in enumerate(planets):
        pygame.draw.ellipse(screen, 0xffffff, (hwidth - abs(cos(deg_to_rad(rotx)) * i[2]),
                                               hheight - abs(cos(deg_to_rad(roty)) * i[2]),
                                               abs(i[2] * cos(deg_to_rad(rotx)) * 2),
                                               abs(i[2] * cos(deg_to_rad(roty)) * 2)),
                            1)
        pygame.draw.circle(screen, i[0],(cos(deg_to_rad(i[3])) * i[2] * cos(deg_to_rad(rotx)) + hwidth,
                                         sin(deg_to_rad(i[3])) * i[2] * cos(deg_to_rad(roty)) + hheight),
                           i[1])

        planets[idx][3] += i[4]
    pygame.display.update()
    clock.tick(60)
