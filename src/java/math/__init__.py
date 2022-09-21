from typing import List

from java.lang import Enum


class RoundingMode(Enum):
    CEILING = None  # type: RoundingMode
    DOWN = None  # type: RoundingMode
    FLOOR = None  # type: RoundingMode
    HALF_DOWN = None  # type: RoundingMode
    HALF_EVEN = None  # type: RoundingMode
    HALF_UP = None  # type: RoundingMode
    UNNECESSARY = None  # type: RoundingMode
    UP = None  # type: RoundingMode

    @staticmethod
    def values():
        # type: () -> List[RoundingMode]
        pass
