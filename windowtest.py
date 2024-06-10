from time import sleep
import pyautogui as pg
import pygame
import pygetwindow as gw
import win32gui
import threading
import win32api

pygame.init()

size = width, height = 640, 480
clock = pygame.time.Clock()

window = gw.getActiveWindow()
running = True

run_sim = False

AIR_FRICTION = 0.99
GRAVITY = 0.3
JUMP_STRENGTH = 5


def mouse_rel():
    global last_mouse, rel
    while True:
        mouse = pg.position()
        if last_mouse is None:
            last_mouse = mouse
            rel = (0, 0)
        rel = (mouse[0] - last_mouse[0], mouse[1] - last_mouse[1])
        last_mouse = mouse
        print(rel)
        sleep(1 / 60)


desktop_width, desktop_height = pygame.display.get_desktop_sizes()[0]


def iint(x: list[float]) -> list[int]:
    return list(map(int, x))


def main():
    screen = pygame.display.set_mode(size)
    global running, run_sim
    vel: list[float] = [0, 0]
    pos: list[float] = [0, 0] if window is None else list(window.topleft)

    last_mouse: pg.Point | None = None
    rel = (0, 0)

    while True:
        if window is None:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    running = False
                    quit()
                elif event.key == pygame.K_SPACE:
                    vel[1] = -JUMP_STRENGTH
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dx = event.pos[0] - width // 2
                    dy = event.pos[1] - height // 2
                    if dx ** 2 + dy ** 2 < 75 ** 2:
                        run_sim = not run_sim

        mouse = pg.position()
        if last_mouse is None:
            last_mouse = mouse
            rel = (0, 0)
        rel = (mouse[0] - last_mouse[0], mouse[1] - last_mouse[1])
        last_mouse = mouse

        screen.fill((255, 255, 255))
        pygame.draw.circle(
            screen, 0x40FF40 if run_sim else 0xF03333, (width // 2, height // 2), 50
        )

        if run_sim and win32api.GetKeyState(0x01) in [0, 1]:
            prev = iint(pos)
            current = list(window.topleft)
            if prev != current:
                pos = current
                vel[0] = rel[0] * 0.35
                vel[1] = rel[1] * 0.45

            vel[0] *= AIR_FRICTION
            vel[1] += GRAVITY

            pos[0] += vel[0]
            pos[1] += vel[1]

            if pos[1] + window.height > desktop_height:
                pos[1] = int(desktop_height - window.height)
                vel[1] = -vel[1] * 0.5
                vel[0] *= 0.9

            elif pos[1] < 0:
                pos[1] = 0
                vel[1] = -vel[1] * 0.5
                vel[0] *= 0.9

            if pos[0] < 0:
                pos[0] = 0
                vel[0] = -vel[0] * 0.5
                
            elif pos[0] + window.width > desktop_width:
                pos[0] = desktop_width - window.width
                vel[0] = -vel[0] * 0.5

            window.moveTo(*iint(pos))

        pygame.display.update()
        clock.tick(60)


threading.Thread(target=main, daemon=True).start()

hwnd = pygame.display.get_wm_info()["window"]
while running:
    message = win32gui.GetMessage(hwnd, 0, 0)
    # print(message)
    if message[0] != 0:
        win32gui.TranslateMessage(message[1])
        win32gui.DispatchMessage(message[1])
    elif message[0] == -1:  # handle exit?
        quit()
