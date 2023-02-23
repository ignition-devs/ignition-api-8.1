__all__ = ["LoggerEx"]

from typing import Any, Optional, Union

from dev.thecesrom.helper.types import AnyStr
from java.io import Closeable
from java.lang import AutoCloseable, Class, Object, Throwable
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
