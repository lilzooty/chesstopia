# Example file showing a basic pygame "game loop"
import pygame
import pygame_gui
from client.constants import *
from client.view.menu_screen import MainMenu
from client.view.host_screen import HostScreen
from client.view.game_screen import GameScreen

# pygame setup
pygame.init()
pygame.display.set_caption("Chesstopia", "Chesstopia")
icon = pygame.image.load(icon_filepath)
pygame.display.set_icon(icon)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags=pygame.RESIZABLE | pygame.SCALED)

manager = pygame_gui.UIManager((SCREEN_WIDTH, SCREEN_HEIGHT))
current_screen = MainMenu(manager)


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

        manager.process_events(event)

        menuAction = current_screen.handle_event(event)
        
        match menuAction:
            case "test":
                current_screen.kill()
                current_screen = GameScreen(manager)
            case "host":
                current_screen.kill()
                current_screen = HostScreen(manager)
            case "join":
                pass
            case "quit":
                running = False
            case "settings":
                pass
            case "back":
                current_screen.kill()
                current_screen = MainMenu(manager)

    manager.update(time_delta)

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("gray")

    # RENDER YOUR GAME HERE
    current_screen.draw(screen)
    manager.draw_ui(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

# when 'running' bool is false we quit (close the window, end process etc. i guess)
pygame.quit()