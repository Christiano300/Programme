import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

snake = [[16, 12]]
food = [20, 10]
dir = None
count = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            elif event.key == pygame.K_UP and dir != "down":
                dir = "up"
            elif event.key == pygame.K_DOWN and dir != "up":
                dir = "down"
            elif event.key == pygame.K_RIGHT and dir != "left":
                dir = "right"
            elif event.key == pygame.K_LEFT and dir != "right":
                dir = "left"

    screen.fill(0)
    for i in snake:
        pygame.draw.rect(screen, 0xffffff, (i[0] * 20, i[1] * 20, 20, 20))
    if count:
        count -= 1
    else:
        count = 10
        match dir:
            case "left":
                snake[0][0] -= 1
            case "right":
                snake[0][0] += 1
            case "up":
                snake[0][1] -= 1
            case "down":
                snake[0][1] += 1

    pygame.display.update()
    clock.tick(60)
