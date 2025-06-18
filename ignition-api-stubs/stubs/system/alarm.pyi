from typing import Any, Dict, List, Optional, Tuple, Union

from com.inductiveautomation.ignition.common.alarming.evaluation import ShelvedPath
from com.inductiveautomation.ignition.common.alarming.query import AlarmQueryResultImpl
from dev.coatl.helper.types import AnyStr
from java.util import Date

def acknowledge(
    alarmIds: List[AnyStr], notes: AnyStr, username: Optional[AnyStr] = ...
) -> List[AnyStr]: ...
def cancel(alarmIds: List[AnyStr]) -> None: ...
def createRoster(name: AnyStr, description: AnyStr) -> None: ...
def getRosters() -> Dict[AnyStr, List[AnyStr]]: ...
def getShelvedPaths() -> List[ShelvedPath]: ...
def listPipelines(projectName: AnyStr = ...) -> List[AnyStr]: ...
def queryJournal(
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    journalName: Optional[AnyStr] = ...,
    priority: Optional[List[Union[AnyStr, int]]] = ...,
    state: Optional[List[Union[AnyStr, int]]] = ...,
    path: Optional[List[AnyStr]] = ...,
    source: Optional[List[AnyStr]] = ...,
    displaypath: Optional[List[AnyStr]] = ...,
    all_properties: Optional[List[Tuple[AnyStr, AnyStr, Any]]] = ...,
    any_properties: Optional[List[Tuple[AnyStr, AnyStr, Any]]] = ...,
    defined: Optional[List[AnyStr]] = ...,
    includeData: Optional[bool] = ...,
    includeSystem: Optional[bool] = ...,
    includeShelved: Optional[bool] = ...,
    isSystem: Optional[bool] = ...,
    provider: Optional[List[AnyStr]] = ...,
) -> AlarmQueryResultImpl: ...
def queryStatus(
    priority: Optional[List[Union[AnyStr, int]]] = ...,
    state: Optional[List[Union[AnyStr, int]]] = ...,
    path: Optional[List[AnyStr]] = ...,
    source: Optional[List[AnyStr]] = ...,
    displaypath: Optional[List[AnyStr]] = ...,
    all_properties: Optional[List[Tuple[AnyStr, AnyStr, Any]]] = ...,
    any_properties: Optional[List[Tuple[AnyStr, AnyStr, Any]]] = ...,
    defined: Optional[List[AnyStr]] = ...,
    includeShelved: bool = ...,
) -> AlarmQueryResultImpl: ...
def shelve(
    path: List[AnyStr], timeoutSeconds: int = ..., timeoutMinutes: int = ...
) -> None: ...
def unshelve(path: List[AnyStr]) -> None: ...
