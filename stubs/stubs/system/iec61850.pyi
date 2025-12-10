from typing import Any, Dict, List, Union

def cancel(
    deviceName: Union[str, unicode], mapParams: Dict[Union[str, unicode], Any]
) -> None: ...
def getControlParams(
    deviceName: Union[str, unicode],
) -> List[Dict[Union[str, unicode], Any]]: ...
def listFiles(
    deviceName: Union[str, unicode], remoteFilePath: Union[str, unicode, None] = ...
) -> List[Union[str, unicode]]: ...
def operate(
    deviceName: Union[str, unicode],
    mapParams: Dict[Union[str, unicode], Any],
    controlValue: float,
) -> None: ...
def readFile(
    deviceName: Union[str, unicode],
    remoteFilePath: Union[str, unicode],
    localFilePath: Union[str, unicode],
) -> None: ...
def select(
    deviceName: Union[str, unicode],
    mapParams: Dict[Union[str, unicode], Any],
    value: float,
) -> None: ...
def writeFile(
    deviceName: Union[str, unicode],
    localFilePath: Union[str, unicode],
    remoteFilePath: Union[str, unicode],
) -> None: ...
