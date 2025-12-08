from __future__ import print_function

__all__ = ["AlarmEvent", "EventData", "PyAlarmEvent", "PyAlarmEventImpl"]

from typing import Any, Iterator, Union

from java.lang import Object
from java.util import UUID

from com.inductiveautomation.ignition.common import QualifiedPath, StringPath
from com.inductiveautomation.ignition.common.config import BasicPropertySet
from org.python.core import PyObject


class AlarmEvent(object):

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
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getId(self):
        # type: () -> UUID
        raise NotImplementedError

    def getLabel(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getLastEventState(self):
        # type: () -> Any
        raise NotImplementedError

    def getName(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getNotes(self):
        # type: () -> Union[str, unicode]
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

    def __iter__(self):
        # type: () -> Iterator[Any]
        raise NotImplementedError


class EventData(BasicPropertySet):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(EventData, self).__init__(*args)

    def getTimeStamp(self):
        # type: () -> long
        pass


class PyAlarmEvent(AlarmEvent):

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
        # type: (Union[str, unicode]) -> bool
        raise NotImplementedError

    def get(self, property):
        # type: (Union[str, unicode]) -> Object
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
        # type: () -> Union[str, unicode]
        pass

    def getId(self):
        # type: () -> UUID
        pass

    def getLabel(self):
        # type: () -> Union[str, unicode]
        pass

    def getLastEventState(self):
        # type: () -> Any
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        pass

    def getNotes(self):
        # type: () -> Union[str, unicode]
        pass

    def getOrDefault(self, property):
        # type: (Union[str, unicode]) -> Object
        raise NotImplementedError

    def getOrElse(self, property, defaultValue):
        # type: (Union[str, unicode], Object) -> Object
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
        return True

    def isCleared(self):
        # type: () -> bool
        return True

    def isShelved(self):
        # type: () -> bool
        return True

    def set(self, property, value):
        # type: (Union[str, unicode], Object) -> None
        raise NotImplementedError

    def setGlobal(self, property, value):
        # type: (Union[str, unicode], Object) -> None
        raise NotImplementedError

    def sourceEvent(self):
        # type: () -> AlarmEvent
        raise NotImplementedError

    def __iter__(self):
        # type: () -> Iterator[Any]
        pass


class PyAlarmEventImpl(PyAlarmEvent, PyObject):
    def __init__(self, event):
        # type: (AlarmEvent) -> None
        print(event)
        super(PyAlarmEventImpl, self).__init__()

    def contains(self, property):
        # type: (Union[str, unicode]) -> bool
        return True

    def get(self, property):
        # type: (Union[str, unicode]) -> Object
        pass

    def getOrDefault(self, property):
        # type: (Union[str, unicode]) -> Object
        pass

    def getOrElse(self, property, defaultValue):
        # type: (Union[str, unicode], Object) -> Object
        pass

    def set(self, property, value):
        # type: (Union[str, unicode], Object) -> None
        pass

    def setGlobal(self, property, value):
        # type: (Union[str, unicode], Object) -> None
        pass

    def sourceEvent(self):
        # type: () -> AlarmEvent
        pass
