from random import randint
from hashlib import sha3_256
import os
import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.NOFRAME)
clock = pygame.time.Clock()

width_range = range(width)
height_range = range(height)

os.makedirs("files/colorfill", exist_ok=True)


def saturate(x):
    return min(max(x, 0), 255)


def change(r, g, b):
    return saturate(r + randint(-variety, variety)), saturate(g + randint(-variety, variety)), saturate(b + randint(-variety, variety))

fillpixels = []
active = False

fuzziness = 8
paint_color = (255, 170, 0)
variety = 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                pygame.display.update()
            
            elif event.key == pygame.K_r:
                screen.fill(0)
            
            elif event.key == pygame.K_c:
                fillpixels = []
                
            elif event.key == pygame.K_q:
                pygame.quit()
                quit()
            
            elif event.key == pygame.K_a:
                active = not active
            
            elif event.key == pygame.K_s:
                pixels = pygame.surfarray.array2d(screen)
                hash = sha3_256(pixels.data.tobytes()).hexdigest()
                pygame.image.save(screen, f"files/colorfill/{hash}.png")
                print(hash)
            
            elif event.key == pygame.K_f:
                for i in width_range:
                    for j in height_range:
                        if screen.get_at((i, j)) == (0, 0, 0, 255):
                            avg = [0, 0, 0]
                            count = 0
                            for x in (-2, -1, 0, 1, 2):
                                if i + x in width_range:
                                    for y in (-2, -1, 0, 1, 2):
                                        if j + y in height_range and screen.get_at((i + x, j + y)) != (0, 0, 0, 255):
                                            color = screen.get_at((i + x, j + y))
                                            for c in range(3):
                                                avg[c] += color[c]
                                            count += 1
                            if count > 0:
                                screen.set_at((i, j), (avg[0] // count, avg[1] // count, avg[2] // count, 255))

    if pygame.mouse.get_pressed()[0]:
        fillpixels.append((pygame.mouse.get_pos(), paint_color))
        screen.set_at(pygame.mouse.get_pos(), paint_color)
    
    if active:
        new_fillpixels = []
        
        for pixel in fillpixels:
            if randint(0, 10) < fuzziness:
                screen.set_at(pixel[0], pixel[1])

                for j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    new_pixel = (pixel[0][0] + j[0], pixel[0][1] + j[1])
                    if new_pixel[0] in width_range and new_pixel[1] in height_range and \
                        screen.get_at(new_pixel) == (0, 0, 0, 255) and not new_pixel in [p[0] for p in new_fillpixels]:
                        new_fillpixels.append((new_pixel, change(*pixel[1])))
            # else:
            #     if not pixel[0] in [p[0] for p in new_fillpixels]:
            #         new_fillpixels.append(pixel)

        fillpixels = new_fillpixels

    pygame.display.update()
    clock.tick(60)