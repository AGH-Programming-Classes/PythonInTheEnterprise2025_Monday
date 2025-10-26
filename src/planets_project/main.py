import pygame
from config import WIN

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()


main()