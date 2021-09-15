__all__ = ["QualityCode", "QualifiedValue", "Quality"]

from abc import ABCMeta, abstractmethod

from java.lang import Object


class QualityCode(Object):
    """QualityCode contains a 32-bit integer code and optionally a
    diagnostic string.
    """

    def __init__(self, *args):
        pass

    def derive(self, diagnosticMessage):
        pass

    def getCode(self):
        pass

    def getDiagnosticMessage(self):
        pass

    def getLevel(self):
        pass

    def getName(self):
        pass

    def isBad(self):
        pass

    def isBadOrError(self):
        pass

    def isError(self):
        pass

    def isGood(self):
        pass

    def isNotGood(self):
        pass

    def isUncertain(self):
        pass

    class Level(Object):
        def __init__(self):
            pass

        def code(self, userCode):
            pass

        @staticmethod
        def valueOf(name):
            pass

        @staticmethod
        def values():
            pass


class QualifiedValue(ABCMeta):
    """Represents a value with a DataQuality & timestamp attached to
    it.
    """

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def getQuality(self):
        pass

    @abstractmethod
    def getTimestamp(self):
        pass

    @abstractmethod
    def getValue(self):
        pass


class Quality(ABCMeta):
    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def getDescription(self):
        pass

    def getLevel(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    def getQualityCode(self):
        pass

    def isGood(self):
        pass
