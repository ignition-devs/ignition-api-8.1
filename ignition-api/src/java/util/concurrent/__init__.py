__all__ = ["CompletableFuture", "Delayed", "Future", "ScheduledFuture", "TimeUnit"]

from typing import Any, List, Optional

from java.lang import Comparable, Enum, Object, Thread
from java.time.temporal import ChronoUnit


class Delayed(Comparable):
    def compareTo(self, o):
        # type: (Any) -> int
        raise NotImplementedError

    def getDelay(self, unit):
        # type: (TimeUnit) -> long
        raise NotImplementedError


class Future(object):
    def cancel(self, mayInterruptIfRunning):
        # type: (bool) -> bool
        raise NotImplementedError

    def get(self, timeout=None, unit=None):
        # type: (Optional[long], Optional[TimeUnit]) -> Any
        raise NotImplementedError

    def isCancelled(self):
        # type: () -> bool
        raise NotImplementedError

    def isDone(self):
        # type: () -> bool
        raise NotImplementedError


class ScheduledFuture(Delayed, Future):
    def cancel(self, mayInterruptIfRunning):
        # type: (bool) -> bool
        raise NotImplementedError

    def compareTo(self, o):
        # type: (Any) -> int
        raise NotImplementedError

    def get(self, timeout=None, unit=None):
        # type: (Optional[long], Optional[TimeUnit]) -> Any
        raise NotImplementedError

    def getDelay(self, unit):
        # type: (TimeUnit) -> long
        raise NotImplementedError

    def isCancelled(self):
        # type: () -> bool
        raise NotImplementedError

    def isDone(self):
        # type: () -> bool
        raise NotImplementedError


class CompletableFuture(Object):
    def __init__(self):
        # type: () -> None
        super(CompletableFuture, self).__init__()


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
