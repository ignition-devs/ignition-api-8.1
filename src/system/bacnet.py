"""BACnet Functions.

The following functions are used with the BACnet driver and a BACnet/IP
device.
"""

from __future__ import print_function

__all__ = ["synchronizeTime", "synchronizeTimeUtc", "writeWithPriority"]


def synchronizeTime(deviceName):
    """Notifies the remote device of the correct current time, which is
    the system time (factoring in timezone and DST) of the server
    Ignition is running on.

    Args:
        deviceName (str): The name of the configured BACnet/IP device
            instance to write from.
    """
    print(deviceName)


def synchronizeTimeUtc(deviceName):
    """Notifies the remote device of the correct current time in UTC.

    Args:
        deviceName (str): The name of the configured BACnet/IP device
            instance to write from.
    """
    print(deviceName)


def writeWithPriority(deviceName, objectType, objectId, value, priority):
    """Write to the Present_Value attribute of an object with a custom
    priority level.

    Args:
        deviceName (str): The name of the configured BACnet/IP device
            instance to write from.
        objectType (int): The numeric id of the objectType of the object
            instance being written to. See the objectType reference
            table below.
        objectId (int): The object instance number to write to.
        value (object): The value to write. Clearing a value can be
            accomplished by writing a None value.
        priority (int): The priority level to write the value at. Must
            be in the range [1...16].
    """
    print(deviceName, objectType, objectId, value, priority)
