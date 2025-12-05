from typing import Any, Callable, Dict, List, Optional, Union

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import (
    BasicQualifiedValue,
    QualityCode,
)
from com.inductiveautomation.ignition.common.sqltags.history.annotations import (
    Annotation,
)
from java.util import Date

DEFAULT_TIMEOUT_MILLIS: int
LEGACY_DEFAULT_TIMEOUT_MILLIS: int
TAG_PATH: Any

def browse(
    path: Union[str, unicode], filter: Optional[Dict[Union[str, unicode], Any]] = ...
) -> Results: ...
def browseHistoricalTags(
    path: Union[str, unicode],
    nameFilters: Optional[List[Union[str, unicode]]] = ...,
    maxSize: Optional[int] = ...,
    continuationPoint: Optional[Any] = ...,
) -> Results: ...
def configure(
    basePath: Union[str, unicode],
    tags: List[Dict[Union[str, unicode], Any]],
    collisionPolicy: Union[str, unicode] = ...,
) -> List[QualityCode]: ...
def copy(
    tags: List[Union[str, unicode]],
    destination: Union[str, unicode],
    collisionPolicy: Union[str, unicode] = ...,
) -> List[QualityCode]: ...
def deleteAnnotations(
    paths: List[Union[str, unicode]], storageIds: List[Union[str, unicode]]
) -> List[BasicQualifiedValue]: ...
def deleteTags(tagPaths: List[Union[str, unicode]]) -> List[QualityCode]: ...
def exists(tagPath: Union[str, unicode]) -> bool: ...
def exportTags(
    filePath: Union[str, unicode, None] = ...,
    tagPaths: Optional[List[Union[str, unicode]]] = ...,
    recursive: bool = ...,
    exportType: Union[str, unicode] = ...,
) -> Union[str, unicode, None]: ...
def getConfiguration(
    basePath: Union[str, unicode], recursive: bool = ...
) -> List[Dict[Union[str, unicode], Any]]: ...
def importTags(
    filePath: Union[str, unicode],
    basePath: Union[str, unicode],
    collisionPolicy: Union[str, unicode] = ...,
) -> List[QualityCode]: ...
def isOverlaysEnabled() -> bool: ...
def move(
    tags: List[Union[str, unicode]],
    destination: Union[str, unicode],
    collisionPolicy: Union[str, unicode] = ...,
) -> List[QualityCode]: ...
def query(
    provider: Union[str, unicode, None] = ...,
    query: Optional[Dict[Union[str, unicode], Any]] = ...,
    limit: Optional[int] = ...,
    continuation: Union[str, unicode, None] = ...,
) -> Results: ...
def queryAnnotations(
    paths: List[Union[str, unicode]],
    startTime: Optional[Date] = ...,
    endTime: Optional[Date] = ...,
    types: Optional[List[Union[str, unicode]]] = ...,
) -> List[Annotation]: ...
def queryTagCalculations(
    paths: List[Union[str, unicode]],
    calculations: List[Union[str, unicode]],
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    rangeHours: Optional[int] = ...,
    rangeMinutes: Optional[int] = ...,
    aliases: Optional[List[Union[str, unicode]]] = ...,
    includeBoundingValues: bool = ...,
    validatesSCExec: bool = ...,
    noInterpolation: bool = ...,
    ignoreBadQuality: bool = ...,
) -> BasicDataset: ...
def queryTagDensity(
    paths: List[Union[str, unicode]], startDate: Date, endDate: Date
) -> BasicDataset: ...
def queryTagHistory(
    paths: List[Union[str, unicode]],
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    returnSize: int = ...,
    aggregationMode: Union[str, unicode] = ...,
    returnFormat: Union[str, unicode] = ...,
    columnNames: Optional[List[Union[str, unicode]]] = ...,
    intervalHours: Optional[int] = ...,
    intervalMinutes: Optional[int] = ...,
    rangeHours: Optional[int] = ...,
    rangeMinutes: Optional[int] = ...,
    aggregationModes: Optional[List[Union[str, unicode]]] = ...,
    includeBoundingValues: Optional[bool] = ...,
    validateSCExec: Optional[bool] = ...,
    noInterpolation: Optional[bool] = ...,
    ignoreBadQuality: Optional[bool] = ...,
    timeout: Optional[int] = ...,
    intervalSeconds: Optional[int] = ...,
    rangeSeconds: Optional[int] = ...,
) -> BasicDataset: ...
def readAsync(
    tagPaths: List[Union[str, unicode]], callback: Callable[..., Any]
) -> None: ...
def readBlocking(
    tagPaths: List[Union[str, unicode]], timeout: int = ...
) -> List[BasicQualifiedValue]: ...
def rename(
    tag: Union[str, unicode],
    newName: Union[str, unicode],
    collisionPollicy: Union[str, unicode] = ...,
) -> QualityCode: ...
def requestGroupExecution(
    provider: Union[str, unicode], tagGroup: Union[str, unicode]
) -> None: ...
def setOverlaysEnabled(enabled: bool) -> None: ...
def storeAnnotations(
    paths: List[Union[str, unicode]],
    startTimes: Optional[List[Date]] = ...,
    endTimes: Optional[List[Date]] = ...,
    types: Optional[List[Annotation]] = ...,
    data: Optional[List[Union[str, unicode]]] = ...,
    storageIds: Optional[List[int]] = ...,
    deleted: Optional[List[bool]] = ...,
) -> List[BasicQualifiedValue]: ...
def storeTagHistory(
    historyprovider: Union[str, unicode],
    tagprovider: Union[str, unicode],
    paths: List[Union[str, unicode]],
    values: List[Any],
    qualities: Optional[List[int]] = ...,
    timestamps: Optional[List[Date]] = ...,
) -> None: ...
def writeAsync(
    tagPaths: List[Union[str, unicode]],
    values: List[Any],
    callback: Optional[Callable[..., Any]] = ...,
) -> None: ...
def writeBlocking(
    tagPaths: List[Union[str, unicode]], values: List[Any], timeout: int = ...
) -> List[QualityCode]: ...
