from __future__ import print_function

__all__ = [
    "ProjectResource",
    "ProjectResourceBuilder",
    "ProjectResourceId",
    "ResourcePath",
    "ResourceSignature",
    "ResourceType",
]

from typing import Any, Mapping, Optional, Union

from com.google.common.collect import ImmutableSet
from com.inductiveautomation.ignition.common import StringPath
from com.inductiveautomation.ignition.common.gson import (
    JsonDeserializationContext,
    JsonElement,
    JsonObject,
    JsonSerializationContext,
)
from dev.thecesrom.helper.types import AnyStr
from java.lang import Comparable, Object
from java.lang.reflect import Type
from java.util.function import Consumer


class ProjectResource(object):
    @staticmethod
    def calculateContentDigest(resource):
        # type: (ProjectResource) -> bytearray
        pass

    def copy(self, consumer=None):
        # type: (Optional[Consumer]) -> ProjectResource
        pass

    def getApplicationScope(self):
        # type: () -> int
        raise NotImplementedError

    def getAttribute(self, key):
        # type: (AnyStr) -> JsonElement
        pass

    def getAttributes(self):
        # type: () -> Mapping[AnyStr, JsonElement]
        raise NotImplementedError

    def getContentDigest(self):
        # type: () -> bytearray
        raise NotImplementedError

    def getData(self):
        # type: () -> bytearray
        raise NotImplementedError

    def getDataKeys(self):
        # type: () -> ImmutableSet
        raise NotImplementedError

    def getDocumentation(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getFolderPath(self):
        # type: () -> AnyStr
        pass

    def getProjectName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getResourceId(self):
        # type: () -> ProjectResourceId
        pass

    def getResourceName(self):
        # type: () -> AnyStr
        pass

    def getResourcePath(self):
        # type: () -> ResourcePath
        raise NotImplementedError

    def getResourceSignature(self):
        # type: () -> ResourceSignature
        raise NotImplementedError

    def getResourceType(self):
        # type: () -> ResourceType
        pass

    def getVersion(self):
        # type: () -> int
        raise NotImplementedError

    def isFolder(self):
        # type: () -> bool
        raise NotImplementedError

    def isLocked(self):
        # type: () -> bool
        raise NotImplementedError

    def isModuleFolder(self):
        # type: () -> bool
        pass

    def isOverridable(self):
        # type: () -> bool
        raise NotImplementedError

    def isResourceTypeFolder(self):
        # type: () -> bool
        pass

    def isRestricted(self):
        # type: () -> bool
        raise NotImplementedError

    def isSingletonResource(self):
        # type: () -> bool
        pass

    @staticmethod
    def newBuilder():
        # type: () -> ProjectResourceBuilder
        pass

    def toBuilder(self):
        # type: () -> ProjectResourceBuilder
        pass


class ProjectResourceBuilder(Object):
    def build(self):
        # type: () -> ProjectResource
        pass

    def clearAttributes(self):
        # type: () -> ProjectResourceBuilder
        pass

    def clearData(self):
        # type: () -> ProjectResourceBuilder
        pass

    def copyFrom(self, resource):
        # type: (ProjectResource) -> ProjectResourceBuilder
        pass

    def putAttribute(self, key, value):
        # type: (AnyStr, Any) -> ProjectResourceBuilder
        pass

    def putData(self, *args):
        # type: (*Any) -> ProjectResourceBuilder
        pass

    def removeAttribute(self, key):
        # type: (AnyStr) -> ProjectResourceBuilder
        pass

    def removeData(self, name):
        # type: (AnyStr) -> ProjectResourceBuilder
        pass

    def setApplicationScope(self, scope):
        # type: (Union[AnyStr, int]) -> ProjectResourceBuilder
        pass

    def setAttributes(self, attributes):
        # type: (Mapping[AnyStr, JsonElement]) -> ProjectResourceBuilder
        pass

    def setData(self, data):
        # type: (Mapping[AnyStr, bytearray]) -> ProjectResourceBuilder
        pass

    def setDocumentation(self, documentation):
        # type: (AnyStr) -> ProjectResourceBuilder
        pass

    def setFolder(self, folder):
        # type: (bool) -> ProjectResourceBuilder
        pass

    def setLocked(self, locked):
        # type: (bool) -> ProjectResourceBuilder
        pass

    def setOverridable(self, overridable):
        # type: (bool) -> ProjectResourceBuilder
        pass

    def setProjectName(self, projectName):
        # type: (AnyStr) -> ProjectResourceBuilder
        pass

    def setResourceId(self, id_):
        # type: (ProjectResourceId) -> ProjectResourceBuilder
        pass

    def setResourcePath(self, resourcePath):
        # type: (ResourcePath) -> ProjectResourceBuilder
        pass

    def setRestricted(self, restricted):
        # type: (bool) -> ProjectResourceBuilder
        pass

    def setVersion(self, version):
        # type: (int) -> ProjectResourceBuilder
        pass


class ProjectResourceId(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(ProjectResourceId, self).__init__()
        print(args)

    @staticmethod
    def fromJson(e):
        # type: (JsonElement) -> ProjectResourceId
        pass

    def getFolderPath(self):
        # type: () -> AnyStr
        pass

    def getProjectName(self):
        # type: () -> AnyStr
        pass

    def getResourcePath(self):
        # type: () -> ResourcePath
        pass

    def getResourceType(self):
        # type: () -> ResourceType
        pass

    def toJson(self):
        # type: () -> JsonObject
        pass


class ResourcePath(Object, Comparable):
    def __init__(self, type_, path):
        # type: (ResourceType, Union[AnyStr, StringPath]) -> None
        super(ResourcePath, self).__init__()
        self._type = type_
        self._path = path

    def compareTo(self, o):
        # type: (Any) -> int
        pass

    @staticmethod
    def createModuleRoot(moduleId):
        # type: (AnyStr) -> ResourcePath
        pass

    def getChild(self, *pathParts):
        # type: (*AnyStr) -> ResourcePath
        pass

    def getFolderPath(self):
        # type: () -> AnyStr
        pass

    def getModuleId(self):
        # type: () -> AnyStr
        pass

    def getName(self):
        # type: () -> AnyStr
        pass

    def getParent(self):
        # type: () -> ResourcePath
        pass

    def getParentPath(self):
        # type: () -> AnyStr
        pass

    def getPath(self):
        # type: () -> StringPath.CaseSensitiveStringPath
        pass

    def getResourceType(self):
        # type: () -> ResourceType
        pass

    def getType(self):
        # type: () -> ResourceType
        return self._type

    def isAncestorOf(self, possibleDescendant):
        # type: (ResourcePath) -> bool
        pass

    def isParentOf(self, possibleChild):
        # type: (ResourcePath) -> bool
        pass

    def isResourceTypeFolder(self):
        # type: () -> bool
        pass


class ResourceSignature(Object):
    def __init__(self, resourceId, signature):
        # type: (ProjectResourceId, bytearray) -> None
        super(ResourceSignature, self).__init__()
        self._resourceId = resourceId
        self._signature = signature

    def getResourceId(self):
        # type: () -> ProjectResourceId
        return self._resourceId

    def getSignature(self):
        # type: () -> bytearray
        return self._signature

    class GsonAdapter(Object):
        def deserialize(
            self,
            json,  # type: JsonElement
            typeOfT,  # type: Type
            context,  # type: JsonDeserializationContext
        ):
            # type: (...) -> ResourceSignature
            pass

        def serialize(
            self,
            src,  # type: ResourceSignature
            typeOfSrc,  # type: Type
            context,  # type: JsonSerializationContext
        ):
            # type: (...) -> JsonElement
            pass


class ResourceType(Object):
    def __init__(self, moduleId, typeId):
        # type: (AnyStr, AnyStr) -> None
        super(ResourceType, self).__init__()
        self._moduleId = moduleId
        self._typeId = typeId

    def childOrSubPath(self, potentialFolder, path):
        # type: (ResourcePath, AnyStr) -> ResourcePath
        pass

    def getModuleId(self):
        # type: () -> AnyStr
        return self._moduleId

    def getTypeId(self):
        # type: () -> AnyStr
        return self._typeId

    def matches(self, op):
        # type: (Any) -> bool
        pass

    def rootPath(self):
        # type: () -> ResourcePath
        pass

    def subPath(self, path):
        # type: (AnyStr) -> ResourcePath
        pass
