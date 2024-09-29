import pygame
import time
from pygame.locals import *


pygame.init()
WIDTH=600
HEIGHT=600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
object_x=200
object_y=200
keys=[False,False,False,False]
object_rocket=pygame.image.load("Pro Python Game Development 2/rocket in space/rocket.png")
bg=pygame.image.load("Pro Python Game Development 2/rocket in space/space.png")

run=True
while object_y<600:
    screen.blit(bg,(0,0))
    screen.blit(object_rocket,(object_x,object_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if event.type==pygame.KEYDOWN:

            if event.key==K_UP:
                keys[0]=True
        
            elif event.key==K_LEFT:
                keys[1]=True

            elif event.key==K_DOWN:
                keys[2]=True
        
            elif event.key==K_RIGHT:
                keys[3]=True
            
        if event.type==pygame.KEYUP:

            if event.key==K_UP:
                keys[0]=False
        
            elif event.key==K_LEFT:
                keys[1]=False

            elif event.key==K_DOWN:
                keys[2]=False
        
            elif event.key==K_RIGHT:
                keys[3]=False
    
    if keys[0]:
        object_y=object_y-8
    
    if keys[1]:
        object_x=object_x-8
    
    if keys[2]:
        object_y=object_y+8
    
    if keys[3]:
        object_x=object_x+8
    

    object_y=object_y+3


print("Game Over")
            
