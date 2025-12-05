from typing import Any, Dict, List, Optional, Union

from com.inductiveautomation.ignition.common import BasicDataset

def executeAndDistribute(
    path: Union[str, unicode],
    project: Union[str, unicode] = ...,
    parameters: Optional[Dict[Union[str, unicode], int]] = ...,
    action: Union[str, unicode, None] = ...,
    actionSettings: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> None: ...
def executeReport(
    path: Union[str, unicode],
    project: Union[str, unicode] = ...,
    parameters: Optional[Dict[Union[str, unicode], int]] = ...,
    fileType: Union[str, unicode] = ...,
) -> Any: ...
def getReportNamesAsDataset(
    project: Union[str, unicode, None] = ..., includeReportName: bool = ...
) -> BasicDataset: ...
def getReportNamesAsList(
    project: Union[str, unicode, None] = ...,
) -> List[Union[str, unicode]]: ...
