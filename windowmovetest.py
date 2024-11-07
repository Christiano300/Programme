
import pygame
import win32gui
from threading import Thread

GAME_WIDTH, GAME_HEIGHT = 750, 250

running = True
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT), flags=pygame.RESIZABLE)
clock = pygame.time.Clock()

def mainloop():
    while True:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT] or event.type in [pygame.KEYDOWN] and event.key in [pygame.K_ESCAPE]:
                pygame.quit()
                global running
                running = False
                quit()
                
        clock.tick(60)
        screen.fill("black")
        print("test")
        pygame.display.flip()

pygame.init()
Thread(target=mainloop, daemon=True).start()

hwnd = pygame.display.get_wm_info()['window']
# while GetMessage != 0 instead of True? TODO
while running:
    message = win32gui.GetMessage(hwnd, 0, 0)
    #print(message)
    if message[0] != 0:
        win32gui.TranslateMessage(message[1])
        win32gui.DispatchMessage(message[1])
    elif message[0] == -1: #handle exit?
        quit()