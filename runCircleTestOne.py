import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 512, 512
CENTER = (255, 255)
RADIUS = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Draw Circle")

# Clock to control the frame rate
clock = pygame.time.Clock()

# Flag to track if mouse button is pressed
drawing = False

# Main game loop
while True:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button pressed
                drawing = True
                start_pos = event.pos
        elif event.type == pygame.MOUSEMOTION and drawing:
            end_pos = event.pos
            pygame.draw.circle(screen, WHITE, CENTER, RADIUS, 1)
            pygame.draw.line(screen, WHITE, start_pos, end_pos, 2)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button released
                drawing = False
                end_pos = event.pos
                radius = int(math.hypot(end_pos[0] - CENTER[0], end_pos[1] - CENTER[1]))
                pygame.draw.circle(screen, WHITE, CENTER, radius, 1)

    pygame.display.flip()
    clock.tick(60)
