__all__ = ["SecurityContext", "TagManager", "TagPath"]

from typing import Any, Optional, Union

from com.inductiveautomation.ignition.common import Path
from com.inductiveautomation.ignition.common.browsing import BrowseFilter
from com.inductiveautomation.ignition.common.config import Property
from com.inductiveautomation.ignition.common.gson import (
    JsonDeserializationContext,
    JsonElement,
    JsonSerializationContext,
)
from com.inductiveautomation.ignition.common.user import AuthenticatedUser
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from java.lang.reflect import Type


class TagManager(object):
    def browseAsync(
        self,
        tagPath,  # type: TagPath
        browseFilter,  # type: BrowseFilter
        securityContext=None,  # type: Optional[SecurityContext]
    ):
        # type: (...) -> Any
        raise NotImplementedError


class SecurityContext(Object):
    @staticmethod
    def emptyContext():
        # type: () -> SecurityContext
        pass

    @staticmethod
    def fromAuthenticatedUser(user):
        # type: (AuthenticatedUser) -> SecurityContext
        pass

    class GsonAdapter(Object):
        def __init__(self):
            # type: () -> None
            super(SecurityContext.GsonAdapter, self).__init__()

        def deserialize(
            self,
            jsonElement,  # type: JsonElement
            type_,  # type: Type
            jsonDeserializationContext,  # type: JsonDeserializationContext
        ):
            # type: (...) -> SecurityContext
            pass

        def serialize(
            self,
            securityContext,  # type: SecurityContext
            type_,  # type: Type
            jsonSerializationContext,  # type: JsonSerializationContext
        ):
            # type: (...) -> JsonElement
            pass


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
