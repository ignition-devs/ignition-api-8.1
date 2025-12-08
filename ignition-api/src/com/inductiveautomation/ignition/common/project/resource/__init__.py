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

from java.lang import Comparable, Object
from java.lang.reflect import Type
from java.util.function import Consumer

from com.google.common.collect import ImmutableSet
from com.inductiveautomation.ignition.common import StringPath
from com.inductiveautomation.ignition.common.gson import (
    JsonDeserializationContext,
    JsonElement,
    JsonObject,
    JsonSerializationContext,
)


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
        # type: (Union[str, unicode]) -> JsonElement
        pass

    def getAttributes(self):
        # type: () -> Mapping[Union[str, unicode], JsonElement]
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
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getFolderPath(self):
        # type: () -> Union[str, unicode]
        pass

    def getProjectName(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getResourceId(self):
        # type: () -> ProjectResourceId
        pass

    def getResourceName(self):
        # type: () -> Union[str, unicode]
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
        return True

    def isOverridable(self):
        # type: () -> bool
        raise NotImplementedError

    def isResourceTypeFolder(self):
        # type: () -> bool
        return True

    def isRestricted(self):
        # type: () -> bool
        raise NotImplementedError

    def isSingletonResource(self):
        # type: () -> bool
        return True

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
        # type: (Union[str, unicode], Any) -> ProjectResourceBuilder
        pass

    def putData(self, *args):
        # type: (*Any) -> ProjectResourceBuilder
        pass

    def removeAttribute(self, key):
        # type: (Union[str, unicode]) -> ProjectResourceBuilder
        pass

    def removeData(self, name):
        # type: (Union[str, unicode]) -> ProjectResourceBuilder
        pass

    def setApplicationScope(self, scope):
        # type: (Union[str, unicode, int]) -> ProjectResourceBuilder
        pass

    def setAttributes(
        self,
        attributes,  # type: Mapping[Union[str, unicode], JsonElement]
    ):
        # type: (...) -> ProjectResourceBuilder
        pass

    def setData(
        self,
        data,  # type: Mapping[Union[str, unicode], bytearray]
    ):
        # type: (...) -> ProjectResourceBuilder
        pass

    def setDocumentation(self, documentation):
        # type: (Union[str, unicode]) -> ProjectResourceBuilder
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
        # type: (Union[str, unicode]) -> ProjectResourceBuilder
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
        # type: () -> Union[str, unicode]
        pass

    def getProjectName(self):
        # type: () -> Union[str, unicode]
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
        # type: (ResourceType, Union[str, unicode, StringPath]) -> None
        super(ResourcePath, self).__init__()
        self._type = type_
        self._path = path

    def compareTo(self, o):
        # type: (Any) -> int
        pass

    @staticmethod
    def createModuleRoot(moduleId):
        # type: (Union[str, unicode]) -> ResourcePath
        pass

    def getChild(self, *pathParts):
        # type: (*Union[str, unicode]) -> ResourcePath
        pass

    def getFolderPath(self):
        # type: () -> Union[str, unicode]
        pass

    def getModuleId(self):
        # type: () -> Union[str, unicode]
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        pass

    def getParent(self):
        # type: () -> ResourcePath
        pass

    def getParentPath(self):
        # type: () -> Union[str, unicode]
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
        return True

    def isParentOf(self, possibleChild):
        # type: (ResourcePath) -> bool
        return True

    def isResourceTypeFolder(self):
        # type: () -> bool
        return True


class ResourceSignature(Object):

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


class ResourceType(Object):
    def __init__(self, moduleId, typeId):
        # type: (Union[str, unicode], Union[str, unicode]) -> None
        super(ResourceType, self).__init__()
        self._moduleId = moduleId
        self._typeId = typeId

    def childOrSubPath(self, potentialFolder, path):
        # type: (ResourcePath, Union[str, unicode]) -> ResourcePath
        pass

    def getModuleId(self):
        # type: () -> Union[str, unicode]
        return self._moduleId

    def getTypeId(self):
        # type: () -> Union[str, unicode]
        return self._typeId

    def matches(self, op):
        # type: (Any) -> bool
        return True

    def rootPath(self):
        # type: () -> ResourcePath
        pass

    def subPath(self, path):
        # type: (Union[str, unicode]) -> ResourcePath
        pass
