# Ethan Lawrence 
# Feb 12 2025
# Pygame template ver 2

import pygame
import sys
import config

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock()
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)

        # Content
        draw_rectange(screen, (100, 100, 100, 100), config.RED, 0)
        draw_rectange(screen, (200, 200, 200, 200), config.BLUE, 5)

        draw_circle(screen, (300, 300), 10, config.BLACK, 0)
        draw_circle(screen, (400, 400), 100, config.RED, 20)

        draw_line(screen, (10, 10), (10, 590), config.BLACK, 5)
        draw_line(screen, (10, 590), (790, 590), config.BLACK, 5)

        pygame.display.flip()

        # Limit clock to FPS
        clock.tick(config.FPS)
    pygame.quit()
    sys.exit()


# Draw Shapes

def draw_rectange(screen, rect, color, thickness):
    pygame.draw.rect(screen, color, rect, thickness)
def draw_circle(screen, center, radius, color, thickness):
    pygame.draw.circle(screen, color, center, radius, thickness)
def draw_line(screen, start_pos, end_pos, color, thickness):
    pygame.draw.line(screen, color, start_pos, end_pos, thickness)

if __name__ == '__main__':
    main()