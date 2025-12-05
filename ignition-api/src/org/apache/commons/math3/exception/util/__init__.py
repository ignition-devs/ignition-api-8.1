from __future__ import print_function

__all__ = ["ExceptionContext"]

from typing import Any, Optional, Set, Union

from java.lang import Object, Throwable
from java.util import Locale


class ExceptionContext(Object):
    def __init__(self, throwable):
        # type: (Throwable) -> None
        super(ExceptionContext, self).__init__()
        print(throwable)

    def addMessage(self, pattern, *args):
        # type: (Union[str, unicode], *Any) -> None
        pass

    def getKeys(self):
        # type: () -> Set[Union[str, unicode]]
        pass

    def getLocalizedMessage(self):
        # type: () -> Union[str, unicode]
        pass

    def getMessage(
        self,
        locale=None,  # type: Optional[Locale]
        separator=None,  # type: Union[str, unicode, None]
    ):
        # type: (...) -> Union[str, unicode]
        pass

    def getThrowable(self):
        # type: () -> Throwable
        pass

    def getValue(self, key):
        # type: (Union[str, unicode]) -> None
        pass

    def setValue(self, key, value):
        # type: (Union[str, unicode], Object) -> None
        pass
