from typing import Any, List, Optional, Union

from system.bacnet.enumerated import ObjectType, PropertyIdentifier

def readRaw(
    deviceName: Union[str, unicode],
    objectType: ObjectType,
    objectId: int,
    propertyId: PropertyIdentifier,
    propertyArrayIndex: Optional[int] = ...,
) -> Any: ...
def readRawMultiple(
    deviceName: Union[str, unicode],
    objectTypes: List[ObjectType],
    objectIds: List[int],
    propertyIds: List[PropertyIdentifier],
    propertyArrayIndices: Optional[List[int]] = ...,
) -> List[Any]: ...
def synchronizeTime(deviceName: Union[str, unicode]) -> None: ...
def synchronizeTimeUtc(deviceName: Union[str, unicode]) -> None: ...
def writeRaw(
    deviceName: Union[str, unicode],
    objectType: ObjectType,
    objectId: int,
    propertyId: PropertyIdentifier,
    value: Any,
    priority: int = ...,
    propertyArrayIndex: Optional[int] = ...,
) -> None: ...
def writeRawMultiple(
    deviceName: Union[str, unicode],
    objectTypes: List[ObjectType],
    objectIds: List[int],
    propertyIds: List[PropertyIdentifier],
    values: List[Any],
    priorities: Optional[List[int]] = ...,
    propertyArrayIndices: Optional[List[int]] = ...,
) -> None: ...
def writeWithPriority(
    deviceName: Union[str, unicode],
    objectType: int,
    objectId: int,
    value: Any,
    priority: int,
) -> None: ...

# Names in __all__ with no definition:
#   enumerated
#   enums
