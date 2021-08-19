import pygame,random,sys
import math
from pygame import mixer

# initialize the pygame
pygame.init()

# create screen
screen = pygame.display.set_mode((900,700))

# Background
background = pygame.image.load('assets/background3.png').convert()
# pygame.display.set_background(background)

# Add Sound Background
mixer.music.load('assets/Background.wav')
mixer.music.play(-1)

# Caption and Logo (icon)
pygame.display.set_caption('SPACE INVADERS')
icon = pygame.image.load('assets/ufo.png')
pygame.display.set_icon(icon)

# Player/Rocket
rocketImg = pygame.image.load('assets/rocket1.png').convert_alpha()
rocketx = 375
rockety = 570
rocket_frames = (rocketx,rockety)
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
    enemyImg.append(pygame.image.load('assets/enemy3.png').convert_alpha())
    enemyImg.append(pygame.image.load('assets/enemy2.png').convert_alpha())
    enemyImg.append(pygame.image.load('assets/enemyAlien.png').convert_alpha())
    enemyImg.append(pygame.image.load('assets/EnemyAlien2.png').convert_alpha())
    enemyImg.append(pygame.image.load('assets/enemyGreen.png').convert_alpha())
    enemyImg.append(pygame.image.load('assets/monsterAlien.png').convert_alpha())
    enemyImg.append(pygame.image.load('assets/monsterAlien2.png').convert_alpha())
    enemyx.append(random.randint(0,735))
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

# Adding Score
score_value = 0 
high_score = 0
font = pygame.font.Font('04B_19.ttf',30)

textx = 10
texty = 10

# Game Over
GameOver_font = pygame.font.Font('04B_19.ttf', 100)

# Frame
enemy_surface = enemyImg[num_of_enemies]
enemy_rect = enemy_surface.get_rect(center = (50,256))


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

def display_score():
    if start :
        score = font.render("Score : " + str(int(score_value)), True, (153,0,153))
        score_place = score.get_rect(center = (100,30))
        screen.blit(score, score_place)
    else :
        score = font.render(f'Score :  {int(score_value)}', True, (153,0,153))
        score_place = score.get_rect(center = (100,30))
        screen.blit(score, score_place)
        
        HighScore = font.render(f'High Score :  {int(score_value)}', True, (153,0,153))
        HighScore_place = score.get_rect(center = (690,650))
        screen.blit(HighScore,HighScore_place)

# def gameOverShow():
def game_over_show():
    game_over = GameOver_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(game_over, (200, 250))

# Loop
start = False
while True :
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit
            sys.exit() # exit
        clicked = False
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
                    # Add sound Bullets
                    bullet_sound = mixer.Sound('assets/bullet.wav')
                    bullet_sound.play()
                    bulletx = rocketx
                    bullet(bulletx,bullety)
            if clicked and not start :
            # start = true // must here !!
            # reset all of them before we start again
                GameOver_font= []
                score_value = 0
                start = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rocketx_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rockety_change = 0  

    if True :
        # movement (rocket)
        rocketx += rocketx_change
        rockety += rockety_change
        # Boundaris rocket +> avoid missing rocket from game
        start = Collision(enemyx[i],enemyy[i],bulletx,bullety)
        if not False:
            if high_score < score_value:
                high_score = score_value
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
        # Enemy Movement
        for i in range(num_of_enemies):
            # Game over
            if enemyy[i] > 440:
                for j in range(num_of_enemies):
                    enemyy[j] = 2000
                game_over_show()
                break
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
                # Add sound shot/explosion
                shot_sound = mixer.Sound('assets/shot.wav')
                shot_sound.play()
                bullety = 480
                bullet_state = 'ready'
                score_value += 1
                enemyx[i] = random.randint(0,735)
                enemyy[i] = random.randint(55,150)
            # invoke move in loop
            enemy(enemyx[i],enemyy[i], i)
        display_score()
        # Bullet Movement
        if bullety <= 0 :
            bullety = 480
            bullet_state = 'ready'
        
        if bullet_state == 'fire':
            bullet(bulletx,bullety)
            bullety -= bullety_change
    pygame.display.update()
