import time
import pygame
from sys import exit
from magball_project.engine import PhysicsEngine
from magball_project.graphics import setWindow, draw_frame
from magball_project.startPositions import create_starting_balls, create_balls_random

pygame.init()

#tab witch balls
tab = create_balls_random()

setWindow()


running = True
engine = PhysicsEngine(tab)

draw = engine.timestep_decorator(func=lambda: draw_frame(engine))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
    draw()


# Quit Pygame
pygame.quit()