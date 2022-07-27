from __future__ import print_function

__all__ = ["EventProperty", "EventPropertyType", "ShelvedPath"]

from typing import Any, List

from com.inductiveautomation.ignition.common import Path, QualifiedPath
from com.inductiveautomation.ignition.common.config import Property
from java.lang import Class, Enum, Object, String
from java.util import Date


class EventProperty(Object):
    @staticmethod
    def create(prop, type):
        # type: (Property, EventPropertyType) -> EventProperty
        pass

    @staticmethod
    def createDynamic(prop, isConfig):
        # type: (Property, bool) -> EventProperty
        pass

    @staticmethod
    def createStatic(prop, isConfig):
        # type: (Property, bool) -> EventProperty
        pass

    def getDefaultValue(self):
        # type: () -> Object
        pass

    def getName(self):
        # type: () -> String
        pass

    def getPropertyType(self):
        # type: () -> EventPropertyType
        pass

    def getType(self):
        # type: () -> Class
        pass


class EventPropertyType(Enum):
    @staticmethod
    def values():
        # type: () -> List[EventPropertyType]
        pass


class ShelvedPath(Object):
    """This class provides information about a path that has been
    "shelved", such as when it was shelved, and by whom, and the actual
    path.
    """

    def __init__(self, *args):
        # type: (Any) -> None
        print(args)

    def getExpiration(self):
        # type: () -> Date
        pass

    def getHitCount(self):
        # type: () -> int
        pass

    def getPath(self):
        # type: () -> Path
        pass

    def getShelveTime(self):
        # type: () -> Date
        pass

    def getUser(self):
        # type: () -> QualifiedPath
        pass

    def incrementHitCount(self):
        # type: () -> None
        pass

    def isExpired(self):
        # type: () -> bool
        pass
