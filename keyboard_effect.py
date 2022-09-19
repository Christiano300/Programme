import pygame
import json

from pygaminter import get_font, center
pygame.init()

size = width, height = 800, 300
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

font = get_font("Calibri_35b")

with open("files/keyboard.json") as f:
    deeta = json.load(f)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(0xffffff)
    for key in deeta:
        pygame.draw.rect(screen, 0, key['pos'])
        pygame.draw.rect(screen, 0xffffff, key['pos'], 3)
        text = font.render(key['key'], True, "0xffff50")
        pos = center(key['pos'][2], key['pos'][3], text.get_width(), text.get_height())
        pos[0] += key['pos'][0]
        pos[1] += key['pos'][1]
        screen.blit(text, pos)
        
    
    pygame.display.update()
    clock.tick(60)