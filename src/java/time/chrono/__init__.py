__all__ = [
    "ChronoLocalDate",
    "ChronoLocalDateTime",
    "ChronoPeriod",
    "ChronoZonedDateTime",
    "Chronology",
    "Era",
]

from typing import TYPE_CHECKING, Any, Dict, List

from dev.coatl.helper.types import AnyStr
from java.lang import Comparable, Object
from java.time.format import DateTimeFormatter, ResolverStyle, TextStyle
from java.time.temporal import (
    ChronoField,
    Temporal,
    TemporalAccessor,
    TemporalAdjuster,
    TemporalAmount,
    TemporalField,
    TemporalUnit,
    ValueRange,
)
from java.util import Comparator, Locale

if TYPE_CHECKING:
    from java.time import Instant, LocalTime, ZoneId, ZoneOffset


class ChronoLocalDate(Temporal, TemporalAdjuster, Comparable):
    def adjustInto(self, temporal):
        # type: (Temporal) -> Temporal
        pass

    def atTime(self, localTime):
        # type: (LocalTime) -> ChronoLocalDateTime
        pass

    def compareTo(self, o):
        # type: (ChronoLocalDate) -> int
        pass

    def equals(self, obj):
        # type: (Any) -> bool
        raise NotImplementedError

    def format(self, formatter):
        # type: (DateTimeFormatter) -> AnyStr
        pass

    def getChronology(self):
        # type: () -> Chronology
        raise NotImplementedError

    def getEra(self):
        # type: () -> Era
        pass

    def hashCode(self):
        # type: () -> int
        raise NotImplementedError

    def isAfter(self, other):
        # type: (ChronoLocalDate) -> bool
        return True

    def isBefore(self, other):
        # type: (ChronoLocalDate) -> bool
        return True

    def isEqual(self, other):
        # type: (ChronoLocalDate) -> bool
        return True

    def isLeapYear(self):
        # type: () -> bool
        raise NotImplementedError

    def lengthOfMonth(self):
        # type: () -> int
        raise NotImplementedError

    def lengthOfYear(self):
        # type: () -> int
        pass

    @staticmethod
    def timeLineOrder():
        # type: () -> Comparator
        pass

    def toEpochDay(self):
        # type: () -> long
        pass

    def toString(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def until(self, endExclusive, unit):
        # type: (Temporal, TemporalUnit) -> long
        raise NotImplementedError


class ChronoLocalDateTime(Temporal, TemporalAdjuster, Comparable):
    def atZone(self, zone):
        # type: (ZoneId) -> ChronoZonedDateTime
        raise NotImplementedError

    def toLocalDate(self):
        # type: () -> Any
        raise NotImplementedError

    def toLocalTime(self):
        # type: () -> LocalTime
        raise NotImplementedError

    def toString(self):
        # type: () -> AnyStr
        pass


class ChronoPeriod(TemporalAmount):
    @staticmethod
    def between(startDateInclusive, endDateExclusive):
        # type: (ChronoLocalDate, ChronoLocalDate) -> ChronoPeriod
        raise NotImplementedError

    def equals(self, obj):
        # type: (Object) -> bool
        raise NotImplementedError

    def getChronology(self):
        # type: () -> Chronology
        raise NotImplementedError

    def hashCode(self):
        # type: () -> int
        raise NotImplementedError

    def isNegative(self):
        # type: () -> bool
        return True

    def isZero(self):
        # type: () -> bool
        return True

    def minus(self, amountToSubtract):
        # type: (TemporalAmount) -> ChronoPeriod
        raise NotImplementedError

    def multipliedBy(self, scalar):
        # type: (int) -> ChronoPeriod
        raise NotImplementedError

    def negated(self):
        # type: () -> ChronoPeriod
        return ChronoPeriod()

    def normalized(self):
        # type: () -> ChronoPeriod
        raise NotImplementedError

    def plus(self, amountToAdd):
        # type: (TemporalAmount) -> ChronoPeriod
        raise NotImplementedError

    def toString(self):
        # type: () -> AnyStr
        raise NotImplementedError


class ChronoZonedDateTime(Temporal, Comparable):

    def format(self, formatter):
        # type: (DateTimeFormatter) -> AnyStr
        pass

    def getChronology(self):
        # type: () -> Chronology
        pass

    def getOffset(self):
        # type: () -> ZoneOffset
        raise NotImplementedError

    def getZone(self):
        # type: () -> ZoneId
        raise NotImplementedError

    def isAfter(self, other):
        # type: (ChronoZonedDateTime) -> bool
        pass

    def isBefore(self, other):
        # type: (ChronoZonedDateTime) -> bool
        pass

    def isEqual(self, other):
        # type: (ChronoZonedDateTime) -> bool
        pass

    @staticmethod
    def timeLineOrder():
        # type: () -> Comparator
        pass

    def toEpochSecond(self):
        # type: () -> long
        pass

    def toInstant(self):
        # type: () -> Instant
        pass

    def toLocalDate(self):
        # type: () -> Any
        pass

    def toLocalDateTime(self):
        # type: () -> ChronoLocalDateTime
        raise NotImplementedError

    def toLocalTime(self):
        # type: () -> LocalTime
        pass

    def withEarlierOffsetAtOverlap(self):
        # type: () -> ChronoZonedDateTime
        raise NotImplementedError

    def withLaterOffsetAtOverlap(self):
        # type: () -> ChronoZonedDateTime
        raise NotImplementedError

    def withZoneSameInstant(self, zone):
        # type: (ZoneId) -> ChronoZonedDateTime
        raise NotImplementedError

    def withZoneSameLocal(self, zone):
        # type: (ZoneId) -> ChronoZonedDateTime
        raise NotImplementedError


class Chronology(Comparable):
    def date(self, *args):
        # type: (*Any) -> ChronoLocalDate
        raise NotImplementedError

    def dateEpochDay(self, epochDay):
        # type: (long) -> ChronoLocalDate
        raise NotImplementedError

    def dateYearDay(self, prolepticYear, dayOfYear):
        # type: (int, int) -> ChronoLocalDate
        raise NotImplementedError

    def equals(self, obj):
        # type: (Object) -> bool
        raise NotImplementedError

    def eraOf(self, eraValue):
        # type: (int) -> Era
        raise NotImplementedError

    def eras(self):
        # type: () -> List[Era]
        raise NotImplementedError

    def getCalendarType(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getId(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def hashCode(self):
        # type: () -> int
        raise NotImplementedError

    def isLeapYear(self, prolepticYear):
        # type: (long) -> bool
        raise NotImplementedError

    def prolepticYear(self, era, yearOfEra):
        # type: (Era, int) -> int
        raise NotImplementedError

    def range(self, field):
        # type: (ChronoField) -> ValueRange
        raise NotImplementedError

    def resolveDate(
        self,
        fieldValues,  # type: Dict[TemporalField, long]
        resolverStyle,  # type: ResolverStyle
    ):
        # type: (...) -> ChronoLocalDate
        raise NotImplementedError

    def toString(self):
        # type: () -> AnyStr
        raise NotImplementedError


class Era(TemporalAccessor, TemporalAdjuster):
    def adjustInto(self, temporal):
        # type: (Temporal) -> Temporal
        pass

    def getDisplayName(self, style, locale):
        # type: (TextStyle, Locale) -> long
        pass

    def getValue(self):
        # type: () -> int
        raise NotImplementedError
