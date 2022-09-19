from math import ceil, sqrt
from random import randint

import pygame

from pygaminter import Button

pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

cookies = 0
cps = 0
cpf = 0.0
cookiefont = pygame.font.SysFont("Lucida Bright", 40, True)
cpsfont = pygame.font.SysFont("Lucida Sans", 20)
plusfont = pygame.font.SysFont("Arial Black", 17)
makertitlefont = pygame.font.SysFont("Calibri", 20, True)
makersubfont = pygame.font.SysFont("Calibri", 15, True)
plusgroup = pygame.sprite.Group()
cooldown = 0

makers = [{"name": "Cursor", "base_price": 15, "price_multi": 1.15, "cps": .1, "bought": 0},
          {"name": "Grandma", "base_price": 100,
              "price_multi": 1.15, "cps": 1, "bought": 0},
          {"name": "Farm", "base_price": 1100,
              "price_multi": 1.15, "cps": 8, "bought": 0},
          {"name": "Mine", "base_price": 12000,
           "price_multi": 1.15, "cps": 47, "bought": 0},
          {"name": "Factory", "base_price": 130000,
           "price_multi": 1.15, "cps": 260, "bought": 0},
          {"name": "Bank", "base_price": 1400000,
           "price_multi": 1.15, "cps": 1400, "bought": 0},
          {"name": "Temple", "base_price": 20000000,
           "price_multi": 1.15, "cps": 7800, "bought": 0},
          {"name": "Wizard Tower", "base_price": 330000000,
           "price_multi": 1.15, "cps": 50000, "bought": 0}]


cookie = pygame.Surface((200, 200), pygame.SRCALPHA)

pygame.draw.circle(cookie, "0xc47a58", (100, 100), 100)
pygame.draw.circle(cookie, "0x542612", (120, 50), 10)
pygame.draw.circle(cookie, "0x542612", (160, 90), 10)
pygame.draw.circle(cookie, "0x542612", (90, 100), 10)
pygame.draw.circle(cookie, "0x542612", (50, 60), 10)
pygame.draw.circle(cookie, "0x542612", (100, 155), 10)


def pos_inside_circle(pos: list, cx: int, cy: int, radius: int) -> bool:
    return sqrt((pos[0] - cx) ** 2 + (pos[1] - cy) ** 2) < radius


def buy(idx: int):
    """Kauft das Teil

    Args:
        idx (int): Index vom Teil
    """
    global cookies
    maker = makers[idx]
    price = ceil(maker["price_multi"] ** maker["bought"] * maker["base_price"])
    if price <= cookies:
        global cps, cpf
        cps += maker["cps"]
        cpf = cps / 60
        maker["bought"] += 1
        cookies -= price


class Plus(pygame.sprite.Sprite):
    def __init__(self, pos: list, text: str, color: pygame.Color, font: pygame.font.Font):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(s := font.size(text), pygame.SRCALPHA)
        self.image.fill(0x00000000)
        self.image.blit(font.render(text, True, color), (0, 0))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = pos[0] - s[0] // 2, pos[1] - s[1] // 2
        self.fade = 255
        plusgroup.add(self)

    def update(self):
        if self.fade:
            self.rect.move_ip(0, -1)
            self.image.set_alpha(self.fade)
            self.fade -= 3
        else:
            self.kill()


for i, maker in enumerate(makers):
    pos = i // 2 * 155 + 15, i % 2 * 65 + 340
    pygame.draw.rect(screen, 0x002138, (*pos, 145, 55), 5, 13)
    Button((*pos, 145, 55), command=lambda x=i: buy(x))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pos_inside_circle(event.pos, width // 2, 120, 100):
                cookies += 1
                Plus([event.pos[0] + randint(-5, 5), event.pos[1] +
                     randint(-5, 5)], "+1", 0xffffffff, plusfont)
                cooldown = 20
            else:
                Button.group.update(event)
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            Button.group.update(event)

    screen.fill(0x173951)

    if cooldown:
        screen.blit(pygame.transform.scale(cookie, (200 + cooldown, 200 +
                    cooldown)), (220 - cooldown // 2, 20 - cooldown // 2))
    else:
        screen.blit(cookie, (220, 20))

    s = cookiefont.size(f"Cookies: {round(cookies)}")[0]
    screen.blit(cookiefont.render(
        f"Cookies: {round(cookies)}", True, 0xffd80000), (width // 2 - s // 2, 230))
    s = cpsfont.size(f"CPS: {round(cps, 1)}")[0]
    screen.blit(cpsfont.render(
        f"CPS: {round(cps, 1)}", True, 0xefd55300), (width // 2 - s // 2, 280))

    plusgroup.draw(screen)

    for i, maker in enumerate(makers):
        pos = i // 2 * 155 + 15, i % 2 * 65 + 340
        pygame.draw.rect(screen, 0x002138, (*pos, 145, 55), 5, 13)
        s1 = makertitlefont.size(maker["name"])
        screen.blit(makertitlefont.render(
            maker["name"], True, 0xffffffff), (145 // 2 - s1[0] // 2 + pos[0], pos[1] + 10))

        if (price := ceil(maker["price_multi"] ** maker["bought"] * maker["base_price"])) <= cookies:
            color = 0x66ff66ff
        else:
            color = 0xff6d7cff

        s2 = makersubfont.size(str(price))
        screen.blit(makersubfont.render(str(price), True, color),
                    (145 // 2 - s2[0] // 2 + pos[0], pos[1] + 10 + s1[1]))

    cookies += cpf
    plusgroup.update()
    if cooldown:
        cooldown -= 2

    pygame.display.update()
    clock.tick(60)
