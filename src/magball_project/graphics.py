import pygame

screen_width = 1500
screen_height = 800
place_of_board = 100

# dsSet up the game window
screen = None
#set color
color = None
board = None
board_color = None

frame = None

def setWindow():
    screen_width = 1500
    screen_height = 800
    place_of_board = 100

    # dsSet up the game window
    screen = pygame.display.set_mode((screen_width, screen_height))

    #set color
    color = (170, 170, 170)
    screen.fill(color)
    pygame.display.set_caption("Magballs")


    board = pygame.Surface((screen_width - place_of_board*2, screen_height - place_of_board*2))
    board_color = ( 170, 170, 170)
    board.fill(board_color)

    frame = pygame.Rect(place_of_board - 5, place_of_board - 5,screen_width - place_of_board*2 + 10, screen_height - place_of_board*2 +10)
    frame.bottomright = (1405, 705)