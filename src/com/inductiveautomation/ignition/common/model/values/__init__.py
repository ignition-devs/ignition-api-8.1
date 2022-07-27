__all__ = ["BasicQualifiedValue", "QualifiedValue", "Quality", "QualityCode"]

from enum import Enum
from typing import Any, Optional, Union

from java.lang import Object, String
from java.util import Date


class QualifiedValue(object):
    """Represents a value with a DataQuality & timestamp attached to
    it.
    """

    def derive(self, arg=None):
        # type: (Union[None, QualityCode, String]) -> QualifiedValue
        raise NotImplementedError

    def getQuality(self):
        # type: () -> QualityCode
        raise NotImplementedError

    def getTimestamp(self):
        # type: () -> Date
        raise NotImplementedError

    def getValue(self):
        # type: () -> Object
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
        # type: (Any) -> None
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
        # type: () -> bool
        pass

    def isBadOrError(self):
        # type: () -> bool
        pass

    def isError(self):
        # type: () -> bool
        pass

    def isGood(self):
        # type: () -> bool
        pass

    def isNotGood(self):
        # type: () -> bool
        pass

    def isUncertain(self):
        # type: () -> bool
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

    _quality = QualityCode.Bad_Stale  # type: QualityCode
    _timestamp = Date()  # type: Date
    _value = None  # type: Object

    def __init__(self, *args):
        # type: (Any) -> None
        pass

    def clone(self):
        # type: () -> BasicQualifiedValue
        pass

    def derive(self, arg=None):
        # type: (Union[None, QualityCode, String]) -> QualifiedValue
        pass

    @staticmethod
    def fromObject(obj):
        # type: (Object) -> QualifiedValue
        pass

    def getQuality(self):
        # type: () -> QualityCode
        return self._quality

    def getTimestamp(self):
        # type: () -> Date
        return self._timestamp

    def getValue(self):
        # type: () -> Object
        return self._value

    def setQuality(self, code):
        # type: (QualityCode) -> None
        self._quality = code

    def setTimestamp(self, timestamp):
        # type: (Date) -> None
        self._timestamp = timestamp

    def setValue(self, value):
        # type: (Object) -> None
        self._value = value

    @staticmethod
    def unwrap(obj):
        # type: (Object) -> Object
        pass

    @staticmethod
    def updateTimestamp(copy):
        # type: (QualifiedValue) -> QualifiedValue
        pass

    @staticmethod
    def valueOf(obj):
        # type: (Object) -> Object
        pass
