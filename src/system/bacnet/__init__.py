"""BACnet Functions.

The following functions are used with the BACnet driver and a BACnet/IP
device.
"""

from __future__ import print_function

__all__ = [
    "enumerated",
    "enums",
    "readRaw",
    "readRawMultiple",
    "synchronizeTime",
    "synchronizeTimeUtc",
    "writeRaw",
    "writeRawMultiple",
    "writeWithPriority",
]

from typing import Any, List, Optional

from dev.thecesrom.helper.types import AnyStr
from system.bacnet.enumerated import ObjectType, PropertyIdentifier


def readRaw(
    deviceName,  # type: AnyStr
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


def readRawMultiple(
    deviceName,  # type: AnyStr
    objectTypes,  # type: List[ObjectType]
    objectIds,  # type: List[int]
    propertyIds,  # type: List[PropertyIdentifier]
):
    # type: (...) -> List[Any]
    """This function is the bulk version of system.bacnet.readRaw to
    allow multiple object/property combinations to be read
    simultaneously from a single request.

    Args:
        deviceName: The name of the configured BACnet/IP device instance
            to read from.
        objectTypes: The numeric ids of the objectType of the object
            instances being read from.
        objectIds: The object instance number to read.
        propertyIds: The PropertyIdentifier of the object instance being
            read.

    Returns:
        A list of Encodable objects corresponding to the properties
        being read.
    """
    print(deviceName, objectTypes, objectIds, propertyIds)
    return []


def synchronizeTime(deviceName):
    # type: (AnyStr) -> None
    """Notifies the remote device of the correct current time, which is
    the system time (factoring in timezone and DST) of the server
    Ignition is running on.

    Args:
        deviceName: The name of the configured BACnet/IP device instance
            to write from.
    """
    print(deviceName)


def synchronizeTimeUtc(deviceName):
    # type: (AnyStr) -> None
    """Notifies the remote device of the correct current time in UTC.

    Args:
        deviceName: The name of the configured BACnet/IP device instance
            to write from.
    """
    print(deviceName)


def writeRaw(
    deviceName,  # type: AnyStr
    objectType,  # type: ObjectType
    objectId,  # type: int
    propertyId,  # type: PropertyIdentifier
    value,  # type: Any
    priority=8,  # type: int
    propertyArrayIndex=None,  # type: Optional[int]
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


def writeRawMultiple(
    deviceName,  # type: AnyStr
    objectTypes,  # type: List[ObjectType]
    objectIds,  # type: List[int]
    propertyIds,  # type: List[PropertyIdentifier]
    values,  # type: List[Any]
    priorities=None,  # type: Optional[List[int]]
    propertyArrayIndices=None,  # type: Optional[List[int]]
):
    # type: (...) -> None
    """This function is the bulk version of system.bacnet.writeRaw by
    writing properties to objects provided equal-length lists of object
    types, object instance numbers, property IDs, values, priorities,
    and property array indices.

    Args:
        deviceName: Name of the configured BACnet/IP device instance to
            write from.
        objectTypes: A list of ObjectType(s) for the object instance
            being written to.
        objectIds: A list of object instance numbers to write to.
        propertyIds: A list of PropertyIdentifier(s) for the object
            instances being written to.
        values: A list of values to write.
        priorities: An optional list of priority levels to use when
            writing to commandable properties. All elements must be in
            the range [1..16]. Defaults to 8 for all properties when
            this parameter is omitted.
        propertyArrayIndices: An optional list of array indices
            corresponding to array properties being written. None should
            be specified as an element when writing to the entire array
            property or if the property is not an array. Defaults to a
            list of None when this parameter is omitted.
    """
    print(
        deviceName,
        objectTypes,
        objectIds,
        propertyIds,
        values,
        priorities,
        propertyArrayIndices,
    )


def writeWithPriority(deviceName, objectType, objectId, value, priority):
    # type: (AnyStr, int, int, Any, int) -> None
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
