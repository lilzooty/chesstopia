from .piece import Piece, PieceType, Color

BACK_RANK = [
    PieceType.ROOK, PieceType.KNIGHT, PieceType.BISHOP, PieceType.QUEEN,
    PieceType.KING, PieceType.BISHOP, PieceType.KNIGHT, PieceType.ROOK,
]

class Board:
    def __init__(self) -> None:
        self.squares: list[list[Piece | None]] = [[None] * 8 for _ in range(8)]

    def setup(self) -> None:
        for col, kind in enumerate(BACK_RANK):
            self.place(Piece(kind, Color.BLACK), 0, col)
            self.place(Piece(PieceType.PAWN, Color.BLACK), 1, col)
            self.place(Piece(PieceType.PAWN, Color.WHITE), 6, col)
            self.place(Piece(kind, Color.WHITE), 7, col)

    def get(self, row: int, col: int) -> Piece | None:
        return self.squares[row][col]

    def place(self, piece: Piece, row: int, col: int) -> None:
        self.squares[row][col] = piece

    def move(self, from_row: int, from_col: int, to_row: int, to_col: int) -> None:
        self.squares[to_row][to_col] = self.squares[from_row][from_col]
        self.squares[from_row][from_col] = None