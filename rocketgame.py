import pygame
import time
from pygame.locals import *


pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
object_x=200
object_y=200
object_rocket=pygame.image.load("Pro Python Game Development 2/rocket in space/rocket.png")
bg=pygame.image.load("Pro Python Game Development 2/rocket in space/space.png")

run=True
while run:
    screen.blit(bg,(0,0))
    screen.blit(object_rocket,(object_x,object_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_UP:
                object_y=object_y-10
        
            elif event.key==pygame.K_LEFT:
                object_x=object_x-10

            elif event.key==pygame.K_DOWN:
                object_y=object_y+10
        
            elif event.key==pygame.K_RIGHT:
                object_x=object_x+10
            
