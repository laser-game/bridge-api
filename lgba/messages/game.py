# coding=utf-8
from lgba.messages.base import BaseGameMessage


class GameStart(BaseGameMessage):
    pass


class GameConfiguration(BaseGameMessage):
    pass
    # TODO: define fields


class GameBreak(BaseGameMessage):
    pass

__all__ = [
    'GameStart',
    'GameConfiguration'
]
