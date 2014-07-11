# 2014-06-11 ( eshagdar )

"""class that contains all moving characters"""

import pygame, sys
from baseClass import *



class CharClass(BaseClass):
    allSprites = pygame.sprite.Group()
    velx = 5
    velY = 1

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
        self.bottom = x + height
        self.right = y + width
        self.widthCenter = x + width / 2


    # returns an array of:
    #     [bottom, left, right, ceiling, isFloorSolid]
    def can_move(self, wallList, minFloor,maxWidth):
        can_move = [minFloor,0,maxWidth,0,1]

        for wall in wallList:
        	# floor
            if ( self.widthCenter >= wall.rect.x and 
            	    self.widthCenter <= wall.rect.right and 
            	    self.rect.bottom <= wall.rect.y and
                    wall.rect.y < can_move[0] ):
                can_move[0] = wall.rect.y
                if wall.type == 'solid':
                    can_move[4] = 1
                else:
                    can_move[4] = 0

            # ceiling
            if ( self.rect.right >= wall.rect.x and
                    self.rect.x <= wall.rect.right and
                    self.rect.y >= wall.rect.bottom and
                    wall.rect.bottom > can_move[3] and
                    wall.type == 'solid' ):
                can_move[3] = wall.rect.bottom

            # walls
            if ( self.rect.y < wall.rect.bottom and
            	    self.rect.bottom > wall.rect.y ):
                # left wall
                if ( wall.rect.right <= self.rect.x and 
                	    wall.rect.right > can_move[1] ):
                	can_move[1] = wall.rect.right
                # right wall
                if (wall.rect.x >= self.rect.right and 
                	    wall.rect.x < can_move[2] ):
                    can_move[2] = wall.rect.x
        return can_move


    def motion (self,direction,jumping,fall_through,gravity,maxGravity,minFloor,maxWidth,wallList):
    	moveArray = []
    	moveArray = self.can_move(wallList,minFloor,maxWidth)

        #print self.rect, moveArray

        #left/right
        if direction == 'Left' and moveArray[1] < self.rect.x:
        	for wall in wallList:
        	    wall.rect.x += CharClass.velx   # move all walls right
        elif direction == 'Right' and moveArray[2] > self.rect.x + self.rect.width:
        	for wall in wallList:
        	    wall.rect.x -= CharClass.velx   # move all walls left

        # jumping/falling
        if jumping:
            if self.rect.y - gravity >= moveArray[3]:
                self.rect.y -= gravity
        else:
            if self.velY < maxGravity:
                self.velY += gravity
            fall_location = self.rect.y + self.velY
            if ( moveArray[0] - self.rect.bottom ) < fall_location and moveArray[0] <> self.rect.bottom:
                fall_location = moveArray[0] - self.rect.bottom
            # nothing below
            if fall_location + self.height <= moveArray[0]:
                self.rect.y = fall_location
            # there is a hollow floor, and user hit down
            elif fall_through == True and moveArray[4] == 0:
                self.rect.y = fall_location        

    
            

    






