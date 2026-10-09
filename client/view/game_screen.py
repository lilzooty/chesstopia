import pygame
import pygame_gui

from shared.model.board import Board
from shared.model.piece import Color, PieceType
from client.constants import *

LETTERS = {
    PieceType.PAWN: "P", PieceType.KNIGHT: "N", PieceType.BISHOP: "B",
    PieceType.ROOK: "R", PieceType.QUEEN: "Q", PieceType.KING: "K",
}

class GameScreen:
    def __init__(self, manager: pygame_gui.UIManager) -> None:
        self.board = Board()
        self.board.setup()
        self.selected: tuple[int, int] | None = None
        self.font = pygame.font.SysFont(None, SQUARE_SIZE // 2)

        # side panel only, so it doesn't cover the board
        self.panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(BOARD_SIZE, 0, PANEL_WIDTH, SCREEN_HEIGHT),
            manager=manager,
        )
        self.resign_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(20, 20, PANEL_WIDTH - 40, 40),
            text="Resign",
            manager=manager,
            container=self.panel,
        )

    def handle_event(self, event: pygame.event.Event) -> str | None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            if x < BOARD_SIZE:
                self.click_square(y // SQUARE_SIZE, x // SQUARE_SIZE)
        elif event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.resign_button:
                return "back"
        return None

    def click_square(self, row: int, col: int) -> None:
        if self.selected is None:
            if self.board.get(row, col) is not None:
                self.selected = (row, col)
        elif self.selected == (row, col):
            self.selected = None
        else:
            self.board.move(*self.selected, row, col)
            self.selected = None

    def draw(self, surface: pygame.Surface) -> None:
        for row in range(8):
            for col in range(8):
                rect = pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE,
                                   SQUARE_SIZE, SQUARE_SIZE)
                if self.selected == (row, col):
                    color = HIGHLIGHT
                elif (row + col) % 2 == 0:
                    color = LIGHT_SQUARE
                else:
                    color = DARK_SQUARE
                pygame.draw.rect(surface, color, rect)

                piece = self.board.get(row, col)
                if piece is not None:
                    self.draw_piece(surface, piece, rect)

    def draw_piece(self, surface: pygame.Surface, piece, rect: pygame.Rect) -> None:
        if piece.color == Color.WHITE:
            fill, text_color = (250, 250, 250), (20, 20, 20)
        else:
            fill, text_color = (20, 20, 20), (250, 250, 250)
        pygame.draw.circle(surface, fill, rect.center, SQUARE_SIZE * 0.35)
        label = self.font.render(LETTERS[piece.type], True, text_color)
        surface.blit(label, label.get_rect(center=rect.center))

    def kill(self) -> None:
        self.panel.kill()