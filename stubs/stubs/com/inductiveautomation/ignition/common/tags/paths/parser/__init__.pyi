from typing import Any, List, Union

from com.inductiveautomation.ignition.common.tags.model import TagPath
from java.lang import Object

class TagPathParser(Object):
    PARENT_RELATIVE: Union[str, unicode]
    PATH_SEPARATOR: Union[str, unicode]
    PROPERTY_SEPARATOR: Union[str, unicode]
    RELATIVE_DIR_UP: Union[str, unicode]
    ROOT_RELATIVE: Union[str, unicode]
    @staticmethod
    def chopPath(string: Union[str, unicode]) -> List[Union[str, unicode]]: ...
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
