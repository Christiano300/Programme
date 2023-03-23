from math import cos, sin
import pygame
pygame.init()

size = width, height = 640, 480
center = width // 2, height // 2
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

rotating = False
rotating_angle = 0
rotating_dir = (0, 0)
points = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
point_pos: list[tuple] = [(0, 0) for _ in range(len(points))]
lines = [(0, 1), (1, 2), (2, 3), (3, 0)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and not rotating:
            if event.key == pygame.K_LEFT:
                rotating_dir = (-1, 0)
                rotating = True

            elif event.key == pygame.K_RIGHT:
                rotating_dir = (1, 0)
                rotating = True

            elif event.key == pygame.K_UP:
                rotating_dir = (0, -1)
                rotating = True

            elif event.key == pygame.K_DOWN:
                rotating_dir = (0, 1)
                rotating = True
    
    screen.fill(0)
    for i, point in enumerate(points):
        idx = abs(rotating_dir[1])
        xpos = center[0] + point[0] * 100 + int(cos(rotating_angle + point[idx] * 50) * rotating_dir[0] * 100)
        ypos = center[1] + point[1] * 100 + int(cos(rotating_angle + point[1 - idx] * 50) * rotating_dir[1] * 100)
        pygame.draw.circle(screen, 0xffffff, (xpos, ypos), 3)
        point_pos[i] = (xpos, ypos)

    for line in lines:
        pygame.draw.line(screen, 0xffffff, point_pos[line[0]], point_pos[line[0]])

    rotating_angle += 0.01
    
    pygame.display.update()
    clock.tick(60)
