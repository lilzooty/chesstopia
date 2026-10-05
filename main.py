# Example file showing a basic pygame "game loop"
import pygame
import pygame_gui
from client.constants import *
from client.view.menu_screen import MainMenu

# pygame setup
pygame.init()
pygame.display.set_caption("Chesstopia", "Chesstopia")
icon = pygame.image.load(icon_filepath)
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.RESIZABLE | pygame.SCALED)

manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
menu = MainMenu(manager)

clock = pygame.time.Clock()
running = True

while running:
    # time since last frame in seconds, pygame_gui needs this for animations
    time_delta = clock.tick(DEFAULT_FPS) / 1000.0  # limits FPS to 60

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        menuAction = menu.handle_event(event)
        
        match menuAction:
            case "host":
                menu.kill() #methinks we kill it then initialize the host screen which we dont have and all that other stuff for join and settings
            case "join":
                menu.kill()
            case "quit":
                running = False
            case "settings":
                menu.kill()
        

        manager.process_events(event)

    manager.update(time_delta)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # RENDER YOUR GAME HERE
    manager.draw_ui(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
