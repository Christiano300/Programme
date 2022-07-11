import pygame
pygame.init()

size = width, height = 640, 480
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()
left_pressed = False
right_pressed = False
chaserimg = pygame.Surface((75, 75), pygame.SRCALPHA)
pygame.draw.polygon(chaserimg, (255, 135, 0, 255), [[0, 75], [75, 75], [37, 0]])

class Chaser(pygame.sprite.Sprite):
    group = pygame.sprite.Group()
    def __init__(self, pos: list, rot: int):
        pygame.sprite.Sprite.__init__(self)
        self.surf = chaserimg
        self.rect = self.surf.get_rect()
        self.image = self.surf
        self.rect.left, self.rect.top = pos
        self.rot = rot
        Chaser.group.add(self)
    
    def update(self):
        center = self.rect.center
        self.image = pygame.transform.rotate(self.surf, self.rot)
        self.rect.center = center

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
        
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left_pressed = False
            elif event.key == pygame.K_RIGHT:
                right_pressed = False
    
    if left_pressed:
        test.rot += 1
    elif right_pressed:
        test.rot -= 1
    Chaser.group.update()
    screen.fill(0)
    Chaser.group.draw(screen)
    pygame.display.update()
    clock.tick(60)