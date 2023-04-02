__all__ = ["ResourceFilter"]

from typing import List, Union

from com.inductiveautomation.ignition.common.project.resource import (
    ProjectResource,
    ProjectResourceId,
    ResourceType,
)
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object


class ResourceFilter(Object):
    def __init__(self, applicationScope, resourceTypes):
        # type: (int, List[ResourceType]) -> None
        super(ResourceFilter, self).__init__()
        self._applicationScope = applicationScope
        self._resourceTypes = resourceTypes

    def apply(self, arg):
        # type: (Union[ProjectResource, ProjectResourceId]) -> bool
        pass

    @staticmethod
    def forScope(applicationScope):
        # type: (int) -> ResourceFilter
        pass

    def getApplicationScope(self):
        # type: () -> int
        return self._applicationScope

    def getResourceTypes(self):
        # type: () -> List[ResourceType]
        return self._resourceTypes

    @staticmethod
    def newBuilder():
        # type: () -> ResourceFilter.Builder
        pass

    class Builder(Object):
        def addResourceType(self, resourceType):
            # type: (ResourceType) -> ResourceFilter.Builder
            pass

        def addResourceTypes(self, resourceTypes):
            # type: (List[ResourceType]) -> ResourceFilter.Builder
            pass

        def build(self):
            # type: () -> ResourceFilter
            pass

        def setApplicationScope(self, applicationScope):
            # type: (Union[AnyStr, int]) -> ResourceFilter.Builder
            pass
