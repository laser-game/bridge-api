# coding=utf-8
import pickle
from datetime import datetime

from ..typing_ import GameIdentifier


class BaseMessage(object):
    """
    Base for messages used in message queue for laser game driver communication.
    """
    _timestamp = None  # type: datetime
    _game_id = None  # type: GameIdentifier

    def __init__(self, game_id: GameIdentifier, timestamp: datetime) -> None:
        super().__init__()

        self._timestamp = timestamp
        self.game_id = game_id

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    def serialize(self) -> bytes:
        return pickle.dumps(self)

    @staticmethod
    def deserialize(content: bytes):
        return pickle.loads(content)


__all__ = ['BaseMessage']
