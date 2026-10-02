from piece import Piece

class Board(): 

    board = [8][8]


    def __init__(self) -> None:
        self.squares: list[list[Piece | None]] = []
        for _ in range(8):
            row: list[Piece | None] = []
            for _ in range(8):
                row.append(None)
            self.squares.append(row)

    
    def get(self, row: int, col: int) -> Piece | None:
        return self.squares[row][col]

    def place(self, piece: Piece, row: int, col: int) -> None:
        self.squares[row][col] = piece

        