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
    _message_id = None  # type: UUID # TODO: is it needed?

    def __init__(self) -> None:
        super().__init__()

        self._timestamp = datetime.now()
        self._message_id = uuid4()

    def __str__(self):
        keys = sorted(dir(self))
        return '{}Message({})'.format(
            self.__class__.__name__,
            ', '.join(
                '{}={}'.format(k, getattr(self, k, '-'))
                for k in keys
                if '__' not in k and not callable(getattr(self, k)) and k[1:] not in keys
            )
        )

    @property
    def timestamp(self) -> datetime:
        return self._timestamp

    def serialize(self) -> str:
        return pickle.dumps(self)

    @staticmethod
    def deserialize(content: bytes):
        return pickle.loads(content)


class BaseGameMessage(BaseMessage):
    """
    Protocol message about game.
    """
    game_id = None  # type: GameIdentifier

    def __init__(self, game_id: GameIdentifier):
        super(BaseGameMessage, self).__init__()

        self.game_id = game_id


__all__ = ['BaseMessage', 'BaseGameMessage']
