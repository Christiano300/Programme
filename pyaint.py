import pygame

pygame.init()

size = width, height = 1820, 1000
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

mouse_pressed = False
shift_pressed = False
strength = 20
colors = ["0xff0000", "0xff7f05", "0xf0e000", "0x00ff00",
          "0x00ffa0", "0x007fff", "0x0000ff", "0xBA00FF",
          "0xffffff", "0x000000", "0xFF59F8"]
color = 0
shapes = ["square", "circle"]
shape = 0
pen = pygame.Surface((strength, strength), pygame.SRCALPHA)


def repen():
    if shapes[shape] == "square":
        pen.fill(colors[color])
    elif shapes[shape] == "circle":
        pen.fill("0x00000000")
        pygame.draw.circle(
            pen, colors[color], (strength / 2, strength / 2), strength / 2)
    pygame.display.set_icon(pen)


repen()
screen.fill("0xffffff")
pygame.display.flip()


def draw_line(start: list, end: list, pen: pygame.Surface, draw_len_0: bool):
    if start == end:
        if draw_len_0:
            screen.blit(pen, [start[i] - strength / 2 for i in range(2)])
    else:
        d = [j - i for i, j in zip(start, end)]
        dist = max(abs(d[0]), abs(d[1]))
        dir = [d[0] / dist, d[1] / dist]
        for i in range(dist):
            screen.blit(pen, [start[j] + dir[j] * i -
                        strength / 2 for j in range(2)])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.init()
            screen = pygame.display.set_mode(size, pygame.RESIZABLE)
            repen()
            screen.fill("0xffffff")
            pygame.display.flip()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            prev_pos = pygame.mouse.get_pos()
            mouse_pressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_pressed = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill("0xffffff")
                pygame.display.flip()

            elif event.key == pygame.K_c:
                color = (color + 1) % len(colors)
                repen()

            elif event.key == pygame.K_s:
                shape = (shape + 1) % len(shapes)
                repen()

            elif event.key == pygame.K_q:
                pygame.quit()
                quit()

            elif event.key == pygame.K_w:
                screen.fill(0xffffff)

            elif event.key == pygame.K_b:
                screen.fill(0)

            elif event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                shift_pressed = True

        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LSHIFT, pygame.K_RSHIFT):
                shift_pressed = False

    if mouse_pressed:
        pos = pygame.mouse.get_pos()
        draw_line(prev_pos, pos, pen, True)
        if not shift_pressed:
            prev_pos = pos

    pygame.display.update()
    clock.tick(60)
