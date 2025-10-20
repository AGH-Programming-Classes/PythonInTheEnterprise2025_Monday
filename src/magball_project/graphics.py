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
    pygame.init()  # Dodanie inicjalizacji pygame
    global screen, color, board, board_color, frame  # Dodanie global dla zmiennych
    
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
    
    # WAŻNE: Narysuj board na ekranie i odśwież
    screen.blit(board, (place_of_board, place_of_board))
    pygame.draw.rect(screen, (0, 0, 0), frame, 5)  # Czarna ramka
    pygame.display.flip()  # Aktualizuj wyświetlacz

def draw_frame(engine=None):
    global screen, board, frame, place_of_board, color
    if screen:
        screen.fill(color)  # Wyczyść ekran
        screen.blit(board, (place_of_board, place_of_board))  # Narysuj board
        pygame.draw.rect(screen, (0, 0, 0), frame, 5)  # Narysuj ramkę
        
        # Narysuj piłki z physics engine
        if engine and hasattr(engine, 'bodies'):
            for body in engine.bodies:
                if hasattr(body, 'shapes') and body.shapes:
                    shape = next(iter(body.shapes))
                    pos = body.position
                    # Pozycja na ekranie
                    screen_pos = (int(pos.x), int(pos.y))
                    color_rgb = (255, 0, 0)  # Domyślny czerwony
                    if hasattr(shape, 'color'):
                        color_rgb = shape.color
                    pygame.draw.circle(screen, color_rgb, screen_pos, int(shape.radius))
        
        pygame.display.flip()  # Odśwież wyświetlacz