__all__ = ["Request", "RequestWatcher"]

from java.lang import Exception as JavaException
from java.lang import Object
from org.python.core import PyFunction


class RequestWatcher(object):
    def block(self):
        # type: () -> bool
        raise NotImplementedError

    def compose(self, *args):
        # type: (RequestWatcher) -> RequestWatcher
        raise NotImplementedError


class Request(RequestWatcher):
    def block(self):
        # type: () -> bool
        pass

    def cancel(self):
        # type: () -> None
        raise NotImplementedError

    def compose(self, *args):
        # type: (RequestWatcher) -> RequestWatcher
        pass

    def get(self):
        # type: () -> Object
        raise NotImplementedError

    def getError(self):
        # type: () -> JavaException
        raise NotImplementedError

    def onError(self, func):
        # type: (PyFunction) -> None
        raise NotImplementedError

    def onSuccess(self, func):
        # type: (PyFunction) -> None
        raise NotImplementedError
