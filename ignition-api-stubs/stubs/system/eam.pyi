from typing import List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.messages import UIResponse
from dev.coatl.helper.types import AnyStr
from java.util import Date

def getGroups() -> List[AnyStr]: ...
def queryAgentHistory(
    groupIds: Optional[List[AnyStr]] = ...,
    agentIds: Optional[List[AnyStr]] = ...,
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    limit: int = ...,
) -> BasicDataset: ...
def queryAgentStatus(
    groupIds: Optional[List[AnyStr]] = ...,
    agentIds: Optional[List[AnyStr]] = ...,
    isConnected: bool = ...,
) -> BasicDataset: ...
def runTask(taskname: AnyStr) -> UIResponse: ...
