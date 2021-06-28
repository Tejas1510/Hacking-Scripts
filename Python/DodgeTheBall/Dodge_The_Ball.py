from tkinter import*
from math import *
import pygame
import sys
import random

pygame.init()

width = 400
height = 500
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Dodge The Ball")
clock = pygame.time.Clock()

background = (51, 51, 51)
playerColor = (249, 231, 159)

red = (203, 67, 53)
yellow = (241, 196, 15)
blue = (46, 134, 193)
green = (34, 153, 84)
purple = (136, 78, 160)
orange = (214, 137, 16)

colors = [red, yellow, blue, green, purple, orange]

score = 0


class Ball:
    def __init__(self, radius, speed):
        self.x = 0
        self.y = 0
        self.r = radius
        self.color = 0
        self.speed = speed
        self.angle = 0
    
    def createBall(self):
        self.x = width/2 - self.r
        self.y = height/2 - self.r
        self.color = random.choice(colors)
        self.angle = random.randint(-180, 180)
    
    def move(self):
        self.x += self.speed*cos(radians(self.angle))
        self.y += self.speed*sin(radians(self.angle))

        if self.x < self.r or self.x + self.r > width:
            self.angle = 180 - self.angle
        if self.y < self.r or self.y + self.r > height:
            self.angle *= -1

    def draw(self):
        pygame.draw.ellipse(display, self.color, (self.x - self.r, self.y - self.r, self.r*2, self.r*2))

    def collision(self, radius):
        pos = pygame.mouse.get_pos()

        dist = ((pos[0] - self.x)**2 + (pos[1] - self.y)**2)**0.5

        if dist <= self.r + radius:
            gameOver()

class Target:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 20
        self.h = self.w

    def generateNewCoord(self):
        self.x = random.randint(self.w, width - self.w)
        self.y = random.randint(self.h, height - self.h)

    def draw(self):
        color = random.choice(colors)

        pygame.draw.rect(display, color, (self.x, self.y, self.w, self.h))

    
def gameOver():
    loop = True

    font = pygame.font.SysFont("Agency FB", 100)
    text = font.render("Game Over!", True, (230, 230, 230))
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()

        display.fill(background)

        display.blit(text, (20, height/2 - 100))
        displayScore()
        
        pygame.display.update()
        clock.tick()


def checkCollision(target, d, objTarget):
    pos = pygame.mouse.get_pos()
    dist = ((pos[0] - target[0] - objTarget.w)**2 + (pos[1] - target[1]  - objTarget.h)**2)**0.5

    if dist <= d + objTarget.w:
        return True
    return False


def drawPlayerPointer(pos, r):
    pygame.draw.ellipse(display, playerColor, (pos[0] - r, pos[1] - r, 2*r, 2*r))


def close():
    pygame.quit()
    sys.exit()

def displayScore():
    font = pygame.font.SysFont("Forte", 30)
    scoreText = font.render("Score: " + str(score), True, (230, 230, 230))
    display.blit(scoreText, (10, 10))


def gameLoop():
    global score
    score = 0
    
    loop = True

    pRadius = 10

    balls = []

    for i in range(1):
        newBall = Ball(pRadius + 2, 5)
        newBall.createBall()
        balls.append(newBall)

    target = Target()
    target.generateNewCoord()
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_r:
                    gameLoop()

        display.fill(background)

        for i in range(len(balls)):
            balls[i].move()
            
        for i in range(len(balls)):
            balls[i].draw()
            
        for i in range(len(balls)):
            balls[i].collision(pRadius)

        playerPos = pygame.mouse.get_pos()
        drawPlayerPointer((playerPos[0], playerPos[1]), pRadius)

        collide = checkCollision((target.x, target.y), pRadius, target)
        
        if collide:
            score += 1
            target.generateNewCoord()
        elif score == 2 and len(balls) == 1:
            newBall = Ball(pRadius + 2, 5)
            newBall.createBall()
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 5 and len(balls) == 2:
            newBall = Ball(pRadius + 2, 6)
            newBall.createBall()
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 10 and len(balls) == 3:
            newBall = Ball(pRadius + 2, 7)
            newBall.createBall()
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 15 and len(balls) == 4:
            newBall = Ball(pRadius + 2, 8)
            newBall.createBall()
            balls.append(newBall)
            target.generateNewCoord()
        elif score == 20 and len(balls) == 5:
            newBall = Ball(pRadius + 2, 9)
            newBall.createBall()
            balls.append(newBall)
            target.generateNewCoord()

        target.draw()
        displayScore()
        
        pygame.display.update()
        clock.tick(60)

gameLoop()
