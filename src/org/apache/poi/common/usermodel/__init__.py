from typing import List, Union

from java.lang import Enum


class Hyperlink(object):
    def getAddress(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getLabel(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getType(self):
        # type: () -> HyperlinkType
        raise NotImplementedError

    def setAddress(self, address):
        # type: (Union[str, unicode]) -> None
        raise NotImplementedError

    def setLabel(self, label):
        # type: (Union[str, unicode]) -> None
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
