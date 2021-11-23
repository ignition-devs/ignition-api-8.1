from __future__ import print_function, unicode_literals

__all__ = ["AlarmEvent", "PyAlarmEvent", "PyAlarmEventImpl"]

from java.lang import Iterable
from org.python.core import PyObject


class AlarmEvent(Iterable):
    def acknowledge(self, ackData):
        raise NotImplementedError

    def active(self, activeData):
        raise NotImplementedError

    def clear(self, clearData):
        raise NotImplementedError

    def getAckData(self):
        raise NotImplementedError

    def getActiveData(self):
        raise NotImplementedError

    def getClearedData(self):
        raise NotImplementedError

    def getDisplayPath(self):
        raise NotImplementedError

    def getId(self):
        raise NotImplementedError

    def getLabel(self):
        raise NotImplementedError

    def getLastEventState(self):
        raise NotImplementedError

    def getName(self):
        raise NotImplementedError

    def getNotes(self):
        raise NotImplementedError

    def getPriority(self):
        raise NotImplementedError

    def getSource(self):
        raise NotImplementedError

    def getState(self):
        raise NotImplementedError

    def isAcked(self):
        raise NotImplementedError

    def isCleared(self):
        raise NotImplementedError

    def isShelved(self):
        raise NotImplementedError

    def iterator(self):
        pass


class PyAlarmEvent(AlarmEvent):
    def acknowledge(self, ackData):
        pass

    def active(self, activeData):
        pass

    def clear(self, clearData):
        pass

    def contains(self, property):
        raise NotImplementedError

    def get(self, property):
        raise NotImplementedError

    def getAckData(self):
        pass

    def getActiveData(self):
        pass

    def getClearedData(self):
        pass

    def getDisplayPath(self):
        pass

    def getId(self):
        pass

    def getLabel(self):
        pass

    def getLastEventState(self):
        pass

    def getName(self):
        pass

    def getNotes(self):
        pass

    def getOrDefault(self, property):
        raise NotImplementedError

    def getOrElse(self, property, defaultValue):
        raise NotImplementedError

    def getPriority(self):
        pass

    def getSource(self):
        pass

    def getState(self):
        pass

    def isAcked(self):
        pass

    def isCleared(self):
        pass

    def isShelved(self):
        pass

    def set(self, property, value):
        raise NotImplementedError

    def setGlobal(self, property, value):
        raise NotImplementedError

    def sourceEvent(self):
        raise NotImplementedError


class PyAlarmEventImpl(PyAlarmEvent, PyObject):
    def __init__(self, event):
        print(event)
        super(PyAlarmEventImpl, self).__init__()

    def contains(self, property):
        pass

    def get(self, property):
        pass

    def getOrDefault(self, property):
        pass

    def getOrElse(self, property, defaultValue):
        pass

    def set(self, property, value):
        pass

    def setGlobal(self, property, value):
        pass

    def sourceEvent(self):
        pass
