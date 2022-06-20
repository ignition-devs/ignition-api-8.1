"""BACnet enums."""

__all__ = ["DayOfWeek", "MaxApduLength", "MaxSegments", "Month"]

from enum import Enum


class DayOfWeek(Enum):
    """DayOfWeek enumerator."""

    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    UNSPECIFIED = 255


class MaxApduLength(Enum):
    """MaxApduLength enumerator."""

    UP_TO_50 = 0
    UP_TO_128 = 1
    UP_TO_206 = 2
    UP_TO_480 = 3
    UP_TO_1024 = 4
    UP_TO_1476 = 5


class MaxSegments(Enum):
    """MaxSegments enumerator."""

    UNSPECIFIED = 0
    UP_TO_2 = 1
    UP_TO_4 = 2
    UP_TO_8 = 3
    UP_TO_16 = 4
    UP_TO_32 = 5
    UP_TO_64 = 6
    MORE_THAN_64 = 7


class Month(Enum):
    """Month enumerator."""

    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12
    ODD_MONTHS = 13
    EVEN_MONTHS = 14
    UNSPECIFIED = 255
