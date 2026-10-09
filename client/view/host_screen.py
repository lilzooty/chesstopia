import pygame
import pygame_gui
from client.constants import SCREEN_HEIGHT, SCREEN_WIDTH



button_rect = pygame.Rect(0, 0, SCREEN_WIDTH*0.10, SCREEN_HEIGHT*0.10)
label_rect = pygame.Rect(0, 0, SCREEN_WIDTH*0.25, SCREEN_HEIGHT*0.5)


class HostScreen:
    

    def __init__(self, manager):
        # main_content = pygame_gui.elements.UIPanel()
        lobby_content = pygame_gui.elements.UIPanel(manager=manager)
        ip_address_label = pygame_gui.elements.UILabel(label_rect, container=lobby_content, text=get_server(), manager=manager)  
