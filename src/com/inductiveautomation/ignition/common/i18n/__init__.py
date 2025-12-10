from __future__ import print_function

__all__ = ["LocaleUtils", "LocalizedString"]

from typing import Any, List, Optional, Union

from java.lang import Object
from java.util import Locale


class LocaleUtils(Object):
    @staticmethod
    def getAvailableLocales(andRegionalVariants):
        # type: (bool) -> List[Locale]
        pass

    @staticmethod
    def parseLocale(locale):
        # type: (Union[str, unicode]) -> Optional[Locale]
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
        # type: (Union[str, unicode]) -> LocalizedString
        pass

    def getDefaultVal(self):
        # type: () -> Union[str, unicode]
        pass

    def getKey(self):
        # type: () -> Union[str, unicode]
        pass

    def getParams(self):
        # type: () -> List[Object]
        pass

    def setDefaultVal(self, defaultVal):
        # type: (Union[str, unicode]) -> None
        pass

    def setKey(self, key):
        # type: (Union[str, unicode]) -> None
        pass

    def setParams(self, params):
        # type: (List[Object]) -> None
        pass

    def toString(self, locale=None):
        # type: (Optional[Locale]) -> Union[str, unicode]
        pass
