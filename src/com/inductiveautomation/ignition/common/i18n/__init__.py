from __future__ import print_function

__all__ = ["LocaleUtils", "LocalizedString"]

from typing import Any, List, Optional

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from java.util import Locale


class LocaleUtils(Object):
    @staticmethod
    def getAvailableLocales(andRegionalVariants):
        # type: (bool) -> List[Locale]
        pass

    @staticmethod
    def parseLocale(locale):
        # type: (AnyStr) -> Optional[Locale]
        pass


class LocalizedString(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(LocalizedString, self).__init__()
        print(args)

    def compareTo(self, other):
        # type: (LocalizedString) -> int
        pass

    @staticmethod
    def createRaw(stringVal):
        # type: (AnyStr) -> LocalizedString
        pass

    def getDefaultVal(self):
        # type: () -> AnyStr
        pass

    def getKey(self):
        # type: () -> AnyStr
        pass

    def getParams(self):
        # type: () -> List[Object]
        pass

    def setDefaultVal(self, defaultVal):
        # type: (AnyStr) -> None
        pass

    def setKey(self, key):
        # type: (AnyStr) -> None
        pass

    def setParams(self, params):
        # type: (List[Object]) -> None
        pass

    def toString(self, locale=None):
        # type: (Optional[Locale]) -> AnyStr
        pass
