# coding=utf-8
from .base import BaseMessage
from ..typing_ import VestIndex


class VestStatus(BaseMessage):
    def __init__(self, vest: VestIndex):
        super(VestStatus, self).__init__()

        self.vest = vest
        # TODO: define fields


__all__ = ['VestStatus']
