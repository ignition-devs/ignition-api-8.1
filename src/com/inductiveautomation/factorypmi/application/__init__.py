from __future__ import print_function

__all__ = ["FPMIApp", "FPMIWindow", "VisionDesktop"]

from com.inductiveautomation.ignition.client.model import ClientContext
from java.lang import String
from javax.swing import JDesktopPane, JInternalFrame


class VisionDesktop(JDesktopPane):
    PRIMARY_DESKTOP_HANDLE = "Primary"

    def __init__(self, clientContext, handle=""):
        # type: (ClientContext, String) -> None
        super(VisionDesktop, self).__init__()
        print(clientContext, handle)

    def getAdapterContext(self):
        pass

    def getHandle(self):
        pass

    def getOpenedWindows(self):
        pass

    def getPath(self, window):
        pass

    def getScriptManager(self):
        pass

    def getWindow(self, arg):
        pass


class FPMIApp(VisionDesktop):
    TIMEZONE_CLIENT = "America/Tijuana"
    TIMEZONE_GATEWAY = "America/Tijuana"

    def getDefaultTimeZone(self):
        pass

    def getLastActivity(self):
        pass

    def shutdownDesigner(self):
        pass

    def startupDesigner(self, gatewayTimeZone):
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

    name = ""  # type: String
    _path = "Path/To/Window"

    def __init__(self, name):
        # type: (String) -> None
        super(FPMIWindow, self).__init__()
        self.name = name

    def getPath(self):
        return self._path

    def getRootContainer(self):
        pass
