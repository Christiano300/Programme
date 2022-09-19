from math import cos, radians, sin
import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()
left_pressed = right_pressed = up_pressed = down_pressed = False
chaserimg = pygame.Surface((75, 75), pygame.SRCALPHA)
pygame.draw.polygon(chaserimg, (255, 135, 0, 255), [[0, 75], [75, 75], [37, 0]])

class Chaser(pygame.sprite.Sprite):
    group = pygame.sprite.Group()
    def __init__(self, pos: list, rot: int):
        pygame.sprite.Sprite.__init__(self)
        self.surf = chaserimg
        self.rect = self.surf.get_rect()
        self.pos = self.surf.get_rect()
        self.image = self.surf
        self.pos.left, self.pos.top = pos
        self.rot = rot
        Chaser.group.add(self)
    
    def update(self):
        center = self.pos.center
        self.image = pygame.transform.rotate(self.surf, self.rot)
        size = self.image.get_size()
        hSize = [n/2 for n in size]
        pos = (center[0]-hSize[0], center[1]-hSize[1])
        self.rect.left, self.rect.top = pos

    
    def move(self, step: int):
        self.pos.move_ip(cos(radians(self.rot)) * step, sin(radians(self.rot)) * step)

test = Chaser([100, 200], 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                quit()
            elif event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_RIGHT:
                right_pressed = True
            elif event.key == pygame.K_UP:
                up_pressed = True
            elif event.key == pygame.K_DOWN:
                down_pressed = True
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_pressed = False
            elif event.key == pygame.K_RIGHT:
                right_pressed = False
            elif event.key == pygame.K_UP:
                up_pressed = False
            elif event.key == pygame.K_DOWN:
                down_pressed = False
    
    if left_pressed:
        test.rot += 1
    elif right_pressed:
        test.rot -= 1
    if up_pressed:
        test.move(3)
    elif down_pressed:
        test.move(-3)
    Chaser.group.update()
    screen.fill(0)
    Chaser.group.draw(screen)
    pygame.display.update()
    clock.tick(60)