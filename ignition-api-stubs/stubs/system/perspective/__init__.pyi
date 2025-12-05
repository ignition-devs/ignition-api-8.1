from typing import Any, Dict, List, Optional, Union

from com.inductiveautomation.ignition.common.script.adapters import PyJsonObjectAdapter

def alterDock(
    dockId: Union[str, unicode],
    config: Optional[Dict[Union[str, unicode], Any]] = ...,
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
) -> None: ...
def alterLogging(
    remoteLoggingEnabled: bool = ...,
    level: Union[str, unicode] = ...,
    remoteLoggingLevel: Union[str, unicode] = ...,
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
) -> None: ...
def authenticationChallenge(
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
    idp: Union[str, unicode] = ...,
    forceAuth: bool = ...,
    timeout: int = ...,
    payload: Optional[Dict[Union[str, unicode], Any]] = ...,
    framing: Union[str, unicode] = ...,
) -> None: ...
def closeDock(
    id: Union[str, unicode],
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
) -> None: ...
def closePage(
    message: Union[str, unicode, None] = ...,
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
) -> None: ...
def closePopup(
    id: Union[str, unicode],
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
) -> None: ...
def closeSession(
    message: Union[str, unicode, None] = ..., sessionId: Union[str, unicode] = ...
) -> None: ...
def download(
    filename: Union[str, unicode],
    data: Any,
    contentType: Union[str, unicode, None] = ...,
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
) -> None: ...
def getProjectInfo() -> Dict[Union[str, unicode], Any]: ...
def getSessionInfo(
    usernameFilter: Union[str, unicode, None] = ...,
    projectFilter: Union[str, unicode, None] = ...,
) -> List[PyJsonObjectAdapter]: ...
def isAuthorized(
    isAllOf: bool,
    securityLevels: List[Union[str, unicode]],
    sessionId: Union[str, unicode] = ...,
) -> bool: ...
def login(
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
    forceAuth: bool = ...,
) -> None: ...
def logout(
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
    message: Union[str, unicode] = ...,
) -> None: ...
def navigate(
    page: Union[str, unicode],
    url: Union[str, unicode, None] = ...,
    view: Union[str, unicode, None] = ...,
    params: Optional[Dict[Union[str, unicode], Union[str, unicode]]] = ...,
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
    newTab: bool = ...,
) -> None: ...
def navigateBack(
    sessionId: Union[str, unicode] = ..., pageId: Union[str, unicode] = ...
) -> None: ...
def navigateForward(
    sessionId: Union[str, unicode] = ..., pageId: Union[str, unicode] = ...
) -> None: ...
def openDock(
    id: Union[str, unicode],
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
    params: Optional[Dict[Union[str, unicode], Union[str, unicode]]] = ...,
) -> None: ...
def openPopup(
    id: Union[str, unicode],
    view: Union[str, unicode],
    params: Optional[Dict[Union[str, unicode], Any]] = ...,
    title: Union[str, unicode] = ...,
    position: Optional[Dict[Union[str, unicode], Union[int, str, unicode]]] = ...,
    showCloseIcon: bool = ...,
    draggable: bool = ...,
    resizable: bool = ...,
    modal: bool = ...,
    overlayDismiss: bool = ...,
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
    viewPortBound: bool = ...,
) -> None: ...
def print(
    message: Union[str, unicode],
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
    destination: Union[str, unicode] = ...,
) -> None: ...
def refresh(
    sessionId: Union[str, unicode] = ..., pageId: Union[str, unicode] = ...
) -> None: ...
def sendMessage(
    messageType: Union[str, unicode],
    payload: Dict[Union[str, unicode], Union[str, unicode]],
    scope: Union[str, unicode] = ...,
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
) -> None: ...
def setTheme(
    name: Union[str, unicode],
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
) -> None: ...
def toggleDock(
    id: Union[str, unicode],
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
    params: Optional[Dict[Union[str, unicode], Union[str, unicode]]] = ...,
) -> None: ...
def togglePopup(
    id: Union[str, unicode],
    view: Union[str, unicode],
    params: Optional[Dict[Union[str, unicode], Any]],
    title: Union[str, unicode] = ...,
    position: Optional[Dict[Union[str, unicode], Union[int, str, unicode]]] = ...,
    showCloseIcon: bool = ...,
    draggable: bool = ...,
    resizable: bool = ...,
    modal: bool = ...,
    overlayDismiss: bool = ...,
    sessionId: Union[str, unicode] = ...,
    pageId: Union[str, unicode] = ...,
    viewPortBound: bool = ...,
) -> None: ...
def vibrateDevice(duration: int, sessionId: Union[str, unicode] = ...) -> None: ...
