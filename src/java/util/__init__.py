"""Contains the collections framework, legacy collection classes, event
model, date and time facilities, internationalization, and miscellaneous
utility classes (a string tokenizer, a random-number generator, and a
bit array).
"""

from __future__ import print_function

__all__ = [
    "Calendar",
    "Collection",
    "Comparator",
    "Currency",
    "Date",
    "EventObject",
    "Iterator",
    "ListIterator",
    "Locale",
    "Spliterator",
    "TimeZone",
    "UUID",
]

from typing import Any, Dict, List, Optional, Set, TypeVar, Union

from dev.thecesrom.utils.decorators import classproperty
from java.lang import Object, String
from java.time import Instant, ZoneId
from java.util.function import (
    Consumer,
    Function,
    Predicate,
    Supplier,
    ToDoubleFunction,
    ToIntFunction,
    ToLongFunction,
)

E = TypeVar("E")
T = TypeVar("T")


class Collection(object):
    def add(self, e):
        # type: (E) -> bool
        raise NotImplementedError

    def addAll(self, c):
        # type: (Collection) -> bool
        raise NotImplementedError

    def clear(self):
        # type: () -> None
        raise NotImplementedError

    def contains(self, o):
        # type: (Object) -> bool
        raise NotImplementedError

    def containsAll(self, c):
        # type: (Collection) -> bool
        raise NotImplementedError

    def equals(self, o):
        # type: (Object) -> bool
        raise NotImplementedError

    def hashCode(self):
        # type: () -> int
        raise NotImplementedError

    def isEmpty(self):
        # type: () -> bool
        raise NotImplementedError

    def iterator(self):
        # type: () -> Iterator
        raise NotImplementedError

    def parallelStream(self):
        # type: () -> Stream
        raise NotImplementedError

    def remove(self, o):
        # type: (Object) -> bool
        raise NotImplementedError

    def removeAll(self, c):
        # type: (Collection) -> bool
        raise NotImplementedError

    def removeIf(self, filter):
        # type: (Predicate) -> bool
        raise NotImplementedError

    def retainAll(self, v):
        # type: (Collection) -> bool
        raise NotImplementedError

    def size(self):
        # type: () -> int
        raise NotImplementedError

    def spliterator(self):
        # type: () -> Spliterator
        raise NotImplementedError

    def stream(self):
        # type: () -> Stream
        raise NotImplementedError

    def toArray(self, arg=None):
        # type: (Optional[Any]) -> List[Object]
        raise NotImplementedError


class Comparator(object):
    def compare(self, o1, o2):
        # type: (T, T) -> int
        raise NotImplementedError

    @staticmethod
    def comparing(keyExtractor, keyComparator):
        # type: (Function, Comparator) -> Comparator
        pass

    @staticmethod
    def comparingDouble(keyExtractor):
        # type: (ToDoubleFunction) -> Comparator
        pass

    @staticmethod
    def comparingInt(keyExtractor):
        # type: (ToIntFunction) -> Comparator
        pass

    @staticmethod
    def comparingLong(keyExtractor):
        # type: (ToLongFunction) -> Comparator
        pass

    def equals(self, obj):
        # type: (Object) -> bool
        raise NotImplementedError

    @staticmethod
    def naturalOrder():
        # type: () -> Comparator
        pass

    @staticmethod
    def nullsFirst(comparator):
        # type: (Comparator) -> Comparator
        pass

    @staticmethod
    def nullsLast(comparator):
        # type: (Comparator) -> Comparator
        pass

    def reversed(self):
        # type: () -> Comparator
        pass

    @staticmethod
    def reverseOrder():
        # type: () -> Comparator
        pass

    def thenComparing(self, *args):
        # type: (*Any) -> Comparator
        pass

    def thenComparingDouble(self, keyExtractor):
        # type: (ToDoubleFunction) -> Comparator
        pass

    def thenComparingInt(self, keyExtractor):
        # type: (ToIntFunction) -> Comparator
        pass

    def thenComparingLong(self, keyExtractor):
        # type: (ToLongFunction) -> Comparator
        pass


class Iterator(object):
    def forEachRemaining(self, action):
        # type: (Consumer) -> None
        pass

    def hasNext(self):
        # type: () -> bool
        raise NotImplementedError

    def next(self):
        # type: () -> E
        raise NotImplementedError

    def remove(self):
        # type: () -> bool
        return True


class ListIterator(Iterator):
    def add(self, e):
        # type: (E) -> None
        raise NotImplementedError

    def hasNext(self):
        # type: () -> bool
        raise NotImplementedError

    def hasPrevious(self):
        # type: () -> bool
        raise NotImplementedError

    def next(self):
        # type: () -> E
        raise NotImplementedError

    def nextIndex(self):
        # type: () -> int
        raise NotImplementedError

    def previous(self):
        # type: () -> E
        raise NotImplementedError

    def previousIndex(self):
        # type: () -> int
        raise NotImplementedError

    def set(self, e):
        # type: (E) -> None
        raise NotImplementedError


class Spliterator(object):
    CONCURRENT = None  # type: int
    DISTINCT = None  # type: int
    IMMUTABLE = None  # type: int
    NONNULL = None  # type: int
    ORDERED = None  # type: int
    SIZED = None  # type: int
    SORTED = None  # type: int
    SUBSIZED = None  # type: int

    def characteristics(self):
        # type: () -> int
        raise NotImplementedError

    def estimateSize(self):
        # type: () -> long
        raise NotImplementedError

    def forEachRemaining(self, action):
        # type: (Consumer) -> None
        pass

    def getComparator(self):
        # type: () -> Comparator
        pass

    def getExactSizeIfKnown(self):
        # type: () -> long
        pass

    def hasCharacteristics(self, characteristics):
        # type: (int) -> bool
        return True

    def tryAdvance(self, action):
        # type: (Consumer) -> bool
        raise NotImplementedError

    def trySplit(self):
        # type: () -> Spliterator
        raise NotImplementedError


class Stream(object):
    @staticmethod
    def builder():
        # type: () -> Builder
        pass

    @staticmethod
    def concat(a, b):
        # type: (Stream, Stream) -> Stream
        pass

    @staticmethod
    def empty():
        # type: () -> Stream
        pass

    @staticmethod
    def generate(s):
        # type: (Supplier) -> Stream
        pass

    @staticmethod
    def iterate(*args):
        # type: (*Any) -> Stream
        pass

    @staticmethod
    def of(*args):
        # type: (*T) -> Stream
        pass

    @staticmethod
    def ofNullable(t):
        # type: (T) -> Stream
        pass

    class Builder(Consumer):
        def accept(self, t):
            # type: (T) -> None
            raise NotImplementedError

        def add(self, t):
            # type: (T) -> Stream.Builder
            pass

        def build(self):
            # type: () -> Stream
            raise NotImplementedError


class Calendar(Object):
    ALL_STYLES = None  # type: int
    AM = None  # type: int
    AM_PM = None  # type: int
    APRIL = None  # type: int
    AUGUST = None  # type: int
    DATE = None  # type: int
    DAY_OF_MONTH = None  # type: int
    DAY_OF_WEEK = None  # type: int
    DAY_OF_WEEK_IN_MONTH = None  # type: int
    DAY_OF_YEAR = None  # type: int
    DECEMBER = None  # type: int
    DST_OFFSET = None  # type: int
    ERA = None  # type: int
    FEBRUARY = None  # type: int
    FIELD_COUNT = None  # type: int
    FRIDAY = None  # type: int
    HOUR = None  # type: int
    HOUR_OF_DAY = None  # type: int
    JANUARY = None  # type: int
    JULY = None  # type: int
    JUNE = None  # type: int
    LONG = None  # type: int
    LONG_FORMAT = None  # type: int
    LONG_STANDALONE = None  # type: int
    MARCH = None  # type: int
    MAY = None  # type: int
    MILLISECOND = None  # type: int
    MINUTE = None  # type: int
    MONDAY = None  # type: int
    MONTH = None  # type: int
    NARROW_FORMAT = None  # type: int
    NARROW_STANDALONE = None  # type: int
    NOVEMBER = None  # type: int
    OCTOBER = None  # type: int
    PM = None  # type: int
    SATURDAY = None  # type: int
    SECOND = None  # type: int
    SEPTEMBER = None  # type: int
    SHORT = None  # type: int
    SHORT_FORMAT = None  # type: int
    SHORT_STANDALONE = None  # type: int
    SUNDAY = None  # type: int
    THURSDAY = None  # type: int
    TUESDAY = None  # type: int
    UNDECIMBER = None  # type: int
    WEDNESDAY = None  # type: int
    WEEK_OF_MONTH = None  # type: int
    WEEK_OF_YEAR = None  # type: int
    YEAR = None  # type: int
    ZONE_OFFSET = None  # type: int

    def add(self, field, amount):
        # type: (int, int) -> None
        raise NotImplementedError

    def after(self, when):
        # type: (Object) -> bool
        return True

    def before(self, when):
        # type: (Object) -> bool
        return True

    def clear(self, field=None):
        # type: (Optional[int]) -> None
        pass

    def clone(self):
        # type: () -> Object
        pass

    def compareTo(self, anotherCalendar):
        # type: (Calendar) -> int
        pass

    def get(self, field):
        # type: (int) -> int
        pass

    def getActualMaximum(self, field):
        # type: (int) -> int
        pass

    def getActualMinimum(self, field):
        # type: (int) -> int
        pass

    @staticmethod
    def getAvailableCalendarTypes():
        # type: () -> Set[String]
        pass

    @staticmethod
    def getAvailableLocales():
        # type: () -> List[Locale]
        pass

    def getCalendarType(self):
        # type: () -> String
        pass

    def getDisplayName(self, field, style, locale):
        # type: (int, int, Locale) -> String
        pass

    def getDisplayNames(self, field, style, locale):
        # type: (int, int, Locale) -> Dict[String, int]
        pass

    def getFirstDayOfWeek(self):
        # type: () -> int
        pass

    def getGreatestMinimum(self, field):
        # type: (int) -> int
        raise NotImplementedError

    def getInstance(self, *args):
        # type: (*Any) -> Calendar
        pass

    def getTimeZone(self):
        # type: () -> TimeZone
        pass

    def getWeeksInWeekYear(self):
        # type: () -> int
        pass

    def getWeekYear(self):
        # type: () -> int
        pass

    def isLenient(self):
        # type: () -> bool
        return True

    def isSet(self, field):
        # type: (int) -> bool
        return True

    def isWeekDateSUpported(self):
        # type: () -> bool
        return True

    def roll(self, field, amount):
        # type: (int, int) -> None
        pass

    def set(self, *args):
        # type: (*int) -> None
        pass

    def setFirstDayOfWeek(self, value):
        # type: (int) -> None
        pass

    def setLenient(self, lenient):
        # type: (bool) -> None
        pass

    def setMinimalDaysInFirstWeek(self, value):
        # type: (int) -> None
        pass

    def setTime(self, date):
        # type: (Date) -> None
        pass

    def setTimeInMillis(self, millis):
        # type: (long) -> None
        pass

    def setTimeZone(self, value):
        # type: (TimeZone) -> None
        pass

    def setWeekDate(self, weekYear, weekOfYear, dayOfWeek):
        # type: (int, int, int) -> None
        pass

    def toInstant(self):
        # type: () -> Instant
        pass


class Currency(Object):
    @staticmethod
    def getAvailableCurrencies():
        # type: () -> Set[Currency]
        pass

    def getCurrencyCode(self):
        # type: () -> String
        pass

    def getDisplayName(self, locale=None):
        # type: (Optional[Locale]) -> String
        pass

    @staticmethod
    def getInstance(arg):
        # type: (Union[Locale, String]) -> Currency
        pass

    def getNumericCode(self):
        # type: () -> int
        pass

    def getNumericCodeAsString(self):
        # type: () -> String
        pass

    def getSymbol(self, locale=None):
        # type: (Optional[Locale]) -> String
        pass


class Date(Object):
    """The class Date represents a specific instant in time, with
    millisecond precision.
    """

    def __init__(self, date=None):
        # type: (Optional[long]) -> None
        print(self, date)

    def after(self, when):
        # type: (Date) -> bool
        return True

    def before(self, when):
        # type: (Date) -> bool
        return True

    def compareTo(self, anotherDate):
        # type: (Date) -> int
        pass

    def getTime(self):
        # type: () -> long
        pass

    def setTime(self, time):
        # type: (long) -> None
        pass


class EventObject(Object):
    """The root class from which all event state objects shall be
    derived.

    All Events are constructed with a reference to the object, the
    "source", that is logically deemed to be the object upon which the
    Event in question initially occurred upon.
    """

    _source = None  # type: Object

    def __init__(self, source):
        # type: (Object) -> None
        self._source = source

    def getSource(self):
        # type: () -> Object
        return self._source


class Locale(Object):
    """A Locale object represents a specific geographical, political, or
    cultural region. An operation that requires a Locale to perform its
    task is called locale-sensitive and uses the Locale to tailor
    information for the user. For example, displaying a number is a
    locale-sensitive operation; the number should be formatted according
    to the customs and conventions of the user's native country, region,
    or culture.
    """

    country = None  # type: Optional[str]
    language = None  # type: str
    variant = None  # type: Optional[str]

    def __init__(self, language, country=None, variant=None):
        # type: (str, Optional[str], Optional[str]) -> None
        self.language = language
        self.country = country
        self.variant = variant

    def __repr__(self):  # type: ignore[no-untyped-def]
        return "{!r}".format(self.__str__())

    def __str__(self):  # type: ignore[no-untyped-def]
        ret = self.language
        if self.country:
            ret += "_{}".format(self.country)
        if self.variant:
            ret += "_{}".format(self.variant)
        return unicode(ret)

    @classproperty
    def CANADA(self):
        # type: () -> Locale
        return Locale("en", "CA")

    @classproperty
    def CANADA_FRENCH(self):
        # type: () -> Locale
        return Locale("fr", "CA")

    @classproperty
    def CHINA(self):
        # type: () -> Locale
        return Locale("zh", "CN")

    @classproperty
    def CHINESE(self):
        # type: () -> Locale
        return Locale("zh")

    @classproperty
    def ENGLISH(self):
        # type: () -> Locale
        return Locale("en")

    @classproperty
    def FRANCE(self):
        # type: () -> Locale
        return Locale("fr", "FR")

    @classproperty
    def FRENCH(self):
        # type: () -> Locale
        return Locale("fr")

    @classproperty
    def GERMAN(self):
        # type: () -> Locale
        return Locale("de")

    @classproperty
    def GERMANY(self):
        # type: () -> Locale
        return Locale("de", "DE")

    @classproperty
    def ITALIAN(self):
        # type: () -> Locale
        return Locale("it")

    @classproperty
    def ITALY(self):
        # type: () -> Locale
        return Locale("it", "IT")

    @classproperty
    def JAPAN(self):
        # type: () -> Locale
        return Locale("ja", "JP")

    @classproperty
    def JAPANESE(self):
        # type: () -> Locale
        return Locale("ja")

    @classproperty
    def KOREA(self):
        # type: () -> Locale
        return Locale("ko", "KR")

    @classproperty
    def KOREAN(self):
        # type: () -> Locale
        return Locale("ko")

    @classproperty
    def PRC(self):
        # type: () -> Locale
        return Locale("zh", "CN")

    @classproperty
    def SIMPLIFIED_CHINESE(self):
        # type: () -> Locale
        return Locale("zh", "CN")

    @classproperty
    def TAIWAN(self):
        # type: () -> Locale
        return Locale("zh", "TW")

    @classproperty
    def TRADITIONAL_CHINESE(self):
        # type: () -> Locale
        return Locale("zh", "TW")

    @classproperty
    def UK(self):
        # type: () -> Locale
        return Locale("en", "GB")

    @classproperty
    def US(self):
        # type: () -> Locale
        return Locale("en", "US")


class TimeZone(Object):
    LONG = None  # type: int
    SHORT = None  # type: int

    def clone(self):
        # type: () -> Object
        pass

    @staticmethod
    def getAvailableIDs(rawOffset=None):
        # type: (Optional[int]) -> List[String]
        pass

    @staticmethod
    def getDefault():
        # type: () -> TimeZone
        pass

    def getDisplayName(self, *args):
        # type: (*Any) -> String
        pass

    def getDSTSavings(self):
        # type: () -> int
        pass

    def getID(self):
        # type: () -> String
        pass

    def getOffset(self, *args):
        # type: (*Any) -> int
        pass

    def getRawOffset(self):
        # type: () -> int
        raise NotImplementedError

    @staticmethod
    def getTimeZone(arg):
        # type: (Union[String, ZoneId]) -> TimeZone
        pass

    def hasSameRules(self, other):
        # type: (TimeZone) -> bool
        return True

    def isDaylightTime(self, date):
        # type: (Date) -> bool
        raise NotImplementedError

    def observesDaylightTime(self):
        # type: () -> bool
        return True

    @staticmethod
    def setDefault(zone):
        # type: (TimeZone) -> None
        pass

    def setID(self, ID):
        # type: (String) -> None
        pass

    def setRawOffset(self, offsetMillis):
        # type: (int) -> None
        raise NotImplementedError

    def toZoneId(self):
        # type: () -> ZoneId
        pass

    def useDaylightTime(self):
        # type: () -> bool
        raise NotImplementedError


class UUID(Object):
    def __init__(self, mostSigBits, leastSigBits):
        # type: (long, long) -> None
        self._leastSigbits = leastSigBits
        self._mostSigBits = mostSigBits

    def clockSequence(self):
        # type: () -> int
        pass

    def compareTo(self, val):
        # type: (UUID) -> int
        pass

    @staticmethod
    def fromString(name):
        # type: (String) -> UUID
        pass

    def getLeastSignificantBits(self):
        # type: () -> long
        return self._leastSigbits

    def getMostSignificantBits(self):
        # type: () -> long
        return self._mostSigBits

    @staticmethod
    def nameUUIDFromBytes(name):
        # type: (bytearray) -> UUID
        pass

    def node(self):
        # type: () -> long
        pass

    @staticmethod
    def randomUUID():
        # type: () -> UUID
        pass

    def timestamp(self):
        # type: () -> long
        pass

    def variant(self):
        # type: () -> int
        pass

    def version(self):
        # type: () -> int
        pass
