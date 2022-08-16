from typing import Any, Generic, Iterator, List, TypeVar, Union

from java.lang import Class, Enum, Object, String

T = TypeVar("T")


class Watchable(object):
    def register(self, *args):
        # type: (Any) -> WatchKey
        raise NotImplementedError


class LinkOption(Enum):
    @staticmethod
    def values():
        # type: () -> List[LinkOption]
        pass


class Path(Watchable):
    def compareTo(self, other):
        # type: (Path) -> int
        pass

    def endsWith(self, other):
        # type: (Union[Object, Path, String]) -> bool
        pass

    def equals(self, other):
        # type: (Object) -> bool
        pass

    def getFileName(self):
        # type: () -> Path
        pass

    def getName(self, index):
        # type: (int) -> Path
        pass

    def getNameCount(self):
        # type: () -> int
        pass

    def getParent(self):
        # type: () -> Path
        pass

    def getRoot(self):
        # type: () -> Path
        pass

    def hashCode(self):
        # type: () -> int
        pass

    def isAbsolute(self):
        # type: () -> bool
        pass

    def iterator(self):
        # type: () -> Iterator[Path]
        pass

    def normalize(self):
        # type: () -> Path
        pass

    @staticmethod
    def of(*args):
        # type: (Any) -> Path
        pass

    def register(self, *args):
        # type: (Any) -> WatchKey
        pass

    def relativize(self, other):
        # type: (Path) -> Path
        pass

    def resolve(self, other):
        # type: (Union[Path, String]) -> Path
        pass

    def resolveSibling(self, other):
        # type: (Path) -> Path
        pass

    def startsWith(self, other):
        # type: (Path) -> bool
        pass

    def subpath(self, beginIndex, endIndex):
        # type: (int, int) -> Path
        pass

    def toAbsolutePath(self):
        # type: () -> Path
        pass

    def toFile(self):
        # type: () -> Any
        pass

    def toRealPath(self, *args):
        # type: (LinkOption) -> Path
        pass

    def toString(self):
        # type: () -> String
        pass

    def toUri(self):
        # type: () -> Any
        pass


class WatchEvent(object):
    def context(self):
        # type: () -> T
        raise NotImplementedError

    def count(self):
        # type: () -> int
        raise NotImplementedError

    def kind(self):
        # type: () -> WatchEvent.Kind
        raise NotImplementedError

    class Kind(object):
        def name(self):
            # type: () -> String
            raise NotImplementedError

        def type(self):
            # type: () -> Class
            raise NotImplementedError

    class Modifier(object):
        def name(self):
            # type: () -> String
            raise NotImplementedError


class WatchKey(object):
    def cancel(self):
        # type: () -> None
        raise NotImplementedError

    def isValid(self):
        # type: () -> bool
        raise NotImplementedError

    def pollEvents(self):
        # type: () -> List[WatchEvent]
        raise NotImplementedError

    def reset(self):
        # type: () -> bool
        raise NotImplementedError

    def watchable(self):
        # type: () -> Watchable
        raise NotImplementedError
