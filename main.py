__author__ = "Trang Ha"

import pygame
import random

def drawNguess():

    # Initialize and customize the screen
    pygame.init()
    gameMode = True
    screen = pygame.display.set_mode((800, 600))
    icon = pygame.image.load("icon.png")
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Draw N Guess")

    # Set variables to store score value, user input
    scoreVal = 0
    guessWord = ""

   # Set up timer



    # Set up random pictionary word
    with open("pictionary.txt", "r") as pictionary:
        w = pictionary.read().split()
    global randomWord
    randomWord = random.choice(w)

    def txtObject(txt, fontSize, color):
        txtFont = pygame.font.Font("freesansbold.ttf", fontSize)
        txtRender = txtFont.render(txt, True, color)
        return txtRender, txtRender.get_rect()

    def display():
        # Display score on the screen
        score, scoreRect = txtObject("Score: " + str(scoreVal), 16, (255, 255, 255))
        screen.blit(score, (50,30))

        # Display pictionary word on the screen
        pygame.draw.rect(screen, (255, 255, 255), [320, 30, 150, 30])
        picWord, txtRect = txtObject(randomWord.upper(), 18, (0, 0, 0))
        txtRect.center = ((320+(150/2), (30+(30/2))))
        screen.blit(picWord, txtRect)


        # Display guesing word on the screen
        pygame.draw.rect(screen, (255, 255, 255), [320, 515, 150, 30])
        userIn, userInRect = txtObject(guessWord, 16, (0, 0, 0))
        userInRect.center = ((320+(150/2), (515+(30/2))))
        screen.blit(userIn, userInRect)

        # Display timer on the screen
        timer, timerRect = txtObject("Timer: " + str(0), 16, (255, 255, 255))
        screen.blit(timer, (660, 30))

    # Set up buton
    def button(buttonTxt, x, y, width, height, active= None):

        getPos = pygame.mouse.get_pos()
        getPress = pygame.mouse.get_pressed()
        button, buttonRect = txtObject(buttonTxt, 16, (0, 0, 0))
        buttonRect.center = ((x+(width/2)), (y+(height/2)))
        pygame.draw.rect(screen, (255, 255, 255), [x, y, width, height])
        screen.blit(button, buttonRect)

        # If the x, y coordinates of the mouse = the x, y coordinates of the button, then executes these following
        if x+width > getPos[0] > x and y+height > getPos[1] > y:
            # Check if the button is clicked
            if getPress[0] == 1 and active != None:
                # If the pass button is clicked, randomize the word and display on the screen again
                if active == "pass":
                    global randomWord
                    randomWord = random.choice(w)
                    screen.fill((0, 0, 0))
                # If the erase button is clicked, clean the screen by color the background to black
                elif active == "erase":
                    screen.fill((0, 0, 0))


    while gameMode:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameMode = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    guessWord = guessWord[:-1]
                else:
                    guessWord += event.unicode
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.draw.rect(screen, (255, 255, 255), (x, y, 10, 10))
                pygame.display.update()

        button("Erase", 50, 515, 60, 30, "erase")
        button("Pass", 668, 515, 60, 30, "pass")


        display()
        pygame.display.update()

drawNguess()