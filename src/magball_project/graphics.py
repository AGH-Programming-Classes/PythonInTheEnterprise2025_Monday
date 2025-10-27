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
button_bg_color = (200, 220, 220)

def setWindow():
    global screen, color, board, board_color, frame, button, button_rect, button_font, button_text, button_normal_bg, button_hover_bg, button_anchor  # Dodanie global dla zmiennych
    
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
    
    # Button configuration stored for per-frame rendering
    button_font = pygame.font.SysFont('Corbel', 70)
    button_text = "RESTART"
    button_normal_bg = (200, 220, 220)
    button_hover_bg = (150, 200, 200)
    button_anchor = (place_of_board + board.get_width() + 5, place_of_board - 5)
    tmp_surf = button_font.render(button_text, True, (0,0,0), button_normal_bg)
    button_rect = tmp_surf.get_rect()
    button_rect.bottomright = button_anchor

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
        # Build button each frame and update button_rect for hover/click checks
        mouse_pos = pygame.mouse.get_pos()
        # create a temp surf using hover bg if mouse over anchor area (we'll compute rect after surf creation)
        # determine hover after creating surf+rect
        # first assume normal background, then check rect collision to pick hover color
        surf_normal = button_font.render(button_text, True, (0,0,0), button_normal_bg)
        rect_normal = surf_normal.get_rect()
        rect_normal.bottomright = button_anchor

        hover = rect_normal.collidepoint(mouse_pos)
        btn_bg = button_hover_bg if hover else button_normal_bg

        button_surf = button_font.render(button_text, True, (0,0,0), btn_bg)
        button_rect = button_surf.get_rect()
        button_rect.bottomright = button_anchor
        screen.blit(button_surf, button_rect)  # Narysuj przycisk
        
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


def get_button_rect():
    """Zwraca button_rect"""
    return button_rect

def button_happens(mouse_pos):
    if button_rect.collidepoint(mouse_pos):
        return True
    return False