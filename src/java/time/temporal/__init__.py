__all__ = [
    "ChronoUnit",
    "Temporal",
    "TemporalAccessor",
    "TemporalAdjuster",
    "TemporalField",
    "TemporalQuery",
    "TemporalUnit",
    "ValueRange",
]

from typing import Any, Dict, List, Optional, TypeVar

from java.lang import Enum, Object, String
from java.time import Duration
from java.time.format import ResolverStyle
from java.util import Locale

R = TypeVar("R")


class TemporalAccessor(object):
    def get(self, field):
        # type: (TemporalField) -> int
        pass

    def getLong(self, field):
        # type: (TemporalField) -> long
        pass

    def isSupported(self, field):
        # type: (TemporalField) -> bool
        pass

    def query(self, query):
        # type: (TemporalQuery) -> R
        pass

    def range(self, field):
        # type: (TemporalField) -> ValueRange
        pass


class TemporalAdjuster(object):
    def adjustInto(self, temporal):
        # type: (Temporal) -> Temporal
        raise NotImplementedError


class TemporalField(object):
    def adjustInto(self, temporal, newValue):
        # type: (R, long) -> Temporal
        raise NotImplementedError

    def getBaseUnit(self):
        # type: () -> TemporalUnit
        raise NotImplementedError

    def getDisplayName(self, locale):
        # type: (Locale) -> String
        pass

    def getFrom(self, temporal):
        # type: (TemporalAccessor) -> long
        raise NotImplementedError

    def getRangeUnit(self):
        # type: () -> TemporalUnit
        raise NotImplementedError

    def isDateBased(self):
        # type: () -> bool
        raise NotImplementedError

    def isSupportedBy(self, temporal):
        # type: (TemporalAccessor) -> bool
        raise NotImplementedError

    def isTimeBased(self):
        # type: () -> bool
        raise NotImplementedError

    def range(self):
        # type: () -> ValueRange
        raise NotImplementedError

    def rangeRefinedBy(self, temporal):
        # type: (TemporalAccessor) -> ValueRange
        raise NotImplementedError

    def resolve(
        self,
        fieldValues,  # type: Dict[TemporalField, long]
        partialTemporal,  # type: TemporalAccessor
        resolverStyle,  # type: ResolverStyle
    ):
        # type: (...) -> TemporalAccessor
        pass

    def toString(self):
        # type: () -> String
        raise NotImplementedError


class TemporalQuery(object):
    def queryFrom(self, temporal):
        # type: (TemporalAccessor) -> R
        raise NotImplementedError


class TemporalUnit(object):
    def addTo(self, temporal, amount):
        # type: (Temporal, long) -> Temporal
        raise NotImplementedError

    def between(self, temporal1Inclusive, temporal2Exclusive):
        # type: (Temporal, Temporal) -> Temporal
        raise NotImplementedError

    def isSupportedBy(self, temporal):
        # type: (Temporal) -> bool
        pass

    def getDuration(self):
        # type: () -> Duration
        raise NotImplementedError

    def isDateBased(self):
        # type: () -> bool
        raise NotImplementedError

    def isDurationEstimated(self):
        # type: () -> bool
        raise NotImplementedError

    def isTimeBased(self):
        # type: () -> bool
        raise NotImplementedError

    def toString(self):
        # type: () -> String
        raise NotImplementedError


class Temporal(TemporalAccessor):
    def minus(self, amount, unit=None):
        # type: (long, Optional[TemporalUnit]) -> Temporal
        pass

    def plus(self, amount, unit=None):
        # type: (long, Optional[TemporalUnit]) -> Temporal
        pass

    def until(self, endExclusive, unit):
        # type: (Temporal, TemporalUnit) -> long
        raise NotImplementedError


class ChronoUnit(Enum, TemporalUnit):
    CENTURIES = None  # type: ChronoUnit
    DAYS = None  # type: ChronoUnit
    DECADES = None  # type: ChronoUnit
    ERAS = None  # type: ChronoUnit
    FOREVER = None  # type: ChronoUnit
    MICROS = None  # type: ChronoUnit
    MILLENNIA = None  # type: ChronoUnit
    MILLIS = None  # type: ChronoUnit
    MINUTES = None  # type: ChronoUnit
    MONTHS = None  # type: ChronoUnit
    NANOS = None  # type: ChronoUnit
    SECONDS = None  # type: ChronoUnit
    HALF_DAYS = None  # type: ChronoUnit
    HOURS = None  # type: ChronoUnit
    WEEKS = None  # type: ChronoUnit
    YEARS = None  # type: ChronoUnit

    def addTo(self, temporal, amount):
        # type: (Temporal, long) -> Temporal
        pass

    def between(self, temporal1Inclusive, temporal2Exclusive):
        # type: (Temporal, Temporal) -> Temporal
        pass

    def getDuration(self):
        # type: () -> Duration
        pass

    def isDateBased(self):
        # type: () -> bool
        pass

    def isDurationEstimated(self):
        # type: () -> bool
        pass

    def isTimeBased(self):
        # type: () -> bool
        pass

    @staticmethod
    def values():
        # type: () -> List[ChronoUnit]
        pass


class ValueRange(Object):
    def checkValidIntValue(self, value, field):
        # type: (long, TemporalField) -> int
        pass

    def checkValidValue(self, value, field):
        # type: (long, TemporalField) -> long
        pass

    def getLargestMinimum(self):
        # type: () -> long
        pass

    def getMaximum(self):
        # type: () -> long
        pass

    def getMinimum(self):
        # type: () -> long
        pass

    def getSmallestMaximum(self):
        # type: () -> long
        pass

    def isFixed(self):
        # type: () -> bool
        pass

    def isIntValue(self):
        # type: () -> bool
        pass

    def isValidIntValue(self, value):
        # type: (long) -> bool
        pass

    def isValidValue(self, value):
        # type: (long) -> bool
        pass

    @staticmethod
    def of(*args):
        # type: (*Any) -> ValueRange
        pass
