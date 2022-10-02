from math import atan2, hypot, radians, sin, cos
import pygame
pygame.init()

size = width, height = 640, 480
hwidth, hheight = width / 2, height / 2
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

rot = pygame.Vector3()
vrot = pygame.Vector3()
coords = [None for i in range(8)]
lines = [(0, 2), (2, 6), (6, 4), (4, 0)]

sign = lambda x: 1 if x > 0 else -1 if x < 0 else 0

cubesize = 50
colors = [0xffffff, 0xff0000, 0x00d010, 0x0040ff, 0xffff20, 0x9f50ff]
corners = [pygame.Vector3([i, j, k]) for i in (-50, 50) for j in (-50, 50) for k in (-50, 50)]
print(corners)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print(round(clock.get_fps()))
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                vrot.x += .3
            elif event.key == pygame.K_s:
                vrot.x -= .3
            elif event.key == pygame.K_a:
                vrot.y += .3
            elif event.key == pygame.K_d:
                vrot.y -= .3
            elif event.key == pygame.K_y:
                vrot.z += .3
            elif event.key == pygame.K_x:
                vrot.z -= .3
            elif event.key == pygame.K_p:
                for i, vector in enumerate(corners):
                    print(f"{i + 1}: {vector.x} | {vector.y} | {vector.z}")
                print(xpos, ypos)
            elif event.key == pygame.K_r:
                vrot.x = vrot.y = vrot.z = rot.x = rot.y = rot.z = 0
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size
            hwidth, hheight = width / 2, height / 2
    rot += vrot
    screen.fill(0)
    for idx, i in enumerate(corners):
        theta = atan2(i.y, i.x)
        xpos = hwidth + cos(theta + radians(rot.z)) * hypot(i.x, i.y) * cos(radians(rot.x))
        ypos = hheight + sin(theta + radians(rot.z)) * hypot(i.x, i.y) * cos(radians(rot.y))
        coords[idx] = xpos, ypos
        pygame.draw.circle(screen, 0xffffff, (xpos, ypos), 3)
    for l in lines:
        pygame.draw.line(screen, 0xffffff, coords[l[0]], coords[l[1]])
    pygame.display.update()
    clock.tick(60)