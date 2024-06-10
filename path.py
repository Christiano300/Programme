from dataclasses import dataclass
from math import cos, pi, sin
import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

@dataclass
class Arc:
    start: tuple[int, int]
    radius: int
    angle: float # in radians
    rotation: float = 0 # in radians
    @property
    def end(self):
        return self.start[0] + self.radius * cos(self.angle), self.start[1] + self.radius * sin(self.angle)
    
    def draw(self, screen):
        pass

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    arc = Arc((width // 2, height // 2), 100, (sin(pygame.time.get_ticks() / 400) / 2 + .5) * pi, pygame.time.get_ticks() / 150)
    
    screen.fill((0, 0, 0))
    arc.draw(screen)

    pygame.display.update()
    clock.tick(60)