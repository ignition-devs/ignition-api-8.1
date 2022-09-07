__all__ = ["BaseStream", "Stream"]

from typing import TypeVar

from java.lang import AutoCloseable, Runnable
from java.util import Iterator, Spliterator
from java.util.function import Consumer

S = TypeVar("S")
T = TypeVar("T")


class BaseStream(AutoCloseable):
    def close(self):
        # type: () -> None
        raise NotImplementedError

    def isParallel(self):
        # type: () -> bool
        raise NotImplementedError

    def iterator(self):
        # type: () -> Iterator
        raise NotImplementedError

    def onClose(self, closeHandler):
        # type: (Runnable) -> S
        raise NotImplementedError

    def parallel(self):
        # type: () -> S
        raise NotImplementedError

    def sequential(self):
        # type: () -> S
        raise NotImplementedError

    def spliterator(self):
        # type: () -> Spliterator
        raise NotImplementedError

    def unordered(self):
        # type: () -> S
        raise NotImplementedError


class Stream(BaseStream):
    @staticmethod
    def builder():
        # type: () -> Stream.Builder
        pass

    def close(self):
        # type: () -> None
        pass

    def isParallel(self):
        # type: () -> bool
        pass

    def iterator(self):
        # type: () -> Iterator
        pass

    def onClose(self, closeHandler):
        # type: (Runnable) -> S
        pass

    def parallel(self):
        # type: () -> S
        pass

    def sequential(self):
        # type: () -> S
        pass

    def spliterator(self):
        # type: () -> Spliterator
        pass

    def unordered(self):
        # type: () -> S
        pass

    class Builder(Consumer):
        def accept(self, t):
            # type: (T) -> None
            raise NotImplementedError

        def add(self, t):
            # type: (T) -> Stream.Builder
            pass

        def build(self):
            raise NotImplementedError
