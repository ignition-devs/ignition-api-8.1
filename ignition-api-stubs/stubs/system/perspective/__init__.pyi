from typing import Any, Dict, List, Optional, Union

from com.inductiveautomation.ignition.common.script.adapters import PyJsonObjectAdapter
from dev.coatl.helper.types import AnyStr

def alterDock(
    dockId: AnyStr,
    config: Optional[Dict[AnyStr, Any]] = ...,
    sessionId: AnyStr = ...,
    pageId: AnyStr = ...,
) -> None: ...
def alterLogging(
    remoteLoggingEnabled: bool = ...,
    level: AnyStr = ...,
    remoteLoggingLevel: AnyStr = ...,
    sessionId: AnyStr = ...,
    pageId: AnyStr = ...,
) -> None: ...
def authenticationChallenge(
    sessionId: AnyStr = ...,
    pageId: AnyStr = ...,
    idp: AnyStr = ...,
    forceAuth: bool = ...,
    timeout: int = ...,
    payload: Optional[Dict[AnyStr, Any]] = ...,
    framing: AnyStr = ...,
) -> None: ...
def closeDock(id: AnyStr, sessionId: AnyStr = ..., pageId: AnyStr = ...) -> None: ...
def closePage(
    message: Optional[AnyStr] = ..., sessionId: AnyStr = ..., pageId: AnyStr = ...
) -> None: ...
def closePopup(id: AnyStr, sessionId: AnyStr = ..., pageId: AnyStr = ...) -> None: ...
def closeSession(message: Optional[AnyStr] = ..., sessionId: AnyStr = ...) -> None: ...
def download(
    filename: AnyStr,
    data: Any,
    contentType: Optional[AnyStr] = ...,
    sessionId: AnyStr = ...,
    pageId: AnyStr = ...,
) -> None: ...
def getProjectInfo() -> Dict[AnyStr, Any]: ...
def getSessionInfo(
    usernameFilter: Optional[AnyStr] = ..., projectFilter: Optional[AnyStr] = ...
) -> List[PyJsonObjectAdapter]: ...
def isAuthorized(
    isAllOf: bool, securityLevels: List[AnyStr], sessionId: AnyStr = ...
) -> bool: ...
def login(
    sessionId: AnyStr = ..., pageId: AnyStr = ..., forceAuth: bool = ...
) -> None: ...
def logout(
    sessionId: AnyStr = ..., pageId: AnyStr = ..., message: AnyStr = ...
) -> None: ...
def navigate(
    page: AnyStr,
    url: Optional[AnyStr] = ...,
    view: Optional[AnyStr] = ...,
    params: Optional[Dict[AnyStr, AnyStr]] = ...,
    sessionId: AnyStr = ...,
    pageId: AnyStr = ...,
    newTab: bool = ...,
) -> None: ...
def navigateBack(sessionId: AnyStr = ..., pageId: AnyStr = ...) -> None: ...
def navigateForward(sessionId: AnyStr = ..., pageId: AnyStr = ...) -> None: ...
def openDock(
    id: AnyStr,
    sessionId: AnyStr = ...,
    pageId: AnyStr = ...,
    params: Optional[Dict[AnyStr, AnyStr]] = ...,
) -> None: ...
def openPopup(
    id: AnyStr,
    view: AnyStr,
    params: Optional[Dict[AnyStr, Any]] = ...,
    title: AnyStr = ...,
    position: Optional[Dict[AnyStr, Union[int, AnyStr]]] = ...,
    showCloseIcon: bool = ...,
    draggable: bool = ...,
    resizable: bool = ...,
    modal: bool = ...,
    overlayDismiss: bool = ...,
    sessionId: AnyStr = ...,
    pageId: AnyStr = ...,
    viewPortBound: bool = ...,
) -> None: ...
def print(
    message: AnyStr,
    sessionId: AnyStr = ...,
    pageId: AnyStr = ...,
    destination: AnyStr = ...,
) -> None: ...
def refresh(sessionId: AnyStr = ..., pageId: AnyStr = ...) -> None: ...
def sendMessage(
    messageType: AnyStr,
    payload: Dict[AnyStr, AnyStr],
    scope: AnyStr = ...,
    sessionId: AnyStr = ...,
    pageId: AnyStr = ...,
) -> None: ...
def setTheme(name: AnyStr, sessionId: AnyStr = ..., pageId: AnyStr = ...) -> None: ...
def toggleDock(
    id: AnyStr,
    sessionId: AnyStr = ...,
    pageId: AnyStr = ...,
    params: Optional[Dict[AnyStr, AnyStr]] = ...,
) -> None: ...
def togglePopup(
    id: AnyStr,
    view: AnyStr,
    params: Optional[Dict[AnyStr, Any]],
    title: AnyStr = ...,
    position: Optional[Dict[AnyStr, Union[int, AnyStr]]] = ...,
    showCloseIcon: bool = ...,
    draggable: bool = ...,
    resizable: bool = ...,
    modal: bool = ...,
    overlayDismiss: bool = ...,
    sessionId: AnyStr = ...,
    pageId: AnyStr = ...,
    viewPortBound: bool = ...,
) -> None: ...
def vibrateDevice(duration: int, sessionId: AnyStr = ...) -> None: ...
