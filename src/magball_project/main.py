import time
import pygame
from sys import exit
from magball_project.engine import PhysicsEngine
from magball_project.graphics import setWindow, draw_frame, button_happens, board_cords
from magball_project.startPositions import create_starting_balls, create_balls_random

pygame.init()

pygame.display.set_icon(pygame.image.load("src/magball_project/icon.png"))

setWindow()



while True:

    #tab witch balls
    tab = create_balls_random()



    #TODO first object


    running = True
    coords = board_cords()
    engine = PhysicsEngine(tab, topLeft=(coords[0], coords[1]), bottomRight=(coords[2], coords[3]))
    draw = engine.timestep_decorator(func=lambda: draw_frame(engine))
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

        draw()


# Quit Pygame
pygame.quit()