from typing import Any, List, Union

from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import QualityCode
from com.inductiveautomation.ignition.common.sqltags.history import AggregateInfo
from com.inductiveautomation.opccom.hda import AttributeInfo, ReadResult
from java.util import Date

def browse(root: Union[str, unicode]) -> List[Results]: ...
def getAggregates(serverName: Union[str, unicode]) -> List[AggregateInfo]: ...
def getAttributes(serverName: Union[str, unicode]) -> List[AttributeInfo]: ...
def getServers() -> List[Union[str, unicode]]: ...
def insert(
    serverName: Union[str, unicode],
    itemId: Union[str, unicode],
    value: Any,
    date: Date,
    quality: int,
) -> QualityCode: ...
def insertReplace(
    serverName: Union[str, unicode],
    itemId: Union[str, unicode],
    value: Any,
    date: Date,
    quality: int,
) -> QualityCode: ...
def isServerAvailable(serverName: Union[str, unicode]) -> bool: ...
def readAttributes(
    serverName: Union[str, unicode],
    itemId: Union[str, unicode],
    attributeIds: List[Union[str, unicode]],
    startDate: Date,
    endDate: Date,
) -> List[ReadResult]: ...
def readProcessed(
    serverName: Union[str, unicode],
    itemIds: List[Union[str, unicode]],
    startDate: Date,
    endDate: Date,
    resampleIntervalMS: int,
    aggregates: List[Any],
) -> List[ReadResult]: ...
def readRaw(
    serverName: Union[str, unicode],
    itemIds: List[Union[str, unicode]],
    startDate: Date,
    endDate: Date,
    maxValues: int,
    boundingValues: bool,
) -> List[Any]: ...
def replace(
    serverName: Union[str, unicode],
    itemId: Union[str, unicode],
    value: Any,
    date: Date,
    quality: int,
) -> QualityCode: ...
