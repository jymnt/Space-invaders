# 7
# Make Collision
# Kill enemy

import pygame,random
import math

# initialize the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((900,700))

# Background
background = pygame.image.load('assets/background3.png')
# pygame.display.set_background(background)

# Caption and Logo (icon)
pygame.display.set_caption('SPACE INVADERS')
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)

# Player/Rocket
rocketImg = pygame.image.load('assets/rocket1.png')
rocketx = 375
rockety = 570
rocketx_change = 0
rockety_change = 0

# Create Enemy 1
enemyImg1 = pygame.image.load('assets/enemy3.png')
# Create Enemy 2
enemyImg2 = pygame.image.load('assets/enemy2.png')
# Create Enemy 3
enemyImg3 = pygame.image.load('assets/enemyAlien.png')
# Create Enemy 4
enemyImg4 = pygame.image.load('assets/EnemyAlien2.png')
# Create Enemy 5
enemyImg5 = pygame.image.load('assets/enemyGreen.png')
# Create Enemy 6
enemyImg6 = pygame.image.load('assets/monsterAlien.png')
# Create Enemy 7
enemyImg7 = pygame.image.load('assets/monsterAlien2.png')
enemyx = random.randint(0,735)
enemyy = random.randint(55,150)
enemyx_change = 3
enemyy_change = 40

# Create Bullet
bulletImg = pygame.image.load('assets/bullet1.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 5
bullet_state = 'ready'

# score
score = 0
    
# function of player
def rocket(x,y):
    screen.blit(rocketImg,(x,y))

# function of enemy
def enemy(x,y):
    screen.blit(enemyImg1,(x,y))
    screen.blit(enemyImg2,(x,y))
    screen.blit(enemyImg3,(x,y))
    screen.blit(enemyImg4,(x,y))
    screen.blit(enemyImg5,(x,y))
    screen.blit(enemyImg6,(x,y))
    screen.blit(enemyImg7,(x,y))

def bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 40, y + 15  ))

def Collision(enemyx,enemyy,bulletx,bullety):
    # using distance formula
    # square (x1-x2)** + (y2-y1)**
    distance = math.sqrt(math.pow(enemyx-bulletx,2) + (math.pow(enemyy-bullety,2)))
    if distance < 27:
        return True
    else:
        return False

# Loop
start = True
while start :
    screen .fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        # Movement rocket with keystroke (right and left)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocketx_change = -7
            if event.key == pygame.K_RIGHT:
                rocketx_change = 7
            if event.key == pygame.K_UP:
                rockety_change = -7
            if event.key == pygame.K_DOWN:
                rockety_change = 7
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletx = rocketx
                    bullet(bulletx,bullety)
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

    # Enemy Movement
    enemyx += enemyx_change
    # Boundaris enemy => avoid missing rocket from game
    if enemyx <= 0:
        enemyx_change = 2
        enemyy += enemyy_change
    elif enemyx >= 736:
        enemyx_change = -2
        enemyy += enemyy_change

    # Bullet Movement
    if bullety <= 0 :
        bullety = 450
        bullet_state = 'ready'
    
    if bullet_state == 'fire':
        bullet(bulletx,bullety)
        bullety -= bullety_change

    # Collision
    collision = Collision(enemyx,enemyy,bulletx,bullety)
    if collision:
        bullety = 480
        bullet_state = 'ready'
        score += 1
        print(score)
        enemyx = random.randint(0,735)
        enemyy = random.randint(55,150)

    # rocket 
    rocket(rocketx,rockety)
    enemy(enemyx,enemyy)
    pygame.display.update()



