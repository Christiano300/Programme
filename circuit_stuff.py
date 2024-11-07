from random import randint
from colorsys import hsv_to_rgb
import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

drawers = []
delete = []


def reset():
    global drawers
    screen.fill((0, 0, 0))
    drawers = []
    for i in range(0, width, 8):
        drawers.append({"x": i, "y": height, "dir": 0,
                       "size": randint(10, 100), "cooldown": 30, "color": randint(0, 360)}) # 140, 230


def colorchange(color: int, factor: float):
    diff = randint(140, 230) - color
    return (color + diff * factor) % 360


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset()
    for i, drawer in enumerate(drawers):
        color = [i * 255 for i in hsv_to_rgb(drawer['color'] / 360, 1, 1)]

        pygame.draw.circle(
            screen, color, (drawer['x'], drawer['y']), drawer['size'])
        drawer['color'] = colorchange(drawer['color'], .7)

        if not drawer['cooldown'] and not randint(0, 40):
            zuf = randint(0, 3)
            if not zuf:
                pass
                # delete.append(i)
            elif zuf == 1:
                drawer['dir'] = min(max(-1, drawer['dir'] + 1), 1)
            elif zuf == 2:
                drawer['dir'] = min(max(-1, drawer['dir'] + -1), 1)
            elif zuf == 3:
                drawer['size'] = max(1, drawer['size'] * .9)
            drawer['cooldown'] = randint(30, 50)

        drawer['x'] += drawer['dir']
        if drawer['y'] == -drawer['size']:
            delete.append(i)

        drawer['y'] -= 1
        if drawer['x'] < 0 and drawer['x'] >= width:
            drawer['dir'] *= -1

        if drawer['cooldown']:
            drawer['cooldown'] -= 1

    drawers = [d for i, d in enumerate(drawers) if not i in delete]
    delete = []

    pygame.display.update()
    # clock.tick(60)
