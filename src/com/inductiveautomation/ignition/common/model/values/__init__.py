__all__ = ["BasicQualifiedValue", "QualityCode", "QualifiedValue"]

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


class QualifiedValue(object):
    """Represents a value with a DataQuality & timestamp attached to
    it.
    """

    def getQuality(self):
        raise NotImplementedError

    def getTimestamp(self):
        raise NotImplementedError

    def getValue(self):
        raise NotImplementedError


class BasicQualifiedValue(QualifiedValue):
    def getQuality(self):
        pass

    def getTimestamp(self):
        pass

    def getValue(self):
        pass
