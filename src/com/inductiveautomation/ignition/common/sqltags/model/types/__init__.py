__all__ = ["DataQuality", "DataType", "DataTypeClass"]

from typing import Iterable, List, Optional

from com.inductiveautomation.ignition.common.i18n import LocalizedString
from com.inductiveautomation.ignition.common.model.values import Quality, QualityCode
from dev.thecesrom.helper.types import AnyStr
from java.lang import Class, Enum, Object
from java.util import Locale


class DataQuality(Object):
    @staticmethod
    def fromIntValue(value):
        # type: (int) -> DataQuality
        pass

    def getDescription(self):
        # type: () -> LocalizedString
        pass

    def getIntValue(self):
        # type: () -> int
        pass

    def getLevel(self):
        # type: () -> Quality.Level
        pass

    def getName(self):
        # type: () -> str
        pass

    def getQualityCode(self):
        # type: () -> QualityCode
        pass

    @staticmethod
    def getQualityFor(value):
        # type: (int) -> DataQuality
        pass

    def isDataUsed(self):
        # type: () -> bool
        return True

    def isGood(self):
        # type: () -> bool
        return True

    def isGoodData(self):
        # type: () -> bool
        return True

    def isOpcBadData(self):
        # type: () -> bool
        return False

    def toString(self, locale=None):
        # type: (Optional[Locale]) -> AnyStr
        pass

    @staticmethod
    def valueOf(name):
        # type: (str) -> DataQuality
        pass

    @staticmethod
    def values():
        # type: () -> List[DataQuality]
        pass

    @staticmethod
    def worstOf(q1, q2):
        # type: (DataQuality, DataQuality) -> DataQuality
        pass

    @staticmethod
    def worstOfAll(*args):
        # type: (DataQuality) -> DataQuality
        pass


class DataType(Enum):
    @staticmethod
    def fromIntValue(val):
        # type: (int) -> DataType
        pass

    def getComponentDataType(self):
        # type: () -> DataType
        pass

    def getIntValue(self):
        # type: () -> int
        pass

    def getJavaType(self):
        # type: () -> Class
        pass

    def getTypeClass(self):
        # type: () -> DataTypeClass
        pass

    @staticmethod
    def getTypeForClass(clazz):
        # type: (Class) -> DataType
        pass

    @staticmethod
    def getTypeForValue(val):
        # type: (int) -> DataType
        pass

    def isArray(self):
        # type: () -> bool
        pass

    def isFloatingPoint(self):
        # type: () -> bool
        pass

    def isNumeric(self):
        # type: () -> bool
        pass

    def legacyDataType(self):
        # type: () -> DataType
        pass

    @staticmethod
    def values():
        # type: () -> Iterable[DataType]
        pass


class DataTypeClass(Enum):
    @staticmethod
    def values():
        # type: () -> Iterable[DataTypeClass]
        pass
