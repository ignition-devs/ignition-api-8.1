from typing import Any, List, Optional

from dev.coatl.helper.types import AnyStr
from system.bacnet.enumerated import ObjectType, PropertyIdentifier

def readRaw(
    deviceName: AnyStr,
    objectType: ObjectType,
    objectId: int,
    propertyId: PropertyIdentifier,
    propertyArrayIndex: Optional[int] = ...,
) -> Any: ...
def readRawMultiple(
    deviceName: AnyStr,
    objectTypes: List[ObjectType],
    objectIds: List[int],
    propertyIds: List[PropertyIdentifier],
    propertyArrayIndices: Optional[List[int]] = ...,
) -> List[Any]: ...
def synchronizeTime(deviceName: AnyStr) -> None: ...
def synchronizeTimeUtc(deviceName: AnyStr) -> None: ...
def writeRaw(
    deviceName: AnyStr,
    objectType: ObjectType,
    objectId: int,
    propertyId: PropertyIdentifier,
    value: Any,
    priority: int = ...,
    propertyArrayIndex: Optional[int] = ...,
) -> None: ...
def writeRawMultiple(
    deviceName: AnyStr,
    objectTypes: List[ObjectType],
    objectIds: List[int],
    propertyIds: List[PropertyIdentifier],
    values: List[Any],
    priorities: Optional[List[int]] = ...,
    propertyArrayIndices: Optional[List[int]] = ...,
) -> None: ...
def writeWithPriority(
    deviceName: AnyStr, objectType: int, objectId: int, value: Any, priority: int
) -> None: ...

# Names in __all__ with no definition:
#   enumerated
#   enums
