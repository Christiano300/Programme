import pygame
import json

pygame.init()
size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)

pygame.key.set_repeat(500, 50)

CUBE_GAP = 100
SPHERE_SIZE = CUBE_GAP // 2
COLOR_MAP = {
    0: 0xA01010,
    1: 0xFF4D00,
    2: 0xE0E000,
    3: 0x008000,
    4: 0x2898E2,
    5: 0x00008B,
    6: 0xBB00E3,
    7: 0x000000,
    8: 0xFFFFFF
}

IMAGES = {}

for (i, color) in COLOR_MAP.items():
    surf = pygame.Surface((SPHERE_SIZE * 2 + 2, SPHERE_SIZE * 2 + 2), pygame.SRCALPHA)
    surf.fill(color)
    pygame.draw.aacircle(surf, color | (0xFF << 24), (SPHERE_SIZE + 1, SPHERE_SIZE + 1), SPHERE_SIZE)
    IMAGES[i] = surf

CUBES = json.load(open("files/mole_cube_solutions.json", encoding="utf-8"))
FONT = pygame.font.SysFont("Segoe UI", 20)

POSITIONS = [pygame.Vector3(x, y, z) for z in range(-1, 2) for y in range(-1, 2) for x in range(-1, 2) if not (x == 0 and y == 0 and z == 0)]

clock = pygame.time.Clock()

cube_index = 0
pitch = 30
yaw = 30
dragging = False
drag_start = (0, 0)
should_render = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit() 

        elif event.type == pygame.VIDEORESIZE:
            width, height = event.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
            should_render = True
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_LEFT:
                cube_index = (cube_index - 1) % len(CUBES)
                should_render = True
            elif event.key == pygame.K_RIGHT:
                cube_index = (cube_index + 1) % len(CUBES)
                should_render = True
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            dragging = True
            drag_start = event.pos
        
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            dragging = False
        
        elif event.type == pygame.MOUSEMOTION and dragging:
            dx, dy = event.pos[0] - drag_start[0], event.pos[1] - drag_start[1]
            yaw = (yaw - dx * .5) % 360
            pitch = max(-90, min(90, pitch + dy * .5))
            drag_start = event.pos
            if dx != 0 or dy != 0:
                should_render = True
            
    clock.tick(60)
    
    if not should_render:
        continue

    screen.fill(0x7F7F7F)
    should_render = False
    
    rotated_positions = [pos.rotate_z(yaw).rotate_x(pitch) for pos in POSITIONS]
    render_order = sorted(range(len(rotated_positions)), key=lambda i: rotated_positions[i].y)
    
    for idx in render_order:
        pos = rotated_positions[idx]
        screenx = pos.x * CUBE_GAP + width / 2
        screeny = pos.z * CUBE_GAP + height / 2
        screen.blit(IMAGES[CUBES[cube_index][idx]], (screenx - SPHERE_SIZE, screeny - SPHERE_SIZE))
    
    screen.blit(FONT.render(f"Solution {cube_index + 1} / {len(CUBES)}", True, 0), (10, 10))

    
    pygame.display.update()
    