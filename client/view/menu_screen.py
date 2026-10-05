import pygame
import pygame_gui
from client.constants import SCREEN_WIDTH

class MainMenu:
    def __init__(self, manager):
        btn_w, btn_h = 240, 50
        x = (SCREEN_WIDTH - btn_w) // 2

        def make_button(text, y):
            return pygame_gui.elements.UIButton(
                relative_rect=pygame.Rect(x, y, btn_w, btn_h),
                text=text,
                manager=manager,
            )

        self.host_button = make_button("Host Game", 250)
        self.join_button = make_button("Join Game", 320)
        self.settings_button = make_button("Settings", 390)
        self.quit_button = make_button("Quit", 460)

    def handle_event(self, event):
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.host_button:
                return "host"
            if event.ui_element == self.join_button:
                return "join"
            if event.ui_element == self.settings_button:
                return "settings"
            if event.ui_element == self.quit_button:
                return "quit"
        return None

    def kill(self):
        for button in (self.host_button, self.join_button, self.settings_button, self.quit_button):
                button.kill()