# coding=utf-8
from lgba.messages.base import BaseGameMessage


class GameStart(BaseGameMessage):
    pass


class GameConfiguration(BaseGameMessage):
    pass
    # TODO: define fields


__all__ = [
    'GameStart',
    'GameConfiguration'
]
