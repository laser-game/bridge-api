# coding=utf-8
from .base import BaseMessage
from ..typing_ import VestIdentifier


class VestStatus(BaseMessage):
    def __init__(self, vest: VestIdentifier):
        super(VestStatus, self).__init__()

        self.vest = vest
        # TODO: define fields


__all__ = ['VestStatus']
