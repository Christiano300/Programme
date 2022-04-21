import pygame
import tqdm
pygame.init()
screen = pygame.display.set_mode([4200, 4200])
for red in tqdm.tqdm(range(256)):
    for green in range(256):
        for blue in range(256):
            pygame.draw.rect(screen, (red, green, blue),
                             (red % 16 * 256 + green, red // 16 * 256 + blue, 1, 1))

pygame.display.flip()
pygame.image.save(screen, r".\files\colors3.png")
