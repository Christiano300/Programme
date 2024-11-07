from random import choice, randint, uniform
import pygame
import os

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
uhr = pygame.time.Clock()
root, files = next(os.walk("files/minecraft-textures"))[::2]

items = pygame.sprite.Group()


class Item(pygame.sprite.Sprite):

    def __init__(self, pos: tuple, size: int, speed: tuple):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.retexture()
        self.rect = self.texture.get_rect()
        self.rect.left, self.rect.top = pos
        self.pos = list(pos)
        self.vel = list(speed)

    def move(self):
        self.pos = [self.vel[i] + self.pos[i] for i in range(len(self.pos))]
        if self.pos != self.rect.topleft:
            self.rect = self.rect.move(
                (self.pos[0] - self.rect.left, self.pos[1] - self.rect.top))
        self.vel[1] += 0.05

        if self.rect.bottom >= height:
            self.vel[1] = abs(self.vel[1]) * -.96
            self.pos[1] = height - self.size

        if self.rect.left > width:
            self.size = randint(50, 100)
            self.pos[0] = -self.size - 25
            self.pos[1] = randint(0, height - self.size - 50)
            self.vel[0] = uniform(2, 5)
            self.vel[1] = uniform(.2, .8)
            self.retexture()

    def retexture(self):
        self.texture = pygame.image.load(os.path.join(
            root, choice(files))).convert_alpha()
        self.texture = pygame.transform.scale(self.texture,
                                              (self.size, self.size))
        self.rect = self.texture.get_rect()

    def draw(self):
        screen.blit(self.texture, self.pos)


for i in range(20):
    current_item = Item((width, 100), 16, (1, 0.3))
    items.add(current_item)

while True:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT, pygame.MOUSEBUTTONDOWN):
            pygame.quit()
            quit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size

    # screen.fill((0,0,0))
    for i in items:
        i.draw()
        i.move()
    pygame.display.update()
    uhr.tick()
