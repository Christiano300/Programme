from pygaminter import Button, Entry, DropdownMenu, draw_widgets
import pygame
pygame.init()

size = width, height = 640, 640
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

screen.fill(0xf0f0f0)
colors = [0xf0f0f0, 0xff0000, 0xff7f00, 0xe0e010, 0x109020, 0x00ffff,
          0x0000ff, 0x7f00ff, 0xff00ff, 0xffffff,  0x000000]
screen.blit(pygame.Surface((12, 12)), (5, -2))
def quadrat(x): return x * x


for i in range(11):
    b = Button((50, i * 50 + 30, 190, 45), f"Hallo {i + 1}", colors[i])
    if i % 5 == 2:
        b.config(command=lambda x=b.config(): print(x))
    if i == 10:
        b.config(textcolor=0xdfdfdf)
    if i:
        b.config(font="Segoe UI_35b")
    if i == 3:
        b.font = "Segoe UI_35b"

# Button((400, 300, 120, 50), "Test", 0xabcdef)
a = DropdownMenu((380, 100, 150, 50), "", 0xfedcba, expansion=500, options=[])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Button.group.update(event)
            Entry.group.mouse_pressed(event)
            print(dir(event))

        elif event.type == pygame.MOUSEBUTTONUP:
            Button.group.update(event)

        elif event.type == pygame.KEYDOWN:
            if Entry.group.focused():
                Entry.group.key_action(event)
            else:
                # regular key control
                pass

    screen.fill(0xf0f0f0)
    draw_widgets(screen)
    pygame.display.update()
    clock.tick(60)
