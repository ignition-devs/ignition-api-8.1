from __future__ import print_function

__all__ = ["ChangeOperation", "Project", "ProjectManifest", "ProjectResourceListener"]

from typing import Iterable, List, Optional, Set

from com.inductiveautomation.ignition.common.project.resource import (
    ProjectResource,
    ProjectResourceId,
    ResourceSignature,
)
from com.inductiveautomation.ignition.gateway.project import ResourceFilter
from dev.thecesrom.helper.types import AnyStr
from java.lang import Enum, Object


class Project(object):
    def addProjectResourceListener(self, listener):
        # type: (ProjectResourceListener) -> None
        raise NotImplementedError


class ProjectResourceListener(object):
    def getResourceFilter(self):
        # type: () -> ResourceFilter
        pass

    def manifestChanged(
        self,
        projectName,  # type: AnyStr
        operation,  # type: List[ChangeOperation.ManifestChangeOperation]
    ):
        # type: (...) -> None
        pass

    def onAfterChanges(self):
        # type: () -> None
        pass

    def onBeforeChanges(self):
        # type: () -> None
        pass

    def resourcesCreated(
        self,
        projectName,  # type: AnyStr
        resources,  # type: List[ChangeOperation.CreateResourceOperation]
    ):
        # type: (...) -> None
        raise NotImplementedError

    def resourcesDeleted(
        self,
        projectName,  # type: AnyStr
        resources,  # type: List[ChangeOperation.DeleteResourceOperation]
    ):
        # type: (...) -> None
        raise NotImplementedError

    def resourcesModified(
        self,
        projectName,  # type: AnyStr
        resources,  # type: List[ChangeOperation.ModifyResourceOperation]
    ):
        # type: (...) -> None
        raise NotImplementedError


class ChangeOperation(Object):
    @staticmethod
    def changeOpsToIdSet(changes):
        # type: (List[ChangeOperation]) -> Set[ProjectResourceId]
        pass

    def getOperationType(self):
        # type: () -> ChangeOperation.OperationType
        pass

    def getProjectName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    @staticmethod
    def getResourceFromChange(op):
        # type: (ChangeOperation) -> ProjectResource
        pass

    @staticmethod
    def getResourceIdFromChange(op):
        # type: (ChangeOperation) -> ProjectResourceId
        pass

    @staticmethod
    def newCreateOp(
        resource,  # type: ProjectResource
    ):
        # type: (...) -> ChangeOperation.CreateResourceOperation
        pass

    @staticmethod
    def newDeleteOp(
        resourceSignature,  # type: ResourceSignature
    ):
        # type: (...) -> ChangeOperation.DeleteResourceOperation
        pass

    @staticmethod
    def newManifestChangeOp(
        projectName,  # type: AnyStr
        manifest,  # type: ProjectManifest
        baseHashCode=None,  # type: Optional[int]
    ):
        # type: (...) -> ChangeOperation.ManifestChangeOperation
        pass

    @staticmethod
    def newModifyOp(
        resource,  # type: ProjectResource
        baseSignature,  # type: ResourceSignature
    ):
        # type: (...) -> ModifyResourceOperation
        pass

    class CreateResourceOperation(Object):
        def getResource(self):
            # type: () -> ProjectResource
            pass

        def getResourceId(self):
            # type: () -> ProjectResourceId
            pass

    class DeleteResourceOperation(Object):
        def getResourceId(self):
            # type: () -> ProjectResourceId
            pass

        def getResourceSignature(self):
            # type: () -> ResourceSignature
            pass

    class ManifestChangeOperation(Object):
        def getBaseHashCode(self):
            # type: () -> int
            pass

        def getManifest(self):
            # type: () -> ProjectManifest
            pass

        def getProjectName(self):
            # type: () -> AnyStr
            pass

    class ModifyResourceOperation(Object):
        def getBaseSignature(self):
            # type: () -> ResourceSignature
            pass

        def getResource(self):
            # type: () -> ProjectResource
            pass

        def getResourceId(self):
            # type: () -> ProjectResourceId
            pass

    class OperationType(Enum):
        @staticmethod
        def values():
            # type: () -> Iterable[ChangeOperation.OperationType]
            pass

    class ResourceChangeOperation(Object):
        def getProjectName(self):
            # type: () -> AnyStr
            pass

        def getResourceId(self):
            # type: () -> ProjectResourceId
            raise NotImplementedError


class ProjectManifest(Object):
    def __init__(
        self,
        title,  # type: AnyStr
        description,  # type: AnyStr
        enabled,  # type: bool
        inheritable,  # type: bool
        parent,  # type: AnyStr
    ):
        # type: (...) -> None
        super(ProjectManifest, self).__init__()
        print(title, description, enabled, inheritable, parent)
