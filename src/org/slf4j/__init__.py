__all__ = ["Logger", "Marker"]

from typing import Any, Iterable, Optional, Union

from java.lang import String


class Logger(object):
    ROOT_LOGGER_NAME = "ROOT"

    def debug(self, *args):
        # type: (Any) -> None
        pass

    def error(self, *args):
        # type: (Any) -> None
        pass

    def getName(self):
        # type: () -> String
        pass

    def info(self, *args):
        # type: (Any) -> None
        pass

    def isErrorEnabled(self, marker=None):
        # type: (Optional[Marker]) -> bool
        pass

    def isInfoEnabled(self, marker=None):
        # type: (Optional[Marker]) -> bool
        pass

    def isTraceEnabled(self, marker=None):
        # type: (Optional[Marker]) -> bool
        pass

    def isWarnEnabled(self, marker=None):
        # type: (Optional[Marker]) -> bool
        pass

    def trace(self, *args):
        # type: (Any) -> None
        pass

    def warn(self, *args):
        # type: (Any) -> None
        pass


class Marker(object):
    ANY_MARKER = "*"
    ANY_NON_NULL_MARKER = "+"

    def add(self, reference):
        # type: (Marker) -> None
        raise NotImplementedError

    def contains(self, arg):
        # type: (Union[Marker, String]) -> bool
        raise NotImplementedError

    def equals(self, o):
        # type: (Any) -> bool
        pass

    def getName(self):
        # type: () -> String
        pass

    def hashCode(self):
        # type: () -> int
        pass

    def hasReferences(self):
        # type: () -> bool
        pass

    def iterator(self):
        # type: () -> Iterable[Marker]
        pass

    def remove(self, reference):
        # type: (Marker) -> bool
        pass
