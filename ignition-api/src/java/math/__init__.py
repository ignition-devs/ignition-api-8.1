from __future__ import print_function

__all__ = ["BigDecimal", "BigInteger", "MathContext", "RoundingMode"]

from typing import Any, List

from java.lang import Enum, Number, Object


class BigDecimal(Number):
    ONE = None  # type: BigDecimal
    TEN = None  # type: BigDecimal
    ZERO = None  # type: BigDecimal

    def __init__(self, *args):
        # type: (*Any) -> None
        super(BigDecimal, self).__init__()
        print(args)

    def doubleValue(self):
        # type: () -> float
        pass

    def floatValue(self):
        # type: () -> float
        pass

    def intValue(self):
        # type: () -> int
        pass

    def longValue(self):
        # type: () -> long
        pass


class BigInteger(Number):
    ONE = None  # type: BigInteger
    TEN = None  # type: BigInteger
    TWO = None  # type: BigInteger
    ZERO = None  # type: BigInteger

    def __init__(self, *args):
        # type: (*Any) -> None
        super(BigInteger, self).__init__()
        print(args)

    def doubleValue(self):
        # type: () -> float
        pass

    def floatValue(self):
        # type: () -> float
        pass

    def intValue(self):
        # type: () -> int
        pass

    def longValue(self):
        # type: () -> long
        pass


class MathContext(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(MathContext, self).__init__()
        print(args)

    def getPrecision(self):
        # type: () -> int
        pass

    def getRoundingMode(self):
        # type: () -> RoundingMode
        pass


class RoundingMode(Enum):
    CEILING = None  # type: RoundingMode
    DOWN = None  # type: RoundingMode
    FLOOR = None  # type: RoundingMode
    HALF_DOWN = None  # type: RoundingMode
    HALF_EVEN = None  # type: RoundingMode
    HALF_UP = None  # type: RoundingMode
    UNNECESSARY = None  # type: RoundingMode
    UP = None  # type: RoundingMode

    @staticmethod
    def values():
        # type: () -> List[RoundingMode]
        pass
