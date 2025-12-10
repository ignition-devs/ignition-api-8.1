from typing import List, Optional, Union

NUL: int
PULSE_ON: int
PULSE_OFF: int
LATCH_ON: int
LATCH_OFF: int
CLOSE: int
TRIP: int

def directOperateAnalog(
    deviceName: Union[str, unicode],
    index: int,
    value: Union[float, int, long],
    variation: Optional[int] = ...,
) -> int: ...
def directOperateBinary(
    deviceName: Union[str, unicode],
    indexes: List[int],
    opType: int,
    tcCode: Optional[int] = ...,
    count: Optional[int] = ...,
    onTime: Optional[int] = ...,
    offTime: Optional[int] = ...,
) -> int: ...
def freezeAnalogs(deviceName: Union[str, unicode], indexes: List[int]) -> None: ...
def freezeAnalogsAtTime(
    deviceName: Union[str, unicode],
    absoluteTime: int,
    intervalTime: int,
    indexes: List[int],
) -> None: ...
def freezeCounters(deviceName: Union[str, unicode], indexes: List[int]) -> None: ...
def freezeCountersAtTime(
    deviceName: Union[str, unicode],
    absoluteTime: int,
    intervalTime: int,
    indexes: List[int],
) -> None: ...
def selectOperateAnalog(
    deviceName: Union[str, unicode],
    index: int,
    value: Union[float, int, long],
    variation: Optional[int] = ...,
) -> int: ...
def selectOperateBinary(
    deviceName: Union[str, unicode],
    indexes: List[int],
    opType: int,
    tcCode: Optional[int] = ...,
    count: Optional[int] = ...,
    onTime: Optional[int] = ...,
    offTime: Optional[int] = ...,
) -> int: ...
