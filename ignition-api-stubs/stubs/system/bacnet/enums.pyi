from enum import Enum

class DayOfWeek(Enum):
    MONDAY: int
    TUESDAY: int
    WEDNESDAY: int
    THURSDAY: int
    FRIDAY: int
    SATURDAY: int
    SUNDAY: int
    UNSPECIFIED: int

class MaxApduLength(Enum):
    UP_TO_50: int
    UP_TO_128: int
    UP_TO_206: int
    UP_TO_480: int
    UP_TO_1024: int
    UP_TO_1476: int

class MaxSegments(Enum):
    UNSPECIFIED: int
    UP_TO_2: int
    UP_TO_4: int
    UP_TO_8: int
    UP_TO_16: int
    UP_TO_32: int
    UP_TO_64: int
    MORE_THAN_64: int

class Month(Enum):
    JANUARY: int
    FEBRUARY: int
    MARCH: int
    APRIL: int
    MAY: int
    JUNE: int
    JULY: int
    AUGUST: int
    SEPTEMBER: int
    OCTOBER: int
    NOVEMBER: int
    DECEMBER: int
    ODD_MONTHS: int
    EVEN_MONTHS: int
    UNSPECIFIED: int
