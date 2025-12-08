from __future__ import print_function

__all__ = [
    "AbstractTagPath",
    "BasicTagPath",
    "PropertyAlteredTagPath",
    "SourceAlteredTagPath",
]

from typing import Any, List, Optional, Union

from java.lang import Object

from com.inductiveautomation.ignition.common.config import Property
from com.inductiveautomation.ignition.common.tags.model import TagPath


class AbstractTagPath(Object, TagPath):
    def __init__(self):
        # type: () -> None
        super(AbstractTagPath, self).__init__()

    @staticmethod
    def compareNullLow(c1, c2):
        # type: (Property, Property) -> int
        pass

    def getChildPath(self, nextId):
        # type: (Union[str, unicode]) -> TagPath
        pass

    def getItemName(self):
        # type: () -> Union[str, unicode]
        pass

    def getParentPath(self):
        # type: () -> TagPath
        pass

    def getProperty(self):
        # type: () -> Property
        pass

    def getSource(self):
        # type: () -> Union[str, unicode]
        pass

    def toStringFull(self):
        # type: () -> Union[str, unicode]
        pass

    def toStringPartial(self):
        # type: () -> Union[str, unicode]
        pass


class BasicTagPath(AbstractTagPath):
    def __init__(
        self,
        source,  # type: Union[str, unicode]
        pathParts=None,  # type: Optional[List[Union[str, unicode]]]
        prop=None,  # type: Optional[Property]
    ):
        # type: (...) -> None
        super(BasicTagPath, self).__init__()
        print(source, pathParts, prop)

    @staticmethod
    def append(root, arg):
        # type: (TagPath, Union[str, unicode, TagPath]) -> TagPath
        pass

    @staticmethod
    def copy(path):
        # type: (TagPath) -> BasicTagPath
        pass

    @staticmethod
    def renameParentFolder(path, newParent):
        # type: (TagPath, TagPath) -> BasicTagPath
        pass

    @staticmethod
    def subPath(path, *args):
        # type: (TagPath, *Any) -> BasicTagPath
        pass


class PropertyAlteredTagPath(AbstractTagPath):
    def __init__(self, path, prop):
        # type: (TagPath, Property) -> None
        super(PropertyAlteredTagPath, self).__init__()
        print(path, prop)


class SourceAlteredTagPath(AbstractTagPath):
    def __init__(self, path, source):
        # type: (TagPath, Union[str, unicode]) -> None
        super(SourceAlteredTagPath, self).__init__()
        print(path, source)
