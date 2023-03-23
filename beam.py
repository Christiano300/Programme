import pygame
pygame.init()

size = width, height = 1600, 900
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

beam = pygame.image.load("files/beam.png")
mouse_pressed = False
center = pygame.Vector2(width // 2, height // 2)

rot1 = 0
rot2 = 0

beam_length = 3

beam_surf = pygame.Surface((beam.get_width() * beam_length, beam.get_height()), pygame.SRCALPHA)
for i in range(beam_length):
    beam_surf.blit(beam, (beam.get_width() * i, 0))

def display_with_rotation(surface: pygame.Surface, pos: pygame.math.Vector2, rotation: float, center_of_rotation: pygame.Vector2):
    screen.blit(pygame.transform.rotate(surface, rotation), pos - center_of_rotation)

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
            if event.key == pygame.K_LEFT:
                rot1 += 5
            elif event.key == pygame.K_RIGHT:
                rot1 -= 5
            elif event.key == pygame.K_DOWN:
                rot2 += 5
            elif event.key == pygame.K_UP:
                rot2 -= 5
        
    screen.fill(0)
    if mouse_pressed:
        mouse = pygame.Vector2(pygame.mouse.get_pos())
        from_center = center - mouse
        pygame.draw.line(screen, 0xc50df0, mouse, center, 10)
    display_with_rotation(beam_surf, center, rot1, pygame.Vector2(16, 16))
    display_with_rotation(beam_surf, center + pygame.Vector2(beam_length * beam.get_width(), 0).rotate(-rot1), rot2, pygame.Vector2(16, 16))
    rot1 += .4
    pygame.display.update()
    clock.tick(60)