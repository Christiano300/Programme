import pygame, sys, random
pygame.init()
groesse = breite, hoehe = 640, 640
screen = pygame.display.set_mode(groesse)

def draw_background():
    screen.fill([255, 255, 255])
    # pygame.draw.circle(screen, [0, 0, 150], [320, 320], 1, 0)

class Rechteck(pygame.sprite.Sprite):
    def __init__(self, farbe, groesse, ort, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(groesse)
        self.image.fill(farbe)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = ort
        self.speed = speed
    def bewegen(self):
        self.rect =self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > breite:
            self.speed[0] = -self.speed[0]
        
        if self.rect.top < 0 or self.rect.bottom > hoehe:
            self.speed[1] = -self.speed[1]

def animieren(gruppe):
    draw_background()
    for rechteck in gruppe:
        rechteck.bewegen()
    for rechteck in gruppe:
        gruppe.remove(rechteck)
        if pygame.sprite.spritecollide(rechteck, gruppe, False):
            rechteck.speed[0] = -rechteck.speed[0]
            rechteck.speed[1] = -rechteck.speed[1]
        gruppe.add(rechteck)
        screen.blit(rechteck.image, rechteck.rect)
    pygame.display.flip()

draw_background()
gruppe = pygame.sprite.Group()
uhr = pygame.time.Clock()

for zeile in range(5):
    for spalte in range(5):
        ort = [spalte * 75 + 200, zeile * 75 + 200]
        speed = [random.randint(-5, 5), random.randint(-5, 5)]
        rechteck = Rechteck([255, spalte * 50, zeile * 50], [35, 35], ort, speed)
        gruppe.add(rechteck)
for rechteck in gruppe:
    screen.blit(rechteck.image, rechteck.rect)


pygame.display.flip()
pygame.time.delay(3000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(uhr.get_fps())
            sys.exit()
    animieren(gruppe)
    uhr.tick(60)
    