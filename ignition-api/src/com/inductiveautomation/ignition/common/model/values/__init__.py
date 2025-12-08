from __future__ import print_function

__all__ = ["BasicQualifiedValue", "QualifiedValue", "Quality", "QualityCode"]

from typing import Any, Iterable, Union

from java.lang import Enum, Object
from java.util import Date

from com.inductiveautomation.ignition.common.gson import JsonObject


class QualifiedValue(object):
    """Represents a value with a DataQuality & timestamp attached to
    it.
    """

    def derive(
        self,
        arg=None,  # type: Union[str, unicode, None, QualityCode]
    ):
        # type: (...) -> QualifiedValue
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
    used.
    """

    class Level(Enum):
        Bad = 512
        Good = 192
        Unknown = 256

        @staticmethod
        def values():
            # type: () -> Iterable[Quality.Level]
            pass

    def getDescription(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getLevel(self):
        # type: () -> Quality.Level
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getQualityCode(self):
        # type: () -> QualityCode
        pass

    def isGood(self):
        # type: () -> bool
        return True


class QualityCode(Object):
    """QualityCode contains a 32-bit integer code and optionally a
    diagnostic string.
    """

    class Level(Enum):
        def code(self, userCode):
            # type: (int) -> int
            pass

        @staticmethod
        def values():
            # type: () -> Iterable[QualityCode.Level]
            pass

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
        # type: (*Any) -> None
        super(QualityCode, self).__init__()
        print(args)

    def derive(self, diagnosticMessage):
        # type: (Union[str, unicode]) -> QualityCode
        pass

    def getCode(self):
        # type: () -> int
        pass

    @staticmethod
    def getCodeName(code):
        # type: (Union[int, QualityCode]) -> Union[str, unicode]
        pass

    @staticmethod
    def getCodesJson():
        # type: () -> JsonObject
        pass

    def getDiagnosticMessage(self):
        # type: () -> Union[str, unicode]
        pass

    def getLevel(self):
        # type: () -> QualityCode.Level
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        pass

    def isBad(self):
        # type: () -> bool
        return True

    def isBadOrError(self):
        # type: () -> bool
        return True

    def isError(self):
        # type: () -> bool
        return True

    def isGood(self):
        # type: () -> bool
        return True

    def isNotGood(self):
        # type: () -> bool
        return True

    def isUncertain(self):
        # type: () -> bool
        return True


class BasicQualifiedValue(QualifiedValue, Object):
    """The basic implementation of QualifiedValue."""

    quality = None  # type: QualityCode
    timestamp = None  # type: Date
    value = None  # type: Object

    # Class attribute constants
    BAD = None  # type: BasicQualifiedValue
    CONFIG_ERROR = None  # type: BasicQualifiedValue
    DISABLED = None  # type: BasicQualifiedValue
    EXPRESSION_EVAL_ERROR = None  # type: BasicQualifiedValue
    INITIAL_VALUE = None  # type: BasicQualifiedValue
    NOT_CONNECTED = None  # type: BasicQualifiedValue
    NOT_FOUND = None  # type: BasicQualifiedValue
    REFERENCE_NOT_FOUND = None  # type: BasicQualifiedValue
    STALE = None  # type: BasicQualifiedValue
    TRANSFORM_ERROR = None  # type: BasicQualifiedValue
    TYPE_CONVERSION = None  # type: BasicQualifiedValue
    UNKNOWN = None  # type: BasicQualifiedValue
    UNSUPPORTED = None  # type: BasicQualifiedValue

    def __init__(self, *args):
        # type: (*Any) -> None
        super(BasicQualifiedValue, self).__init__()
        print(args)
        self.quality = QualityCode.Bad_Stale
        self.timestamp = Date()
        self.value = Object()

    def clone(self):
        # type: () -> BasicQualifiedValue
        pass

    def derive(
        self,
        arg=None,  # type: Union[str, unicode, None, QualityCode]
    ):
        # type: (...) -> QualifiedValue
        pass

    @staticmethod
    def fromObject(obj):
        # type: (Object) -> QualifiedValue
        pass

    def getQuality(self):
        # type: () -> QualityCode
        return self.quality

    def getTimestamp(self):
        # type: () -> Date
        return self.timestamp

    def getValue(self):
        # type: () -> Object
        return self.value

    def setQuality(self, code):
        # type: (QualityCode) -> None
        self.quality = code

    def setTimestamp(self, timestamp):
        # type: (Date) -> None
        self.timestamp = timestamp

    def setValue(self, value):
        # type: (Object) -> None
        self.value = value

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


BasicQualifiedValue.BAD = BasicQualifiedValue(None, QualityCode.Bad)
BasicQualifiedValue.CONFIG_ERROR = BasicQualifiedValue(
    None, QualityCode.Error_Configuration
)
BasicQualifiedValue.DISABLED = BasicQualifiedValue(None, QualityCode.Bad_Disabled)
BasicQualifiedValue.EXPRESSION_EVAL_ERROR = BasicQualifiedValue(
    None, QualityCode.Error_ExpressionEval
)
BasicQualifiedValue.INITIAL_VALUE = BasicQualifiedValue(
    None, QualityCode.Uncertain_InitialValue
)
BasicQualifiedValue.NOT_CONNECTED = BasicQualifiedValue(
    None, QualityCode.Bad_NotConnected
)
BasicQualifiedValue.NOT_FOUND = BasicQualifiedValue(None, QualityCode.Bad_NotFound)
BasicQualifiedValue.REFERENCE_NOT_FOUND = BasicQualifiedValue(
    None, QualityCode.Bad_ReferenceNotFound
)
BasicQualifiedValue.STALE = BasicQualifiedValue(None, QualityCode.Bad_Stale)
BasicQualifiedValue.TRANSFORM_ERROR = BasicQualifiedValue(None, QualityCode.Bad)
BasicQualifiedValue.TYPE_CONVERSION = BasicQualifiedValue(
    None, QualityCode.Error_TypeConversion
)
BasicQualifiedValue.UNKNOWN = BasicQualifiedValue(None, QualityCode.Uncertain)
BasicQualifiedValue.UNSUPPORTED = BasicQualifiedValue(None, QualityCode.Bad_Unsupported)
