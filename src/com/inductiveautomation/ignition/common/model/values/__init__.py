__all__ = ["BasicQualifiedValue", "QualityCode", "QualifiedValue"]

from java.lang import Object
from java.util import Date


class QualityCode(Object):
    """QualityCode contains a 32-bit integer code and optionally a
    diagnostic string.
    """

    Bad = None
    Bad_AccessDenied = None
    Bad_AggregateNotFound = None
    Bad_DatabaseNotConnected = None
    Bad_Disabled = None
    Bad_Failure = None
    Bad_GatewayCommOff = None
    Bad_LicenseExceeded = None
    Bad_NotConnected = None
    Bad_NotFound = None
    Bad_OutOfRange = 524
    Bad_ReadOnly = None
    Bad_Stale = None
    Bad_ReferenceNotFound = None
    Bad_TrialExpired = None
    Bad_Unauthorized = None
    Bad_Unsupported = None
    Error = None
    Error_Configuration = None
    Error_CycleDetected = None
    Error_DatabaseQuery = None
    Error_Exception = None
    Error_ExpressionEval = None
    Error_Formatting = None
    Error_InvalidPathSyntax = None
    Error_IO = None
    Error_ScriptEval = None
    Error_TagExecution = None
    Error_TimeoutExpired = None
    Error_TypeConversion = None
    Good = None
    Good_Backfill = None
    Good_Initial = None
    Good_Overload = None
    Good_Provisional = None
    Good_Unspecified = None
    Good_WritePending = None
    Uncertain = None
    Uncertain_LastKnownValue = None
    Uncertain_InitialValue = None
    Uncertain_DataSubNormal = None
    Uncertain_EngineeringUnitsExceeded = None
    Uncertain_IncompleteOperation = None

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


class BasicQualifiedValue(QualifiedValue, Object):
    """The basic implementation of QualifiedValue."""

    quality = QualityCode.Bad_Stale
    timestamp = Date()
    value = None

    def __init__(self, *arg):
        pass

    @staticmethod
    def fromObject(obj):
        pass

    def getQuality(self):
        return self.quality

    def getTimestamp(self):
        return self.timestamp

    def getValue(self):
        return self.value

    def setQuality(self, code):
        self.quality = code

    def setTimestamp(self, timestamp):
        self.timestamp = timestamp

    def setValue(self, value):
        self.value = value

    @staticmethod
    def unwrap(obj):
        pass

    @staticmethod
    def updateTimestamp(copy):
        pass

    @staticmethod
    def valueOf(obj):
        pass
