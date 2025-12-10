from typing import Iterable

from java.lang import Enum

class Level(Enum):
    def toInt(self) -> int: ...
    @staticmethod
    def values() -> Iterable[Level]: ...
