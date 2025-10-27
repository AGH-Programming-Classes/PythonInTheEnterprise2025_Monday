import pygame
from src.planets_project.config import WIN
from assets.fonts.colors_fonts import WHITE, FONT
from src.planets_project.factory.planets_factory import make_solar_system
from src.planets_project.renderer.camera import zoom_in, zoom_out


def main():
    run = True
    clock = pygame.time.Clock()

    # Client Code - Factory Pattern — Centralized Object Creation
    planets = make_solar_system()

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        instructions = [
            "Press + to Zoom In",
            "Press - to Zoom Out",
            "Press ESC to Quit"
        ]

        y_offset = 10  # start slightly from top

        for line in instructions:
            text_surf = FONT.render(line, True, WHITE)
            WIN.blit(text_surf, (10, y_offset))
            y_offset += text_surf.get_height() + 5

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_PLUS, pygame.K_EQUALS):
                    zoom_in()
                elif event.key == pygame.K_MINUS:
                    zoom_out()

        for p in planets:
            p.update_position(planets)
            p.draw(WIN)

        pygame.display.update()

    pygame.quit()


main()