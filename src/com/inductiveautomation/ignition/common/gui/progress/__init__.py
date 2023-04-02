from __future__ import print_function

__all__ = ["ProgressListener", "TaskProgressListener", "TaskProgressState"]

from typing import Any

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object


class ProgressListener(object):
    def setIndeterminate(self, arg):
        # type: (bool) -> None
        raise NotImplementedError

    def setNote(self, note):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setProgress(self, val):
        # type: (int) -> None
        raise NotImplementedError

    def setProgressMax(self, max_):
        # type: (int) -> None
        raise NotImplementedError


class TaskProgressListener(ProgressListener):
    def isCanceled(self):
        # type: () -> bool
        raise NotImplementedError

    def setIndeterminate(self, arg):
        # type: (bool) -> None
        raise NotImplementedError

    def setNote(self, note):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setProgress(self, val):
        # type: (int) -> None
        raise NotImplementedError

    def setProgressMax(self, max_):
        # type: (int) -> None
        raise NotImplementedError


class TaskProgressState(Object, ProgressListener):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(TaskProgressState, self).__init__()
        print(args)

    def applyTo(self, listener):
        # type: (ProgressListener) -> None
        pass

    def getNote(self):
        # type: () -> AnyStr
        pass

    def getProgress(self):
        # type: () -> int
        pass

    def getProgressMax(self):
        # type: () -> int
        pass

    def getResult(self):
        # type: () -> Object
        pass

    def getTaskUID(self):
        # type: () -> AnyStr
        pass

    def isFinished(self):
        # type: () -> bool
        pass

    def isIndeterminant(self):
        # type: () -> bool
        pass

    def setFinished(self, finished):
        # type: (bool) -> None
        pass

    def setIndeterminate(self, arg):
        # type: (bool) -> None
        pass

    def setNote(self, note):
        # type: (AnyStr) -> None
        pass

    def setProgress(self, val):
        # type: (int) -> None
        pass

    def setProgressMax(self, max_):
        # type: (int) -> None
        pass

    def setResult(self, result):
        # type: (Object) -> None
        pass
