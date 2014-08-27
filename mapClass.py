# 2014-06-11 ( eshagdar )

"""class that contains all walls"""
import pygame, sys
from baseClass import *


class MapClass(BaseClass):
    allSprites = pygame.sprite.Group()

    def __init__(self, x, y, height, width, color = (220, 220, 220), type_='solid'):
        BaseClass.__init__(self,x,y,width,height,color)
        MapClass.allSprites.add(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.type = type_
        self.bottom = x + height
        self.right = y + width