import pygame
import time
import random
pygame.init()
white = (255, 255, 255)  # creating colour with RGB parameter
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode(
    (display_width, display_height))  # creating the game room
pygame.display.set_caption('snake dj')  # adding the screen title
pygame.display.update()

clock = pygame.time.Clock()  # capital C activating pygame clock
block_size = 10
FPS = 30
font = pygame.font.SysFont(None, 25)
# font size


def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [
                         XnY[0], XnY[1], block_size, block_size])


def message_to_screen(msg, colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [200, 300])
    # blit is used to show text(what,where)


def gameLoop():
    gameExit = False
    gameOver = False
    # snake is made of blocks,so we r specifying the positon of leading block
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    snakelist = []
    snakelength = 1
    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(
        0, display_height-block_size)/10.0)*10.0
    while not gameExit:  # starting game loop
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen(
                "game over,press C to play again or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            # event handling loop
            if event.type == pygame.QUIT:
                # activating the exit button
                gameExit = True
            if event.type == pygame.KEYDOWN:  # pressing key
                if event.key == pygame.K_LEFT:  # pressing left arrow
                    lead_x_change = -block_size
                    lead_y_change = 0
                    # move to left by same amount
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:  # pressing left arrow
                    lead_y_change = -block_size
                    lead_x_change = 0
                    # move to left by same amount
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True  # x>=800 y>=600 is used to avoid boundary problem

            '''if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    lead_x_change = 0
             '''
        lead_x += lead_x_change
        lead_y += lead_y_change
        # problem due to not defining fps

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [
                         randAppleX, randAppleY, block_size, block_size])

        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
            del snakelist[0]
        for eachsegment in snakelist[:-1]:
            if eachsegment == snakehead:
                gameOver = True

        snake(block_size, snakelist)
        # (where it is drawn,colour,[positons,width,height])
        # gameDisplay.fill(red,rect=[200,200,50,50])#quick process to draw
        # it does not make the block moving continuously
        pygame.display.update()
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = round(random.randrange(
                0, display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(
                0, display_height-block_size)/10.0)*10.0
            snakelength += 5
        clock.tick(FPS)
    #message_to_screen("YOU LOSE",red)
        # right fps for snake game
        # first define movement then define fps

        # updating the display in each step
        # print(event)
   # message_to_screen("YOU LOSE,GO OUTSIDE YOU FOOL",red)
    # pygame.display.update()
    # time.sleep(2)#user have to wait for some time
    pygame.quit()
    quit()


gameLoop()
