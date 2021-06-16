import random 
import sys # We will use sys.exit to exit the program
import pygame
from pygame.locals import * # Basic pygame imports

pygame.init()# Initialize all pygame's modules
# Global Variables for the game
FPS = 45
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 500
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

GROUNDY = SCREEN_HEIGHT * 0.8
GAME_PHOTOS = {}
GAME_SOUNDS = {}
PLAYER = 'gallery/PHOTOS/bird.png'
BACKGROUND = 'gallery/PHOTOS/background.png'
PIPE = 'gallery/PHOTOS/pipe.png'



def welcomeScreen():
    """
    Shows welcome images on the screen
    """
    playerx = int(SCREEN_WIDTH/5)
    playery = int((SCREEN_HEIGHT - GAME_PHOTOS['player'].get_height())/2.5)
    messagex = int((SCREEN_WIDTH - GAME_PHOTOS['message'].get_width())/2)
    messagey = int(SCREEN_HEIGHT*0.13)
    basex = 0
    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT or (event.type==K_DOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            # If the user presses space or up key, start the game for them
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key == K_UP):
                return    
            else:
                SCREEN.blit(GAME_PHOTOS['background'], (0, 0))    
                SCREEN.blit(GAME_PHOTOS['player'], (playerx, playery))    
                SCREEN.blit(GAME_PHOTOS['message'], (messagex,messagey ))    
                SCREEN.blit(GAME_PHOTOS['base'], (basex, GROUNDY))    
                pygame.display.update()
                FPSCLOCK.tick(FPS)   


def mainGame():
    playerx = int(SCREEN_WIDTH/5)
    playery = int(SCREEN_WIDTH/2)
    basex = 0
    score = 0

    # Create 2 pipes for blitting on the screen
    newPipe1 = getRandomPipe()
    newPipe2 = getRandomPipe()

    # my List of upper pipes
    upperPipes = [
        {'x': SCREEN_WIDTH+200, 'y':newPipe1[0]['y']},
        {'x': SCREEN_WIDTH+200+(SCREEN_WIDTH/2), 'y':newPipe2[0]['y']},
    ]
    # my List of lower pipes
    lowerPipes = [
        {'x': SCREEN_WIDTH+200, 'y':newPipe1[1]['y']},
        {'x': SCREEN_WIDTH+200+(SCREEN_WIDTH/2), 'y':newPipe2[1]['y']},
    ]

    pipeVelX = -4

    playerVelY = -9
    playerMaxVelY = 10
    playerMinVelY = -8
    playerAccY = 1

    playerFlapAccv = -8 # velocity while flapping
    playerFlapped = False # It is true only when the bird is flapping


    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and (event.key == K_SPACE or event.key == K_UP):
                if playery > 0:
                    playerVelY = playerFlapAccv
                    playerFlapped = True
                    GAME_SOUNDS['wing'].play()


        crashTest = isCollide(playerx, playery, upperPipes, lowerPipes) # This function will return true if the player is crashed
        if crashTest:
            X1 = 300
            Y1 = 600
            X2 = 300
            Y2 = 600
            SCREEN.blit(GAME_PHOTOS['background'], (0, 0))
            font = pygame.font.SysFont(None, 35)
            GAME_OVER = font.render('GAME OVER ', True, (255, 0, 0))
            SCORE_TEXT= font.render(f'Your Score Was {score}', True, (0, 0, 0))
            GAME_OVER.set_alpha(127)
            SCORE_TEXT.set_alpha(127)
            SCREEN.blit(GAME_OVER, (SCREEN_WIDTH, SCREEN_HEIGHT))
            SCREEN.blit(GAME_OVER, (X1, Y1))
            textRect = GAME_OVER.get_rect()
            textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
            textRect1 = SCORE_TEXT.get_rect()
            textRect1.center = (X1 // 2, Y1 // 3)
            RESTART_GAME= font.render('Press Enter to play again', True, (0, 0, 0))
            RESTART_GAME.set_alpha(127)
            textRect2 = RESTART_GAME.get_rect()
            textRect2.center = (X1//2, 2*Y1//3)
            while True:
                SCREEN.blit(GAME_OVER, textRect)
                SCREEN.blit(SCORE_TEXT, textRect1)
                SCREEN.blit(RESTART_GAME, textRect2)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            pygame.init()
                            welcomeScreen()
                            mainGame()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                pygame.display.update()        
        playerMidPos = playerx + GAME_PHOTOS['player'].get_width()/2
        for pipe in upperPipes:
            pipeMidPos = pipe['x'] + GAME_PHOTOS['pipe'][0].get_width()/2
            if pipeMidPos<= playerMidPos < pipeMidPos +4:
                score +=1
                GAME_SOUNDS['point'].play()
                


        if playerVelY <playerMaxVelY and not playerFlapped:
            playerVelY += playerAccY

        if playerFlapped:
            playerFlapped = False            
        playerHeight = GAME_PHOTOS['player'].get_height()
        playery = playery + min(playerVelY, GROUNDY - playery - playerHeight)

        # moving pipes to the left
        for upperPipe , lowerPipe in zip(upperPipes, lowerPipes):
            upperPipe['x'] += pipeVelX
            lowerPipe['x'] += pipeVelX

        # Adding a new pipe when the first is about to cross the leftmost part of the screen
        if 0<upperPipes[0]['x']<5:
            newpipe = getRandomPipe()
            upperPipes.append(newpipe[0])
            lowerPipes.append(newpipe[1])

        # if the pipe is out of the screen, it removes it
        if upperPipes[0]['x'] < -GAME_PHOTOS['pipe'][0].get_width():
            upperPipes.pop(0)
            lowerPipes.pop(0)
        
        # blitting the photos 
        SCREEN.blit(GAME_PHOTOS['background'], (0, 0))
        for upperPipe, lowerPipe in zip(upperPipes, lowerPipes):
            SCREEN.blit(GAME_PHOTOS['pipe'][0], (upperPipe['x'], upperPipe['y']))
            SCREEN.blit(GAME_PHOTOS['pipe'][1], (lowerPipe['x'], lowerPipe['y']))

        SCREEN.blit(GAME_PHOTOS['base'], (basex, GROUNDY))
        SCREEN.blit(GAME_PHOTOS['player'], (playerx, playery))
        myDigits = [int(x) for x in list(str(score))]
        width = 0
        for digit in myDigits:
            width += GAME_PHOTOS['numbers'][digit].get_width()
        Xoffset = (SCREEN_WIDTH - width)/2

        for digit in myDigits:
            SCREEN.blit(GAME_PHOTOS['numbers'][digit], (Xoffset, SCREEN_HEIGHT*0.12))
            Xoffset += GAME_PHOTOS['numbers'][digit].get_width()
        pygame.display.update()
        FPSCLOCK.tick(FPS)



def isCollide(playerx, playery, upperPipes, lowerPipes):
    if playery> GROUNDY - 25  or playery<0:
        GAME_SOUNDS['hit'].play()
        return True
    
    for pipe in upperPipes:
        pipeHeight = GAME_PHOTOS['pipe'][0].get_height()
        if(playery < pipeHeight + pipe['y'] and abs(playerx - pipe['x']) < GAME_PHOTOS['pipe'][0].get_width()):
            GAME_SOUNDS['hit'].play()
            return True

    for pipe in lowerPipes:
        if (playery + GAME_PHOTOS['player'].get_height() > pipe['y']) and abs(playerx - pipe['x']) < GAME_PHOTOS['pipe'][0].get_width():
            GAME_SOUNDS['hit'].play()
            return True

    return False
def getRandomPipe():
    """
    Generate positions of two pipes(one bottom straight and one top rotated ) for blitting on the screen
    """
    pipeHeight = GAME_PHOTOS['pipe'][0].get_height()
    offset = SCREEN_HEIGHT/3
    y2 = offset + random.randrange(0, int(SCREEN_HEIGHT - GAME_PHOTOS['base'].get_height()  - 1.2 *offset))
    pipeX = SCREEN_WIDTH + 10
    y1 = pipeHeight - y2 + offset
    pipe = [
        {'x': pipeX, 'y': -y1}, #upper Pipe
        {'x': pipeX, 'y': y2}   #lower Pipe
    ]
    return pipe






if __name__ == "__main__":
    # This will be the main point from where our game will start
    pygame.init() 
    FPSCLOCK = pygame.time.Clock()
    pygame.display.set_caption('Flappy Bird by thefunnyintrovert')
    GAME_PHOTOS['numbers'] = ( 
        pygame.image.load('gallery/PHOTOS/0.png').convert_alpha(),
        pygame.image.load('gallery/PHOTOS/1.png').convert_alpha(),
        pygame.image.load('gallery/PHOTOS/2.png').convert_alpha(),
        pygame.image.load('gallery/PHOTOS/3.png').convert_alpha(),
        pygame.image.load('gallery/PHOTOS/4.png').convert_alpha(),
        pygame.image.load('gallery/PHOTOS/5.png').convert_alpha(),
        pygame.image.load('gallery/PHOTOS/6.png').convert_alpha(),
        pygame.image.load('gallery/PHOTOS/7.png').convert_alpha(),
        pygame.image.load('gallery/PHOTOS/8.png').convert_alpha(),
        pygame.image.load('gallery/PHOTOS/9.png').convert_alpha(),
    )

    GAME_PHOTOS['message'] =pygame.image.load('gallery/PHOTOS/test.png').convert_alpha()
    GAME_PHOTOS['base'] =pygame.image.load('gallery/PHOTOS/base.png').convert_alpha()
    GAME_PHOTOS['pipe'] =(pygame.transform.rotate(pygame.image.load( PIPE).convert_alpha(), 180), 
    pygame.image.load(PIPE).convert_alpha()
    )

    # Game sounds
    GAME_SOUNDS['die'] = pygame.mixer.Sound('gallery/audio/die.wav')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('gallery/audio/hit.wav')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('gallery/audio/point.wav')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('gallery/audio/swoosh.wav')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('gallery/audio/wing.wav')

    GAME_PHOTOS['background'] = pygame.image.load(BACKGROUND).convert()
    GAME_PHOTOS['player'] = pygame.image.load(PLAYER).convert_alpha()

    while True:
        welcomeScreen() # Shows welcome screen to the user until he presses a shown button
        mainGame() # This is the main game function 
pygame.quit()