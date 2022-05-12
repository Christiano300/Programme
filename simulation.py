import pygame
import sys
import math
import os
pygame.init()
groesse = breite, hoehe = 640, 640
screen = pygame.display.set_mode(groesse)


def draw_background():
    pygame.draw.rect(screen, [0, 0, 0, 0], [0, 0, breite, hoehe], 0)
    pygame.draw.circle(screen, [255, 255, 255], [320, 320], 1, 0)


class Partikel(pygame.sprite.Sprite):
    def __init__(self, farbe, groesse, ort, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(groesse)
        self.image.fill(farbe)
        self.rect = self.image.get_rect()
        self.pos = ort
        self.rect.left, self.rect.top = ort
        self.speed = speed

    def bewegen(self):
        for i in range(len(self.pos)):
            self.pos[i] += self.speed[i]
        if self.pos != self.rect.topleft:
            self.rect = self.rect.move(
                [self.pos[0] - self.rect.left, self.pos[1] - self.rect.top])

    def apply_gravity(self, position, mass):
        x, y = self.rect.center
        distance = math.sqrt(abs(x - position[0] ** 2 + y - position[1] ** 2))
        x_d = position[0] - x
        y_d = position[1] - y
        try:
            dir_x = (1 / math.sqrt(x_d ** 2 + y_d ** 2)) * x_d
            dir_y = (1 / math.sqrt(x_d ** 2 + y_d ** 2)) * y_d
            self.speed[0] += mass / distance * dir_x
            self.speed[1] += mass / distance * dir_y
        except ZeroDivisionError:
            pass


def animieren(gruppe):
    draw_background()
    for rechteck in gruppe:
        rechteck.apply_gravity([320, 320], 10)
        rechteck.bewegen()
        os.system('cls')
        print(rechteck.rect)
    # for rechteck in gruppe:
    #     gruppe.remove(rechteck)
    #     if pygame.sprite.spritecollide(rechteck, gruppe, False):
    #         rechteck.speed[0] = -rechteck.speed[0]
    #         rechteck.speed[1] = -rechteck.speed[1]
    #     gruppe.add(rechteck)
        if rechteck.rect.left < 0 or rechteck.rect.right > breite:
            rechteck.kill()
        if rechteck.rect.top < 0 or rechteck.rect.bottom > hoehe:
            rechteck.kill()
        # if rechteck.rect.left > breite:
        #     rechteck.rect.move_ip(0, rechteck.rect.top)
        # elif rechteck.rect.right < 0:
        #     rechteck.rect.move_ip(breite, rechteck.rect.top)

        # elif rechteck.rect.top > hoehe:
        #     rechteck.rect.move_ip(rechteck.rect.left, 0)
        # elif rechteck.rect.bottom < 0:
        #     rechteck.rect.move_ip(rechteck.rect.left, hoehe)
        screen.blit(rechteck.image, rechteck.rect)
    pygame.display.flip()


gruppe = pygame.sprite.Group()
uhr = pygame.time.Clock()

partikel = Partikel([255, 255, 150], [3, 3], [100, 200], [1, 0])
gruppe.add(partikel)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    animieren(gruppe)
    uhr.tick(60)
