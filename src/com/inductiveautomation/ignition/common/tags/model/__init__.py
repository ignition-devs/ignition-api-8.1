__all__ = ["TagPath"]

from typing import Union

from com.inductiveautomation.ignition.common import Path
from com.inductiveautomation.ignition.common.config import Property
from dev.thecesrom.helper.types import AnyStr


class TagPath(Path):
    def compareTo(self, that):
        # type: (TagPath) -> int
        pass

    def getChildPath(self, arg):
        # type: (Union[Property, AnyStr]) -> TagPath
        pass

    def getItemName(self):
        # type: () -> AnyStr
        pass

    def getLastPathComponent(self):
        # type: () -> AnyStr
        pass

    def getParentPath(self):
        # type: () -> Path
        pass

    def getPathComponent(self, i):
        # type: (int) -> AnyStr
        pass

    def getPathLength(self):
        # type: () -> int
        pass

    def getProperty(self):
        # type: () -> Property
        pass

    def getSource(self):
        # type: () -> AnyStr
        pass

    def isAncestorOf(self, path):
        # type: (Path) -> bool
        return True

    def toStringFull(self):
        # type: () -> AnyStr
        pass

    def toStringPartial(self):
        # type: () -> AnyStr
        pass
