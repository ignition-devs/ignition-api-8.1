"""BACnet Functions.

The following functions are used with the BACnet driver and a BACnet/IP
device.
"""

from __future__ import print_function

__all__ = [
    "enumerated",
    "enums",
    "readRaw",
    "synchronizeTime",
    "synchronizeTimeUtc",
    "writeRaw",
    "writeWithPriority",
]

from typing import Any, List, Optional

from java.lang import String
from system.bacnet.enumerated import ObjectType, PropertyIdentifier


def readRaw(
    deviceName,  # type: String
    objectType,  # type: ObjectType
    objectId,  # type: int
    propertyId,  # type: PropertyIdentifier
    propertyArrayIndex=None,  # type: Optional[int]
):
    # type: (...) -> List[Any]
    """Read from any BACnet object not explicitly supported by the
    BACnet driver.

    Args:
        deviceName: The name of the configured BACnet/IP device instance
            to read from.
        objectType: The numeric id of the objectType of the object
            instance being read from.
        objectId: The object instance number to read.
        propertyId: The PropertyIdentifier of the object instance being
            read.
        propertyArrayIndex: The array index of the property to read
            from. This parameter is optional and should not be used when
            reading from the entire array or if the property is not an
            array.
    """
    print(deviceName, objectType, objectId, propertyId, propertyArrayIndex)
    return [0]


def synchronizeTime(deviceName):
    # type: (String) -> None
    """Notifies the remote device of the correct current time, which is
    the system time (factoring in timezone and DST) of the server
    Ignition is running on.

    Args:
        deviceName: The name of the configured BACnet/IP device instance
            to write from.
    """
    print(deviceName)


def synchronizeTimeUtc(deviceName):
    # type: (String) -> None
    """Notifies the remote device of the correct current time in UTC.

    Args:
        deviceName: The name of the configured BACnet/IP device instance
            to write from.
    """
    print(deviceName)


def writeRaw(
    deviceName,  # type: String
    objectType,  # type: ObjectType
    objectId,  # type: int
    propertyId,  # type: PropertyIdentifier
    value,  # type: Any
    priority,  # type: int
    propertyArrayIndex,  # type: int
):
    # type: (...) -> None
    """Write to any BACnet object not explicitly supported by the BACnet
    driver.

    Args:
        deviceName: The name of the configured BACnet/IP device instance
            to write from.
        objectType: The numeric id of the objectType of the object
            instance being written to.
        objectId: The object instance number to write to.
        propertyId: The PropertyIdentifier of the object instance being
            written to.
        value: The value to write. Clearing a value can be accomplished
            by writing a None value.
        priority: The priority level to use when writing to commandable
            properties. Must match a level in the standard BACnet
            priority array (a value from 1 to 16). See the Priority
            Reference table below. This parameter is optional and
            defaults to 8 if not specified.
        propertyArrayIndex: The array index of the property to write to.
            This parameter is optional and should not be used when
            writing to the entire array or if the property is not an
            array.
    """
    print(
        deviceName,
        objectType,
        objectId,
        propertyId,
        value,
        priority,
        propertyArrayIndex,
    )


def writeWithPriority(deviceName, objectType, objectId, value, priority):
    # type: (String, int, int, Any, int) -> None
    """Write to the Present_Value attribute of an object with a custom
    priority level.

    Args:
        deviceName: The name of the configured BACnet/IP device instance
            to write from.
        objectType: The numeric id of the objectType of the object
            instance being written to.
        objectId: The object instance number to write to.
        value: The value to write. Clearing a value can be accomplished
            by writing a None value.
        priority: The priority level to write the value at. Must be in
            the range [1...16].
    """
    print(deviceName, objectType, objectId, value, priority)
