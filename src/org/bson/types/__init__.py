"""Contains classes implementing various BSON types."""
from __future__ import print_function

__all__ = [
    "BSONTimestamp",
    "Binary",
    "Code",
    "CodeWScope",
    "CodeWithScope",
    "Decimal128",
    "MaxKey",
    "MinKey",
    "ObjectId",
    "Symbol",
]

from typing import Any, Union

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from java.math import BigDecimal
from java.nio import ByteBuffer
from java.util import Date
from org.bson import BSONObject, Document


class Binary(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        print(args)
        super(Binary, self).__init__()

    def getData(self):
        # type: () -> Any
        pass

    def getType(self):
        # type: () -> Any
        pass

    def length(self):
        # type: () -> int
        pass


class BSONTimestamp(Object):
    def __init__(self, time=0, increment=0):
        # type: (int, int) -> None
        super(BSONTimestamp, self).__init__()
        self._time = time
        self._increment = increment

    def compareTo(self, ts):
        # type: (BSONTimestamp) -> int
        pass

    def getInc(self):
        # type: () -> int
        return self._increment

    def getTime(self):
        # type: () -> int
        return self._time


class Code(Object):
    def __init__(self, code):
        # type: (AnyStr) -> None
        self._code = code
        super(Code, self).__init__()

    def getCode(self):
        # type: () -> AnyStr
        return self._code


class CodeWScope(Code):
    def __init__(self, code, scope):
        # type: (AnyStr, BSONObject) -> None
        super(CodeWScope, self).__init__(code)
        self._scope = scope

    def getScope(self):
        # type: () -> BSONObject
        return self._scope


class CodeWithScope(Code):
    def __init__(self, code, scope):
        # type: (AnyStr, Document) -> None
        super(CodeWithScope, self).__init__(code)
        self._scope = scope

    def getScope(self):
        # type: () -> Document
        return self._scope


class Decimal128(Object):
    Nan = None  # type: Decimal128
    NEGATIVE_INFINITY = None  # type: Decimal128
    NEGATIVE_NaN = None  # type: Decimal128
    NEGATIVE_ZERO = None  # type: Decimal128
    POSITIVE_INFINITY = None  # type: Decimal128
    POSITIVE_ZERO = None  # type: Decimal128

    def __init__(self, value):
        # type: (Union[BigDecimal, long]) -> None
        print(value)
        super(Decimal128, self).__init__()

    def bigDecimalValue(self):
        # type: () -> BigDecimal
        pass

    @staticmethod
    def fromIEEE754BIDEncoding(high, low):
        # type: (long, long) -> Decimal128
        pass

    def getHigh(self):
        # type: () -> long
        pass

    def getLow(self):
        # type: () -> long
        pass

    def isFinite(self):
        # type: () -> bool
        pass

    def isInfinite(self):
        # type: () -> bool
        pass

    def isNaN(self):
        # type: () -> bool
        pass

    def isNegative(self):
        # type: () -> bool
        pass

    @staticmethod
    def parse(value):
        # type: (AnyStr) -> Decimal128
        pass


class MaxKey(Object):
    def __init__(self):
        # type: () -> None
        super(MaxKey, self).__init__()


class MinKey(Object):
    def __init__(self):
        # type: () -> None
        super(MinKey, self).__init__()


class ObjectId(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        print(args)
        super(ObjectId, self).__init__()

    @staticmethod
    def createFromLegacyFormat(time, machine, inc):
        # type: (int, int, int) -> ObjectId
        pass

    def getCounter(self):
        # type: () -> int
        pass

    def getDate(self):
        # type: () -> Date
        pass

    @staticmethod
    def getGeneratedMachineIdentifier():
        # type: () -> int
        pass

    @staticmethod
    def getGeneratedProcessIdentifier():
        # type: () -> int
        pass

    def getMachineIdentifier(self):
        # type: () -> int
        pass

    def getProcessIdentifier(self):
        # type: () -> int
        pass

    def getTimestamp(self):
        # type: () -> int
        pass

    @staticmethod
    def isValid(hexString):
        # type: (AnyStr) -> bool
        pass

    def putToByteBuffer(self, buffer):
        # type: (ByteBuffer) -> None
        pass

    def toHexString(self):
        # type: () -> AnyStr
        pass


class Symbol(Object):
    def __init__(self, symbol):
        # type: (AnyStr) -> None
        super(Symbol, self).__init__()
        self._symbol = symbol

    def getSymbol(self):
        # type: () -> AnyStr
        return self._symbol
