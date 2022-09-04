from random import choice
import pygame
import os
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()
mouse_pressed = False
root, files = next(os.walk("files/minecraft-textures"))[::2]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            mouse_pressed = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            elif event.key == pygame.K_r:
                screen.fill("0x000000")
    if mouse_pressed:
        # screen.blit(pygame.transform.rotozoom(pygame.transform.scale(pygame.image.load(os.path.join(root, choice(
        #     files))), pygame.mouse.get_pos()), ((pos := pygame.mouse.get_pos())[0] + pos[1]) % 360, 1), (pos[0] // 2, pos[1] // 2))
        screen.blit((pygame.transform.rotozoom(pygame.transform.scale(pygame.image.load(os.path.join(
            root, choice(files))), (64, 64)), (pos := pygame.mouse.get_pos())[0], 1)), (pos[0] - 32, pos[1] - 32))
    pygame.display.update()
    clock.tick(60)
