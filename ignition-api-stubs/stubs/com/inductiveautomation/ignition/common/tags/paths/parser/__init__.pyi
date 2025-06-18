from typing import Any, List

from com.inductiveautomation.ignition.common.tags.model import TagPath
from dev.coatl.helper.types import AnyStr
from java.lang import Object

class TagPathParser(Object):
    PARENT_RELATIVE: AnyStr
    PATH_SEPARATOR: AnyStr
    PROPERTY_SEPARATOR: AnyStr
    RELATIVE_DIR_UP: AnyStr
    ROOT_RELATIVE: AnyStr
    @staticmethod
    def chopPath(string: AnyStr) -> List[AnyStr]: ...
    @staticmethod
    def derelativize(tagPath: TagPath, relativeRoot: TagPath) -> TagPath: ...
    @staticmethod
    def isRelativePath(path: TagPath) -> bool: ...
    @staticmethod
    def parse(*args: Any) -> TagPath: ...
    @staticmethod
    def parseSafe(*args: Any) -> TagPath: ...
    @staticmethod
    def relativize(newPath: TagPath, relativeTo: TagPath) -> TagPath: ...
