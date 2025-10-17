import pygame
from sys import exit

pygame.init()

#size of window
screen_width = 1500
screen_height = 800

# dsSet up the game window
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Magballs")


#tab witch balls
tab = []



#TODO first object


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# Quit Pygame
pygame.quit()