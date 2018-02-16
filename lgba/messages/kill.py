# coding=utf-8
from .base import BaseGameMessage
from ..typing_ import GameIdentifier, VestIndex


class Kill(BaseGameMessage):
    def __init__(self, game_id: GameIdentifier, who: VestIndex, by_who: VestIndex) -> None:
        super().__init__(game_id=game_id)

        self.who = who
        self.by_who = by_who


__all__ = ['Kill']
