__all__ = ["Level"]

from typing import Any

import org.slf4j.event
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object


class Level(Object):
    @staticmethod
    def convertAnSLF4JLevel(slf4jLevel):
        # type: (org.slf4j.event.Level) -> Level
        pass

    @staticmethod
    def fromLocationAwareLoggerInteger(levelInt):
        # type: (int) -> Level
        pass

    def isGreaterOrEqual(self, r):
        # type: (Level) -> bool
        pass

    def toInt(self):
        # type: () -> int
        pass

    def toInteger(self):
        # type: () -> int
        pass

    @staticmethod
    def toLevel(*args):
        # type: (*Any) -> Level
        pass

    @staticmethod
    def toLocationAwareLoggerInteger(level):
        # type: (Level) -> int
        pass

    @staticmethod
    def valueOf(sArg):
        # type: (AnyStr) -> Level
        pass
