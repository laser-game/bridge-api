# coding=utf-8
from ..typing_ import GameIdentifier, VestIdentifier
from .base import BaseGameMessage


class Kill(BaseGameMessage):
    def __init__(self, game_id: GameIdentifier, who: VestIdentifier, by_who: VestIdentifier) -> None:
        super().__init__(game_id=game_id)

        self.who = who
        self.by_who = by_who


__all__ = ['Kill']
