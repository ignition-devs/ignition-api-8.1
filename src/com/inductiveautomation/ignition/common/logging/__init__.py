__all__ = ["Level", "LogFilterSettings"]

from typing import Iterable, Mapping

import ch.qos.logback.classic
from dev.thecesrom.helper.types import AnyStr
from java.lang import Enum


class LogFilterSettings(object):
    def addPropertyFilter(self, key, value):
        # type: (AnyStr, AnyStr) -> None
        raise NotImplementedError

    def clearPropertyLevel(self, key, value):
        # type: (AnyStr, AnyStr) -> None
        raise NotImplementedError

    def clearPropertyLevels(self):
        # type: () -> None
        raise NotImplementedError

    def propertyFilterSettings(self):
        # type: () -> Mapping[AnyStr, Mapping[AnyStr, Level]]
        raise NotImplementedError

    def removePropertyFilter(self, key, value):
        # type: (AnyStr, AnyStr) -> None
        raise NotImplementedError

    def setLevel(self, logger, level):
        # type: (AnyStr, Level) -> None
        raise NotImplementedError

    def setPropertyLevel(self, key, value, level):
        # type: (AnyStr, AnyStr, Level) -> None
        raise NotImplementedError


class Level(Enum):
    def toLevel(self, value):
        # type: (ch.qos.logback.classic.Level) -> Level
        pass

    def toLogBack(self):
        # type: () -> ch.qos.logback.classic.Level
        pass

    @staticmethod
    def values():
        # type: () -> Iterable[Level]
        pass
