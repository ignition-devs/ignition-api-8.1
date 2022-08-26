__all__ = ["LocalizedString"]

from typing import Any, List, Optional

from java.lang import Object, String
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
        # type: (String) -> LocalizedString
        pass

    def getDefaultVal(self):
        # type: () -> String
        pass

    def getKey(self):
        # type: () -> String
        pass

    def getParams(self):
        # type: () -> List[Object]
        pass

    def setDefaultVal(self, defaultVal):
        # type: (String) -> None
        pass

    def setKey(self, key):
        # type: (String) -> None
        pass

    def setParams(self, params):
        # type: (List[Object]) -> None
        pass

    def toString(self, locale=None):
        # type: (Optional[Locale]) -> String
        pass
