__all__ = ["BasicQualifiedValue", "QualifiedValue", "Quality", "QualityCode"]

from enum import Enum
from typing import Any

from java.lang import Object
from java.util import Date


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


class Quality(object):
    """Needed for gateway network interop with v7, but otherwise not
    used."""

    def getDescription(self):
        pass

    def getLevel(self):
        pass

    def getName(self):
        pass

    def getQualityCode(self):
        pass

    def isGood(self):
        pass

    class Level(Enum):
        Bad = 512
        Good = 192
        Unknown = 256

        def values(self):
            pass


class QualityCode(Object):
    """QualityCode contains a 32-bit integer code and optionally a
    diagnostic string.
    """

    Bad = None  # type: QualityCode
    Bad_AccessDenied = None  # type: QualityCode
    Bad_AggregateNotFound = None  # type: QualityCode
    Bad_DatabaseNotConnected = None  # type: QualityCode
    Bad_Disabled = None  # type: QualityCode
    Bad_Failure = None  # type: QualityCode
    Bad_GatewayCommOff = None  # type: QualityCode
    Bad_LicenseExceeded = None  # type: QualityCode
    Bad_NotConnected = None  # type: QualityCode
    Bad_NotFound = None  # type: QualityCode
    Bad_OutOfRange = None  # type: QualityCode
    Bad_ReadOnly = None  # type: QualityCode
    Bad_Stale = None  # type: QualityCode
    Bad_ReferenceNotFound = None  # type: QualityCode
    Bad_TrialExpired = None  # type: QualityCode
    Bad_Unauthorized = None  # type: QualityCode
    Bad_Unsupported = None  # type: QualityCode
    Error = None  # type: QualityCode
    Error_Configuration = None  # type: QualityCode
    Error_CycleDetected = None  # type: QualityCode
    Error_DatabaseQuery = None  # type: QualityCode
    Error_Exception = None  # type: QualityCode
    Error_ExpressionEval = None  # type: QualityCode
    Error_Formatting = None  # type: QualityCode
    Error_InvalidPathSyntax = None  # type: QualityCode
    Error_IO = None  # type: QualityCode
    Error_ScriptEval = None  # type: QualityCode
    Error_TagExecution = None  # type: QualityCode
    Error_TimeoutExpired = None  # type: QualityCode
    Error_TypeConversion = None  # type: QualityCode
    Good = None  # type: QualityCode
    Good_Backfill = None  # type: QualityCode
    Good_Initial = None  # type: QualityCode
    Good_Overload = None  # type: QualityCode
    Good_Provisional = None  # type: QualityCode
    Good_Unspecified = None  # type: QualityCode
    Good_WritePending = None  # type: QualityCode
    Uncertain = None  # type: QualityCode
    Uncertain_LastKnownValue = None  # type: QualityCode
    Uncertain_InitialValue = None  # type: QualityCode
    Uncertain_DataSubNormal = None  # type: QualityCode
    Uncertain_EngineeringUnitsExceeded = None  # type: QualityCode
    Uncertain_IncompleteOperation = None  # type: QualityCode

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


class BasicQualifiedValue(QualifiedValue, Object):
    """The basic implementation of QualifiedValue."""

    quality = QualityCode.Bad_Stale  # type: QualityCode
    timestamp = Date()  # type: Date
    value = None  # type: Any

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
