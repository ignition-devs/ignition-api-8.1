from typing import List, Optional, Union

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.messages import UIResponse
from java.util import Date

def getGroups() -> List[Union[str, unicode]]: ...
def queryAgentHistory(
    groupIds: Optional[List[Union[str, unicode]]] = ...,
    agentIds: Optional[List[Union[str, unicode]]] = ...,
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    limit: int = ...,
) -> BasicDataset: ...
def queryAgentStatus(
    groupIds: Optional[List[Union[str, unicode]]] = ...,
    agentIds: Optional[List[Union[str, unicode]]] = ...,
    isConnected: bool = ...,
) -> BasicDataset: ...
def runTask(taskname: Union[str, unicode]) -> UIResponse: ...
