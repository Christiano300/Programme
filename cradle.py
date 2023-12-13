from math import sin
import pygame
pygame.init()

size = width, height = 1280, 720
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

a = 2
b = 1
state = 0
prev = 0
t = 0
base_vector = pygame.Vector2(0, 300)

pendulum_bases = [pygame.Vector2(100 * i + 400, 200) for i in range(5)]
pendulum_angles = [base_vector for _ in range(5)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    state = sin(t / 60) * 360 * 2
    if state * prev < 0:
        pendulum_angles = [base_vector for _ in range(5)]
        a, b = b, a
    
    vector_a = base_vector.rotate(abs(state))
    vector_b = base_vector.rotate(-abs(state))
    
    for i in range(a):
        pendulum_angles[i] = vector_a
    
    for i in range(b):
        pendulum_angles[4 - i] = vector_b
    
    screen.fill(0xffffff)
    pygame.draw.line(screen, 0, (390, 200), (810, 200), 10)
    for base, angle in zip(pendulum_bases, pendulum_angles):
        pygame.draw.line(screen, 0, base, base + angle, 3)
        pygame.draw.circle(screen, 0, base + angle, 50)
    
    prev = state
    t += 1
    pygame.display.update()
    clock.tick(60)