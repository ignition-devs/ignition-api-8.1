from __future__ import print_function

__all__ = [
    "AbstractTagPath",
    "BasicTagPath",
    "PropertyAlteredTagPath",
    "SourceAlteredTagPath",
]

from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common.config import Property
from com.inductiveautomation.ignition.common.tags.model import TagPath
from java.lang import Object, String


class AbstractTagPath(Object, TagPath):
    @staticmethod
    def compareNullLow(c1, c2):
        # type: (Property, Property) -> int
        pass


class BasicTagPath(AbstractTagPath):
    def __init__(
        self,
        source,  # type: String
        pathParts=None,  # type: Optional[List[String]]
        prop=None,  # type: Optional[Property]
    ):
        # type: (...) -> None
        print(source, pathParts, prop)

    @staticmethod
    def append(root, arg):
        # type: (TagPath, Union[String, TagPath]) -> TagPath
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
        print(path, prop)


class SourceAlteredTagPath(AbstractTagPath):
    def __init__(self, path, source):
        # type: (TagPath, String) -> None
        print(path, source)
