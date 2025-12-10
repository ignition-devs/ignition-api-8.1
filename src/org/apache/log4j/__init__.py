__all__ = ["Appender", "Category", "Layout", "Level", "Logger", "Priority"]

from typing import Any, Optional, Union

from java.lang import Object, Throwable
from java.util import Enumeration

from org.apache.log4j.spi import ErrorHandler, Filter, LoggerRepository, LoggingEvent


class Appender(object):
    def addFilter(self, newFilter):
        # type: (Filter) -> None
        raise NotImplementedError

    def clearFilters(self):
        # type: () -> None
        raise NotImplementedError

    def close(self):
        # type: () -> None
        raise NotImplementedError

    def doAppend(self, event):
        # type: (LoggingEvent) -> None
        raise NotImplementedError

    def getErrorHandler(self):
        # type: () -> ErrorHandler
        raise NotImplementedError

    def getFilter(self):
        # type: () -> Filter
        raise NotImplementedError

    def getLayout(self):
        # type: () -> Layout
        raise NotImplementedError

    def getName(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def requiresLayout(self):
        # type: () -> bool
        raise NotImplementedError

    def setErrorHandler(self, errorHandler):
        # type: (ErrorHandler) -> None
        raise NotImplementedError

    def setLayout(self, layout):
        # type: (Layout) -> None
        raise NotImplementedError

    def setName(self, name):
        # type: (Union[str, unicode]) -> None
        raise NotImplementedError


class Category(Object):
    def addApender(self, newAppender):
        # type: (Appender) -> None
        pass

    def assertLog(self, assertion, msg):
        # type: (bool, Union[str, unicode]) -> None
        pass

    def callAppenders(self, event):
        # type: (LoggingEvent) -> None
        pass

    def debug(self, message, t=None):
        # type: (Union[str, unicode], Optional[Throwable]) -> None
        pass

    def error(self, message, t=None):
        # type: (Union[str, unicode], Optional[Throwable]) -> None
        pass

    def fatal(self, message, t=None):
        # type: (Union[str, unicode], Optional[Throwable]) -> None
        pass

    def getAdditivity(self):
        # type: () -> bool
        return True

    def getAllAppenders(self):
        # type: () -> Enumeration
        pass

    def getAppender(self, name):
        # type: (Union[str, unicode]) -> Appender
        pass

    def getLevel(self):
        # type: () -> Level
        pass

    def getLoggerRepository(self):
        # type: () -> LoggerRepository
        pass

    def info(self, message, t=None):
        # type: (Union[str, unicode], Optional[Throwable]) -> None
        pass

    def warn(self, message, t=None):
        # type: (Union[str, unicode], Optional[Throwable]) -> None
        pass


class Layout(Object):
    def __init__(self):
        # type: () -> None
        super(Layout, self).__init__()

    def format(self, event):
        # type: (LoggingEvent) -> Union[str, unicode]
        raise NotImplementedError

    def getContentType(self):
        # type: () -> Union[str, unicode]
        pass

    def getFooter(self):
        # type: () -> Union[str, unicode]
        pass

    def getHeader(self):
        # type: () -> Union[str, unicode]
        pass

    def ignoresThrowable(self):
        # type: () -> bool
        raise NotImplementedError


class Priority(Object):
    def getSyslogEquivalent(self):
        # type: () -> int
        pass

    def isGreaterOrEqual(self, r):
        # type: (Priority) -> bool
        return True

    def toInt(self):
        # type: () -> int
        pass


class Level(Priority):
    @staticmethod
    def toLevel(*args):
        # type: (*Any) -> Level
        pass


class Logger(Category):
    @staticmethod
    def getLogger(*args):
        # type: (*Any) -> Logger
        pass

    def isTraceEnabled(self):
        # type: () -> bool
        return True

    def trace(self, message, t=None):
        # type: (Union[str, unicode], Optional[Throwable]) -> None
        pass
