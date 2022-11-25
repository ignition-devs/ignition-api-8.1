from __future__ import print_function

__all__ = [
    "AttributedCharacterIterator",
    "CharacterIterator",
    "DateFormat",
    "DateFormatSymbols",
    "FieldPosition",
    "Format",
    "NumberFormat",
    "ParsePosition",
    "SimpleDateFormat",
]

from typing import Any, Dict, List, Optional, Set, Union

from java.lang import Number, Object, String, StringBuffer
from java.math import RoundingMode
from java.util import Calendar, Currency, Date, Locale, TimeZone


class CharacterIterator(object):
    DONE = None  # type: str

    def clone(self):
        # type: () -> str
        raise NotImplementedError

    def current(self):
        # type: () -> str
        raise NotImplementedError

    def first(self):
        # type: () -> str
        raise NotImplementedError

    def getBeginIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getEndIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getIndex(self):
        # type: () -> int
        raise NotImplementedError

    def last(self):
        # type: () -> str
        raise NotImplementedError

    def next(self):
        # type: () -> str
        raise NotImplementedError

    def previous(self):
        # type: () -> str
        raise NotImplementedError

    def setIndex(self, position):
        # type: (int) -> str
        raise NotImplementedError


class AttributedCharacterIterator(CharacterIterator):
    def clone(self):
        # type: () -> str
        raise NotImplementedError

    def current(self):
        # type: () -> str
        raise NotImplementedError

    def first(self):
        # type: () -> str
        raise NotImplementedError

    def getAllAttributeKeys(self):
        # type: () -> Set[AttributedCharacterIterator.Attribute]
        raise NotImplementedError

    def getAttribute(self, attribute):
        # type: (AttributedCharacterIterator.Attribute) -> Object
        raise NotImplementedError

    def getAttributes(self):
        # type: () -> Dict[AttributedCharacterIterator.Attribute, Object]  # noqa: W505
        raise NotImplementedError

    def getBeginIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getEndIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getIndex(self):
        # type: () -> int
        raise NotImplementedError

    def last(self):
        # type: () -> str
        raise NotImplementedError

    def next(self):
        # type: () -> str
        raise NotImplementedError

    def previous(self):
        # type: () -> str
        raise NotImplementedError

    def setIndex(self, position):
        # type: (int) -> str
        raise NotImplementedError

    class Attribute(Object):
        INPUT_METHOD_SEGMENT = None  # type: AttributedCharacterIterator.Attribute
        LANGUAGE = None  # type: AttributedCharacterIterator.Attribute
        READING = None  # type: AttributedCharacterIterator.Attribute


class FieldPosition(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        pass

    def getBeginIndex(self):
        # type: () -> int
        pass

    def getEndIndex(self):
        # type: () -> int
        pass

    def getField(self):
        # type: () -> Any
        pass

    def getFieldAttribute(self):
        # type: () -> Format.Field
        pass

    def setBeginIndex(self, bi):
        # type: (int) -> None
        pass

    def setEndIndex(self, ei):
        # type: (int) -> None
        pass


class Format(Object):
    def clone(self):
        # type: () -> Object
        pass

    def formatToCharacterIterator(self, obj):
        # type: (Object) -> AttributedCharacterIterator
        pass

    def parseObject(self, source, pos=None):
        # type: (String, Optional[ParsePosition]) -> Object
        pass

    class Field(AttributedCharacterIterator.Attribute):
        pass


class DateFormat(Format):
    AM_PM_FIELD = None  # type: int
    DATE_FIELD = None  # type: int
    DAY_OF_WEEK_FIELD = None  # type: int
    DAY_OF_WEEK_IN_MONTH_FIELD = None  # type: int
    DAY_OF_YEAR_FIELD = None  # type: int
    DEFAULT = None  # type: int
    ERA_FIELD = None  # type: int
    FULL = None  # type: int
    HOUR_OF_DAY0_FIELD = None  # type: int
    HOUR_OF_DAY1_FIELD = None  # type: int
    HOUR0_FIELD = None  # type: int
    HOUR1_FIELD = None  # type: int
    LONG = None  # type: int
    MEDIUM = None  # type: int
    MILLISECOND_FIELD = None  # type: int
    MONTH_FIELD = None  # type: int
    SECOND_FIELD = None  # type: int
    SHORT = None  # type: int
    TIMEZONE_FIELD = None  # type: int
    WEEK_OF_MONTH_FIELD = None  # type: int
    WEEK_OF_YEAR_FIELD = None  # type: int
    YEAR_FIELD = None  # type: int

    def format(
        self,
        date,  # type: Union[Date, Object]
        toAppendTo=None,  # type: Optional[StringBuffer]
        pos=None,  # type: Optional[FieldPosition]
    ):  # type: (...) -> Union[String, StringBuffer]
        pass

    @staticmethod
    def getAvailableLocales():
        # type: () -> List[Locale]
        pass

    def getCalendar(self):
        # type: () -> Calendar
        pass

    @staticmethod
    def getDateInstance(style=None, aLocale=None):
        # type: (Optional[int], Optional[Locale]) -> DateFormat
        pass

    @staticmethod
    def getDateTimeInstance():
        # type: () -> DateFormat
        pass

    @staticmethod
    def getInstance():
        # type: () -> DateFormat
        pass

    def getNumberFormat(self):
        # type: () -> NumberFormat
        pass

    @staticmethod
    def getTimeInstance(style, aLocale=None):
        # type: (int, Optional[Locale]) -> DateFormat
        pass

    def getTimeZone(self):
        # type: () -> TimeZone
        pass

    def isLenient(self):
        # type: () -> bool
        return True

    def parse(self, source):
        # type: (String) -> Date
        pass

    def setCalendar(self, newCalendar):
        # type: (Calendar) -> None
        pass

    def setLenient(self, lenient):
        # type: (bool) -> None
        pass

    def setNumberFormat(self, newNumberFormat):
        # type: (NumberFormat) -> None
        pass

    def setTimeZone(self, zone):
        # type: (TimeZone) -> None
        pass


class DateFormatSymbols(Object):
    def __init__(self, locale=None):
        # type: (Optional[Locale]) -> None
        print(locale)

    def clone(self):
        # type: () -> Object
        pass

    def getAmPmStrings(self):
        # type: () -> List[String]
        pass

    @staticmethod
    def getAvailableLocales():
        # type: () -> List[Locale]
        pass

    def getEras(self):
        # type: () -> List[String]
        pass

    @staticmethod
    def getInstance(locale=None):
        # type: (Optional[Locale]) -> DateFormatSymbols
        pass

    def getLocalPatternChars(self):
        # type: () -> String
        pass

    def getMonths(self):
        # type: () -> List[String]
        pass

    def getShortMonths(self):
        # type: () -> List[String]
        pass

    def getShortWeekdays(self):
        # type: () -> List[String]
        pass

    def getWeekdays(self):
        # type: () -> List[String]
        pass

    def getZoneStrings(self):
        # type: () -> List[List[String]]
        pass

    def setAmPmStrings(self, newAmpms):
        # type: (List[String]) -> None
        pass

    def setEras(self, newEras):
        # type: (List[String]) -> None
        pass

    def setLocalPatternChars(self, newLocalPatternChars):
        # type: (String) -> None
        pass

    def setMonths(self, newMonths):
        # type: (List[String]) -> None
        pass

    def setShortMonths(self, newShortMonths):
        # type: (List[String]) -> None
        pass

    def setShortWeekdays(self, newShortWeekdays):
        # type: (List[String]) -> None
        pass

    def setWeekdays(self, newWeekdays):
        # type: (List[String]) -> None
        pass

    def setZoneStrings(self, newZoneStrings):
        # type: (List[List[String]]) -> None
        pass


class NumberFormat(Format):
    FRACTION_FIELD = None  # type: int
    INTEGER_FIELD = None  # type: int

    def format(
        self,
        number,  # type: Union[float, long, Object]
        toAppendTo=None,  # type: Optional[StringBuffer]
        pos=None,  # type: Optional[FieldPosition]
    ):
        # type: (...) -> Union[String, StringBuffer]
        raise NotImplementedError

    @staticmethod
    def getAvailableLocales():
        # type: () -> List[Locale]
        pass

    def getCurrency(self):
        # type: () -> Currency
        pass

    @staticmethod
    def getCurrencyInstance(inLocale=None):
        # type: (Optional[Locale]) -> NumberFormat
        pass

    @staticmethod
    def getInstance(inLocale=None):
        # type: (Optional[Locale]) -> NumberFormat
        pass

    @staticmethod
    def getIntegerInstance(inLocale=None):
        # type: (Optional[Locale]) -> NumberFormat
        pass

    def getMaximumFractionDigits(self):
        # type: () -> int
        pass

    def getMaximumIntegerDigits(self):
        # type: () -> int
        pass

    def getMinimumFractionDigits(self):
        # type: () -> int
        pass

    def getMinimumIntegerDigits(self):
        # type: () -> int
        pass

    @staticmethod
    def getNumberInstance(inLocale=None):
        # type: (Optional[Locale]) -> NumberFormat
        pass

    @staticmethod
    def getPercentInstance(inLocale=None):
        # type: (Optional[Locale]) -> NumberFormat
        pass

    def getRoundingMode(self):
        # type: () -> RoundingMode
        pass

    def isGroupingUsed(self):
        # type: () -> bool
        return True

    def isParseIntegerOnly(self):
        # type: () -> bool
        return True

    def parse(self, source):
        # type: (String) -> Number
        pass

    def setCurrency(self, currency):
        # type: (Currency) -> None
        pass

    def setGroupingUsed(self, newValue):
        # type: (bool) -> None
        pass

    def setMaximumFractionDigits(self, newValue):
        # type: (int) -> None
        pass

    def setMaximumIntegerDigits(self, newValue):
        # type: (int) -> None
        pass

    def setMinimumFractionDigits(self, newValue):
        # type: (int) -> None
        pass

    def setMinimumIntegerDigits(self, newValue):
        # type: (int) -> None
        pass

    def setParseIntegerOnly(self, value):
        # type: (bool) -> None
        pass

    def setRoundingMode(self, roundingMode):
        # type: (RoundingMode) -> None
        pass

    class Field(Format.Field):
        CURRENCY = None  # type: NumberFormat.Field
        DECIMAL_SEPARATOR = None  # type: NumberFormat.Field
        EXPONENT = None  # type: NumberFormat.Field
        EXPONENT_SIGN = None  # type: NumberFormat.Field
        EXPONENT_SYMBOL = None  # type: NumberFormat.Field
        FRACTION = None  # type: NumberFormat.Field
        GROUPING_SEPARATOR = None  # type: NumberFormat.Field
        INTEGER = None  # type: NumberFormat.Field
        PERCENT = None  # type: NumberFormat.Field
        PERMILLE = None  # type: NumberFormat.Field
        SIGN = None  # type: NumberFormat.Field


class ParsePosition(Object):
    def __init__(self, index):
        # type: (int) -> None
        print(index)

    def getErrorIndex(self):
        # type: () -> int
        pass

    def getIndex(self):
        # type: () -> int
        pass

    def setErrorIndex(self, ei):
        # type: (int) -> None
        pass

    def setIndex(self, index):
        # type: (int) -> None
        pass


class SimpleDateFormat(DateFormat):
    def __init__(
        self,
        pattern=None,  # type: Optional[String]
        arg=None,  # type: Union[DateFormatSymbols, Locale, None]
    ):
        # type: (...) -> None
        print(pattern, arg)

    def applyLocalizedPattern(self, pattern):
        # type: (String) -> None
        pass

    def applyPattern(self, pattern):
        # type: (String) -> None
        pass

    def get2DigitYearStart(self):
        # type: () -> Date
        pass

    def getDateFormatSymbols(self):
        # type: () -> DateFormatSymbols
        pass

    def set2DigitYearStart(self, startDate):
        # type: (Date) -> None
        pass

    def setDateFormatSymbols(self, newFormatSymbols):
        # type: (DateFormatSymbols) -> None
        pass

    def toLocalizedPattern(self):
        # type: () -> String
        pass

    def toPattern(self):
        # type: () -> String
        pass
