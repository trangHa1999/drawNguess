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

    # Set up score
    scoreVal = 0
    scoreFont = pygame.font.Font("freesansbold.ttf", 16)

    # Set up random pictionary word
    with open("pictionary.txt", "r") as pictionary:
        w = pictionary.read().split()
    global randomWord
    randomWord = random.choice(w)
    wordFont = pygame.font.Font("freesansbold.ttf", 18)

    # Set up user enters word on the screen
    guessWord = "None"
    guessFont = pygame.font.Font("freesansbold.ttf", 18)

    # Set up clock
    clock = pygame.time.Clock()
    clockFont = pygame.font.Font("freesansbold.ttf", 16)

    def display():
        # Display score on the screen
        score = scoreFont.render("Score: " + str(scoreVal), True, (255,255,255))
        screen.blit(score, (50,30))

        # Display pictionary word on the screen
        picWord = wordFont.render(randomWord.upper(), True, (0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), [320, 30, 150, 30])
        screen.blit(picWord, (335,32))

        # Display guesing word on the screen
        userGuess = guessFont.render(guessWord, True, (255, 255, 255))
        screen.blit(userGuess, (300, 515))

        # Display timer on the screen
        timer = clockFont.render("Timer: " + str(clock), True, (255, 255, 255))
        screen.blit(timer, (660, 30))

    # Set up buton
    def button(buttonTxt, x, y, width, height, active= None):

        getPos = pygame.mouse.get_pos()
        getPress = pygame.mouse.get_pressed()
        buttonFont = pygame.font.Font("freesansbold.ttf", 16)
        renderButton = buttonFont.render(buttonTxt, True, (0, 0, 0))
        pygame.draw.rect(screen, (255, 255, 255), [x, y, width, height])
        screen.blit(renderButton, [(x + 7), (y + 8)])

        # If the x, y coordinates of the mouse = the x, y coordinates of the button, then executes these following
        if x+width > getPos[0] > x and y+height > getPos[1] > y:
            # Check if the button is clicked
            if getPress[0] == 1 and active != None:
                # If the pass button is clicked, randomize the word and display on the screen again
                if active == "pass":
                    global randomWord
                    randomWord = random.choice(w)
                # If the erase button is clicked, clean the screen by color the background to black
                elif active == "erase":
                    screen.fill((0, 0, 0))


    while gameMode:
        x, y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameMode = False
        if pygame.mouse.get_pressed() == (1, 0, 0):
            pygame.draw.rect(screen, (255, 255, 255), (x, y, 10, 10))

        button("Erase", 50, 515, 60, 30, "erase")
        button("Pass", 668, 515, 60, 30, "pass")

        display()
        pygame.display.update()

drawNguess()