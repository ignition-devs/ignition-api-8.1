__all__ = ["BaseStream", "Collector", "Stream"]

from typing import Any, Iterable, Set

from java.lang import AutoCloseable, Enum, Runnable
from java.util import Iterator, Spliterator
from java.util.function import BiConsumer, BinaryOperator, Consumer, Function, Supplier


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
        # type: (Runnable) -> Any
        raise NotImplementedError

    def parallel(self):
        # type: () -> Any
        raise NotImplementedError

    def sequential(self):
        # type: () -> Any
        raise NotImplementedError

    def spliterator(self):
        # type: () -> Spliterator
        raise NotImplementedError

    def unordered(self):
        # type: () -> Any
        raise NotImplementedError


class Collector(object):
    def accumulator(self):
        # type: () -> BiConsumer
        pass

    def characteristic(self):
        # type: () -> Set[Collector.Characteristics]
        pass

    def combiner(self):
        # type: () -> BinaryOperator
        pass

    def finisher(self):
        # type: () -> Function
        pass

    @staticmethod
    def of(*args):
        # type: (*Any) -> Collector
        pass

    def supplier(self):
        # type: () -> Supplier
        pass

    class Characteristics(Enum):
        @staticmethod
        def values():
            # type: () -> Iterable[Collector.Characteristics]
            pass


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
        return True

    def iterator(self):
        # type: () -> Iterator
        pass

    def onClose(self, closeHandler):
        # type: (Runnable) -> Any
        pass

    def parallel(self):
        # type: () -> Any
        pass

    def sequential(self):
        # type: () -> Any
        pass

    def spliterator(self):
        # type: () -> Spliterator
        pass

    def unordered(self):
        # type: () -> Any
        pass

    class Builder(Consumer):
        def accept(self, t):
            # type: (Any) -> None
            raise NotImplementedError

        def add(self, t):
            # type: (Any) -> Stream.Builder
            pass

        def build(self):
            # type: () -> Stream
            raise NotImplementedError
