from math import atan2, hypot, radians, sin, cos
import pygame
pygame.init()

size = width, height = 640, 480
hwidth, hheight = width // 2, height // 2
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

pygame.key.set_repeat(100, 20)

rot = pygame.Vector3()
vrot = pygame.Vector3()
coords: list[tuple[int, int]] = [(0, 0) for _ in range(8)]
lines = [(0, 2), (2, 6), (6, 4), (4, 0), (0, 1), (2, 3), (6, 7), (4, 5), (1, 3), (3, 7), (7, 5), (5, 1)]

cubesize = 50
colors = [0xffffff, 0xff0000, 0x00d010, 0x0040ff, 0xffff20, 0x9f50ff]
corners = [pygame.Vector3(x, y, z) for x in (-50, 50) for y in (-50, 50) for z in (-50, 50)]

camera = pygame.Vector3(0, 0, -200)
screendepth = 0

def add_center_offset(point: tuple[int, int]) -> tuple[int, int]:
    return point[0] + hwidth, point[1] + hheight

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            print(round(clock.get_fps()))
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                screendepth += 3
                camera.z += 3
            elif event.key == pygame.K_DOWN:
                screendepth -= 3
                camera.z -= 3
            elif event.key == pygame.K_LEFT:
                camera.x += 3
            elif event.key == pygame.K_RIGHT:
                camera.x -= 3
                
            elif event.key == pygame.K_w:
                for i in corners:
                    i.rotate_ip(2, (1, 0, 0))
            elif event.key == pygame.K_s:
                for i in corners:
                    i.rotate_ip(-2, (1, 0, 0))
            elif event.key == pygame.K_a:
                for i in corners:
                    i.rotate_ip(2, (0, 1, 0))
            elif event.key == pygame.K_d:
                for i in corners:
                    i.rotate_ip(-2, (0, 1, 0))
            elif event.key == pygame.K_y:
                for i in corners:
                    i.rotate_ip(2, (0, 0, 1))
            elif event.key == pygame.K_x:
                for i in corners:
                    i.rotate_ip(-2, (0, 0, 1))
            
            elif event.key == pygame.K_p:
                for i, vector in enumerate(corners):
                    print(f"{i + 1}: {vector.x} | {vector.y} | {vector.z}")
            elif event.key == pygame.K_r:
                vrot.x = vrot.y = vrot.z = rot.x = rot.y = rot.z = 0
                
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size
            hwidth, hheight = width / 2, height / 2
    rot += vrot
    screen.fill(0)
    for idx, i in enumerate(corners):
        if i.z != camera.z:
            screeen_to_camera = screendepth - camera.z
            screenx = round(screeen_to_camera / (i.z - camera.z) * (i.x - camera.x))
            screeny = round(screeen_to_camera / (i.z - camera.z) * (i.y - camera.y))
            if i.z < camera.z:
                screenx *= -1
                screeny *= -1
            pygame.draw.circle(screen, 0xffffff, add_center_offset((screenx, screeny)), 3)
            coords[idx] = (screenx, screeny)

    for l in lines:
        pygame.draw.line(screen, 0xffffff, add_center_offset(coords[l[0]]), add_center_offset(coords[l[1]]))
    pygame.display.update()
    clock.tick(60)