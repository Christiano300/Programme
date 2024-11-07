from math import cos, pi, sin
import random
import pygame
pygame.init()

auto = input("Auto? (y/N): ").lower() == "y"

size = width, height = 640, 480
center = (width//2, height//2)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
y = 0 # 1025
n = 0 # 439

radius = height / 2 - 50
draw = True

def update():
    screen.fill(0xffffff)
    pygame.draw.circle(screen, (0, 0, 0), center, radius, 2)
    
    a1 = [rand() for _ in range(3)]
    a2 = [rand() for _ in range(3)]
    
    if auto:
        corners = a1 + a2
        t = list(range(6))
        t.sort(key=lambda i: corners[i])
        t = [t // 3 for t in t]
        three = are_three(t)
        global y, n
        if three:
            n += 1
        else:
            y += 1
    if draw:
        t1 = [cartesian(a) for a in a1]
        t2 = [cartesian(a) for a in a2]
        
        pygame.draw.polygon(screen, "0xc000007f", t1)
        pygame.draw.polygon(screen, "0x00c0007f", t2)
        
    print(f"{y = }, {n = }, %y = {y / (y + n) * 100 if y + n > 0 else 0}")

def rand():
    return random.uniform(0, pi * 2)
    

def cartesian(angle):
    return (cos(angle) * radius + center[0], sin(angle) * radius + center[1])

def are_three(l) -> bool:
    candidate = -1
    count = 0
    for i in l:
        if i == candidate:
            if count == 2:
                return True
            count += 1
        else:
            candidate = i
            count = 1
    return False

update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN and not auto:
            if event.key == pygame.K_j:
                y += 1
                update()
            elif event.key == pygame.K_n:
                n += 1
                update()
    
    if auto:
        update()
    draw = True
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_h]:
        draw = False
    elif keys[pygame.K_s]:
        pygame.display.update()
        clock.tick()
    elif keys[pygame.K_f]:
        pygame.display.update()
        clock.tick(60)
    else:
        pygame.display.update()
        clock.tick(2)