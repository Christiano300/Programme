from random import randrange, random
from math import ceil
import pygame
pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

chars = "abcdefghijklmnopqrstuvwxyzäöü"
current_char = ""
time_reset = 60 * 5
time_left = 0
font = pygame.font.Font(None, 70)
score_font = pygame.font.Font(None, 25)
offset = 0
correct = False
score = 0
life = 20
dir = 0

BLACK = pygame.Color(0, 0, 0)
CORRECT = pygame.Color(0, 200, 0)
WRONG = pygame.Color(200, 0, 0)
WRONG_START = pygame.Color(0, 0, 200)
background = BLACK

def draw_text(surf: pygame.Surface, font: pygame.font.Font, text: str, pos: tuple[int, int], color: pygame.Color):
    text_surface = font.render(text, True, color)
    surf.blit(text_surface, pos)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            if event.unicode == current_char:
                score += int(50 * time_left / time_reset) + 50
                time_left = 0
                correct = True
            else:
                time_left = 0
                correct = False

    if time_left <= 0:
        if not correct:
            if score == 0:
                background = WRONG_START
            else:
                life -= 1
                background = WRONG
                if life <= 0:
                    print(f"Game Over. Score: {score}")
                    pygame.quit()
                    quit()
        else:
            background = CORRECT
        current_char = chars[randrange(len(chars))]
        time_left = time_reset
        time_reset = (time_reset * 0.975)
        offset = random()
        dir = randrange(4)
        correct = False


    else:
        time_left -= 1

    screen.fill(background)
    background = pygame.Color.lerp(background, BLACK, .1)
    x: int = ((0 if dir == 0 else width) + (1 if dir == 0 else -1) * time_left / time_reset * width) if dir % 2 == 0 else offset * (width - 50) + 10 # type: ignore
    y: int = ((0 if dir == 1 else height) + (1 if dir == 1 else -1) * time_left / time_reset * height) if dir % 2 == 1 else offset * (height - 50) + 10 # type: ignore
    draw_text(screen, font, current_char.upper(), (x, y), (255, 255, 255))
    draw_text(screen, score_font, f"Score: {score}", (5, 5), (255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 50), (width - life * 10, 0, life * 10, 10))

    pygame.display.update()
    clock.tick(60)
