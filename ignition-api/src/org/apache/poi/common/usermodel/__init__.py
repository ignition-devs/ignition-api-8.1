from typing import List

from dev.coatl.helper.types import AnyStr
from java.lang import Enum


class Hyperlink(object):
    def getAddress(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getLabel(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getType(self):
        # type: () -> HyperlinkType
        raise NotImplementedError

    def setAddress(self, address):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setLabel(self, label):
        # type: (AnyStr) -> None
        raise NotImplementedError


class HyperlinkType(Enum):
    DOCUMENT = None  # type: int
    EMAIL = None  # type: int
    FILE = None  # type: int
    NONE = None  # type: int
    URL = None  # type: int

    @staticmethod
    def values():
        # type: () -> List[HyperlinkType]
        pass
