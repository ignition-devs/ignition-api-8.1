__all__ = ["LocalizedString"]

from typing import Any, List, Optional

from java.lang import Object
from java.util import Locale


class LocalizedString(Object):
    def __init__(self, *args):
        # type: (Any) -> None
        pass

    def compareTo(self, other):
        # type: (LocalizedString) -> int
        pass

    @staticmethod
    def createRaw(stringVal):
        # type: (str) -> LocalizedString
        pass

    def getDefaultVal(self):
        # type: () -> str
        pass

    def getKey(self):
        # type: () -> str
        pass

    def getParams(self):
        # type: () -> List[Object]
        pass

    def setDefaultVal(self, defaultVal):
        # type: (str) -> None
        pass

    def setKey(self, key):
        # type: (str) -> None
        pass

    def setParams(self, params):
        # type: (List[Object]) -> None
        pass

    def toString(self, locale=None):
        # type: (Optional[Locale]) -> str
        pass
