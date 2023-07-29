__all__ = ["SecurityContext", "TagManager", "TagPath"]

from typing import TYPE_CHECKING, Any, Optional

from com.inductiveautomation.ignition.common import Path
from com.inductiveautomation.ignition.common.config import Property
from com.inductiveautomation.ignition.common.gson import (
    JsonDeserializationContext,
    JsonElement,
    JsonSerializationContext,
)
from com.inductiveautomation.ignition.common.user import AuthenticatedUser
from dev.thecesrom.helper.types import AnyStr
from java.lang import Comparable, Object
from java.lang.reflect import Type

if TYPE_CHECKING:
    from com.inductiveautomation.ignition.common.browsing import BrowseFilter


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


class TagPath(Path, Comparable):
    def compareTo(self, o):
        # type: (TagPath) -> int
        pass

    def getChildPath(self, nextId):
        # type: (AnyStr) -> TagPath
        raise NotImplementedError

    def getItemName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getLastPathComponent(self):
        # type: () -> AnyStr
        pass

    def getParentPath(self):
        # type: () -> TagPath
        raise NotImplementedError

    def getPathComponent(self, i):
        # type: (int) -> AnyStr
        pass

    def getPathLength(self):
        # type: () -> int
        pass

    def getProperty(self):
        # type: () -> Property
        raise NotImplementedError

    def getSource(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def isAncestorOf(self, path):
        # type: (Path) -> bool
        return True

    def toStringFull(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def toStringPartial(self):
        # type: () -> AnyStr
        raise NotImplementedError
