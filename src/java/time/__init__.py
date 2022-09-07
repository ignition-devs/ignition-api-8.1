__all__ = ["Clock", "Duration", "Instant", "ZoneId", "ZoneOffset"]

from typing import Dict, Optional, Set

from java.lang import CharSequence, Object, String


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


class ZoneId(Object):
    SHORT_IDS = None  # type: Dict[String, String]

    @staticmethod
    def getAvailableZoneIds():
        # type: () -> Set[String]
        pass

    @staticmethod
    def of(zoneId, aliasMap=None):
        # type: (String, Optional[Dict[String, String]]) -> ZoneId
        pass

    @staticmethod
    def ofOffset(prefix, offset):
        # type: (String, ZoneOffset) -> ZoneId
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
        # type: (String) -> ZoneOffset
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
