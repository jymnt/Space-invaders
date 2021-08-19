# First
# Make window -FIRST-
import pygame,random

# initialize the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((800,500))

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

