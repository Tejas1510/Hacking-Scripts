# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame
# random library displays the image anywhere
import random
import math
# mixer library is for sound effects
from pygame import mixer

# initialise our pygame
pygame.init()

# create the gaming screen
screen = pygame.display.set_mode((800, 600))

# background image
background = pygame.image.load('background.png')

# background sound
# mixer.music is to play the music continuously but if we have to play a very short sound like that of bullet than we
# have to add mixer.sound
mixer.music.load('background.wav')
mixer.music.play(-1)  # -1 is to play the sound continuously

# title and logo
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space-invaders.png')
playerX = 370
playerY = 480
playerXchange = 0

# Enemy single
# enemyImg = pygame.image.load('enemy.png')
# enemyX = random.randint(0, 735)
# enemyY = random.randint(50, 150)
# enemyXchange = 4
# enemyYchange = 40

# enemy multiple
enemyImg = []
enemyX = []
enemyY = []
enemyXchange = []
enemyYchange = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyXchange.append(4)
    enemyYchange.append(40)

# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletXchange = 0
bulletYchange = 10
# ready state means you cant see the bullet right now
# fire state means bullet is currently in motion
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)


def show_score(x, y):
    score = font.render("Score:" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    # blit means to draw
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# gaming Zone loop
running = True
while running:
    # background color (rgb)
    # everything that is running continuously should be written inside the infinite loop
    # for eg screen.fill((0, 128, 0)) = green
    # make sure to call the player after screen.fill since after drawing the screen we will do the next steps
    screen.fill((0, 0, 0))

    # background image
    screen.blit(background, (0, 0))
    # whenever we press any key stroke it is an event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check whether the pressed keystroke is left or right key (this actually checks if any key on the keyboard is pressed)
        if event.type == pygame.KEYDOWN:  # checks if any key on the keyboard is being pressed
            if event.key == pygame.K_LEFT:
                playerXchange = -5  # it os actually speed of the movement
            if event.key == pygame.K_RIGHT:
                playerXchange = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # bullet sound
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    # gets the current x-coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:  # checks whether the pressed key is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0

    # setting the boundaries so that player doesnt go off-screen
    playerX += playerXchange

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # setting movement boundaries for the enemy
    for i in range(num_of_enemy):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemy):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyXchange[i]
        if enemyX[i] <= 0:
            enemyXchange[i] = 4
            enemyY[i] += enemyYchange[i]
        elif enemyX[i] >= 736:
            enemyXchange[i] = -4
            enemyY[i] += enemyYchange[i]

        # collision
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # explosion sound
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            # print(score_value)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYchange

    player(playerX, playerY)

    show_score(textX, textY)

    pygame.display.update()
