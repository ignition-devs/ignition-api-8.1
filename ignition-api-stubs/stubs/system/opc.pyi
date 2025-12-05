from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common.model.values import (
    BasicQualifiedValue,
    QualityCode,
)
from com.inductiveautomation.ignition.common.opc import BasicOPCBrowseElement
from com.inductiveautomation.ignition.common.script.builtin import AbstractOPCUtilities
from com.inductiveautomation.ignition.common.script.builtin.ialabs import OPCBrowseTag

BrowseServerResult = List[Union[BasicOPCBrowseElement, AbstractOPCUtilities.PyOPCTag]]

def browse(
    opcServer: Union[str, unicode],
    device: Union[str, unicode],
    folderPath: Union[str, unicode],
    opcItemPath: Union[str, unicode],
) -> List[OPCBrowseTag]: ...
def browseServer(
    opcServer: Union[str, unicode], nodeId: Union[str, unicode]
) -> BrowseServerResult: ...
def browseSimple(
    opcServer: Union[str, unicode],
    device: Union[str, unicode],
    folderPath: Union[str, unicode],
    opcItemPath: Union[str, unicode],
) -> List[OPCBrowseTag]: ...
def getServerState(opcServer: Union[str, unicode]) -> Union[str, unicode, None]: ...
def getServers(includeDisabled: Optional[bool] = ...) -> List[Union[str, unicode]]: ...
def isServerEnabled(serverName: Union[str, unicode]) -> bool: ...
def readValue(
    opcServer: Union[str, unicode], itemPath: Union[str, unicode]
) -> BasicQualifiedValue: ...
def readValues(
    opcServer: Union[str, unicode], itemPaths: List[Union[str, unicode]]
) -> List[BasicQualifiedValue]: ...
def setServerEnabled(serverName: Union[str, unicode], enabled: bool) -> None: ...
def writeValue(
    opcServer: Union[str, unicode], itemPath: Union[str, unicode], value: Any
) -> QualityCode: ...
def writeValues(
    opcServer: Union[str, unicode],
    itemPaths: List[Union[str, unicode]],
    values: List[Any],
) -> List[QualityCode]: ...
