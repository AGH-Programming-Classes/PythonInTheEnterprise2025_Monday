import pygame
from sys import exit

pygame.init()

# dsSet up the game window
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Blondi symulation")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

# Quit Pygame
pygame.quit()