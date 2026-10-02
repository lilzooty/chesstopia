from http import URL
from dataclasses import dataclass, field
from enum import Enum, auto
import uuid
from game import new_id

from pydantic import BaseModel, Field

class Color(Enum):
    WHITE = auto()
    BLACK = auto()


class Player(BaseModel, table=True):

    username: str
    email: str
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))

    @property
    def games_played(self) -> int:
        return self.wins + self.losses + self.draws


    def add_win() -> None:
        wins += 1
    def add_loss() -> None:
        losses += 1
    def add_draw() -> None:
        draws += 1

    
