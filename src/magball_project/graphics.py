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

button = None
button_rect = None 

def setWindow():
    global screen, color, board, board_color, frame, button, button_rect # Dodanie global dla zmiennych
    
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
    
    screen.blit(board, (place_of_board, place_of_board))
    pygame.draw.rect(screen, (0, 0, 0), frame, 5)  # Czarna ramka
    button = pygame.font.SysFont('Corbel',70).render('RESTART', True, (255,255,255), (56,220,220))
    button_rect = button.get_rect()
    button_rect.bottomright = ( place_of_board + board.get_width() + 5, place_of_board - 5)

    pygame.display.flip()  


def draw_frame(engine=None):
    global screen, board, frame, place_of_board, color
    if screen:
        screen.fill(color) 
        screen.blit(board, (place_of_board, place_of_board))  
        pygame.draw.rect(screen, (0, 0, 0), frame, 5) 
        screen.blit(button, button_rect)  
        
        if engine and hasattr(engine, 'bodies'):
            for body in engine.bodies:
                if hasattr(body, 'shapes') and body.shapes:
                    shape = next(iter(body.shapes))
                    pos = body.position
                    screen_pos = (int(pos.x), int(pos.y))
                    color_rgb = (255, 0, 0)  
                    if hasattr(shape, 'color'):
                        color_rgb = shape.color
                    pygame.draw.circle(screen, color_rgb, screen_pos, int(shape.radius))

        pygame.display.flip()


def get_button_rect():
    """Zwraca button_rect"""
    return button_rect

def button_happens(mouse_pos):
    if button_rect.collidepoint(mouse_pos):
        return True
    return False

def board_cords():
    return (place_of_board, place_of_board, screen_width - place_of_board, screen_height - place_of_board)