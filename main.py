# Example file showing a basic pygame "game loop"
import pygame
from client.constants import *

# pygame setup
pygame.init()
pygame.display.set_caption("Chesstopia", "Chesstopia")
icon = pygame.image.load(icon_filepath)
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.RESIZABLE | pygame.SCALED)

clock = pygame.time.Clock()
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    screen.fill("gray")
    
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(DEFAULT_FPS)  # limits FPS to 60

pygame.quit()