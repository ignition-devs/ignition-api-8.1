__all__ = [
    "ImmutableCollection",
    "ImmutableList",
    "ImmutableSet",
    "UnmodifiableIterator",
    "UnmodifiableListIterator",
]

from typing import Any, Iterable, Optional

from java.lang import Object
from java.util import AbstractCollection, Comparator
from java.util.stream import Collector


class ImmutableCollection(AbstractCollection):
    def asList(self):
        # type: () -> ImmutableList
        pass

    def contains(self, o):
        # type: (Object) -> bool
        raise NotImplementedError

    class Builder(Object):
        def add(self, *elements):
            # type: (*Any) -> ImmutableCollection.Builder
            pass

        def addAll(self, elements):
            # type: (Any) -> ImmutableCollection.Builder
            pass

        def build(self):
            # type: () -> ImmutableCollection
            raise NotImplementedError


class ImmutableList(ImmutableCollection):
    @staticmethod
    def builder():
        # type: () -> ImmutableList.Builder
        pass

    @staticmethod
    def builderWithExpectedSize():
        # type: () -> ImmutableList.Builder
        pass

    def contains(self, o):
        # type: (Object) -> bool
        pass

    @staticmethod
    def copyOf(*args):
        # type: (*Any) -> ImmutableList
        pass

    def indexOf(self, obj):
        # type: (Object) -> int
        pass

    def lastIndexOf(self, obj):
        # type: (Object) -> int
        pass

    def listIterator(self, index=None):
        # type: (Optional[int]) -> UnmodifiableListIterator
        pass

    @staticmethod
    def of(*args):
        # type: (*Any) -> ImmutableList
        pass

    @staticmethod
    def sortedCopyOf(comparator, elements):
        # type: (Comparator, Iterable[Any]) -> ImmutableList
        pass

    def subList(self, fromIndex, toIndex):
        # type: (int, int) -> ImmutableList
        pass

    @staticmethod
    def toImmutableList():
        # type: () -> Collector
        pass

    class Builder(ImmutableCollection.Builder):
        def build(self):
            # type: () -> ImmutableList
            pass


class ImmutableSet(ImmutableCollection):
    @staticmethod
    def builder():
        # type: () -> ImmutableSet.Builder
        pass

    @staticmethod
    def builderWithExpectedSize():
        # type: () -> ImmutableSet.Builder
        pass

    def contains(self, o):
        # type: (Object) -> bool
        pass

    @staticmethod
    def copyOf(*args):
        # type: (*Any) -> ImmutableSet
        pass

    @staticmethod
    def of(*args):
        # type: (*Any) -> ImmutableSet
        pass

    @staticmethod
    def toImmutableSet():
        # type: () -> Collector
        pass

    class Builder(ImmutableCollection.Builder):
        def __init__(self):
            # type: () -> None
            super(ImmutableSet.Builder, self).__init__()

        def build(self):
            # type: () -> ImmutableSet
            pass


class UnmodifiableIterator(Object):
    def remove(self):
        # type: () -> None
        pass


class UnmodifiableListIterator(UnmodifiableIterator):
    def add(self, e):
        # type: (Any) -> None
        pass

    def set(self, e):
        # type: (Any) -> None
        pass
