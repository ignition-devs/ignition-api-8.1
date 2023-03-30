from __future__ import print_function

__all__ = ["LoggerEx", "Platform", "Timeline", "TimelineList"]

from typing import Any, Iterable, List, Optional, Union

from dev.thecesrom.helper.types import AnyStr
from java.io import Closeable
from java.lang import AutoCloseable, Class, Comparable, Enum, Object, Throwable
from java.util import Date
from org.apache.commons.lang3.builder import ToStringStyle
from org.slf4j import Logger


class LoggerEx(Object):
    """This class is a wrapper around a logger which provides additional
    useful tools.

    To create one, use the newBuilder() function and configure the
    builder.
    """

    DEFAULT_TO_STRING_STYLE = None  # type: ToStringStyle

    def createSubLogger(self, arg):
        # type: (Union[Class, AnyStr]) -> LoggerEx
        pass

    def debug(self, message, t=None):
        # type: (AnyStr, Optional[Throwable]) -> None
        pass

    def debugDuration(self, message):
        # type: (AnyStr) -> Closeable
        pass

    def debugEvent(self, message, *args):
        # type: (AnyStr, Any) -> None
        pass

    def debugf(self, message, *args):
        # type: (AnyStr, Any) -> None
        pass

    def error(self, message, t=None):
        # type: (AnyStr, Optional[Throwable]) -> None
        pass

    def errorEvent(self, message, *args):
        # type: (AnyStr, Any) -> None
        pass

    def errorf(self, message, *args):
        # type: (AnyStr, Any) -> None
        pass

    def fatal(self, message, t=None):
        # type: (AnyStr, Optional[Throwable]) -> None
        pass

    def getIdentObject(self):
        # type: () -> Object
        pass

    def getLoggerSLF4J(self):
        # type: () -> Logger
        pass

    def getName(self):
        # type: () -> AnyStr
        pass

    def getToStringStyle(self):
        # type: () -> ToStringStyle
        pass

    def info(self, message, t=None):
        # type: (AnyStr, Optional[Throwable]) -> None
        pass

    def infoDuration(self, message):
        # type: (AnyStr) -> Closeable
        pass

    def infoEvent(self, message, *args):
        # type: (AnyStr, Any) -> None
        pass

    def infof(self, message, *args):
        # type: (AnyStr, Any) -> None
        pass

    def isDebugEnabled(self):
        # type: () -> bool
        return True

    def isIdentObjectEnabled(self):
        # type: () -> bool
        return True

    def isInfoEnabled(self):
        # type: () -> bool
        return True

    def isTraceEnabled(self):
        # type: () -> bool
        return True

    def mdcClose(self):
        # type: () -> None
        pass

    def mdcPut(self, key, value):
        # type: (AnyStr, AnyStr) -> None
        pass

    def mdcPutCloseable(self, key, value):
        # type: (AnyStr, AnyStr) -> LoggerEx.MDCCloseable
        pass

    def mdcRemove(self, key):
        # type: (AnyStr) -> None
        pass

    def mdcSet(self):
        # type: () -> LoggerEx.MDCCloseable
        pass

    @staticmethod
    def newBuilder():
        # type: () -> LoggerEx.Builder
        pass

    def setIdentObject(self, identObj):
        # type: (Object) -> None
        pass

    def setToStringStyle(self, toStringStyle):
        # type: (ToStringStyle) -> None
        pass

    def trace(self, message, t=None):
        # type: (AnyStr, Optional[Throwable]) -> None
        pass

    def traceDuration(self, message):
        # type: (AnyStr) -> Closeable
        pass

    def traceEvent(self, message, *args):
        # type: (AnyStr, Any) -> None
        pass

    def tracef(self, message, *args):
        # type: (AnyStr, Any) -> None
        pass

    def warn(self, message, t=None):
        # type: (AnyStr, Optional[Throwable]) -> None
        pass

    def warnEvent(self, message, *args):
        # type: (AnyStr, Any) -> None
        pass

    def warnf(self, message, *args):
        # type: (AnyStr, Any) -> None
        pass

    class Builder(Object):
        def build(self, *args):
            # type: (*Any) -> LoggerEx
            pass

        def eventSystem(self, systemId):
            # type: (str) -> LoggerEx.Builder
            pass

        def identObject(self, identObj):
            # type: (Object) -> LoggerEx.Builder
            pass

        def mdcContext(self, *args):
            # type: (Object) -> LoggerEx.Builder
            pass

        def mutableIdentObject(self, identObj):
            # type: (Object) -> LoggerEx.Builder
            pass

    class MDCCloseable(Object, AutoCloseable):
        def close(self):
            # type: () -> None
            pass


class Platform(Object):
    LINUX_AARCH64 = None  # type: Platform
    LINUX_ARM = None  # type: Platform
    LINUX_X64 = None  # type: Platform
    LINUX_X86 = None  # type: Platform
    OSX_X64 = None  # type: Platform
    OSX_X86 = None  # type: Platform
    WINDOWS_X64 = None  # type: Platform
    WINDOWS_X86 = None  # type: Platform

    def __init__(
        self,
        operatingSystem,  # type: Platform.OperatingSystem
        architecture,  # type: Platform.Architecture
    ):
        # type: (...) -> None
        super(Platform, self).__init__()
        self._operatingSystem = operatingSystem
        self._architecture = architecture

    def getArchitecture(self):
        # type: () -> Platform.Architecture
        return self._architecture

    @staticmethod
    def getCurrent():
        # type: () -> Platform
        pass

    def getOperatingSystem(self):
        # type: () -> Platform.OperatingSystem
        return self._operatingSystem

    class Architecture(Enum):
        @staticmethod
        def fromString(s):
            # type: (AnyStr) -> Platform.Architecture
            pass

        def getSignatures(self):
            # type: () -> Iterable[AnyStr]
            pass

        @staticmethod
        def values():
            # type: () -> Iterable[Platform.Architecture]
            pass

    class OperatingSystem(Enum):
        @staticmethod
        def fromString(s):
            # type: (AnyStr) -> Platform.OperatingSystem
            pass

        def getSignatures(self):
            # type: () -> Iterable[AnyStr]
            pass

        @staticmethod
        def values():
            # type: () -> Iterable[Platform.OperatingSystem]
            pass


class TimelineList(Object):
    def __init__(self):
        # type: () -> None
        super(TimelineList, self).__init__()

    def add(self, *args):
        # type: (*Any) -> None
        pass

    def covered(self, time):
        # type: (long) -> bool
        pass

    def get(self, time):
        # type: (long) -> Any
        pass

    def getClosest(self, time):
        # type: (long) -> Any
        pass

    def getSegment(self, *args):
        # type: (*Any) -> TimelineList.TimeSegment
        pass

    def getSegments(self, *args):
        # type: (*Any) -> List[TimelineList.TimeSegment]
        pass

    def mergeSegments(self):
        # type: () -> None
        pass

    def nextEvent(self, time, allowRollover=None):
        # type: (long, Optional[bool]) -> bool
        pass

    def size(self):
        # type: () -> int
        pass

    def sort(self):
        # type: () -> None
        pass

    class TimeSegment(Object, Comparable):
        def __init__(self, *args):
            # type: (*Any) -> None
            super(TimelineList.TimeSegment, self).__init__()
            print(args)

        def compareTo(self, o):
            # type: (Any) -> int
            pass

        def contains(self, time):
            # type: (long) -> bool
            pass

        def endsBefore(self, time):
            # type: (long) -> bool
            pass

        def getDuration(self):
            # type: () -> long
            pass

        def getEnd(self):
            # type: () -> long
            pass

        def getStart(self):
            # type: () -> long
            pass

        def getValue(self):
            # type: () -> Any
            pass

        def setEnd(self, end):
            # type: (long) -> None
            pass

        def setStart(self, start):
            # type: (long) -> None
            pass

        def setStartAfter(self, start):
            # type: (long) -> None
            pass


class Timeline(TimelineList):
    def __init__(self, style=None):
        # type: (Optional[Timeline.TimelineStyle]) -> None
        super(Timeline, self).__init__()
        self._style = style

    def addSegment(self, start, end):
        # type: (long, long) -> None
        pass

    @staticmethod
    def createParser(style):
        # type: (Timeline.TimelineStyle) -> Timeline.TimelineParser
        pass

    def getStyle(self):
        # type: () -> Timeline.TimelineStyle
        pass

    def invert(self):
        # type: () -> Timeline
        pass

    class TimelineParser(object):
        def parse(self, input):
            # type: (AnyStr) -> Timeline
            raise NotImplementedError

    class TimelineStyle(Enum):
        def toDateForStyle(self, value):
            # type: (long) -> Date
            pass

        def toLongForStyle(self, dateMillis):
            # type: (Union[Date, long]) -> long
            pass

        @staticmethod
        def values():
            # type: () -> Iterable[Timeline.TimelineStyle]
            pass
