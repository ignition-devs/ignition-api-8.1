from typing import Any, Dict, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from dev.coatl.helper.types import AnyStr

def executeAndDistribute(
    path: AnyStr,
    project: AnyStr = ...,
    parameters: Optional[Dict[AnyStr, int]] = ...,
    action: Optional[AnyStr] = ...,
    actionSettings: Optional[Dict[AnyStr, Any]] = ...,
) -> None: ...
def executeReport(
    path: AnyStr,
    project: AnyStr = ...,
    parameters: Optional[Dict[AnyStr, int]] = ...,
    fileType: AnyStr = ...,
) -> Any: ...
def getReportNamesAsDataset(
    project: Optional[AnyStr] = ..., includeReportName: bool = ...
) -> BasicDataset: ...
def getReportNamesAsList(project: Optional[AnyStr] = ...) -> List[AnyStr]: ...
