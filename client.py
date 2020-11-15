__author__ = "Trang Ha"

import pygame
from network import Network

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Draw N Guess")


def txtObject(txt, fontSize, color):
    txtFont = pygame.font.Font("freesansbold.ttf", fontSize)
    txtRender = txtFont.render(txt, True, color)
    return txtRender, txtRender.get_rect()

def display(screen, score, chances, picWord, guessWord):
    # Display score on the screen
    pygame.draw.rect(screen, (0, 0, 0), [50, 30, 100, 30])
    score, scoreRect = txtObject("Score: " + str(score), 16, (255, 255, 255))
    scoreRect.center = ((50 + (100 / 2), (30 + (30 / 2))))
    screen.blit(score, scoreRect)

    # Display player role on the screen
    pygame.draw.rect(screen, (0, 0, 0), [650, 30, 100, 30])
    heart, heartRect = txtObject("Chances: " + str(chances), 16, (255, 255, 255))
    heartRect.center = ((650 + (100 / 2), (30 + (30 / 2))))
    screen.blit(heart, heartRect)

    # Display pictionary word on the screen
    pygame.draw.rect(screen, (255, 255, 255), [320, 30, 150, 30])
    picWord, txtRect = txtObject(picWord, 18, (0, 0, 0))
    txtRect.center = ((320+(150/2), (30+(30/2))))
    screen.blit(picWord, txtRect)

    # Display guesing word on the screen
    pygame.draw.rect(screen, (255, 255, 255), [320, 515, 150, 30])
    userIn, userInRect = txtObject(guessWord, 16, (0, 0, 0))
    userInRect.center = ((320+(150/2), (515+(30/2))))
    screen.blit(userIn, userInRect)





# Set up buton
def button(buttonTxt, x, y, width, height, active= None):

    getPos = pygame.mouse.get_pos()
    getPress = pygame.mouse.get_pressed()
    button, buttonRect = txtObject(buttonTxt, 16, (0, 0, 0))
    buttonRect.center = ((x+(width/2)), (y+(height/2)))
    pygame.draw.ellipse(screen, (255, 255, 255), [x, y, width, height])
    screen.blit(button, buttonRect)

    # If the x, y coordinates of the mouse = the x, y coordinates of the button, then executes these following
    if x+width > getPos[0] > x and y+height > getPos[1] > y:
        # Check if the button is clicked
        if getPress[0] == 1 and active != None:
            # If the pass button is clicked, randomize the word and display on the screen again
            if active == "pass":
                pass
            # If the erase button is clicked, clean the screen by color the background to black
            elif active == "erase":
                screen.fill((0, 0, 0))

def updateScreen(screen, guessP, drawP):
    guessP.drawRect(screen)
    drawP.drawRect(screen)
    if guessP.id == 2:
        display(screen, guessP.score, guessP.life, "_ " * len(guessP.picWord), guessP.guessWord)
    else:
        display(screen, drawP.score, drawP.life, drawP.picWord, drawP.guessWord)
    button("Erase", 50, 515, 60, 30, "erase")
    button("Pass", 668, 515, 60, 30, "pass")
    pygame.display.update()

def main():
    run = True
    n = Network()
    guessP = n.getP()
    userInput = ""

    while run:
        drawP = n.send(guessP)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if guessP.id == 2:
                    if event.key == pygame.K_BACKSPACE:
                        userInput = userInput[:-1]
                        drawP.guessWord = guessP.guessWord = userInput
                    elif event.key == pygame.K_RETURN:
                        guessP.checkWord()
                        drawP.checkWord()
                    else:
                        userInput += event.unicode
                        drawP.guessWord = guessP.guessWord = userInput

                print("guessP.picWord: {0}, guessP.guessWord: {1}, guessP.score: {2}, guessP.life: {3}, guessP.id: {4}".format(guessP.picWord, guessP.guessWord, str(guessP.score), str(guessP.life), str(guessP.id)))
                print("drawP.picWord: {0}, drawP.guessWord: {1}, drawP.score: {2}, drawP.life: {3}, drawP.id: {4}".format(drawP.picWord, drawP.guessWord, str(drawP.score), str(drawP.life), str(drawP.id)))



        guessP.playerDrawing()
        updateScreen(screen, guessP, drawP)

main()

