from typing import Any, Iterable

from java.io import OutputStream
from java.lang import Object

class Snapshot(Object):
    def __init__(self) -> None: ...
    def dump(self, output: OutputStream) -> None: ...
    def get75thPercentile(self) -> float: ...
    def get95thPercentile(self) -> float: ...
    def get98thPercentile(self) -> float: ...
    def get999thPercentile(self) -> float: ...
    def get99thPercentile(self) -> float: ...
    def getMax(self) -> long: ...
    def getMean(self) -> float: ...
    def getMedian(self) -> float: ...
    def getMin(self) -> long: ...
    def getStdDev(self) -> float: ...
    def getValue(self, quantile: float) -> float: ...
    def getValues(self) -> Iterable[long]: ...
    def size(self) -> int: ...

class Timer(Object):
    class Context(Object):
        def close(self) -> None: ...
        def stop(self) -> long: ...

    def __init__(self, *args: Any) -> None: ...
    def getCount(self) -> long: ...
    def getFifteenMinuteRate(self) -> float: ...
    def getFiveMinuteRate(self) -> float: ...
    def getMeanRate(self) -> float: ...
    def getOneMinuteRate(self) -> float: ...
    def getSnapshot(self) -> Snapshot: ...
    def time(self) -> Timer.Context: ...
    def update(self, *args: Any) -> None: ...
