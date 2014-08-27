# 2014-06-10 ( eshagdar )


""" things to do:

    gravity should not be Constant
    - along with that, jump shouldn't be either
    - not should you be able to jump unless you land - check velY
    moving the map up/down when on a platform/falling from 'base height'
   
"""

import pygame, sys
from pygame.locals import *
from baseClass import *
from charClass import *
from mapClass import *
import Text 
"""this is the main file to run """



def texts(score):
    font=pygame.font.Font(None,30)
    scoretext=font.render("Score:"+str(score), 1,(0,0,255))
    screen.blit(scoretext, (500, 457))



#Constants
FPS = 30
screenWidth = 800
screenHeight = 600
charWidth = 20
charHeight = 40
gravity = 1
maxGravity = 10
maxJumpAccel = - 15
minFloor = screenHeight + charHeight/2
maxWidth = screenWidth # change this later to the max width of the map

#Colors
Black = (0,0,0)
Gray = (220,220,220)
HollowWall = (130,130,130)
#Red = (220,0,0)
Blue = (0,0,220)


#init
pygame.init()


#setup
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Testing This All')
fpsTime = pygame.time.Clock()


#(x,y,depth,width)
wall01 = MapClass(0,0,minFloor,10)

#(x,y,depth,width)
floor01 = MapClass(10,500,minFloor-500,90)
floor02 = MapClass(100,500,10,200,HollowWall,'hollow')
floor03 = MapClass(300,450,minFloor-450,200)


# Char
char = CharClass((screenWidth + charWidth)/2,10,charHeight,charWidth,Blue)

# Text
#text = texts("hi")


#Main loop
while True:

    #EVENTS
    for event in pygame.event.get():

        #print event

        # hit the 'x' in the top left corner
        if event.type == pygame.QUIT:
            # click red 'x'
            pygame.quit()
            sys.exit
        # ADD CMD + Q to quit
        # ADD DIED
        # ADD RESET

        keys = pygame.key.get_pressed()

        if keys[K_q]:
            pygame.quit()
            sys.exit

        if keys[K_a]:
            # Left
            direction = 'Left'
        elif keys[K_d]:
            # Right
            direction = 'Right'
        else:
            direction = 'None'

        if keys[K_w]:
            # Jump
            jumping = True
            fall_through = False
        elif keys[K_s]:
            jumping = False
            fall_through = True
        else:
            jumping = False
            fall_through = False



    #LOGIC
    # if char.rect.bottom == minFloor:
    #     pygame.event.Event(USEREVENT, code='DIED', )
    char.motion(direction,jumping,fall_through,gravity,maxGravity,maxJumpAccel,minFloor,maxWidth,screenWidth,MapClass.allSprites)

    #DRAW
    screen.fill(Black)
    BaseClass.allSprites.draw(screen)
    #Text.text_to_screen(screen, "hello", 10, 10,10,(250,40,43))
    pygame.display.update()

    #Clock
    fpsTime.tick(FPS)






