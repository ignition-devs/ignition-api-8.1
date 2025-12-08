__all__ = ["TagPathParser"]

from typing import Any, List, Union

from java.lang import Object

from com.inductiveautomation.ignition.common.tags.model import TagPath


class TagPathParser(Object):
    PARENT_RELATIVE = None  # type: Union[str, unicode]
    PATH_SEPARATOR = None  # type: Union[str, unicode]
    PROPERTY_SEPARATOR = None  # type: Union[str, unicode]
    RELATIVE_DIR_UP = None  # type: Union[str, unicode]
    ROOT_RELATIVE = None  # type: Union[str, unicode]

    @staticmethod
    def chopPath(string):
        # type: (Union[str, unicode]) -> List[Union[str, unicode]]
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
