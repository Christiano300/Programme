import pygame
pygame.init()

size = width, height = pygame.display.Info().current_w, pygame.display.Info().current_h
hwidth, hheight = width // 2, height // 2
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

coords: list[tuple[int, int]] = [(0, 0) for _ in range(8)]

def lerp_2d(p1: pygame.Vector3, p2: pygame.Vector3, p3: pygame.Vector3, tx: float, ty: float) -> pygame.Vector3:
    return p1.lerp(p2, tx).lerp(p3.lerp(-p1 + p2 + p3, tx), ty)

def add_center_offset(point: tuple[int, int]) -> tuple[int, int]:
    return point[0] + hwidth // 2, point[1] + hheight

def to_point_with_offset(point: pygame.Vector3) -> tuple[int, int]:
    return round(point.x) + hwidth // 2, round(point.y) + hheight

corners = [pygame.Vector3(x, y, z) for x in (-150, 150) for y in (-150, 150) for z in (-150, 150)]

for i in corners:
    i.rotate_ip(30, (0, 1, 0))
    i.rotate_ip(30, (1, 0, 0))

lines = [(0, 1), (1, 3), (3, 2), (2, 0), (0, 4), (1, 5), (3, 7), (2, 6), (4, 5), (5, 7), (7, 6), (6, 4)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                pygame.quit()
                quit()

    screen.fill(0x7f7f7f)
    for i in corners:
        i.rotate_ip(0.5, (0, 1, 0))
    
    for idx, i in enumerate(corners):
        coords[idx] = (round(i.x), round(i.y))
        pygame.draw.circle(screen, 0x202020 * idx, add_center_offset(coords[idx]), 5)
    
    
    for r in range(256):
        for g in range(256):
            screen.set_at(to_point_with_offset(lerp_2d(corners[0], corners[1], corners[2], r / 255, g / 255)), (r, g, 255))

    for l in lines:
        pygame.draw.line(screen, 0xffffff, add_center_offset(coords[l[0]]), add_center_offset(coords[l[1]]))

    pygame.display.update()
    clock.tick(60)