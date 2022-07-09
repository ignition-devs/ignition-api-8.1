__all__ = ["LoggerEx"]

from typing import Any, Optional, Union

from java.io import Closeable
from java.lang import AutoCloseable, Class, Object, String, Throwable
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
        # type: (Union[Class, String]) -> LoggerEx
        pass

    def debug(self, message, t=None):
        # type: (String, Optional[Throwable]) -> None
        pass

    def debugDuration(self, message):
        # type: (String) -> Closeable
        pass

    def debugEvent(self, message, *args):
        # type: (String, Any) -> None
        pass

    def debugf(self, message, *args):
        # type: (String, Any) -> None
        pass

    def error(self, message, t=None):
        # type: (String, Optional[Throwable]) -> None
        pass

    def errorEvent(self, message, *args):
        # type: (String, Any) -> None
        pass

    def errorf(self, message, *args):
        # type: (String, Any) -> None
        pass

    def fatal(self, message, t=None):
        # type: (String, Optional[Throwable]) -> None
        pass

    def getIdentObject(self):
        # type: () -> Object
        pass

    def getLoggerSLF4J(self):
        # type: () -> Logger
        pass

    def getName(self):
        # type: () -> String
        pass

    def getToStringStyle(self):
        # type: () -> ToStringStyle
        pass

    def info(self, message, t=None):
        # type: (String, Optional[Throwable]) -> None
        pass

    def infoDuration(self, message):
        # type: (String) -> Closeable
        pass

    def infoEvent(self, message, *args):
        # type: (String, Any) -> None
        pass

    def infof(self, message, *args):
        # type: (String, Any) -> None
        pass

    def isDebugEnabled(self):
        # type: () -> bool
        pass

    def isIdentObjectEnabled(self):
        # type: () -> bool
        pass

    def isInfoEnabled(self):
        # type: () -> bool
        pass

    def isTraceEnabled(self):
        # type: () -> bool
        pass

    def mdcClose(self):
        # type: () -> None
        pass

    def mdcPut(self, key, value):
        # type: (String, String) -> None
        pass

    def mdcPutCloseable(self, key, value):
        # type: (String, String) -> LoggerEx.MDCCloseable
        pass

    def mdcRemove(self, key):
        # type: (String) -> None
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
        # type: (String, Optional[Throwable]) -> None
        pass

    def traceDuration(self, message):
        # type: (String) -> Closeable
        pass

    def traceEvent(self, message, *args):
        # type: (String, Any) -> None
        pass

    def tracef(self, message, *args):
        # type: (String, Any) -> None
        pass

    def warn(self, message, t=None):
        # type: (String, Optional[Throwable]) -> None
        pass

    def warnEvent(self, message, *args):
        # type: (String, Any) -> None
        pass

    def warnf(self, message, *args):
        # type: (String, Any) -> None
        pass

    class Builder(Object):
        def build(self, *args):
            # type: (Any) -> LoggerEx
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
