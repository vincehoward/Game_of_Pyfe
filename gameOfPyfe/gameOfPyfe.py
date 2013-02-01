#!/usr/bin/env python

import pygame
from soup import *

pygame.init()

gray = (50, 50, 50)

clock = pygame.time.Clock()
pygame.display.set_caption('The Game of Pyfe')
screen = pygame.display.set_mode([500, 500])
background = pygame.Surface(screen.get_size())
background = background.convert()
screen.fill(gray)

x = 0
y = 0
pixel_x = 0
pixel_y = 0
theSoup = {}

sprites = pygame.sprite.RenderPlain()

for x in range(1, 50):
    theSoup[(x, y)] = cell(pixel_x, pixel_y)
    cells = theSoup[(x, y)]
    sprites.add(cells)
    for y in range(1, 50):
        theSoup[(x, y)] = cell(pixel_x, pixel_y)
        cells = theSoup[(x, y)]
        sprites.add(cells)
        pixel_y = pixel_y + 10
    pixel_x = pixel_x + 10
    y = 0
    pixel_y = 0

pause = True

def main():
    done = False

    while done == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    pause = not pause
            elif (event.type == pygame.MOUSEBUTTONDOWN and \
                   pygame.mouse.get_pressed()[0]):
                for sprite in sprites:
                    sprite.clicked(pygame.mouse.get_pos())

        sprites.draw(screen)
        pygame.display.update()
        pygame.display.flip()
        clock.tick(10)

if __name__ == '__main__': main()