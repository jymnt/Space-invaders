# 4
# adding player into our game
# Movement rocket with keyboard input 
# Keyboard input (left,right and up,down)
import pygame,random

# initialize the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('assets/background3.png')
# pygame.display.set_background(background)

# Caption and Logo (icon)
pygame.display.set_caption('SPACE INVADERS')
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)

# Player/Rocket
rocketImg = pygame.image.load('assets/rocket1.png')
rocketx = 370
rockety = 480
rocketx_change = 0
rockety_change = 0

    
# function of player
def rocket(x,y):
    screen.blit(rocketImg,(x,y))

# Loop
start = True
while start :
    screen .fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        # Movement rocket with keystroke (right and left)
        if event.type == pygame.KEYDOWN:
            # Make rocket left and right
            if event.key == pygame.K_LEFT:
                rocketx_change = -7
            if event.key == pygame.K_RIGHT:
                rocketx_change = 7
            # Make rocket up and down
            if event.key == pygame.K_UP:
                rockety_change = -7
            if event.key == pygame.K_DOWN:
                rockety_change = 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rocketx_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rockety_change = 0  
                
    # Background image
    screen.blit(background,(0,0))
    # movement (rocket)
    rocketx += rocketx_change
    rockety += rockety_change
    # Boundaris rocket +> avoid missing rocket from game
    if rocketx <= 0:
        rocketx = 0
    elif rocketx >= 800:
        rocketx = 736
    if rockety <= 0:
        rockety = 0
    elif rockety >= 900:
        rockety = 500
        
    # rocket 
    rocket(rocketx,rockety)
    pygame.display.update()



