import os
from random import choice
import pygame
pygame.init()

size = width, height = 810, 540
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()
BLOCKSIZE = 16
PADDING = 7

blocks = []  # [..., [index, posx(>), posy(\/)], ...]
blocks = [[0, 0, 10], [1, 1, 10], [2, 2, 10], [3, 3, 10],
          [4, 4, 10], [5, 5, 10], [6, 6, 10], [7, 7, 10],
          [8, 8, 10], [9, 9, 10], [10, 10, 10], [11, 11, 10],
          [12, 12, 10], [13, 13, 10], [14, 14, 10], [15, 15, 10],
          [12, 5, 0], [3, 5, 1], [10, 5, 2], [13, 5, 3]]
menu_open = False
f1_mode = False
menu_buttons = [[None, None, False] for _ in range(16)]

blocknames = [i for i in sorted(os.listdir(
    "files/minecraft-textures")) if "wool" in i]
textures = [pygame.transform.scale(pygame.image.load(
    f"files/minecraft-textures/{i}"), [BLOCKSIZE, BLOCKSIZE]) for i in blocknames]


def resize(size: tuple):
    global width, height, screen, menu_buttons
    width = max(256, round(size[0] / BLOCKSIZE) * BLOCKSIZE)
    height = max(144, round(size[1] / BLOCKSIZE) * BLOCKSIZE)
    size = width, height
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    menu_buttons = [[[PADDING + i * (w := round((width - PADDING * 2) / 16)) + 3, PADDING + 3], \
                [w - 6, w - 6], menu_buttons[i][2]] for i in range(16)]


def button_pressed(bpos: tuple, bsize: tuple, mpos: tuple):
    return mpos[0] in range(bpos[0], bpos[0] + bsize[0]) \
        and mpos[1] in range(bpos[1], bpos[1] + bsize[1])


def draw():
    screen.fill("0x000000")
    for i in blocks:
        screen.blit(textures[i[0]], (i[1] * BLOCKSIZE, i[2] * BLOCKSIZE))
    if not f1_mode:
        if menu_open:  # Draw menu
            s = pygame.Surface((width, h := menu_buttons[0][1][0] + menu_buttons[0][0][1] * 2), pygame.SRCALPHA)
            pygame.draw.rect(s, "0x00000080", (0, 0, width, h), 0, 20)
            screen.blit(s, (0, 0))
            for i, button in enumerate(menu_buttons):
                screen.blit(pygame.transform.scale(textures[i], button[1]), button[0])
                if button[2]:
                    pygame.draw.rect(screen, "0xffffff", (button[0][0] - 2, button[0][1] - 2, \
                        button[1][0] + 4, button[1][1] + 4), 2, 2)
            pygame.draw.rect(screen, "0xffffff", (5, h + 15, 30, 30))
            pygame.draw.line(screen, "0x000000", (10, h + 40), (20, h + 20), 3)
            pygame.draw.line(screen, "0x000000", (20, h + 20), (30, h + 40), 3)

        else:
            # Draw menu button
            pygame.draw.rect(screen, "0xffffff", (5, 5, 30, 30))
            pygame.draw.line(screen, "0x000000", (10, 10), (20, 30), 3)
            pygame.draw.line(screen, "0x000000", (20, 30), (30, 10), 3)
    pygame.display.update()

def tile():
    global blocks
    colors = [menu_buttons.index(i) for i in menu_buttons if i[2]]
    if len(colors):
        blocks = []
        for i in range(width // BLOCKSIZE):
            for j in range(height // BLOCKSIZE):
                blocks.append([choice(colors), i, j])
    draw()

resize((810, 540))
draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(clock.get_fps())
            pygame.quit()
            quit()

        elif event.type == pygame.VIDEORESIZE:
            resize(event.size)
            tile()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if menu_open:
                if button_pressed((5, 75), (30, 30), event.pos):
                    menu_open = False
                    draw()
                    break
                for i, button in enumerate(menu_buttons):
                    if button_pressed(button[0], button[1], event.pos):
                        menu_buttons[i][2] = False if menu_buttons[i][2] else True
                        tile()
                        break
            else:
                if button_pressed((5, 5), (30, 30), event.pos):
                    menu_open = True
                    draw()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
                
            elif event.key == pygame.K_r:
                colors = [menu_buttons.index(i) for i in menu_buttons if i[2]]
                tile()
                            
            elif event.key == pygame.K_F1:
                f1_mode = False if f1_mode else True
                draw()
            
            elif event.key == pygame.K_s:
                pygame.image.save(screen, "files/concrete.png")

    clock.tick(60)
