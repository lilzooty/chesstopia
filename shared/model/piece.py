from dataclasses import dataclass
from enum import Enum, auto

class PieceType(Enum):
    PAWN = auto()
    KNIGHT = auto()
    BISHOP = auto()
    ROOK = auto()
    KING = auto()
    QUEEN = auto()

class Color(Enum):
    WHITE = auto()
    BLACK = auto()

@dataclass(frozen=True)
class Piece:
    type: PieceType
    color: Color