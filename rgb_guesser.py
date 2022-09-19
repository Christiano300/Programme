from random import randint
import pygame
from pygaminter import Button
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()
scorefont = pygame.font.Font(None, 50)
sliders = pygame.sprite.Group()
mouse_pressed = False
score = 0
randomcolor = (randint(0, 255), randint(0, 255), randint(0, 255))

points = lambda x: max(min(5095160250096001 / 1000000000000000000000 * x ** 3 - 2923348193492581 / 500000000000000000 * x ** 2 + 389600 / 2120641 * x + 1000, 1000), 0)

def submit():
    global randomcolor, score
    guess = rslider.get(), gslider.get(), bslider.get()
    diff = sum((abs(i - j) for i, j in zip(guess, randomcolor)))
    score += int(points(diff))
    
    
    
    randomcolor = (randint(0, 255), randint(0, 255), randint(0, 255))
    

def lerpcolor(a: pygame.Color, b: pygame.Color, t: float) -> float:
    return pygame.Color(int(a.r * (1 - t) + b.r * t), int(a.g * (1 - t) + b.g * t), int(a.b * (1 - t) + b.b * t))

def draw_frame(screen: pygame.Surface, rect: pygame.Rect, color: pygame.Color):
    if not isinstance(rect, pygame.Rect):
        rect = pygame.Rect(rect)
    pygame.draw.rect(screen, 0x979797, (rect.left + 1, rect.top + 1, *rect.size), 3)
    pygame.draw.rect(screen, color, rect)
    pygame.draw.rect(screen, 0, rect, 3)

class Slider(pygame.sprite.Sprite):
    def __init__(self, rect: pygame.Rect, color: pygame.Color | int, mousecolor: pygame.Color | int, max: int):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(rect)
        self.mousecolor = mousecolor
        self.pressed = False
        self.image = pygame.Surface(self.rect.size)
        self.bg = pygame.Surface(self.rect.size)
        self.max = max
        self.progress = 0
        for i in range(w := self.rect.width):
            pygame.draw.rect(self.bg, lerpcolor(pygame.Color(
                0, 0, 0, 255), color, i / w), (i, 0, 1, self.rect.height))
        self.image.blit(self.bg, (0, 0))
        pygame.draw.circle(self.image, self.mousecolor, (self.progress,
                           self.rect.height / 2), self.rect.height / 2.5, 2)
        sliders.add(self)

    def update(self, mousepos: tuple, pressed: int):
        if pressed == 1:
            if pygame.Rect.collidepoint(self.rect, mousepos):
                self.pressed = True
        elif pressed == -1:
            self.pressed = False
        elif self.pressed:
            self.progress = min(
                max(mousepos[0], self.rect.left), self.rect.right) - self.rect.left
            self.image.blit(self.bg, (0, 0))
            pygame.draw.circle(self.image, self.mousecolor, (self.progress,
                               self.rect.height / 2), self.rect.height / 2.5, 2)

    def get(self) -> int:
        return int(self.progress * self.max / self.rect.width)
    
    def set(self, value: int):
        self.progress = value * self.rect.width / self.max


rslider = Slider((350, 300, 150, 23), pygame.Color(
    0xff0000ff), pygame.Color(0xffffffff), 255)
gslider = Slider((350, 350, 150, 23), pygame.Color(
    0x00ff00ff), pygame.Color(0xffffffff), 255)
bslider = Slider((350, 400, 150, 23), pygame.Color(
    0x0000ffff), pygame.Color(0xffffffff), 255)
Button((75, 320, 200, 65), "Submit", 0xf0f0f0, submit)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Button.group.update(event)
            sliders.update(event.pos, 1)
            mouse_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            Button.group.update(event)
            sliders.update(event.pos, -1)
            mouse_pressed == False

    screen.fill(0xf0f0f0)
    if mouse_pressed:
        sliders.update(pygame.mouse.get_pos(), 0)
    sliders.draw(screen)
    Button.group.draw(screen)
    r, g, b = rslider.get(), gslider.get(), bslider.get()
    draw_frame(screen, (520, 290, 40, 40), (r & 255) << 16)
    draw_frame(screen, (520, 340, 40, 40), (g & 255) << 8)
    draw_frame(screen, (520, 390, 40, 40), (b & 255))
    screen.blit(scorefont.render(f"Score: {score:05d}", True, 0), (50, 390))
    draw_frame(screen, (50, 50, 200, 200), randomcolor)

    pygame.display.update()
    clock.tick(60)
