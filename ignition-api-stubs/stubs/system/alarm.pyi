from typing import Any, Dict, List, Optional, Tuple, Union

from com.inductiveautomation.ignition.common.alarming.evaluation import ShelvedPath
from com.inductiveautomation.ignition.common.alarming.query import AlarmQueryResultImpl
from java.util import Date

def acknowledge(
    alarmIds: List[Union[str, unicode]],
    notes: Union[str, unicode],
    username: Union[str, unicode, None] = ...,
) -> List[Union[str, unicode]]: ...
def cancel(alarmIds: List[Union[str, unicode]]) -> None: ...
def createRoster(
    name: Union[str, unicode], description: Union[str, unicode]
) -> None: ...
def getRosters() -> Dict[Union[str, unicode], List[Union[str, unicode]]]: ...
def getShelvedPaths() -> List[ShelvedPath]: ...
def listPipelines(
    projectName: Union[str, unicode] = ...,
) -> List[Union[str, unicode]]: ...
def queryJournal(
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    journalName: Union[str, unicode, None] = ...,
    priority: Optional[List[Union[str, unicode, int]]] = ...,
    state: Optional[List[Union[str, unicode, int]]] = ...,
    path: Optional[List[Union[str, unicode]]] = ...,
    source: Optional[List[Union[str, unicode]]] = ...,
    displaypath: Optional[List[Union[str, unicode]]] = ...,
    all_properties: Optional[
        List[Tuple[Union[str, unicode], Union[str, unicode], Any]]
    ] = ...,
    any_properties: Optional[
        List[Tuple[Union[str, unicode], Union[str, unicode], Any]]
    ] = ...,
    defined: Optional[List[Union[str, unicode]]] = ...,
    includeData: Optional[bool] = ...,
    includeSystem: Optional[bool] = ...,
    includeShelved: Optional[bool] = ...,
    isSystem: Optional[bool] = ...,
    provider: Optional[List[Union[str, unicode]]] = ...,
) -> AlarmQueryResultImpl: ...
def queryStatus(
    priority: Optional[List[Union[str, unicode, int]]] = ...,
    state: Optional[List[Union[str, unicode, int]]] = ...,
    path: Optional[List[Union[str, unicode]]] = ...,
    source: Optional[List[Union[str, unicode]]] = ...,
    displaypath: Optional[List[Union[str, unicode]]] = ...,
    all_properties: Optional[
        List[Tuple[Union[str, unicode], Union[str, unicode], Any]]
    ] = ...,
    any_properties: Optional[
        List[Tuple[Union[str, unicode], Union[str, unicode], Any]]
    ] = ...,
    defined: Optional[List[Union[str, unicode]]] = ...,
    includeShelved: bool = ...,
) -> AlarmQueryResultImpl: ...
def shelve(
    path: List[Union[str, unicode]],
    timeoutSeconds: int = ...,
    timeoutMinutes: int = ...,
) -> None: ...
def unshelve(path: List[Union[str, unicode]]) -> None: ...
