from __future__ import print_function

__all__ = ["Snapshot", "Timer"]

from typing import Any, Iterable

from java.io import OutputStream
from java.lang import Object


class Snapshot(Object):
    def __init__(self):
        # type: () -> None
        super(Snapshot, self).__init__()

    def dump(self, output):
        # type: (OutputStream) -> None
        raise NotImplementedError

    def get75thPercentile(self):
        # type: () -> float
        pass

    def get95thPercentile(self):
        # type: () -> float
        pass

    def get98thPercentile(self):
        # type: () -> float
        pass

    def get999thPercentile(self):
        # type: () -> float
        pass

    def get99thPercentile(self):
        # type: () -> float
        pass

    def getMax(self):
        # type: () -> long
        raise NotImplementedError

    def getMean(self):
        # type: () -> float
        raise NotImplementedError

    def getMedian(self):
        # type: () -> float
        pass

    def getMin(self):
        # type: () -> long
        raise NotImplementedError

    def getStdDev(self):
        # type: () -> float
        raise NotImplementedError

    def getValue(self, quantile):
        # type: (float) -> float
        raise NotImplementedError

    def getValues(self):
        # type: () -> Iterable[long]
        raise NotImplementedError

    def size(self):
        # type: () -> int
        raise NotImplementedError


class Timer(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Timer, self).__init__()
        print(args)

    def getCount(self):
        # type: () -> long
        pass

    def getFifteenMinuteRate(self):
        # type: () -> float
        pass

    def getFiveMinuteRate(self):
        # type: () -> float
        pass

    def getMeanRate(self):
        # type: () -> float
        pass

    def getOneMinuteRate(self):
        # type: () -> float
        pass

    def getSnapshot(self):
        # type: () -> Snapshot
        pass

    def time(self):
        # type: () -> Timer.Context
        pass

    def update(self, *args):
        # type: (*Any) -> None
        pass

    class Context(Object):
        def close(self):
            # type: () -> None
            pass

        def stop(self):
            # type: () -> long
            pass
