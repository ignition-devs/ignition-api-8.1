__all__ = ["DataQuality", "DataType"]

from typing import List, Optional

from com.inductiveautomation.ignition.common.i18n import LocalizedString
from com.inductiveautomation.ignition.common.model.values import Quality, QualityCode
from java.lang import Enum, Object, String
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
        pass

    def isGood(self):
        # type: () -> bool
        pass

    def isGoodData(self):
        # type: () -> bool
        pass

    def isOpcBadData(self):
        # type: () -> bool
        pass

    def toString(self, locale=None):
        # type: (Optional[Locale]) -> String
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
    def fromIntValue(self, val):
        pass

    def getComponentDataType(self):
        pass

    def getIntValue(self):
        pass

    def getJavaType(self):
        pass

    def getTypeClass(self):
        pass

    def getTypeForClass(self, clazz):
        pass

    def getTypeForValue(self, val):
        pass

    def isArray(self):
        pass

    def isFloatingPoint(self):
        pass

    def isNumeric(self):
        pass

    def legacyDataType(self):
        pass

    def values(self):
        pass
