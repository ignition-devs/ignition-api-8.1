from typing import Any, Dict, List, Tuple, Union

from com.inductiveautomation.ignition.common import BasicDataset

def copyEquipment(
    equipmentSource: Union[str, unicode],
    newEquipmentName: Union[str, unicode],
    enabled: bool,
    activeAddress: Union[str, unicode],
    activePort: int,
    passiveAddress: Union[str, unicode],
    passivePort: int,
    deviceId: int,
    dbTablePrefix: Union[str, unicode, None] = ...,
    description: Union[str, unicode, None] = ...,
) -> None: ...
def deleteToolProgram(ppid: Union[str, unicode]) -> None: ...
def enableDisableEquipment(
    enable: bool, names: Tuple[Union[str, unicode], ...]
) -> List[unicode]: ...
def getResponse(
    transactionID: int,
    equipment: Union[str, unicode],
    timeout: int = ...,
    poll: int = ...,
) -> Any: ...
def getToolProgram(ppid: Union[str, unicode]) -> Dict[Union[str, unicode], Any]: ...
def getToolProgramDataset() -> BasicDataset: ...
def sendRequest(
    streamFunction: Union[str, unicode],
    reply: bool,
    body: Any,
    equipment: Union[str, unicode],
) -> int: ...
def sendResponse(
    transactionID: int,
    systemBytes: int,
    streamFunction: Union[str, unicode],
    body: Any,
    equipment: Union[str, unicode],
) -> None: ...
def startSimEventRun(
    simulatorName: Union[str, unicode], eventRunName: Union[str, unicode]
) -> None: ...
def toDataSet(secsObject: Any) -> BasicDataset: ...
def toTreeDataSet(dataset: BasicDataset) -> BasicDataset: ...
