__all__ = ["Level", "LogFilterSettings"]

from typing import Iterable, Mapping, Union

from java.lang import Enum

import ch.qos.logback.classic


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


class LogFilterSettings(object):
    def addPropertyFilter(self, key, value):
        # type: (Union[str, unicode], Union[str, unicode]) -> None
        raise NotImplementedError

    def clearPropertyLevel(self, key, value):
        # type: (Union[str, unicode], Union[str, unicode]) -> None
        raise NotImplementedError

    def clearPropertyLevels(self):
        # type: () -> None
        raise NotImplementedError

    def propertyFilterSettings(self):
        # type: () -> Mapping[Union[str, unicode], Mapping[Union[str, unicode], Level]] # noqa: W505
        raise NotImplementedError

    def removePropertyFilter(self, key, value):
        # type: (Union[str, unicode], Union[str, unicode]) -> None
        raise NotImplementedError

    def setLevel(self, logger, level):
        # type: (Union[str, unicode], Level) -> None
        raise NotImplementedError

    def setPropertyLevel(
        self,
        key,  # type: Union[str, unicode]
        value,  # type: Union[str, unicode]
        level,  # type: Level
    ):
        # type: (...) -> None
        raise NotImplementedError
