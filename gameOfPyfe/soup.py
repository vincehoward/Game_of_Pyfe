#!/usr/bin/env python

import pygame

white = (255, 255, 255)
black = (0, 0, 0)

class cell(pygame.sprite.Sprite):

    alive = False
    x = 0
    y = 0

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([10, 10])
        self.image.fill((white))
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        cell.x = x
        cell.y = y
        self.alive = False

    """    
    def test(self, x, y):
        surroundingLife = area(cell, x, y)
        
        if surroundingLife > 3:
            if cell.alive == True:
                lifeSwitch(cell)

        if surroundingLife < 2:
            if self.alive == True:
                lifeSwitch(cell)

        if surroundingLife == 3:
            if self.alive == False:
                lifeSwitch(cell)
    """

    #def area(self, x, y):
        
        # nothing...     ...yet

    def lifeSwitch(self):
        self.alive = not self.alive
        
        if cell.alive == True:
            self.image.fill((black))
        elif cell.alive == False:
            self.image.fill((white))

    def clicked(self, pos):
        self.rect = self.image.get_rect()
        if self.rect.collidepoint(pos[0], pos[1]):
            lifeSwitch()
