from typing import Any, List

from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import QualityCode
from com.inductiveautomation.ignition.common.sqltags.history import AggregateInfo
from com.inductiveautomation.opccom.hda import AttributeInfo, ReadResult
from dev.coatl.helper.types import AnyStr
from java.util import Date

def browse(root: AnyStr) -> List[Results]: ...
def getAggregates(serverName: AnyStr) -> List[AggregateInfo]: ...
def getAttributes(serverName: AnyStr) -> List[AttributeInfo]: ...
def getServers() -> List[AnyStr]: ...
def insert(
    serverName: AnyStr, itemId: AnyStr, value: Any, date: Any, quality: int
) -> QualityCode: ...
def insertReplace(
    serverName: AnyStr, itemId: AnyStr, value: Any, date: Date, quality: int
) -> QualityCode: ...
def isServerAvailable(serverName: AnyStr) -> bool: ...
def readAttributes(
    serverName: AnyStr,
    itemId: AnyStr,
    attributeIds: List[AnyStr],
    startDate: Date,
    endDate: Date,
) -> List[ReadResult]: ...
def readProcessed(
    serverName: AnyStr,
    itemIds: List[AnyStr],
    startDate: Date,
    endDate: Date,
    resampleIntervalMS: int,
    aggregates: List[Any],
) -> List[ReadResult]: ...
def readRaw(
    serverName: AnyStr,
    itemIds: List[AnyStr],
    startDate: Date,
    endDate: Date,
    maxValues: int,
    boundingValues: bool,
) -> List[Any]: ...
def replace(
    serverName: AnyStr, itemId: AnyStr, value: Any, date: Date, quality: int
) -> QualityCode: ...
