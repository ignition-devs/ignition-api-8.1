"""Contains the collections framework, legacy collection classes, event
model, date and time facilities, internationalization, and miscellaneous
utility classes (a string tokenizer, a random-number generator, and a
bit array).
"""

from __future__ import print_function

__all__ = [
    "AbstractCollection",
    "AbstractMap",
    "Arrays",
    "Calendar",
    "Collection",
    "Comparator",
    "Currency",
    "Date",
    "Dictionary",
    "Enumeration",
    "EventObject",
    "HashMap",
    "Hashtable",
    "Iterator",
    "ListIterator",
    "Locale",
    "Map",
    "Properties",
    "Spliterator",
    "Stream",
    "TimeZone",
    "UUID",
]

from typing import Any, Dict, Iterable, List, Mapping, Optional, Set, Union

from dev.thecesrom.helper.types import AnyStr
from dev.thecesrom.utils.decorators import classproperty
from java.lang import Class, Object
from java.time import Instant, ZoneId
from java.util.function import (
    BiFunction,
    Consumer,
    Function,
    Predicate,
    Supplier,
    ToDoubleFunction,
    ToIntFunction,
    ToLongFunction,
)


class Collection(object):
    def add(self, e):
        # type: (Any) -> bool
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

    def forEach(self, action):
        # type: (Consumer) -> None
        pass

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
        pass

    def remove(self, o):
        # type: (Object) -> bool
        raise NotImplementedError

    def removeAll(self, c):
        # type: (Collection) -> bool
        raise NotImplementedError

    def removeIf(self, filter):
        # type: (Predicate) -> bool
        pass

    def retainAll(self, v):
        # type: (Collection) -> bool
        raise NotImplementedError

    def size(self):
        # type: () -> int
        raise NotImplementedError

    def spliterator(self):
        # type: () -> Spliterator
        pass

    def stream(self):
        # type: () -> Stream
        pass

    def toArray(self, arg=None):
        # type: (Optional[Any]) -> List[Object]
        pass


class Comparator(object):
    def compare(self, o1, o2):
        # type: (Any, Any) -> int
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


class Enumeration(object):
    def asIterator(self):
        # type: () -> Iterator
        pass

    def hasMoreElements(self):
        # type: () -> bool
        raise NotImplementedError

    def nextElement(self):
        # type: () -> Any
        raise NotImplementedError


class Iterator(object):
    def forEachRemaining(self, action):
        # type: (Consumer) -> None
        pass

    def hasNext(self):
        # type: () -> bool
        raise NotImplementedError

    def next(self):
        # type: () -> Any
        raise NotImplementedError

    def remove(self):
        # type: () -> bool
        return True


class ListIterator(Iterator):
    def add(self, e):
        # type: (Any) -> None
        raise NotImplementedError

    def hasNext(self):
        # type: () -> bool
        raise NotImplementedError

    def hasPrevious(self):
        # type: () -> bool
        raise NotImplementedError

    def next(self):
        # type: () -> Any
        raise NotImplementedError

    def nextIndex(self):
        # type: () -> int
        raise NotImplementedError

    def previous(self):
        # type: () -> Any
        raise NotImplementedError

    def previousIndex(self):
        # type: () -> int
        raise NotImplementedError

    def set(self, e):
        # type: (Any) -> None
        raise NotImplementedError


class Map(object):
    def clear(self):
        # type: () -> None
        raise NotImplementedError

    def compute(self, key, remappingFuntion):
        # type: (Any, BiFunction) -> Any
        pass

    def computeIfAbsent(self, key, mappingFuntion):
        # type: (Any, BiFunction) -> Any
        pass

    def computeIfPresent(self, key, remappingFuntion):
        # type: (Any, BiFunction) -> Any
        pass

    def containsKey(self, key):
        # type: (Object) -> bool
        raise NotImplementedError

    def containsValue(self, value):
        # type: (Object) -> bool
        raise NotImplementedError

    @staticmethod
    def copyOf(map):
        # type: (Map) -> Map
        pass

    @staticmethod
    def entry(k, v):
        # type: (Any, Any) -> Map.Entry
        pass

    def entrySet(self):
        # type: () -> Set[Map.Entry]
        raise NotImplementedError

    def forEach(self, action):
        # type: (BiFunction) -> None
        pass

    def get(self, key):
        # type: (Object) -> Any
        raise NotImplementedError

    def getOrDefault(self, key, defaultValue):
        # type: (Object, Any) -> Any
        pass

    def isEmpty(self):
        # type: () -> bool
        raise NotImplementedError

    def keySet(self):
        # type: () -> Set[Any]
        raise NotImplementedError

    def merge(self, key, value, remappingFunction):
        # type: (Any, Any, BiFunction) -> Any
        pass

    @staticmethod
    def of(*args):
        # type: (*Any) -> Map
        pass

    @staticmethod
    def ofEntries(*entries):
        # type: (*Map.Entry) -> Map
        pass

    def put(self, key, value):
        # type: (Any, Any) -> Any
        raise NotImplementedError

    def putAll(self, m):
        # type: (Mapping[Any, Any]) -> None
        raise NotImplementedError

    def putIfAbsent(self, key, value):
        # type: (Any, Any) -> Any
        pass

    def remove(self, key):
        # type: (Object) -> Any
        pass

    def replace(self, *args):
        # type: (*Any) -> Union[Any, bool]
        pass

    def replaceAll(self, function):
        # type: (BiFunction) -> None
        pass

    def size(self):
        # type: () -> int
        raise NotImplementedError

    def values(self):
        # type: () -> Collection
        raise NotImplementedError

    class Entry(object):
        @staticmethod
        def comparingByKey(cmp=None):
            # type: (Optional[Comparator]) -> Any
            pass

        @staticmethod
        def comparingByValue(cmp=None):
            # type: (Optional[Comparator]) -> Any
            pass

        def getKey(self):
            # type: () -> Any
            raise NotImplementedError

        def getValue(self):
            # type: () -> Any
            raise NotImplementedError

        def hashCode(self):
            # type: () -> int
            raise NotImplementedError

        def setValue(self, value):
            # type: (Any) -> Any
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
        # type: (*Any) -> Stream
        pass

    @staticmethod
    def ofNullable(t):
        # type: (Any) -> Stream
        pass

    class Builder(Consumer):
        def accept(self, t):
            # type: (Any) -> None
            raise NotImplementedError

        def add(self, t):
            # type: (Any) -> Stream.Builder
            pass

        def build(self):
            # type: () -> Stream
            raise NotImplementedError


class Arrays(Object):
    @staticmethod
    def asList(a):
        # type: (Any) -> List[Any]
        pass

    @staticmethod
    def binarySearch(*args, **kwargs):
        # type: (*Any, **Any) -> int
        pass

    @staticmethod
    def compare(*args, **kwargs):
        # type: (*Any, **Any) -> int
        pass

    @staticmethod
    def compareUnsigned(*args, **kwargs):
        # type: (*Any, **Any) -> int
        pass

    @staticmethod
    def copyOf(original, newLength, newType=None):
        # type: (List[Any], int, Optional[Class]) -> List[Any]
        pass

    @staticmethod
    def copyOfRange(original, from_, to, newType=None):
        # type: (List[Any], int, int, Optional[Class]) -> List[Any]
        pass

    @staticmethod
    def deepEquals(a1, a2):
        # type: (List[Object], List[Object]) -> bool
        pass

    @staticmethod
    def equals(*args, **kwargs):
        # type: (*Any, **Any) -> bool
        pass

    @staticmethod
    def fill(a, *args):
        # type: (List[Any], *Any) -> None
        pass

    @staticmethod
    def mismatch(*args, **kwargs):
        # type: (*Any, **Any) -> int
        pass

    @staticmethod
    def parallelPrefix(*args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    @staticmethod
    def parallelSetAll(*args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    @staticmethod
    def parallelSort(*args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    @staticmethod
    def setAll(*args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    @staticmethod
    def sort(*args, **kwargs):
        # type: (*Any, **Any) -> None
        pass

    @staticmethod
    def spliterator(
        array,  # type: Iterable[Any]
        startInclusive=None,  # type: Optional[int]
        endExclusive=None,  # type: Optional[int]
    ):
        # type: (...) -> Spliterator
        pass

    @staticmethod
    def stream(array, startInclusive=None, endExclusive=None):
        # type: (Iterable[Any], Optional[int], Optional[int]) -> Stream
        pass


class AbstractCollection(Object, Collection):
    def add(self, e):
        # type: (Any) -> bool
        pass

    def addAll(self, c):
        # type: (Collection) -> bool
        pass

    def clear(self):
        # type: () -> None
        pass

    def contains(self, o):
        # type: (Object) -> bool
        pass

    def containsAll(self, c):
        # type: (Collection) -> bool
        pass

    def isEmpty(self):
        # type: () -> bool
        pass

    def iterator(self):
        # type: () -> Iterator
        pass

    def remove(self, o):
        # type: (Object) -> bool
        pass

    def removeAll(self, c):
        # type: (Collection) -> bool
        pass

    def retainAll(self, v):
        # type: (Collection) -> bool
        pass

    def size(self):
        # type: () -> int
        pass


class AbstractMap(Object, Map):
    def clear(self):
        # type: () -> None
        pass

    def containsKey(self, key):
        # type: (Object) -> bool
        pass

    def containsValue(self, value):
        # type: (Object) -> bool
        pass

    def entrySet(self):
        # type: () -> Set[Map.Entry]
        raise NotImplementedError

    def get(self, key):
        # type: (Object) -> Any
        pass

    def isEmpty(self):
        # type: () -> bool
        pass

    def keySet(self):
        # type: () -> Set[Any]
        pass

    def put(self, key, value):
        # type: (Any, Any) -> Any
        pass

    def putAll(self, m):
        # type: (Mapping[Any, Any]) -> None
        pass

    def remove(self, key):
        # type: (Object) -> Any
        pass

    def size(self):
        # type: () -> int
        pass

    def values(self):
        # type: () -> Collection
        pass


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
        # type: () -> Set[AnyStr]
        pass

    @staticmethod
    def getAvailableLocales():
        # type: () -> List[Locale]
        pass

    def getCalendarType(self):
        # type: () -> AnyStr
        pass

    def getDisplayName(self, field, style, locale):
        # type: (int, int, Locale) -> AnyStr
        pass

    def getDisplayNames(self, field, style, locale):
        # type: (int, int, Locale) -> Dict[AnyStr, int]
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
        # type: () -> AnyStr
        pass

    def getDisplayName(self, locale=None):
        # type: (Optional[Locale]) -> AnyStr
        pass

    @staticmethod
    def getInstance(arg):
        # type: (Union[Locale, AnyStr]) -> Currency
        pass

    def getNumericCode(self):
        # type: () -> int
        pass

    def getNumericCodeAsString(self):
        # type: () -> AnyStr
        pass

    def getSymbol(self, locale=None):
        # type: (Optional[Locale]) -> AnyStr
        pass


class Date(Object):
    """The class Date represents a specific instant in time, with
    millisecond precision.
    """

    def __init__(self, date=None):
        # type: (Optional[long]) -> None
        super(Date, self).__init__()
        self._date = date

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


class Dictionary(Object):
    def __init__(self):
        # type: () -> None
        super(Dictionary, self).__init__()

    def elements(self):
        # type: () -> Enumeration
        raise NotImplementedError

    def get(self, key):
        # type: (Object) -> Any
        raise NotImplementedError

    def isEmpty(self):
        # type: () -> bool
        raise NotImplementedError

    def keys(self):
        # type: () -> Enumeration
        raise NotImplementedError

    def put(self, key, value):
        # type: (Any, Any) -> Any
        raise NotImplementedError

    def remove(self, key):
        # type: (Object) -> Any
        raise NotImplementedError

    def size(self):
        # type: () -> int
        raise NotImplementedError


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
        super(EventObject, self).__init__()
        self._source = source

    def getSource(self):
        # type: () -> Object
        return self._source


class HashMap(AbstractMap, Map):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(HashMap, self).__init__()
        print(args)

    def entrySet(self):
        # type: () -> Set[Map.Entry]
        pass


class Hashtable(Dictionary, Map):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Hashtable, self).__init__()
        print(args)

    def clear(self):
        # type: () -> None
        pass

    def clone(self):
        # type: () -> Object
        pass

    def contains(self, value):
        # type: (Object) -> bool
        pass

    def containsKey(self, key):
        # type: (Object) -> bool
        pass

    def containsValue(self, value):
        # type: (Object) -> bool
        pass

    def elements(self):
        # type: () -> Enumeration
        pass

    def entrySet(self):
        # type: () -> Set[Map.Entry]
        pass

    def get(self, key):
        # type: (Object) -> Any
        pass

    def isEmpty(self):
        # type: () -> bool
        pass

    def keySet(self):
        # type: () -> Set[Any]
        pass

    def keys(self):
        # type: () -> Enumeration
        pass

    def put(self, key, value):
        # type: (Any, Any) -> Any
        pass

    def putAll(self, m):
        # type: (Mapping[Any, Any]) -> None
        pass

    def remove(self, key):
        # type: (Object) -> Any
        pass

    def size(self):
        # type: () -> int
        pass

    def values(self):
        # type: () -> Collection
        pass


class Locale(Object):
    """A Locale object represents a specific geographical, political, or
    cultural region.

    An operation that requires a Locale to perform its task is called
    locale-sensitive and uses the Locale to tailor information for the
    user. For example, displaying a number is a locale-sensitive
    operation; the number should be formatted according to the customs
    and conventions of the user's native country, region, or culture.
    """

    country = None  # type: Optional[str]
    language = None  # type: str
    variant = None  # type: Optional[str]

    def __init__(self, language, country=None, variant=None):
        # type: (str, Optional[str], Optional[str]) -> None
        super(Locale, self).__init__()
        self.language = language
        self.country = country
        self.variant = variant

    def __repr__(self):
        # type: () -> str
        return "{!r}".format(self.__str__())

    def __str__(self):
        # type: () -> str
        ret = self.language
        if self.country:
            ret += "_{}".format(self.country)
        if self.variant:
            ret += "_{}".format(self.variant)
        return ret

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


class Properties(Hashtable):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Properties, self).__init__()


class TimeZone(Object):
    LONG = None  # type: int
    SHORT = None  # type: int

    def __init__(self):
        # type: () -> None
        super(TimeZone, self).__init__()

    def clone(self):
        # type: () -> Object
        pass

    @staticmethod
    def getAvailableIDs(rawOffset=None):
        # type: (Optional[int]) -> List[AnyStr]
        pass

    @staticmethod
    def getDefault():
        # type: () -> TimeZone
        pass

    def getDisplayName(self, *args):
        # type: (*Any) -> AnyStr
        pass

    def getDSTSavings(self):
        # type: () -> int
        pass

    def getID(self):
        # type: () -> AnyStr
        pass

    def getOffset(self, *args):
        # type: (*Any) -> int
        pass

    def getRawOffset(self):
        # type: () -> int
        raise NotImplementedError

    @staticmethod
    def getTimeZone(arg):
        # type: (Union[AnyStr, ZoneId]) -> TimeZone
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
        # type: (AnyStr) -> None
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
        super(UUID, self).__init__()
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
        # type: (AnyStr) -> UUID
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
