from typing import List

from dev.coatl.helper.types import AnyStr
from java.lang import Enum


class Hyperlink(object):
    def getAddress(self):
        # type: () -> AnyStr
        pass

    def getLabel(self):
        # type: () -> AnyStr
        pass

    def getType(self):
        # type: () -> HyperlinkType
        pass

    def setAddress(self, address):
        # type: (AnyStr) -> None
        pass

    def setLabel(self, label):
        # type: (AnyStr) -> None
        pass


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
