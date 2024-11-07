import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

mouse_pressed = False
current_point = None
num_points = 3
max_dist = 5

movable_points: list[pygame.Vector2] = [pygame.Vector2(100, 150),
                                        pygame.Vector2(150, 150),
                                        pygame.Vector2(200, 150),
                                        pygame.Vector2(250, 150)]

def mnht_dist(a: pygame.Vector2, b: pygame.Vector2):
    return abs(abs(a.x) - abs(b.x)) + abs(abs(a.y) - abs(b.y))

def new_point(t):
    p1, p2, p3, p4 = movable_points
    p5 = p1.lerp(p2, t)
    p6 = p2.lerp(p3, t)
    p7 = p3.lerp(p4, t)
    
    p8 = p5.lerp(p6, t)
    p9 = p6.lerp(p7, t)
    
    return p8.lerp(p9, t)

def draw(low = 0, high = 1):
    p_low = new_point(low)
    p_high = new_point(high)
    if mnht_dist(p_low, p_high) > max_dist:
        mid = (high + low) / 2
        draw(low, mid)
        draw(mid, high)
    else:
        points.append(p_low)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pressed = True
            for i in movable_points:
                if mnht_dist(i, pygame.Vector2(event.pos)) < 10:
                    current_point = i
                    break
            else:
                mouse_pressed = False
        
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            current_point = None
            mouse_pressed = False
    
    if mouse_pressed:
        x, y = pygame.mouse.get_pos()
        current_point.x = x
        current_point.y = y
    
    screen.fill(0xffffff)
    for i in movable_points:
        pygame.draw.circle(screen, 0, i, 5)

    points = []
    draw()
    points.append(movable_points[3])
    print(len(points))
    # pygame.draw.lines(screen, 0, False, points, 2)
    pygame.draw.aalines(screen, 0, False, points)
    
    pygame.display.update()
    clock.tick(60)