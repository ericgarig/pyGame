# 2014-06-11 ( eshagdar )

"""Contains the base class of all sprites"""

import pygame, sys


class BaseClass (pygame.sprite.Sprite):
    allSprites = pygame.sprite.Group()

    # base constructor
    def __init__(self, x, y, height, width, color):

        pygame.sprite.Sprite.__init__(self)
        BaseClass.allSprites.add(self)

        self.image = pygame.Surface((width, height))
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height


