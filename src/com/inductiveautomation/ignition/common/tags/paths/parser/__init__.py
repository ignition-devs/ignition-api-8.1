__all__ = ["TagPathParser"]

from typing import Any, List

from com.inductiveautomation.ignition.common.tags.model import TagPath
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object


class TagPathParser(Object):
    PARENT_RELATIVE = None  # type: AnyStr
    PATH_SEPARATOR = None  # type: AnyStr
    PROPERTY_SEPARATOR = None  # type: AnyStr
    RELATIVE_DIR_UP = None  # type: AnyStr
    ROOT_RELATIVE = None  # type: AnyStr

    @staticmethod
    def chopPath(string):
        # type: (AnyStr) -> List[AnyStr]
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
