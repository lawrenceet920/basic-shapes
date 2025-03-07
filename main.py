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
        draw_rectange(screen, (200, 10, 200, 200), config.BLUE, 5)

        draw_circle(screen, (300, 300), 10, config.BLACK, 0)
        draw_circle(screen, (400, 400), 100, config.RED, 20)

        draw_line(screen, (10, 10), (10, 590), config.BLACK, 5)
        draw_line(screen, (10, 590), (790, 590), config.BLACK, 5)

        draw_polygon(screen, [(10, 10), (10, 20), (20, 20), (20, 30), (30,30), (30, 10)], config.ORANGE, 0)
        draw_polygon(screen, [(10, 10), (790, 10), (790, 590)], config.ORANGE, 3)
        draw_polygon(screen, [(300, 300), (320, 300), (340, 320), (320, 340), (300, 340), (280, 320), (280, 320)], config.RED, 10)

        # Additional Features
        mouse_pos = pygame.mouse.get_pos()
        draw_text(screen, mouse_pos, mouse_pos, 15) # Tells user mouse coordinates

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
def draw_text(screen, text, pos, font_size):
    font = pygame.font.SysFont('LiberationMono', font_size)
    display_text = font.render(str(text), True, config.BLACK)
    screen.blit(display_text, (pos))
def draw_polygon(screen, points, color, thickness):
    pygame.draw.polygon(screen, color, points, thickness)


if __name__ == '__main__':
    main()