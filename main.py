#!/usr/bin/env python

"""
to do:
- dead state

"""



"""main file of side-scroller game"""

__author__ = "Erik Shagdar"
__version__ = "1.0.1"
__email__ = "erik.shagdar@gmail.com"
__status__ = "Development"


import pygame
import sys
import os
import random
from pygame.locals import *
from baseClass import *
from charClass import *
from mapClass import *



"""Constants"""
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
Blue = (0,0,220)



"""init"""
pygame.init()



"""setup"""
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Testing This All')
fpsTime = pygame.time.Clock()



#Map Setup

"""enable this when there are multiple maps, for now just specify file"""
# files = os.listdir(os.getcwd() + '/Maps')
# index = random.randrange(1,len(files))   # do not include the .DS_Store file
# with open("Maps/"+files[index]) as file:    # Use file to refer to the file object

with open("Maps/Level01.txt") as file:    # Use file to refer to the file object
    data = file.read()
    exec(data)


# Char
char = CharClass((screenWidth + charWidth)/2,10,charHeight,charWidth,Blue)



"""Text"""
# texts = TextClass.text_to_screen(screen, "hello", 100, 100, size = 25, color = (0, 255, 255), font_type = 'monospace' )



"""Main loop"""
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
    if char.isDead(screen,minFloor,Black):
        break
    char.motion(direction,jumping,fall_through,gravity,maxGravity,maxJumpAccel,minFloor,maxWidth,screenWidth,MapClass.allSprites)


    #DRAW
    screen.fill(Black)
    BaseClass.allSprites.draw(screen)
    Text.text_to_screen(screen, "Under Development",10,screenHeight-30,20,(255,0,0))
    pygame.display.update()
    

    #Clock
    fpsTime.tick(FPS)






