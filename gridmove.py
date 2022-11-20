import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

offset = [0, 0]
zoom = 1
linespace = 50

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0] and dragging:
                rel = pygame.mouse.get_rel()
                offset[0] += rel[0]
                offset[1] += rel[1]
        elif event.type == pygame.MOUSEBUTTONDOWN:
            dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

    screen.fill(0xffffff)
    for i in range(round(width / (zoom * linespace))):
        x = i * (zoom * linespace) + offset[0] % (zoom * linespace)
        pygame.draw.line(screen, 0x969696, (x, 0), (x, height))
        
    for i in range(round(height / (zoom * linespace))):
        y = i * (zoom * linespace) + offset[1] % (zoom * linespace)
        pygame.draw.line(screen, 0x969696, (0, y), (width, y))
    
    pygame.display.update()
    clock.tick(60)