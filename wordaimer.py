from random import choice, randint, randrange, sample
from tkinter.tix import MAX
import pygame
from numpy import array
from math import pow, e
pygame.init()

size = width, height = pygame.display.get_desktop_sizes()[0] # type: ignore
size = (width := 1920 - 200, height := 1080 - 200)
screen = pygame.display.set_mode(size, pygame.RESIZABLE)
clock = pygame.time.Clock()

words = pygame.sprite.Group()

word_fonts = {i: pygame.font.SysFont("Segoe UI", i) for i in range(20, 35)}
text_font = pygame.font.SysFont("Segoe UI", 46, True)
subtext_font = pygame.font.SysFont("Segoe UI", 30)

with open('files/words_new.txt', encoding="utf-8") as f:
    ram_eater = [i.strip() for i in f.readlines()]
    words_list = array(ram_eater)
    del ram_eater

words_len = words_list.size

MAX_TIME_EASY = 600
MAX_TIME_HARD = 1000

RADIUS_CALC_EASY = lambda r: r + 10
RADIUS_CALC_HARD = lambda r: r / 2 + 20

WORD_COUNT_EASY = 20
WORD_COUNT_HARD = 40

POINTS_EASY = 100
POINTS_HARD = 150

score = 0
max_time = 1000
current_max_time = max_time
current_time_left = current_max_time
current_word: str
current_word_r: pygame.surface.Surface = pygame.Surface((0, 0))
active = False
gameover = False

class Word(pygame.sprite.Sprite):
    rect: tuple
    def __init__(self, x, y, text, font: pygame.font.Font):
        super().__init__()
        self.text = text
        self.font = font
        self.size = font.size(text)
        self.radius = self.size[0] / 2 + 20
        self.image = font.render(text, True, 0)
        self.update_pos(x, y)
    
    def in_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) < (self.radius + other.radius) ** 2
    
    def point_in_distance(self, point):
        return ((self.x - point[0]) ** 2 + (self.y - point[1]) ** 2) < (self.radius) ** 2
    
    def update_pos(self, x, y):
        self.x = x
        self.y = y
        self.rect = (x - self.size[0] // 2, y - self.size[1] // 2, self.size[0], self.size[1])
    
    def update(self, screen, draw_circle):
        if draw_circle:
            pygame.draw.circle(screen, hash(self.text) % 0xffffff, (self.x, self.y), self.radius)
        else:
            screen.blit(self.image, self.rect)
            
        
def get_random_position():
    return randint(100, width - 100), randint(50, height - 200)

def range_sample(sample_range: tuple[int, int], sample_size):
    sample = []
    for _ in range(sample_size):
        while True:
            new_sample = randrange(*sample_range)
            if not new_sample in sample:
                break
        sample.append(new_sample)
    return sample

def reset():
    global current_word, current_word_r
    words.empty()
    word_idxs = []
    word_idxs.extend(range_sample((0, words_len), 40))
    for i in word_idxs:
        new_word = Word(*get_random_position(), 
                        words_list[i], choice(list(word_fonts.values())))
        for i in range(1000):
            all_ok = all(not word.in_distance(new_word) for word in words) # type: ignore
            if all_ok:
                break
            new_word.update_pos(*get_random_position())
        else:
            reset()
            return
        words.add(new_word)
    current_word = words_list[choice(word_idxs)]
    current_word_r = text_font.render(current_word, True, 0)
    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.VIDEORESIZE:
            size = width, height = event.size
            
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_KP_ENTER, pygame.K_SPACE) and not active:
                score = 0
                current_max_time = max_time
                current_time_left = current_max_time
                active = True
                reset()

            elif event.key == pygame.K_r:
                reset()
            
            elif event.key == pygame.K_q:
                pygame.quit()
                quit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and active:
            for i in words:
                if i.point_in_distance(event.pos): # type: ignore
                    break
            else:
                continue
            if i.text == current_word: # type: ignore
                x = current_time_left / current_max_time
                score += round(1 / (1 + pow(e, -10 * (x - 0.5))) * 150)
                current_time_left = current_max_time
                current_max_time = current_max_time // 1.05
                reset()
            else:
                active = False
                gameover = True

    if active:
        screen.fill(0xffffff)
        # words.update(screen, True)
        words.update(screen, False)
        screen.blit(current_word_r, ((width - current_word_r.get_width()) // 2,
                                     height - 30 - current_word_r.get_height()))
        bar_width = round(width * current_time_left / current_max_time)
        pygame.draw.rect(screen, 0x10c010, (width - bar_width, height - 30, bar_width, 30))
        current_time_left -= 1
        if current_time_left == 0:
            active = False
            gameover = True
    
    elif gameover:
        screen.fill(0xffffff)
        text = "Press Enter to restart"
        s1 = text_font.size(text)
        screen.blit(text_font.render(text, True, 0), ((width - s1[0]) // 2, (height - s1[1]) // 2))
        
        text = f"Your Score was: {score}"
        s2 = subtext_font.size(text)
        screen.blit(subtext_font.render(text, True, 0), ((width - s2[0]) // 2, (height - s2[1]) // 2 + s1[1]))
    
    else:
        screen.fill(0xffffff)
        s = text_font.size("Press Enter to start")
        screen.blit(text_font.render("Press Enter to start", True, 0), ((width - s[0]) // 2, (height - s[1]) // 2))
    pygame.display.update()
        
    
    pygame.display.update()
    clock.tick(60)