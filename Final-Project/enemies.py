# 8
# multiple enemies
import pygame,sys,random
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
# Enemyy
enemyImg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6
# make the enemy scatter
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('assets/enemy3.png'))
    enemyImg.append(pygame.image.load('assets/enemy2.png'))
    enemyImg.append(pygame.image.load('assets/enemyAlien.png'))
    enemyImg.append(pygame.image.load('assets/EnemyAlien2.png'))
    enemyImg.append(pygame.image.load('assets/enemyGreen.png'))
    enemyImg.append(pygame.image.load('assets/monsterAlien.png'))
    enemyImg.append(pygame.image.load('assets/monsterAlien2.png'))
    enemyx.append(random.randint(0,736))
    enemyy.append(random.randint(55,150))
    enemyx_change.append(3)
    enemyy_change.append(40)

# Create Bullet
bulletImg = pygame.image.load('assets/bullet1.png')
bulletx = 0
bullety = 480
bulletx_change = 0
bullety_change = 5
bullet_state = 'ready'
    
# function of player
def rocket(x,y):
    screen.blit(rocketImg,(x,y))

# function of enemy
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))

def bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 40, y + 15  ))

def Collision(enemyx,enemyy,bulletx,bullety):
    # using distance formula
    # square (x1-x2)** + (y2-y1)**
    distance = math.sqrt(math.pow(enemyx-bulletx,2) + (math.pow(enemyy-bullety,2)))
    if distance < 50:
        return True
    else:
        return False

# Loop
start = True
while start :
    screen .fill((0, 0, 0))
    # Background image
    screen.blit(background,(0,0))
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
                    bullety = rockety
                    bullet(bulletx,bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rocketx_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rockety_change = 0  
                

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
    for i in range(num_of_enemies):
        enemyx[i] += enemyx_change[i]
        # Boundaris enemy => avoid missing rocket from game
        if enemyx[i] <= 0:
            enemyx_change[i] = 2
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 736:
            enemyx_change[i] = -2
            enemyy[i] += enemyy_change[i]
        
        # Collision
        # move collision in loop
        collision = Collision(enemyx[i],enemyy[i],bulletx,bullety)
        if collision:
            bullety = 480
            bullet_state = 'ready'
            enemyx[i] = random.randint(0,800)
            enemyy[i] = random.randint(55,150)
        # invoke move in loop
        enemy(enemyx[i],enemyy[i], i)

    # Bullet Movement
    if bullety <= 0 :
        bullety = 480
        bullet_state = 'ready'
    
    if bullet_state == 'fire':
        bullet(bulletx,bullety)
        bullety -= bullety_change
 
    # rocket 
    rocket(rocketx,rockety)
    pygame.display.update()



