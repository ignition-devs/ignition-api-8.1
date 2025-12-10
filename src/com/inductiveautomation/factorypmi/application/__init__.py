from __future__ import print_function

__all__ = ["FPMIApp", "FPMIWindow", "VisionDesktop"]

from typing import Any, List, Union

from java.util import TimeZone
from javax.swing import JDesktopPane, JInternalFrame

from com.inductiveautomation.factorypmi.application.components import BasicContainer
from com.inductiveautomation.ignition.client.model import ClientContext, DesktopListener
from com.inductiveautomation.ignition.common.project.resource import ResourcePath
from com.inductiveautomation.ignition.common.script import ScriptManager


class VisionDesktop(JDesktopPane):
    PRIMARY_DESKTOP_HANDLE = "Primary"

    def __init__(self, clientContext, handle=""):
        # type: (ClientContext, Union[str, unicode]) -> None
        super(VisionDesktop, self).__init__()
        print(clientContext, handle)

    def addDesktopListener(self, arg):
        # type: (DesktopListener) -> None
        pass

    def getAdapterContext(self):
        # type: () -> Any
        pass

    def getHandle(self):
        # type: () -> Union[str, unicode]
        pass

    def getOpenedWindows(self):
        # type: () -> List[FPMIWindow]
        pass

    def getPath(self, window):
        # type: (FPMIWindow) -> Union[str, unicode]
        pass

    def getScriptManager(self):
        # type: () -> ScriptManager
        pass

    def getWindow(self, arg):
        # type: (Union[str, unicode, ResourcePath]) -> FPMIWindow
        pass


class FPMIApp(VisionDesktop):
    TIMEZONE_CLIENT = "America/Tijuana"
    TIMEZONE_GATEWAY = "America/Tijuana"

    def getDefaultTimeZone(self):
        # type: () -> Union[str, unicode]
        pass

    def getLastActivity(self):
        # type: () -> long
        pass

    def shutdownDesigner(self):
        # type: () -> None
        pass

    def startupDesigner(self, gatewayTimeZone):
        # type: (TimeZone) -> None
        pass


class FPMIWindow(JInternalFrame):
    CACHE_ALWAYS = 2
    CACHE_AUTO = 0
    CACHE_NEVER = 1
    DOCK_EAST = 2
    DOCK_FLOAT = 0
    DOCK_NORTH = 2
    DOCK_SOUTH = 4
    DOCK_WEST = 3
    PARENT_WINDOW_NAME = "_parent"
    SHOW_ALWAYS = 0
    SHOW_NEVER = 1
    SHOW_MAXIMIZED = 2

    name = ""  # type: Union[str, unicode]
    _path = "Path/To/Window"

    def __init__(self, name):
        # type: (Union[str, unicode]) -> None
        super(FPMIWindow, self).__init__()
        self.name = name

    def getPath(self):
        # type: () -> Union[str, unicode]
        return self._path

    def getRootContainer(self):
        # type: () -> BasicContainer
        pass
