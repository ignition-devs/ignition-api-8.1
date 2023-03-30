from __future__ import print_function

__all__ = ["AlarmEvent", "EventData", "PyAlarmEvent", "PyAlarmEventImpl"]

from typing import Any, Iterator

from com.inductiveautomation.ignition.common import QualifiedPath, StringPath
from com.inductiveautomation.ignition.common.config import BasicPropertySet
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from java.util import UUID
from org.python.core import PyObject


class AlarmEvent(object):
    def __iter__(self):
        # type: () -> Iterator[Any]
        raise NotImplementedError

    def acknowledge(self, ackData):
        # type: (EventData) -> None
        raise NotImplementedError

    def active(self, activeData):
        # type: (EventData) -> None
        raise NotImplementedError

    def clear(self, clearData):
        # type: (EventData) -> None
        raise NotImplementedError

    def getAckData(self):
        # type: () -> EventData
        raise NotImplementedError

    def getActiveData(self):
        # type: () -> EventData
        raise NotImplementedError

    def getClearedData(self):
        # type: () -> EventData
        raise NotImplementedError

    def getDisplayPath(self):
        # type: () -> StringPath
        raise NotImplementedError

    def getDisplayPathOrSource(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getId(self):
        # type: () -> UUID
        raise NotImplementedError

    def getLabel(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getLastEventState(self):
        # type: () -> Any
        raise NotImplementedError

    def getName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getNotes(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getPriority(self):
        # type: () -> Any
        raise NotImplementedError

    def getSource(self):
        # type: () -> QualifiedPath
        raise NotImplementedError

    def getState(self):
        # type: () -> Any
        raise NotImplementedError

    def isAcked(self):
        # type: () -> bool
        raise NotImplementedError

    def isCleared(self):
        # type: () -> bool
        raise NotImplementedError

    def isShelved(self):
        # type: () -> bool
        raise NotImplementedError

    def iterator(self):
        # type: () -> Any
        pass


class EventData(BasicPropertySet):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(EventData, self).__init__(*args)

    def getTimeStamp(self):
        # type: () -> long
        pass


class PyAlarmEvent(AlarmEvent):
    def __iter__(self):
        # type: () -> Iterator[Any]
        pass

    def acknowledge(self, ackData):
        # type: (EventData) -> None
        pass

    def active(self, activeData):
        # type: (EventData) -> None
        pass

    def clear(self, clearData):
        # type: (EventData) -> None
        pass

    def contains(self, property):
        # type: (AnyStr) -> bool
        raise NotImplementedError

    def get(self, property):
        # type: (AnyStr) -> Object
        raise NotImplementedError

    def getAckData(self):
        # type: () -> EventData
        pass

    def getActiveData(self):
        # type: () -> EventData
        pass

    def getClearedData(self):
        # type: () -> EventData
        pass

    def getDisplayPath(self):
        # type: () -> StringPath
        pass

    def getDisplayPathOrSource(self):
        # type: () -> AnyStr
        pass

    def getId(self):
        # type: () -> UUID
        pass

    def getLabel(self):
        # type: () -> AnyStr
        pass

    def getLastEventState(self):
        # type: () -> Any
        pass

    def getName(self):
        # type: () -> AnyStr
        pass

    def getNotes(self):
        # type: () -> AnyStr
        pass

    def getOrDefault(self, property):
        # type: (AnyStr) -> Object
        raise NotImplementedError

    def getOrElse(self, property, defaultValue):
        # type: (AnyStr, Object) -> Object
        raise NotImplementedError

    def getPriority(self):
        # type: () -> Any
        pass

    def getSource(self):
        # type: () -> QualifiedPath
        pass

    def getState(self):
        # type: () -> Any
        pass

    def isAcked(self):
        # type: () -> bool
        pass

    def isCleared(self):
        # type: () -> bool
        pass

    def isShelved(self):
        # type: () -> bool
        pass

    def set(self, property, value):
        # type: (AnyStr, Object) -> None
        raise NotImplementedError

    def setGlobal(self, property, value):
        # type: (AnyStr, Object) -> None
        raise NotImplementedError

    def sourceEvent(self):
        # type: () -> AlarmEvent
        raise NotImplementedError


class PyAlarmEventImpl(PyAlarmEvent, PyObject):
    def __init__(self, event):
        # type: (AlarmEvent) -> None
        print(event)
        super(PyAlarmEventImpl, self).__init__()

    def contains(self, property):
        # type: (AnyStr) -> bool
        pass

    def get(self, property):
        # type: (AnyStr) -> Object
        pass

    def getOrDefault(self, property):
        # type: (AnyStr) -> Object
        pass

    def getOrElse(self, property, defaultValue):
        # type: (AnyStr, Object) -> Object
        pass

    def set(self, property, value):
        # type: (AnyStr, Object) -> None
        pass

    def setGlobal(self, property, value):
        # type: (AnyStr, Object) -> None
        pass

    def sourceEvent(self):
        # type: () -> AlarmEvent
        pass
