__all__ = ["Logger", "Marker"]

from typing import Any, Iterable, Optional, Union

from dev.coatl.helper.types import AnyStr


class Logger(object):
    ROOT_LOGGER_NAME = "ROOT"

    def debug(self, *args):
        # type: (Any) -> None
        pass

    def error(self, *args):
        # type: (Any) -> None
        pass

    def getName(self):
        # type: () -> AnyStr
        pass

    def info(self, *args):
        # type: (Any) -> None
        pass

    def isErrorEnabled(self, marker=None):
        # type: (Optional[Marker]) -> bool
        return True

    def isInfoEnabled(self, marker=None):
        # type: (Optional[Marker]) -> bool
        return True

    def isTraceEnabled(self, marker=None):
        # type: (Optional[Marker]) -> bool
        return True

    def isWarnEnabled(self, marker=None):
        # type: (Optional[Marker]) -> bool
        return True

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
        # type: (Union[Marker, AnyStr]) -> bool
        raise NotImplementedError

    def equals(self, o):
        # type: (Any) -> bool
        return True

    def getName(self):
        # type: () -> AnyStr
        pass

    def hashCode(self):
        # type: () -> int
        pass

    def hasReferences(self):
        # type: () -> bool
        return True

    def iterator(self):
        # type: () -> Iterable[Marker]
        pass

    def remove(self, reference):
        # type: (Marker) -> bool
        return True
