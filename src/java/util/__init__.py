"""Contains the collections framework, legacy collection classes, event
model, date and time facilities, internationalization, and miscellaneous
utility classes (a string tokenizer, a random-number generator, and a
bit array).
"""

from __future__ import print_function

__all__ = [
    "Comparator",
    "Date",
    "EventObject",
    "Iterator",
    "Locale",
    "Spliterator",
    "UUID",
]

from typing import Any, Optional, TypeVar

from dev.thecesrom.utils.decorators import classproperty
from java.lang import Object, String
from java.util.function import (
    Consumer,
    Function,
    ToDoubleFunction,
    ToIntFunction,
    ToLongFunction,
)

E = TypeVar("E")
T = TypeVar("T")


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
        # type: (Any) -> Comparator
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
        pass


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
        pass

    def tryAdvance(self, action):
        # type: (Consumer) -> bool
        raise NotImplementedError

    def trySplit(self):
        # type: () -> Spliterator
        raise NotImplementedError


class Date(Object):
    """The class Date represents a specific instant in time, with
    millisecond precision.
    """

    def __init__(self, date=None):
        # type: (Optional[long]) -> None
        print(self, date)

    def after(self, when):
        # type: (Date) -> bool
        pass

    def before(self, when):
        # type: (Date) -> bool
        pass

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

    def __repr__(self):
        return "{!r}".format(self.__str__())

    def __str__(self):
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
