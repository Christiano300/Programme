from hashlib import sha1
from math import cos, pi, sin, sqrt
from random import randint
import pygame
pygame.init()

size = width, height = pygame.display.get_desktop_sizes()[0] # type: ignore
# size = width, height = 256, 256 # type: ignore
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

print(screen.get_height(), screen.get_width())

stars = [[randint(50, 640), randint(-360, 360), randint(0, 1000)] for _ in range(1000)]
# stars = [[x / 15, y / 15, z] for x in (60, 640) for y in range(-360, 360, 100) for z in range(0, 1000, 100)]
front = False
back = False

r = 50
theta = 0

pos = 0
acc = 0
vel = 0
rot = 0

zoom = 25
zs = 10

xofs = 0
yofs = 0

pressed = [False, False, False, False]

def screenspace(star: list[int]) -> tuple[int, int]:
    x, y, z = star

    z2 = sin(theta + z / 100) + x * sin(theta + z / 100) / 200 + zs
    x *= cos(theta + z / 100)

    x *= zoom / z2
    y *= zoom / z2

    cr = cos(rot)
    ci = sin(rot)

    x, y = x * cr - y * ci, x * ci + y * cr

    return x + xofs + width // 2, y + height // 2 + yofs # type: ignore

star_recent_pos = [screenspace(star) for star in stars]

_perm = [sha1(f"{i}".encode(), usedforsecurity=False).digest()[0] for i in range(256)]
def simplex_1d(x):
    i0 = int(x)
    i1 = i0 + 1
    x0 = x - i0
    x1 = x0 - 1

    t0 = 1 - x0 * x0
    t0 *= t0
    n0 = t0 * t0 * gradient(_perm[i0 & 0xff], x0)

    t1 = 1 - x1 * x1
    t1 *= t1
    n1 = t1 * t1 * gradient(_perm[i1 & 0xff], x1)

    return (0.395 * (n0 + n1))

def gradient(hash: int, x: float) -> float:
    h = hash & 15
    grad = 1 + (h & 7)              # Gradient value 1.0, 2.0, ..., 8.0
    if (h & 8) != 0: grad = -grad   # Set a random sign for the gradient
    return (grad * x)               # Multiply the gradient with the distance

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                front = True
            elif event.key == pygame.K_s:
                back = True
            elif event.key == pygame.K_UP:
                pressed[0] = True
            elif event.key == pygame.K_DOWN:
                pressed[1] = True
            elif event.key == pygame.K_LEFT:
                pressed[2] = True
            elif event.key == pygame.K_RIGHT:
                pressed[3] = True

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_q, pygame.K_ESCAPE):
                pygame.quit()
                quit()
            elif event.key == pygame.K_w:
                front = False
            elif event.key == pygame.K_s:
                back = False
            elif event.key == pygame.K_UP:
                pressed[0] = False
            elif event.key == pygame.K_DOWN:
                pressed[1] = False
            elif event.key == pygame.K_LEFT:
                pressed[2] = False
            elif event.key == pygame.K_RIGHT:
                pressed[3] = False
                
            elif event.key == pygame.K_r:
                screen.fill(0)

    if pressed[0]:
        yofs -= 5
    elif pressed[1]:
        yofs += 5
    if pressed[2]:
        xofs -= 5
    elif pressed[3]:
        xofs += 5
    
    

    screen.fill(0)
    
    # for star in stars:
    #     screenpos = screenspace(star)
    #     # pygame.draw.rect(screen, 0xffffff, (*screenpos, 2, 2))
    #     pygame.draw.aaline(screen, 0xffffff, screenpos, (screenpos[0], screenpos[1] + 1))
    
    new_star_positions = [screenspace(star) for star in stars]
    for old, new in zip(star_recent_pos, new_star_positions):
        pygame.draw.aaline(screen, 0xffffff, old, new)
    star_recent_pos = new_star_positions

    if front:
        zoom *= 1.01

    elif back:
        zoom /= 1.01

    theta += 0.002
    # pos += .002
    acc = simplex_1d(pos) * 100
    vel += acc / 85
    vel *= 0.99
    rot += vel / 6500

    pygame.draw.line(screen, 0x0000ff, (50, 200 - acc), (200, 200 - acc))
    pygame.draw.line(screen, 0xff0000, (50, 200 - vel), (200, 200 - vel))
    pygame.draw.line(screen, 0x00ff00, (50, 200 - rot * 100), (200, 200 - rot * 100))
    pygame.draw.line(screen, 0xffffff, (50, 200), (200, 200))

    pygame.display.update()
    clock.tick(60)
