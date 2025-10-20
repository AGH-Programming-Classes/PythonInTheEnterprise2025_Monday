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



#TODO first object


running = True
engine = PhysicsEngine(tab)  # Assuming you have a PhysicsEngine class to handle the physics
TIME = time.time()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    if time.time() > TIME + 0.01:
        engine.timestep()
        TIME = time.time()
    draw_frame(engine)


# Quit Pygame
pygame.quit()