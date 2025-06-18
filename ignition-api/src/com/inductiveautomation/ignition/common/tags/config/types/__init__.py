__all__ = ["TagObjectType"]

from typing import Iterable

from dev.coatl.helper.types import AnyStr
from java.lang import Enum


class TagObjectType(Enum):
    @staticmethod
    def fromString(value):
        # type: (AnyStr) -> TagObjectType
        pass

    def isComplexTag(self):
        # type: () -> bool
        return True

    @staticmethod
    def values():
        # type: () -> Iterable[TagObjectType]
        pass
