from __future__ import print_function

__all__ = [
    "ErrorHandler",
    "Filter",
    "HierarchyEventListener",
    "LoggerFactory",
    "LoggerRepository",
    "LoggingEvent",
    "OptionHandler",
]

from typing import Any, Optional

from dev.thecesrom.helper.types import AnyStr
from java.lang import Exception, Object
from java.util import Enumeration


class OptionHandler(object):
    def activateOptions(self):
        # type: () -> None
        raise NotImplementedError


class ErrorHandler(OptionHandler):
    def activateOptions(self):
        # type: () -> None
        raise NotImplementedError

    def error(
        self,
        message,  # type: AnyStr
        e=None,  # type: Optional[Exception]
        errorCode=None,  # type: Optional[int]
        event=None,  # type: Optional[LoggingEvent]
    ):
        # type: (...) -> None
        raise NotImplementedError

    def setAppender(self, appender):
        # type: (Any) -> None
        raise NotImplementedError

    def setBackupAppender(self, appender):
        # type: (Any) -> None
        raise NotImplementedError

    def setLogger(self, logger):
        # type: (Any) -> None
        raise NotImplementedError


class HierarchyEventListener(object):
    def addAppenderEvent(self, cat, appender):
        # type: (Any, Any) -> None
        raise NotImplementedError

    def removeAppenderEvent(self, cat, appender):
        # type: (Any, Any) -> None
        raise NotImplementedError


class LoggerFactory(object):
    def makeNewLoggerInstance(self, name):
        # type: (AnyStr) -> Any
        raise NotImplementedError


class LoggerRepository(object):
    def addHierarchyEventListener(self, listener):
        # type: (HierarchyEventListener) -> None
        raise NotImplementedError

    def emitNoAppenderWarning(self, cat):
        # type: (Any) -> None
        raise NotImplementedError

    def exists(self, name):
        # type: (AnyStr) -> Any
        raise NotImplementedError

    def fireAddAppenderEvent(self, logger, appender):
        # type: (Any, Any) -> None
        raise NotImplementedError

    def getCurrentLoggers(self):
        # type: () -> Enumeration
        raise NotImplementedError

    def getLogger(self, name, factory=None):
        # type: (AnyStr, Optional[LoggerFactory]) -> Any
        raise NotImplementedError

    def getRootLogger(self):
        # type: () -> Any
        raise NotImplementedError

    def getThreshold(self):
        # type: () -> Any
        raise NotImplementedError

    def isDisabled(self, level):
        # type: (int) -> bool
        raise NotImplementedError

    def resetConfiguration(self):
        # type: () -> None
        raise NotImplementedError

    def setThreshold(self, arg):
        # type: (Any) -> None
        raise NotImplementedError

    def shutdown(self):
        # type: () -> None
        raise NotImplementedError


class Filter(Object, OptionHandler):
    def activateOptions(self):
        # type: () -> None
        pass

    def decide(self, event):
        # type: (LoggingEvent) -> int
        raise NotImplementedError

    def getNext(self):
        # type: () -> Filter
        pass

    def setNext(self, next):
        # type: (Filter) -> None
        pass


class LoggingEvent(Object):
    categoryName = None  # type: AnyStr
    fqnOfCategoryClass = None  # type: AnyStr
    level = None  # type: Any
    timeStamp = None  # type: long

    def __init__(self, *args):
        # type: (*Any) -> None
        super(LoggingEvent, self).__init__()
        print(args)
