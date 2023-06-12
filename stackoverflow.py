# Template: Starter code for all pygame graphics

# Import some libraries
import pygame
import sys
import random
import time
import math
import os
from pygame.locals import *  #don't need on home computer
from cProfile import run
# Initialize the game engine
pygame.init()

# Set the height and width of the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 900
SCREEN_HEIGHT_NEW = 475
#this code will right justify the screen in the top right
RIGHT_JUSTIFY_X = 1910 - SCREEN_WIDTH - 50
RIGHT_JUSTIFY_Y = 50
RIGHT_JUSTIFY_STRING = str(RIGHT_JUSTIFY_X) + "," +  str(RIGHT_JUSTIFY_Y)
os.environ['SDL_VIDEO_WINDOW_POS'] = RIGHT_JUSTIFY_STRING

#sets the variable name for the display
screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

# Define some basic colors in RGB format. You can create your own colors if you want more options.
BLACK = (  0,   0,   0)
GRAY =  (150, 150, 150)
WHITE = (255, 255, 255)
RED =   (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE =  (  0,   0, 255)
RED =   (255,   0,   0)
YELLOW = (255, 255, 0)
CYAN =  (  0, 255, 255)
MAGENTA = (255,  0, 255)

# this function will draw guidelines on the screen
def drawGridLines():
   for i in range(100):
      pygame.draw.line(screen, (200,200,200), [0 + i*10, 0], [0 + i*10,800], 1)
      pygame.draw.line(screen, (200,200,200), [0, 0 + i*10], [1000,0 + i*10], 1)
   for i in range(10):
      pygame.draw.line(screen, (100,100,100), [0 + i*100, 0], [0 + i*100,800], 1)
      pygame.draw.line(screen, (100,100,100), [0, 0 + i*100], [1000,0 + i*100], 1)
      
# this function prints the current mouse coordinates on bottom right of screen
def print_coordinates_on_screen():
   fontObj = pygame.font.Font("C:\Windows\Fonts\cour.ttf",15)
   mousex, mousey = pygame.mouse.get_pos()
   mouse_position = "({:3d}, {:3d})".format(mousex,mousey) #converts mouse coords to a formatted string
   timer_text = fontObj.render( mouse_position, True, BLUE, WHITE)
   timer_rect = timer_text.get_rect()
   timer_rect.bottomright = (SCREEN_WIDTH-5, SCREEN_HEIGHT-5) 
   screen.blit(timer_text, timer_rect)

#START CODE HERE FOR THIS SPECIFIC PROGRAM

#DEFINE VARIABLES
#RED SIDE
redY = 400
red_score = 0
#BLUE SIDE
blueY = 400
blue_score = 0
#BALL
xPos = 400
yPos = 400
ball_speed = 4
ball_dx = random.choice( [-ball_speed, ball_speed] )
ball_dy = random.choice( [-ball_speed, ball_speed] )
#OTHER
game_over = False
winner = None
max_points = 3
#DEFINE FUNCTIONS

#DRAW ITEMS AND MAKE CALCULATIONS THAT DON'T REQUIRE THE GAME LOOP

#GAME LOOP
FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

running = True
count = 0
screen.fill((255, 255, 255))  # Fill the background with white


while running: # This loop will continue to run until user closes program
    for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          exit()

    fpsClock.tick(FPS) # sets the timing of the loop in frames per second
    screen.fill(BLACK)
    #Pos = xPos + 2 
    #yPos = yPos + 1
    ball = pygame.image.load("files/ball.jpg")
    ball = pygame.transform.scale(ball, (float(ball.get_width()*.12), float(ball.get_height()*.12)))
    ballRect = ball.get_rect()
    ballWidth = ball.get_width()
    
    red_paddle = pygame.Rect(0, redY, 15, 75)
    blue_paddle = pygame.Rect(785, blueY, 15, 75)


    keys = pygame.key.get_pressed()
   
    if keys[K_w]:
      redY -= 7
    if keys[K_s]:
      redY += 7

    if keys[K_UP]:
      blueY -= 7
    if keys[K_DOWN]:
      blueY += 7

   # this limits paddles to stay on the screen
    redY = max(200, min(redY, SCREEN_WIDTH - 200))
    blueY = max(200, min(blueY, SCREEN_WIDTH - 200))
    
    #BALL INFO
    xPos += ball_dx
    yPos += ball_dy
    if xPos <= 0 or xPos >= SCREEN_WIDTH - ballWidth:
      ball_dx = -ball_dx
      #ball_dy = max( -18, min( ball_dy + random.randint(-6,6),18) )
    if yPos <= 175 + ballWidth or yPos >= 675 - ballWidth:
      ball_dy = -ball_dy
      #ball_dx = max( -18, min( ball_dy + random.randint(-6,6),18) )
    #BALL WIDTH IS 23

    #RED SCORE
    pygame.draw.rect(screen, WHITE, [0, 0, 800, 200], 0)
    pygame.draw.rect(screen, WHITE, [0, 675, 800, 250], 0)
    font = pygame.font.SysFont("Arial",80) #choose font
    text = font.render(str(red_score), True, BLACK, None) #text that you want to display
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (150, 150) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen  

    #BLUE SCORE
    font = pygame.font.SysFont("Arial",80) #choose font
    text = font.render(str(blue_score), True, BLACK, None) #text that you want to display
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (650, 150) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen  

    #RED HEADER
    font = pygame.font.SysFont("Arial",80) #choose font
    text = font.render(str("RED"), True, BLACK, None) #text that you want to display
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (150, 45) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen  

    #BLUE HEADER
    font = pygame.font.SysFont("Arial",80) #choose font
    text = font.render(str("BLUE"), True, BLACK, None) #text that you want to displays)
    text_rect = text.get_rect() #creates text bounding box
    text_rect.center = (640, 45) #positions bounding box at screen coordinates
    screen.blit(text, text_rect) #writes the text to the screen  
    
    # line = pygame.image.load("line.png")
    # lineRect = line.get_rect()
    # screen.blit(line, (0,200))
    # hit_red = ballRect.colliderect(lineRect) 
    # hit_blue = ballRect.colliderect(lineRect) 

    # if hit_red:
    #   blue_score += 1
    #   time.sleep(1)
    #   xPos = 400
    #   yPos = 400
    # elif hit_blue:
    #   red_score += 1
    #   time.sleep(1)
    #   xPos = 400
    #   yPos = 400

    #COLLISIONS
    if red_paddle.colliderect(ballRect):
      ball_dy = -ball_dy
      print("collision")
    if blue_paddle.colliderect(ballRect):
      ball_dy = -ball_dy
      print("collision")
    
    print(red_paddle)
    #DRAWS PADDLES
    #RED
    pygame.draw.rect(screen, RED, red_paddle, 0)
    #BLUE
    pygame.draw.rect(screen, BLUE, blue_paddle, 0)  

    screen.blit(ball, (xPos, yPos))

    #update the screen
    print_coordinates_on_screen()
    pygame.display.update()  
    #end of while loop