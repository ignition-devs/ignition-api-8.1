from typing import Any, Callable, Dict, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import (
    BasicQualifiedValue,
    QualityCode,
)
from com.inductiveautomation.ignition.common.sqltags.history.annotations import (
    Annotation,
)
from dev.coatl.helper.types import AnyStr
from java.util import Date

DEFAULT_TIMEOUT_MILLIS: int
LEGACY_DEFAULT_TIMEOUT_MILLIS: int
TAG_PATH: Any

def browse(path: AnyStr, filter: Optional[Dict[AnyStr, Any]] = ...) -> Results: ...
def browseHistoricalTags(
    path: AnyStr,
    nameFilters: Optional[List[AnyStr]] = ...,
    maxSize: Optional[int] = ...,
    continuationPoint: Optional[Any] = ...,
) -> Results: ...
def configure(
    basePath: AnyStr, tags: List[Dict[AnyStr, Any]], collisionPolicy: AnyStr = ...
) -> List[QualityCode]: ...
def copy(
    tags: List[AnyStr], destination: AnyStr, collisionPolicy: AnyStr = ...
) -> List[QualityCode]: ...
def deleteAnnotations(
    paths: List[AnyStr], storageIds: List[AnyStr]
) -> List[BasicQualifiedValue]: ...
def deleteTags(tagPaths: List[AnyStr]) -> List[QualityCode]: ...
def exists(tagPath: AnyStr) -> bool: ...
def exportTags(
    filePath: Optional[AnyStr] = ...,
    tagPaths: Optional[List[AnyStr]] = ...,
    recursive: bool = ...,
    exportType: AnyStr = ...,
) -> Optional[AnyStr]: ...
def getConfiguration(
    basePath: AnyStr, recursive: bool = ...
) -> List[Dict[AnyStr, Any]]: ...
def importTags(
    filePath: AnyStr, basePath: AnyStr, collisionPolicy: AnyStr = ...
) -> List[QualityCode]: ...
def isOverlaysEnabled() -> bool: ...
def move(
    tags: List[AnyStr], destination: AnyStr, collisionPolicy: AnyStr = ...
) -> List[QualityCode]: ...
def query(
    provider: Optional[AnyStr] = ...,
    query: Optional[Dict[AnyStr, Any]] = ...,
    limit: Optional[int] = ...,
    continuation: Optional[AnyStr] = ...,
) -> Results: ...
def queryAnnotations(
    paths: List[AnyStr],
    startTime: Optional[Date] = ...,
    endTime: Optional[Date] = ...,
    types: Optional[List[AnyStr]] = ...,
) -> List[Annotation]: ...
def queryTagCalculations(
    paths: List[AnyStr],
    calculations: List[AnyStr],
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    rangeHours: Optional[int] = ...,
    rangeMinutes: Optional[int] = ...,
    aliases: Optional[List[AnyStr]] = ...,
    includeBoundingValues: bool = ...,
    validatesSCExec: bool = ...,
    noInterpolation: bool = ...,
    ignoreBadQuality: bool = ...,
) -> BasicDataset: ...
def queryTagDensity(
    paths: List[AnyStr], startDate: Date, endDate: Date
) -> BasicDataset: ...
def queryTagHistory(
    paths: List[AnyStr],
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    returnSize: int = ...,
    aggregationMode: AnyStr = ...,
    returnFormat: AnyStr = ...,
    columnNames: Optional[List[AnyStr]] = ...,
    intervalHours: Optional[int] = ...,
    intervalMinutes: Optional[int] = ...,
    rangeHours: Optional[int] = ...,
    rangeMinutes: Optional[int] = ...,
    aggregationModes: Optional[List[AnyStr]] = ...,
    includeBoundingValues: Optional[bool] = ...,
    validateSCExec: Optional[bool] = ...,
    noInterpolation: Optional[bool] = ...,
    ignoreBadQuality: Optional[bool] = ...,
    timeout: Optional[int] = ...,
    intervalSeconds: Optional[int] = ...,
    rangeSeconds: Optional[int] = ...,
) -> BasicDataset: ...
def readAsync(tagPaths: List[AnyStr], callback: Callable[..., Any]) -> None: ...
def readBlocking(
    tagPaths: List[AnyStr], timeout: int = ...
) -> List[BasicQualifiedValue]: ...
def rename(
    tag: AnyStr, newName: AnyStr, collisionPollicy: AnyStr = ...
) -> QualityCode: ...
def requestGroupExecution(provider: AnyStr, tagGroup: AnyStr) -> None: ...
def setOverlaysEnabled(enabled: bool) -> None: ...
def storeAnnotations(
    paths: List[AnyStr],
    startTimes: Optional[List[Date]] = ...,
    endTimes: Optional[List[Date]] = ...,
    types: Optional[List[Annotation]] = ...,
    data: Optional[List[AnyStr]] = ...,
    storageIds: Optional[List[int]] = ...,
    deleted: Optional[List[bool]] = ...,
) -> List[BasicQualifiedValue]: ...
def storeTagHistory(
    historyprovider: AnyStr,
    tagprovider: AnyStr,
    paths: List[AnyStr],
    values: List[Any],
    qualities: Optional[List[int]] = ...,
    timestamps: Optional[List[Date]] = ...,
) -> None: ...
def writeAsync(
    tagPaths: List[AnyStr],
    values: List[Any],
    callback: Optional[Callable[..., Any]] = ...,
) -> None: ...
def writeBlocking(
    tagPaths: List[AnyStr], values: List[Any], timeout: int = ...
) -> List[QualityCode]: ...
