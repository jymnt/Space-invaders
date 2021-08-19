# 3
# adding image into our game
import pygame,random

# initialize the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('assets/background3.png')
# pygame.display.set_background(background)

# Title and Logo (icon)
pygame.display.set_caption('SPACE INVADERS')
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)
    
# Loop
start = True
while start :
    # loop for check event in pygame its quit or not
    for event in pygame.event.get():
        # if event in pygame quit, start not works
        # all black in pygame
        if event.type == pygame.QUIT:
            pygame.quit
            start = False

    # RGB (READ, GREEN AND BLUE)
    # White background
    screen .fill((0, 0, 0))
    # Background image
    screen.blit(background,(0,0))
    pygame.display.update()



