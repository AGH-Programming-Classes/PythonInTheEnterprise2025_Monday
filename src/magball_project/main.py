import pygame
from sys import exit
from magball_project.graphics import setWindow, draw_frame

pygame.init()

#tab witch balls
tab = []

setWindow()



#TODO first object


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    draw_frame()


# Quit Pygame
pygame.quit()