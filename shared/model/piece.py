from dataclasses import dataclass
from enum import Enum, auto

class PieceType(Enum):
    PAWN = auto()
    KNIGHT = auto()
    BISHOP = auto()
    ROOK = auto()
    KING = auto()
    QUEEN = auto()


@dataclass
class Piece(frozen = True):
    type : PieceType
     

