from typing import List

from java.lang import Enum


class ResolverStyle(Enum):
    LENIENT = None  # type: ResolverStyle
    SMART = None  # type: ResolverStyle
    STRICT = None  # type: ResolverStyle

    @staticmethod
    def values():
        # type: () -> List[ResolverStyle]
        pass
