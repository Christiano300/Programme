from math import sin
from random import uniform
import pygame
pygame.init()

size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
tiles = pygame.sprite.Group()

x2 = pygame.transform.scale2x
tile = pygame.image.load("files/isotile.png").convert_alpha()
size = width, height = 720, 640 + tile.get_height() // 2
screen = pygame.display.set_mode(size)

w, h = tile.get_width(), tile.get_height()


class IsoTile(pygame.sprite.Sprite):
    def __init__(self, x, y, img):
        super().__init__(tiles)
        self.image: pygame.Surface = img
        self.x, self.y = x, y
        self.rect = img.get_rect()
        self.rect.left, self.rect.top = x, y
        self.height = 0

    def draw(self):
        screen.blit(self.image, (self.x * (-.5 * w) + self.y * (.5 * w) + width // 2 - w // 2,
                                 self.x * (.25 * h) + self.y * (.25 * h) - self.height - height // 2))


tilenx = tileny = 20
grid = [[IsoTile(i, j, tile) for j in range(tileny)] for i in range(tilenx)]

sx = sy = 0
frame = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEMOTION:
            if sx in range(tilenx) and sy in range(tileny):
                grid[sx][sy].height = 0
            x, y = event.pos
            x -= width // 2 + w // 2
            sx = y / h * 2 - x / w
            sy = y / h * 2 + x / w
            sx = round(sx) - 1
            sy = round(sy)
            if sx in range(tilenx) and sy in range(tileny):
                grid[sx][sy].height = 20

    # if not (sx in range(tilenx) and sy in range(tileny)):
    for i in range(tilenx):
        for j in range(tileny):
            grid[i][j].height = sin(i + frame / 2) * \
                20 - sin(j + frame / 3) * 40
            frame += 0.0001

    screen.fill(0xC99FFF)
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if i == sx and j == sy:
                col.draw()
            else:
                col.draw()

    pygame.display.update()
    clock.tick(60)
