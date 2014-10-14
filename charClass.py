# 2014-06-11 ( eshagdar )

"""class that contains all moving characters"""

import pygame, sys
from baseClass import *
from time import sleep
import Text




class CharClass(BaseClass):
    allSprites = pygame.sprite.Group()
    vel_X = 5
    vel_Y = 1
    isFalling = True

    #base constructor
    def __init__(self,x,y,height,width,color):
        BaseClass.__init__(self,x,y,width,height,color)
        CharClass.allSprites.add(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()  # left, top, width, height
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.bottom = y + height
        self.right = x + width


    # returns an array of:
    #     [floor, left, right, ceiling, isFloorSolid]
    def movementArray(self, wallList, minFloor,maxWidth):
        movementArray = [minFloor,0,maxWidth,0,1]

        for wall in wallList:

            # floor/ceiling
            if ( self.rect.right >= wall.rect.x and
                    self.rect.x <= wall.rect.right ):
                # floor
                if ( self.rect.bottom <= wall.rect.y and
                            wall.rect.y < movementArray[0] ):
                    movementArray[0] = wall.rect.y
                    if wall.type == 'solid':
                        movementArray[4] = 1
                    else:
                        movementArray[4] = 0
                # ceiling
                elif ( self.rect.y >= wall.rect.bottom and
                        wall.rect.bottom > movementArray[3] and
                        wall.type == 'solid' ):
                    movementArray[3] = wall.rect.bottom

            # walls
            if ( self.rect.y < wall.rect.bottom and
                    self.rect.bottom > wall.rect.y ):
                # left wall
                if ( wall.rect.right <= self.rect.x and 
                        wall.rect.right > movementArray[1] ):
                    movementArray[1] = wall.rect.right
                # right wall
                if (wall.rect.x >= self.rect.right and 
                        wall.rect.x < movementArray[2] ):
                    movementArray[2] = wall.rect.x
        #print self.rect, movementArray
        return movementArray


    def motion (self,direction,jumping,fall_through,gravity,maxGravity,maxJumpAccel,minFloor,maxWidth,screenWidth,wallList):
        moveArray = []
        moveArray = self.movementArray(wallList,minFloor,maxWidth)
        #left/right
        if direction == 'Left' and moveArray[1] < self.rect.x:
            for wall in wallList:
                wall.rect.x += self.vel_X   # move all walls right
        elif direction == 'Right' and moveArray[2] > self.rect.x + self.rect.width:
            for wall in wallList:
                wall.rect.x -= self.vel_X   # move all walls left

        # jumping/falling
        if jumping:
            if self.rect.y - gravity >= moveArray[3]:
                self.rect.y -= gravity
            if not self.isFalling:
                self.vel_Y = maxJumpAccel
                self.isFalling = True
        else:
            if self.vel_Y < 0:
                self.vel_Y = 0

        # increase vel due to gravity
        if self.vel_Y < maxGravity:
            self.vel_Y += gravity

        # free-falling
        if self.rect.bottom < moveArray[0]:
            # fall distance less than falling, so set it what is left
            if ( moveArray[0] - self.rect.bottom ) < self.vel_Y:
                self.vel_Y = moveArray[0] - self.rect.bottom
            self.rect.y = self.rect.y + self.vel_Y
        elif fall_through == True and moveArray[4] == 0:
            self.rect.y = self.rect.y + self.vel_Y
            self.isFalling = True
        if self.rect.bottom == moveArray[0]:
            self.isFalling = False
        print self.rect.x, self.rect.y

    def isDead(self,screen,DeathPos,backGroundColor):
        if self.rect.bottom >= DeathPos:
            screen.fill(backGroundColor)
            Text.text_to_screen(screen, "You fell to your death",10,10,100,(255,0,0))
            Text.text_to_screen(screen, "Try again",10,200,100,(255,0,0))
            pygame.display.update()
            sleep(2)
            return True




