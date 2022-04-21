from math import ceil

import pygame

pygame.init()
size = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
images = [
    pygame.image.load(f"files/parallax/plx{i}.png").convert_alpha()
    for i in range(4)
]
colors = [(255, 0, 0), (255, 106, 0), (255, 221, 0), (167, 236, 0)]

pos = 320, 240
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.VIDEORESIZE:
            size = event.size

        elif event.type == pygame.MOUSEMOTION:
            pos = [event.pos[i] for i in range(len(size))]

    screen.fill((0, 0, 0))
    for i, image in enumerate(images):
        xpos = (pos[0] - size[0] // 2) * (i * .5 + .2)
        ypos = (pos[1] - size[1] // 2) * (i * .4 + .2) + 75
        dir1 = ceil((size[0] - xpos) / image.get_width())
        dir2 = ceil((size[0] + xpos) / image.get_width())

        for j in range(-dir2, dir1):
            screen.blit(image, ((xpos + j * image.get_width(), ypos)))
            pygame.draw.rect(
                screen, colors[i],
                (xpos + j * image.get_width(), max(
                    0, ypos + image.get_height()), image.get_width(),
                 max(0, size[1] - image.get_height() - ypos)))

    pygame.display.update()
