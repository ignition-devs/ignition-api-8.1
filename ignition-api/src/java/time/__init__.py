__all__ = [
    "Clock",
    "DayOfWeek",
    "Duration",
    "Instant",
    "LocalDate",
    "LocalDateTime",
    "LocalTime",
    "Month",
    "OffsetDateTime",
    "ZoneId",
    "ZoneOffset",
    "ZonedDateTime",
]

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Set, Union

from dev.coatl.helper.types import AnyStr
from java.lang import CharSequence, Comparable, Enum, Object
from java.time.chrono import ChronoLocalDateTime, ChronoZonedDateTime
from java.time.format import DateTimeFormatter, TextStyle
from java.time.temporal import (
    Temporal,
    TemporalAccessor,
    TemporalAdjuster,
    TemporalUnit,
)

if TYPE_CHECKING:
    from java.util import Locale


class Clock(Object):
    @staticmethod
    def offset(baseClock, offsetDuration):
        # type: (Instant, ZoneId) -> Clock
        pass

    @staticmethod
    def systemDefaultZone():
        # type: () -> Clock
        pass

    @staticmethod
    def systemUTC():
        # type: () -> Clock
        pass

    @staticmethod
    def tick(baseClock, tickDuration):
        # type: (Clock, Duration) -> Clock
        pass

    @staticmethod
    def tickMillis(zone):
        # type: (ZoneId) -> Clock
        pass

    @staticmethod
    def tickMinutes(zone):
        # type: (ZoneId) -> Clock
        pass

    @staticmethod
    def tickSeconds(zone):
        # type: (ZoneId) -> Clock
        pass


class DayOfWeek(Enum, TemporalAccessor, TemporalAdjuster):
    FRIDAY = None  # type: DayOfWeek
    MONDAY = None  # type: DayOfWeek
    SATURDAY = None  # type: DayOfWeek
    SUNDAY = None  # type: DayOfWeek
    THURSDAY = None  # type: DayOfWeek
    TUESDAY = None  # type: DayOfWeek
    WEDNESDAY = None  # type: DayOfWeek

    def getValue(self):
        # type: () -> int
        pass

    def minus(self, days):
        # type: (long) -> DayOfWeek
        pass

    @staticmethod
    def of(dayOfWeek):
        # type: (int) -> DayOfWeek
        pass

    def plus(self, days):
        # type: (long) -> DayOfWeek
        pass

    @staticmethod
    def values():
        # type: () -> List[DayOfWeek]
        pass


class Duration(Object):
    ZERO = None  # type: Duration

    def toDays(self):
        # type: () -> long
        pass

    def toDaysPart(self):
        # type: () -> long
        pass

    def toHours(self):
        # type: () -> long
        pass

    def toHoursPart(self):
        # type: () -> int
        pass

    def toMillis(self):
        # type: () -> long
        pass

    def toMillisPart(self):
        # type: () -> int
        pass

    def toMinutes(self):
        # type: () -> long
        pass

    def toMinutesPart(self):
        # type: () -> int
        pass

    def toNanos(self):
        # type: () -> long
        pass

    def toNanosPart(self):
        # type: () -> int
        pass

    def toSeconds(self):
        # type: () -> long
        pass

    def toSecondsPart(self):
        # type: () -> int
        pass


class Instant(Object):
    EPOCH = None  # type: Instant
    MAX = None  # type: Instant
    MIN = None  # type: Instant

    @staticmethod
    def now(clock=None):
        # type: (Optional[Clock]) -> Instant
        pass

    @staticmethod
    def ofEpochMilli(epochMilli):
        # type: (long) -> Instant
        pass

    @staticmethod
    def ofEpochSecond(epochSecond, nanoAdjustment=None):
        # type: (long, Optional[long]) -> Instant
        pass

    @staticmethod
    def parse(text):
        # type: (CharSequence) -> Instant
        pass


class LocalDate(Object, Temporal, TemporalAdjuster, Comparable):
    EPOCH = None  # type: LocalDate
    MAX = None  # type: LocalDate
    MIN = None  # type: LocalDate

    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def until(self, endExclusive, unit):
        # type: (Temporal, TemporalUnit) -> long
        pass

    def atStartOfDay(self, zone):
        # type: (ZoneId) -> LocalDateTime
        pass

    def atTime(self, *args):
        # type: (*Any) -> Union[LocalDateTime, OffsetDateTime]
        pass

    @staticmethod
    def now(clock=None):
        # type: (Optional[Clock]) -> LocalDate
        pass

    @staticmethod
    def of(year, month, dayOfMonth):
        # type: (int, int, int) -> LocalDate
        pass

    @staticmethod
    def parse(text):
        # type: (CharSequence) -> LocalDate
        pass


class LocalDateTime(Object, ChronoLocalDateTime):
    MAX = None  # type: LocalDateTime
    MIN = None  # type: LocalDateTime

    def atOffset(self, offset):
        # type: (ZoneOffset) -> OffsetDateTime
        pass

    def atZone(self, zone):
        # type: (ZoneId) -> ZonedDateTime
        pass

    def toLocalDate(self):
        # type: () -> LocalDate
        pass

    def toLocalTime(self):
        # type: () -> LocalTime
        pass

    def until(self, endExclusive, unit):
        # type: (Temporal, TemporalUnit) -> long
        pass

    def adjustInto(self, temporal):
        # type: (Temporal) -> Temporal
        pass

    def compareTo(self, o):
        # type: (Any) -> int
        pass


class LocalTime(Object, Temporal, TemporalAdjuster, Comparable):
    MAX = None  # type: LocalTime
    MIDNIGHT = None  # type: LocalTime
    MIN = None  # type: LocalTime
    NOON = None  # type: LocalTime

    def adjustInto(self, temporal):
        # type: (Temporal) -> Temporal
        pass

    def atDate(self, date):
        # type: (LocalDate) -> LocalDateTime
        pass

    def compareTo(self, o):
        # type: (Any) -> int
        pass

    @staticmethod
    def now(clock=None):
        # type: (Optional[Clock]) -> LocalTime
        pass

    @staticmethod
    def of(hour, minute, second=0, nano=0):
        # type: (int, int, Optional[int], Optional[int]) -> LocalTime
        pass

    @staticmethod
    def parse(text):
        # type: (CharSequence) -> LocalTime
        pass

    def until(self, endExclusive, unit):
        # type: (Temporal, TemporalUnit) -> long
        pass


class Month(Enum, TemporalAccessor, TemporalAdjuster):
    JANUARY = None  # type: Month
    FEBRUARY = None  # type: Month
    MARCH = None  # type: Month
    APRIL = None  # type: Month
    MAY = None  # type: Month
    JUNE = None  # type: Month
    JULY = None  # type: Month
    AUGUST = None  # type: Month
    SEPTEMBER = None  # type: Month
    OCTOBER = None  # type: Month
    NOVEMBER = None  # type: Month
    DECEMBER = None  # type: Month

    def adjustInto(self, temporal):
        # type: (Temporal) -> Temporal
        pass

    def firstDayOfYear(self, leapYear):
        # type: (bool) -> int
        pass

    def firstMonthOfQuarter(self):
        # type: () -> Month
        pass

    def getDisplayName(self, style, locale):
        # type: (TextStyle, Locale) -> AnyStr
        pass

    def getValue(self):
        # type: () -> int
        pass

    def length(self, leapYear):
        # type: (bool) -> int
        pass

    def maxLength(self):
        # type: () -> int
        pass

    def minLength(self):
        # type: () -> int
        pass

    def minus(self, months):
        # type: (long) -> Month
        pass

    @staticmethod
    def of(month):
        # type: (int) -> Month
        pass

    def plus(self, months):
        # type: (long) -> Month
        pass

    @staticmethod
    def values():
        # type: () -> List[Month]
        pass


class OffsetDateTime(Object, Temporal, TemporalAdjuster, Comparable):
    MAX = None  # type: OffsetDateTime
    MIN = None  # type: OffsetDateTime

    def adjustInto(self, temporal):
        # type: (Temporal) -> Temporal
        pass

    def atZoneSameInstant(self, zone):
        # type: (ZoneId) -> ZonedDateTime
        pass

    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def toLocalDateTime(self):
        # type: () -> LocalDateTime
        pass

    def until(self, endExclusive, unit):
        # type: (Temporal, TemporalUnit) -> long
        pass


class ZoneId(Object):
    SHORT_IDS = None  # type: Dict[AnyStr, AnyStr]

    @staticmethod
    def getAvailableZoneIds():
        # type: () -> Set[AnyStr]
        pass

    @staticmethod
    def of(zoneId, aliasMap=None):
        # type: (AnyStr, Optional[Dict[AnyStr, AnyStr]]) -> ZoneId
        pass

    @staticmethod
    def ofOffset(prefix, offset):
        # type: (AnyStr, ZoneOffset) -> ZoneId
        pass

    @staticmethod
    def systemDefault():
        # type: () -> ZoneId
        pass


class ZoneOffset(Object):
    MAX = None  # type: ZoneOffset
    MIN = None  # type: ZoneOffset
    UTC = None  # type: ZoneOffset

    @staticmethod
    def of(offsetId):
        # type: (AnyStr) -> ZoneOffset
        pass

    @staticmethod
    def ofHours(hours):
        # type: (int) -> ZoneOffset
        pass

    @staticmethod
    def ofHoursMinutes(hours, minutes):
        # type: (int, int) -> ZoneOffset
        pass

    @staticmethod
    def ofHoursMinutesSeconds(hours, minutes, seconds):
        # type: (int, int, int) -> ZoneOffset
        pass

    @staticmethod
    def ofTotalSeconds(totalSeconds):
        # type: (int) -> ZoneOffset
        pass


class ZonedDateTime(Object, ChronoZonedDateTime):
    def toLocalDateTime(self):
        # type: () -> LocalDateTime
        pass

    def withEarlierOffsetAtOverlap(self):
        # type: () -> ZonedDateTime
        pass

    def withLaterOffsetAtOverlap(self):
        # type: () -> ZonedDateTime
        pass

    def withZoneSameInstant(self, zone):
        # type: (ZoneId) -> ZonedDateTime
        pass

    def withZoneSameLocal(self, zone):
        # type: (ZoneId) -> ZonedDateTime
        pass

    def until(self, endExclusive, unit):
        # type: (Temporal, TemporalUnit) -> long
        pass

    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def getDayOfMonth(self):
        # type: () -> int
        pass

    def getDayOfWeek(self):
        # type: () -> DayOfWeek
        pass

    def getDayOfYear(self):
        # type: () -> int
        pass

    def getHour(self):
        # type: () -> int
        pass

    def getMinute(self):
        # type: () -> int
        pass

    def getMonth(self):
        # type: () -> Month
        pass

    def getMonthValue(self):
        # type: () -> int
        pass

    def getNano(self):
        # type: () -> int
        pass

    def getOffset(self):
        # type: () -> ZoneOffset
        pass

    def getSecond(self):
        # type: () -> int
        pass

    def getYear(self):
        # type: () -> int
        pass

    def getZone(self):
        # type: () -> ZoneId
        pass

    def minusDays(self, days):
        # type: (int) -> ZonedDateTime
        pass

    def minusHours(self, hours):
        # type: (int) -> ZonedDateTime
        pass

    def minusMinutes(self, minutes):
        # type: (int) -> ZonedDateTime
        pass

    def minusMonths(self, months):
        # type: (int) -> ZonedDateTime
        pass

    def minusNanos(self, nanos):
        # type: (int) -> ZonedDateTime
        pass

    def minusSeconds(self, seconds):
        # type: (int) -> ZonedDateTime
        pass

    def minusWeeks(self, weeks):
        # type: (int) -> ZonedDateTime
        pass

    def minusYears(self, years):
        # type: (int) -> ZonedDateTime
        pass

    @staticmethod
    def now(arg=None):
        # type: (Optional[Union[Clock, ZoneId]]) -> ZonedDateTime
        pass

    @staticmethod
    def of(*args):
        # type: (*Any) -> ZonedDateTime
        pass

    @staticmethod
    def ofInstant(*args):
        # type: (*Any) -> ZonedDateTime
        pass

    @staticmethod
    def ofLocal(localDateTime, zone, preferredOffset):
        # type: (LocalDateTime, ZoneId, ZoneOffset) -> ZonedDateTime
        pass

    @staticmethod
    def ofStrict(localDateTime, offset, zone):
        # type: (LocalDateTime, ZoneOffset, ZoneId) -> ZonedDateTime
        pass

    @staticmethod
    def parse(
        text,  # type: CharSequence
        formatter=None,  # type: Optional[DateTimeFormatter]
    ):
        # type: (...) -> ZonedDateTime
        pass
