from typing import Any, Optional, Set

from java.lang import Object, String, Throwable
from java.util import Locale


class ExceptionContext(Object):
    def __init__(self, throwable):
        # type: (Throwable) -> None
        pass

    def addMessage(self, pattern, *args):
        # type: (String, *Any) -> None
        pass

    def getKeys(self):
        # type: () -> Set[String]
        pass

    def getLocalizedMessage(self):
        # type: () -> String
        pass

    def getMessage(self, locale=None, separator=None):
        # type: (Optional[Locale], Optional[String]) -> String
        pass

    def getThrowable(self):
        # type: () -> Throwable
        pass

    def getValue(self, key):
        # type: (String) -> None
        pass

    def setValue(self, key, value):
        # type: (String, Object) -> None
        pass
