# coding=utf-8
import pickle
from datetime import datetime
from uuid import UUID, uuid4

from ..typing_ import GameIdentifier


class BaseMessage(object):
    """
    Base for messages used in message queue for laser game driver communication.
    """
    _timestamp = None  # type: datetime
    _game_id = None  # type: GameIdentifier
    _message_id = None  # type: UUID # TODO: is it needed?

    def __init__(self, game_id: GameIdentifier) -> None:
        super().__init__()

        self._timestamp = datetime.now()
        self.game_id = game_id
        self._message_id = uuid4()

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    def serialize(self) -> bytes:
        return pickle.dumps(self)

    @staticmethod
    def deserialize(content: bytes):
        return pickle.loads(content)


__all__ = ['BaseMessage']
