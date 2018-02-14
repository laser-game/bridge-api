# coding=utf-8
from lgba.typing_ import GameIdentifier
from .base import BaseMessage
from ..typing_ import VestIndex


class Kill(BaseMessage):
    def __init__(self, game_id: GameIdentifier, who: VestIndex, by_who: VestIndex, timestamp) -> None:
        super().__init__(game_id=game_id)

        self.who = who
        self.by_who = by_who


__all__ = ['Kill']
