import pygame
import random
import math
from pygame import mixer
pygame.init()
# for screen to display game
screen = pygame.display.set_mode((800, 600))

# background image
background = pygame.image.load('bg.png')

# bg music
mixer.music.load('bg_music.mp3')
mixer.music.play(-1)
# changing the terminal name to project name
pygame.display.set_caption(" Space killer ashwan game ")
# to change the icon from python to our own
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# adding shooter
playerImg = pygame.image.load('fire.png')
playerX = 360
playerY = 460
playerX_change = 0

# add villen
villenImg = []
villenX = []
villenY = []
villenX_change = []
villenY_change = []
num_of_villens = 4
for i in range( num_of_villens):
    villenImg.append(pygame.image.load('villen.png'))
    villenX.append(random.randint(0, 736))
    villenY.append(random.randint(50, 150))
    villenX_change.append(0.3)
    villenY_change.append(40)

# add bullet
# ready means you cant see the bullet but for the wright time
bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state= "ready"
# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10
# game over
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score = font.render("score:"+ str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def player(x, y):
    screen.blit(playerImg, (x, y))
def game_over_text():
     over_text = over_font.render("GAME OVER", True, (255, 255, 255))
     screen.blit(over_text, (200,250))

def villen(x, y):
    screen.blit(villenImg[i], (x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet, (x+16, y+10))

def iscollision(villenX, villenY, bulletX, bulletY):
    distance= math.sqrt((math.pow(bulletX-bulletY, 2))+(math.pow(villenX-villenY, 2)))
    if distance<25:
        return True
    else:
        return False
# game loop to stay terminal for long timr
running = True
while running:
    # here three values are for RGB colours
    screen.fill((0, 26, 5))
    # background image
    screen.blit(background,(0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # for input keyboard
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.7
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.7
            if event.key == pygame.K_SPACE:
                    bullet_sound=mixer.Sound('bullet.mp3')
                    bullet_sound.play()
                    bulletX= playerX
                    fire_bullet(playerX,bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    for i in range(num_of_villens):
        # game over
            if villenY[i]>400:
                for j in range(num_of_villens):
                    villenY[j] = 2000
                game_over_text()
                break
            villenX[i] += villenX_change[i]
            if villenX[i] <= 0:
                villenX_change[i] = 0.3
                villenY[i]+=villenY_change[i]
            elif villenX[i] >= 736:
                villenX_change[i] = -0.3
                villenY[i]+=villenY_change[i]
                # collision
            collision = iscollision(villenX[i], villenY[i], bulletX, bulletY)
            if collision:
                explosion_sound = mixer.Sound('collision.mp3')
                explosion_sound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                # print(score)
                villenX[i] = random.randint(0, 735)
                villenY[i] = random.randint(50, 150)
            villen(villenX[i], villenY[i])
    # bullet movement
    if bulletY<=0:
        bulletY=480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX ,textY)
    pygame.display.update()









