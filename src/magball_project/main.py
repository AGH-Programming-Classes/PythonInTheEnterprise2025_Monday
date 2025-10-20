import time
import pygame
from sys import exit
from magball_project.engine import PhysicsEngine
from magball_project.graphics import setWindow, draw_frame, button_happens
from magball_project.startPositions import create_starting_balls, create_balls_random

pygame.init()


setWindow()


while True:

    #tab witch balls
    tab = create_balls_random()



    #TODO first object


    running = True
    engine = PhysicsEngine(tab)  # Assuming you have a PhysicsEngine class to handle the physics
    TIME = time.time()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_pos = pygame.mouse.get_pos()
                    if button_happens(mouse_pos):
                        running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    running = False

        if time.time() > TIME + 0.01:
            engine.timestep()
            TIME = time.time()
        draw_frame(engine)


# Quit Pygame
pygame.quit()