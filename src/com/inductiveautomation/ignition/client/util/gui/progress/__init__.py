__all__ = ["AsyncClientTask", "ClientProgressManager", "TaskHandle"]

from typing import Any, List, Optional

from com.inductiveautomation.ignition.common.gui.progress import (
    TaskProgressListener,
    TaskProgressState,
)
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from java.util.concurrent import CompletableFuture
from java.util.function import Consumer


class AsyncClientTask(object):
    def canCancel(self):
        # type: () -> bool
        raise NotImplementedError

    def getTaskTitle(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def run(self, progressListener):
        # type: (TaskProgressListener) -> None
        raise NotImplementedError


class TaskHandle(object):
    def cancel(self):
        # type: () -> None
        raise NotImplementedError

    def getUid(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def waitForResult(self, timeout):
        # type: (int) -> Object
        raise NotImplementedError


class ClientProgressManager(Object):
    def addListener(self, listener):
        # type: (ClientProgressManager.ModelListener) -> None
        pass

    def cancelAllTasks(self):
        # type: () -> None
        pass

    def cancelTask(self, uid):
        # type: (AnyStr) -> None
        pass

    @staticmethod
    def getInstance():
        # type: () -> ClientProgressManager
        pass

    def getStates(self):
        # type: () -> List[TaskProgressState]
        pass

    def registerGatewayTask(self, taskId):
        # type: (AnyStr) -> TaskHandle
        pass

    def removeListener(self, listener):
        # type: (ClientProgressManager.ModelListener) -> None
        pass

    def run(self, cf, handler, owner):
        # type: (CompletableFuture, Consumer, Object) -> None
        pass

    def runTask(self, task, dominant=None):
        # type: (AsyncClientTask, Optional[bool]) -> TaskHandle
        pass

    def setClientContext(self, context):
        # type: (Any) -> None
        pass

    def setUIPaused(self, value):
        # type: (bool) -> None
        pass

    def shutdown(self):
        # type: () -> None
        pass

    def startup(self):
        # type: () -> None
        pass

    class ModelListener(object):
        def progressModelChanged(self):
            # type: () -> None
            raise NotImplementedError
