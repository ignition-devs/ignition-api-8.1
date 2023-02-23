from __future__ import print_function

__all__ = ["ExceptionContext"]

from typing import Any, Optional, Set

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object, Throwable
from java.util import Locale


class ExceptionContext(Object):
    def __init__(self, throwable):
        # type: (Throwable) -> None
        super(ExceptionContext, self).__init__()
        print(throwable)

    def addMessage(self, pattern, *args):
        # type: (AnyStr, *Any) -> None
        pass

    def getKeys(self):
        # type: () -> Set[AnyStr]
        pass

    def getLocalizedMessage(self):
        # type: () -> AnyStr
        pass

    def getMessage(self, locale=None, separator=None):
        # type: (Optional[Locale], Optional[AnyStr]) -> AnyStr
        pass

    def getThrowable(self):
        # type: () -> Throwable
        pass

    def getValue(self, key):
        # type: (AnyStr) -> None
        pass

    def setValue(self, key, value):
        # type: (AnyStr, Object) -> None
        pass
