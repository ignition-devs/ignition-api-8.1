"""DNP3 Functions.

The following functions give you access to interact with the DNP3
devices.
"""

__all__ = [
    "directOperateAnalog",
    "directOperateBinary",
    "freezeAnalogs",
    "freezeAnalogsAtTime",
    "freezeCounters",
    "freezeCountersAtTime",
    "selectOperateAnalog",
    "selectOperateBinary",
]

# Constants
NUL = 0
PULSE_ON = 1
PULSE_OFF = 2
LATCH_ON = 3
LATCH_OFF = 4
CLOSE = 1
TRIP = 2


def directOperateAnalog(deviceName, index, value, variation=None):
    """Issues a Select-And-Operate command to set an analog value in an
    analog output point.

    Args:
        deviceName (str): The name of the DNP3 device driver.
        index (int): The index of the object to be modified in the
            outstation.
        value (object): The analog value that is requested (of type int,
            short, float, or double).
        variation (int): The DNP3 object variation to use in the
            request. Optional.

    Returns:
        int: The DNP3 status code of the response, as an integer.
    """
    print(deviceName, index, value, variation)
    return 0


def directOperateBinary(
    deviceName,
    indexes,
    opType,
    tcCode=None,
    count=None,
    onTime=None,
    offTime=None,
):
    """Issues a Direct-Operate command for digital control operations at
    binary output points (CROB).

    Args:
        deviceName (str): The name of the DNP3 device driver.
        indexes (list[object]): A list of indexes of the objects to be
            modified in the outstation.
        opType (int): The type of the operation. 0=NUL, 1=PULSE_ON,
            2=PULSE_OFF, 3=LATCH_ON, 4=LATCH_OFF.
        tcCode (int): The Trip-Close code, used in conjunction with the
            opType. 0=NUL, 1=CLOSE, 2=TRIP. Optional.
        count (int): The number of times the outstation shall execute
            the operation. Optional.
        onTime (long): The duration that the output drive remains
            active, in millis. Optional.
        offTime (long): The duration that the output drive remains
            non-active, in millis. Optional.

    Returns:
        int: The DNP3 status code of the response, as an integer.
    """
    print(deviceName, indexes, opType, tcCode, count, onTime, offTime)
    return 0


def freezeAnalogs(deviceName, indexes=None):
    """Issues a freeze command on the given analog outputs.

    Args:
        deviceName (str): The name of the DNP3 device driver.
        indexes (list[object]): An optional list of specific indexes on
            which to issue the freeze command.
    """
    print(deviceName, indexes)


def freezeAnalogsAtTime(deviceName, absoluteTime, intervalTime, indexes=None):
    """Issues a freeze command on the given analog outputs at the given
    time for the specified duration.

    Args:
        deviceName (str): The name of the DNP3 device driver.
        absoluteTime (int): The absolute time at which to freeze, in
            millis.
        intervalTime (int): The interval at which to periodically
            freeze, in millis.
        indexes (list[object]): An optional list of specific indexes on
            which to issue the freeze command. Optional.
    """
    print(deviceName, absoluteTime, intervalTime, indexes)


def freezeCounters(deviceName, indexes=None):
    """Issues a freeze command on the given counters.

    Args:
        deviceName (str): The name of the DNP3 device driver.
        indexes (list[object]): An optional list of specific indexes on
            which to issue the freeze command. Optional.
    """
    print(deviceName, indexes)


def freezeCountersAtTime(deviceName, absoluteTime, intervalTime, indexes=None):
    """Issues a freeze command on the given counters at the given time
    for the specified duration.

    Args:
        deviceName (str): The name of the DNP3 device driver.
        absoluteTime (int): The absolute time at which to freeze, in
            millis.
        intervalTime (int): The interval at which to periodically
            freeze, in millis.
        indexes (list[object]): An optional list of specific indexes on
            which to issue the freeze command. Optional.
    """
    print(deviceName, absoluteTime, intervalTime, indexes)


def selectOperateAnalog(deviceName, index, value, variation=None):
    """Issues a Select-And-Operate command to set an analog value in an
    analog output point.

    Args:
        deviceName (str): The name of the DNP3 device driver.
        index (int): The index of the object to be modified in the
            outstation.
        value (object): The analog value that is requested (of type int,
            short, float, or double).
        variation (int): The DNP3 object variation to use in the
            request. Optional.

    Returns:
        int: The DNP3 status code of the response, as an integer.
    """
    print(deviceName, index, value, variation)


def selectOperateBinary(
    deviceName,
    indexes,
    opType,
    tcCode=None,
    count=None,
    onTime=None,
    offTime=None,
):
    """Issues a Select-And-Operate command for digital control
    operations at binary output points (CROB).

    Args:
        deviceName: The name of the DNP3 device driver.
        indexes (list[object]): A list of indexes of the objects to be
            modified in the outstation.
        opType (int): The type of operation. 0=NUL, 1=PULSE_ON,
            2=PULSE_OFF, 3=LATCH_ON, 4=LATCH_OFF
        tcCode (int): The Trip-Close code, used in conjunction with the
            opType. 0=NUL, 1=CLOSE, 2=TRIP. Optional.
        count (int): The number of times the outstation shall execute
            the operation. Optional.
        onTime (int): The duration that the output drive remains active,
            in millis. Optional.
        offTime (int): The duration that the output drive remains
            non-active, in millis. Optional.

    Returns:
        int: The DNP3 status code of the response, as an integer.
    """
    print(deviceName, indexes, opType, tcCode, count, onTime, offTime)
    return 0
