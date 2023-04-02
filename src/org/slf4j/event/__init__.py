__all__ = ["Level"]

from typing import Iterable

from java.lang import Enum


class Level(Enum):
    def toInt(self):
        # type: () -> int
        pass

    @staticmethod
    def values():
        # type: () -> Iterable[Level]
        pass
