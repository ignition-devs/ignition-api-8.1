"""DNP3 Functions.

The following functions give you access to interact with the DNP3
devices.
"""

from __future__ import print_function

__all__ = [
    "CLOSE",
    "LATCH_OFF",
    "LATCH_ON",
    "NUL",
    "PULSE_OFF",
    "PULSE_ON",
    "TRIP",
    "directOperateAnalog",
    "directOperateBinary",
    "freezeAnalogs",
    "freezeAnalogsAtTime",
    "freezeCounters",
    "freezeCountersAtTime",
    "selectOperateAnalog",
    "selectOperateBinary",
]

from typing import List, Optional, Union

# Constants
from java.lang import String

NUL = 0
PULSE_ON = 1
PULSE_OFF = 2
LATCH_ON = 3
LATCH_OFF = 4
CLOSE = 1
TRIP = 2


def directOperateAnalog(
    deviceName,  # type: String
    index,  # type: int
    value,  # type: Union[float, int]
    variation=None,  # type: Optional[int]
):
    # type: (...) -> int
    """Issues a Select-And-Operate command to set an analog value in an
    analog output point.

    Args:
        deviceName: The name of the DNP3 device driver.
        index: The index of the object to be modified in the outstation.
        value: The analog value that is requested (of type int, short,
            float, or double).
        variation: The DNP3 object variation to use in the request.
            Optional.

    Returns:
        The DNP3 status code of the response, as an integer.
    """
    print(deviceName, index, value, variation)
    return 0


def directOperateBinary(
    deviceName,  # type: String
    indexes,  # type: List[int]
    opType,  # type: int
    tcCode=None,  # type: Optional[int]
    count=None,  # type: Optional[int]
    onTime=None,  # type: Optional[int]
    offTime=None,  # type: Optional[int]
):
    # type: (...) -> int
    """Issues a Direct-Operate command for digital control operations
    at binary output points (CROB).

    Args:
        deviceName: The name of the DNP3 device driver.
        indexes: A list of indexes of the objects to be modified in the
            outstation.
        opType: The type of the operation. 0=NUL, 1=PULSE_ON,
            2=PULSE_OFF, 3=LATCH_ON, 4=LATCH_OFF.
        tcCode: The Trip-Close code, used in conjunction with the
            opType. 0=NUL, 1=CLOSE, 2=TRIP. Optional.
        count: The number of times the outstation shall execute the
            operation. Optional.
        onTime: The duration that the output drive remains active, in
            millis. Optional.
        offTime: The duration that the output drive remains non-active,
            in millis. Optional.

    Returns:
        The DNP3 status code of the response, as an integer.
    """
    print(deviceName, indexes, opType, tcCode, count, onTime, offTime)
    return 0


def freezeAnalogs(deviceName, indexes):
    # type: (String, List[int]) -> None
    """Issues a freeze command on the given analog outputs.

    Args:
        deviceName: The name of the DNP3 device driver.
        indexes: An optional list of specific indexes on which to issue
            the freeze command. An empty list can be passed to freeze
            all analogs.
    """
    print(deviceName, indexes)


def freezeAnalogsAtTime(deviceName, absoluteTime, intervalTime, indexes):
    # type: (String, int, int, List[int]) -> None
    """Issues a freeze command on the given analog outputs at the given
    time for the specified duration.

    Args:
        deviceName: The name of the DNP3 device driver.
        absoluteTime: The absolute time at which to freeze, in millis.
        intervalTime: The interval at which to periodically freeze, in
            millis.
        indexes: An optional list of specific indexes on which to issue
            the freeze command. An empty list will freeze all points.
    """
    print(deviceName, absoluteTime, intervalTime, indexes)


def freezeCounters(deviceName, indexes):
    # type: (String, List[int]) -> None
    """Issues a freeze command on the given counters.

    Args:
        deviceName: The name of the DNP3 device driver.
        indexes: An optional list of specific indexes on which to issue
            the freeze command. An empty list can be passed to freeze
            all counters.
    """
    print(deviceName, indexes)


def freezeCountersAtTime(deviceName, absoluteTime, intervalTime, indexes):
    # type: (String, int, int, List[int]) -> None
    """Issues a freeze command on the given counters at the given time
    for the specified duration.

    Args:
        deviceName: The name of the DNP3 device driver.
        absoluteTime: The absolute time at which to freeze, in millis.
        intervalTime: The interval at which to periodically freeze, in
            millis.
        indexes: An optional list of specific indexes on which to issue
            the freeze command. An empty list will freeze all counters.
    """
    print(deviceName, absoluteTime, intervalTime, indexes)


def selectOperateAnalog(
    deviceName,  # type: String
    index,  # type: int
    value,  # type: Union[float, int]
    variation=None,  # type: Optional[int]
):
    # type: (...) -> int
    """Issues a Select-And-Operate command to set an analog value in an
    analog output point.

    Args:
        deviceName: The name of the DNP3 device driver.
        index: The index of the object to be modified in the outstation.
        value: The analog value that is requested (of type int, short,
            float, or double).
        variation: The DNP3 object variation to use in the request.
            Optional.

    Returns:
        The DNP3 status code of the response, as an integer.
    """
    print(deviceName, index, value, variation)
    return 0


def selectOperateBinary(
    deviceName,  # type: String
    indexes,  # type: List[int]
    opType,  # type: int
    tcCode=None,  # type: Optional[int]
    count=None,  # type: Optional[int]
    onTime=None,  # type: Optional[int]
    offTime=None,  # type: Optional[int]
):
    # type: (...) -> int
    """Issues a Select-And-Operate command for digital control
    operations at binary output points (CROB).

    Args:
        deviceName: The name of the DNP3 device driver.
        indexes: A list of indexes of the objects to be modified in the
            outstation.
        opType: The type of operation. 0=NUL, 1=PULSE_ON, 2=PULSE_OFF,
            3=LATCH_ON, 4=LATCH_OFF.
        tcCode: The Trip-Close code, used in conjunction with the
            opType. 0=NUL, 1=CLOSE, 2=TRIP. Optional.
        count: The number of times the outstation shall execute the
            operation. Optional.
        onTime: The duration that the output drive remains active, in
            millis. Optional.
        offTime: The duration that the output drive remains non-active,
            in millis. Optional.

    Returns:
        The DNP3 status code of the response, as an integer.
    """
    print(deviceName, indexes, opType, tcCode, count, onTime, offTime)
    return 0
