from dataclasses import dataclass, field
from player import Player
from piece import Piece, PieceType
from sqlmodel import SQLModel, Field
from uuid import uuid4



def new_id() -> str:
    return str(uuid4())

@dataclass(frozen=True)
class Move:
    from_sq: str
    to_sq: str
    promote_to: PieceType | None = None

@dataclass
class Game:
    white: Player
    black: Player
    move_list: list[Move] = field(default_factory=list)
    

# game_record.py: the finished match, saved to the database
class GameRecord(SQLModel, table=True):
    id: str = Field(default_factory=new_id, primary_key=True)
    white_id: str = Field(foreign_key="player.id")
    black_id: str = Field(foreign_key="player.id")
    result: str
    moves: str   # "e2e4 e7e5 g1f3"

