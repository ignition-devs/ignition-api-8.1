__all__ = ["TimeUnit"]

from typing import Any, List

from java.lang import Enum, Object, Thread
from java.time.temporal import ChronoUnit


class TimeUnit(Enum):
    DAYS = None  # type: TimeUnit
    HOURS = None  # type: TimeUnit
    MICROSECONDS = None  # type: TimeUnit
    MILLISECONDS = None  # type: TimeUnit
    MINUTES = None  # type: TimeUnit
    NANOSECONDS = None  # type: TimeUnit
    SECONDS = None  # type: TimeUnit

    def convert(self, *args):
        # type: (*Any) -> long
        pass

    @staticmethod
    def of(chronoUnit):
        # type: (ChronoUnit) -> TimeUnit
        pass

    def sleep(self, timeout):
        # type: (long) -> None
        pass

    def timedJoin(self, thread, timeout):
        # type: (Thread, long) -> None
        pass

    def timedWait(self, obj, timeout):
        # type: (Object, long) -> None
        pass

    def toChronoUnit(self):
        # type: () -> ChronoUnit
        pass

    def toDays(self, duration):
        # type: (long) -> long
        pass

    def toHours(self, duration):
        # type: (long) -> long
        pass

    def toMicros(self, duration):
        # type: (long) -> long
        pass

    def toMillis(self, duration):
        # type: (long) -> long
        pass

    def toMinutes(self, duration):
        # type: (long) -> long
        pass

    def toNanos(self, duration):
        # type: (long) -> long
        pass

    def toSeconds(self, duration):
        # type: (long) -> long
        pass

    @staticmethod
    def values():
        # type: () -> List[TimeUnit]
        pass
