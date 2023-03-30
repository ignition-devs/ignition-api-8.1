from __future__ import print_function

__all__ = ["Annotation", "AnnotationType"]

from typing import Any, Union

from com.inductiveautomation.ignition.common import QualifiedPath
from com.inductiveautomation.ignition.common.gson import JsonElement
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from java.util import Date


class Annotation(Object):
    def __init__(self):
        # type: () -> None
        super(Annotation, self).__init__()

    def clone(self):
        # type: () -> Annotation
        pass

    def delete(self):
        # type: () -> None
        pass

    @staticmethod
    def fromJson(json):
        # type: (JsonElement) -> Annotation
        pass

    def getData(self):
        # type: () -> AnyStr
        pass

    def getLastUpdated(self):
        # type: () -> Date
        pass

    def getPath(self):
        # type: () -> QualifiedPath
        pass

    def getRangeEnd(self):
        # type: () -> Date
        pass

    def getRangeStart(self):
        # type: () -> Date
        pass

    def getStorageId(self):
        # type: () -> Any
        pass

    def getType(self):
        # type: () -> AnyStr
        pass

    def hasStorageId(self):
        # type: () -> bool
        pass

    def isDeleted(self):
        # type: () -> bool
        pass

    def isUpdated(self):
        # type: () -> bool
        pass

    @staticmethod
    def newBuilder():
        # type: () -> Annotation.Builder
        pass

    @staticmethod
    def newDelete(storageId):
        # type: (Any) -> Annotation
        pass

    def toJson(self):
        # type: () -> AnyStr
        pass

    def updatePath(self, path):
        # type: (QualifiedPath) -> None
        pass

    class Builder(Object):
        def build(self):
            # type: () -> Annotation
            pass

        def copy(self, ann):
            # type: (Annotation) -> Annotation.Builder
            pass

        def data(self, value):
            # type: (AnyStr) -> Annotation.Builder
            pass

        def delete(self):
            # type: () -> Annotation.Builder
            pass

        def end(self, time):
            # type: (Date) -> Annotation.Builder
            pass

        def lastUpdated(self, time):
            # type: (Date) -> Annotation.Builder
            pass

        def path(self, path):
            # type: (QualifiedPath) -> Annotation.Builder
            pass

        def start(self, time):
            # type: (Date) -> Annotation.Builder
            pass

        def storageId(self, id_):
            # type: (Any) -> Annotation.Builder
            pass

        def time(self, time):
            # type: (Date) -> Annotation.Builder
            pass

        def type(
            self,
            arg,  # type: Union[AnnotationType, AnyStr]
        ):
            # type: (...) -> Annotation.Builder
            pass


class AnnotationType(Object):
    def __init__(self, type_, isRange):
        # type: (AnyStr, bool) -> None
        super(AnnotationType, self).__init__()
        print(type_, isRange)
