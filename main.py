__author__ = "Trang Ha"

import pygame

class Player():
    def __init__(self, x, y, id, picWord):
        self.id = id
        self.x = x
        self.y = y
        self.score = 0
        self.life = 5
        self.guessWord = ""
        self.picWord = picWord
        self.rect = (x, y, 10, 10)

    def checkWord(self):
        if self.guessWord == self.picWord:
            self.score = self.score + 1
        else:
            if self.id == 2:
                self.life = self.life - 1
            else:
                pass

    def drawRect(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def playerDrawing(self):
        x, y = pygame.mouse.get_pos()
        if self.id == 1:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                self.rect = (x, y, 10, 10)


# def drawNguess():
#
#     # Initialize and customize the screen
#     pygame.init()
#     screen = pygame.display.set_mode((800, 600))
#     pygame.display.set_caption("Draw N Guess")
#
#
#     # Set variables to store score value, user input
#     global scoreVal, chances, guessWord, randomWord, gameMode
#     gameMode = True
#     scoreVal = 0
#     chances = 5
#     guessWord = ""
#
#     # Set up random pictionary word
#     with open("pictionary.txt", "r") as pictionary:
#         w = pictionary.read().split()
#     randomWord = random.choice(w)
#
#     def txtObject(txt, fontSize, color):
#         txtFont = pygame.font.Font("freesansbold.ttf", fontSize)
#         txtRender = txtFont.render(txt, True, color)
#         return txtRender, txtRender.get_rect()
#
#     def display():
#         # Display score on the screen
#         pygame.draw.rect(screen, (0, 0, 0), [50, 30, 100, 30])
#         score, scoreRect = txtObject("Score: " + str(scoreVal), 16, (255, 255, 255))
#         scoreRect.center = ((50 + (100 / 2), (30 + (30 / 2))))
#         screen.blit(score, scoreRect)
#
#         # Display player role on the screen
#         pygame.draw.rect(screen, (0, 0, 0), [650, 30, 100, 30])
#         heart, heartRect = txtObject("Chances: " + str(chances), 16, (255, 255, 255))
#         heartRect.center = ((650 + (100 / 2), (30 + (30 / 2))))
#         screen.blit(heart, heartRect)
#
#         # Display pictionary word on the screen
#         pygame.draw.rect(screen, (255, 255, 255), [320, 30, 150, 30])
#         picWord, txtRect = txtObject(randomWord.upper(), 18, (0, 0, 0))
#         txtRect.center = ((320+(150/2), (30+(30/2))))
#         screen.blit(picWord, txtRect)
#
#
#         # Display guesing word on the screen
#         pygame.draw.rect(screen, (255, 255, 255), [320, 515, 150, 30])
#         userIn, userInRect = txtObject(guessWord, 16, (0, 0, 0))
#         userInRect.center = ((320+(150/2), (515+(30/2))))
#         screen.blit(userIn, userInRect)
#
#
#     # Set up buton
#     def button(buttonTxt, x, y, width, height, active= None):
#
#         getPos = pygame.mouse.get_pos()
#         getPress = pygame.mouse.get_pressed()
#         button, buttonRect = txtObject(buttonTxt, 16, (0, 0, 0))
#         buttonRect.center = ((x+(width/2)), (y+(height/2)))
#         pygame.draw.ellipse(screen, (255, 255, 255), [x, y, width, height])
#         screen.blit(button, buttonRect)
#
#         # If the x, y coordinates of the mouse = the x, y coordinates of the button, then executes these following
#         if x+width > getPos[0] > x and y+height > getPos[1] > y:
#             # Check if the button is clicked
#             if getPress[0] == 1 and active != None:
#                 # If the pass button is clicked, randomize the word and display on the screen again
#                 if active == "pass":
#                     next()
#                 # If the erase button is clicked, clean the screen by color the background to black
#                 elif active == "erase":
#                     screen.fill((0, 0, 0))
#
#     # Check if user guess the right word
#     def checkWord():
#         global scoreVal, chances, guessWord
#         if guessWord == randomWord:
#             scoreVal += 1
#             next()
#         else:
#             chances -=1
#             if chances == 0:
#                 screen.fill((255, 255, 255))
#                 gameover, gameoverRect = txtObject("Game over!", 35, (0, 0, 0))
#                 gameoverRect.center = (800/2, 600/2)
#                 screen.blit(gameover, gameoverRect)
#
#
#
#     def next():
#         global randomWord, guessWord
#         guessWord = ""
#         randomWord = random.choice(w)
#         screen.fill((0, 0, 0))
#
#
#
#     while gameMode:
#         x, y = pygame.mouse.get_pos()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 gameMode = False
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_BACKSPACE:
#                     guessWord = guessWord[:-1]
#                 elif event.key ==pygame.K_RETURN:
#                     checkWord()
#                 else:
#                     guessWord += event.unicode
#             if pygame.mouse.get_pressed() == (1, 0, 0):
#                 pygame.draw.rect(screen, (255, 255, 255), (x, y, 10, 10))
#                 pygame.display.update()
#
#
#         button("Erase", 50, 515, 60, 30, "erase")
#         button("Pass", 668, 515, 60, 30, "pass")
#
#
#         display()
#         pygame.display.update()
#
# drawNguess()