__all__ = ["TagObjectType"]

from typing import Iterable, Union

from java.lang import Enum


class TagObjectType(Enum):
    @staticmethod
    def fromString(value):
        # type: (Union[str, unicode]) -> TagObjectType
        pass

    def isComplexTag(self):
        # type: () -> bool
        return True

    @staticmethod
    def values():
        # type: () -> Iterable[TagObjectType]
        pass
