__all__ = ["TagPathParser"]

from typing import Any, List

from com.inductiveautomation.ignition.common.tags.model import TagPath
from java.lang import Object, String


class TagPathParser(Object):
    PARENT_RELATIVE = None  # type: String
    PATH_SEPARATOR = None  # type: String
    PROPERTY_SEPARATOR = None  # type: String
    RELATIVE_DIR_UP = None  # type: String
    ROOT_RELATIVE = None  # type: String

    @staticmethod
    def chopPath(string):
        # type: (String) -> List[String]
        pass

    @staticmethod
    def derelativize(tagPath, relativeRoot):
        # type: (TagPath, TagPath) -> TagPath
        pass

    @staticmethod
    def isRelativePath(path):
        # type: (TagPath) -> bool
        return True

    @staticmethod
    def parse(*args):
        # type: (*Any) -> TagPath
        pass

    @staticmethod
    def parseSafe(*args):
        # type: (*Any) -> TagPath
        pass

    @staticmethod
    def relativize(newPath, relativeTo):
        # type: (TagPath, TagPath) -> TagPath
        pass
