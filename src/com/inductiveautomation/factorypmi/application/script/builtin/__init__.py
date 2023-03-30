from __future__ import print_function

__all__ = [
    "ClientDatasetUtilities",
    "ClientSystemUtilities",
    "INavUtilities",
    "NavUtilities",
    "PrintUtilities",
    "WindowUtilities",
]

from typing import Any, Dict, List, Optional, Tuple, Union

from com.inductiveautomation.factorypmi.application import FPMIApp, FPMIWindow
from com.inductiveautomation.factorypmi.application.script import PyComponentWrapper
from com.inductiveautomation.ignition.common.model.values import QualityCode
from dev.thecesrom.helper.types import AnyStr
from java.awt import Color, Component, Graphics
from java.awt.event import ActionEvent, ComponentEvent, MouseEvent
from java.awt.image import BufferedImage
from java.awt.print import PageFormat
from java.lang import Number, Object
from java.util import EventObject
from javax.swing import JComponent, JFrame, JPopupMenu
from org.python.core import PyObject, PySequence, PyTuple


class INavUtilities(object):
    """Parent interface to coordinate the functions between NavUtilities
    and NavUtilitiesDispatcher.
    """

    def centerWindow(self, arg):
        # type: (Union[FPMIWindow, AnyStr]) -> None
        raise NotImplementedError

    def closeParentWindow(self, event):
        # type: (EventObject) -> None
        raise NotImplementedError

    def closeWindow(self, arg):
        # type: (Union[FPMIWindow, AnyStr]) -> None
        raise NotImplementedError

    def getCurrentWindow(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def goBack(self):
        # type: () -> PyObject
        raise NotImplementedError

    def goForward(self):
        # type: () -> PyObject
        raise NotImplementedError

    def goHome(self):
        # type: () -> PyObject
        raise NotImplementedError

    def openWindow(self, path, params=None):
        # type: (AnyStr, Optional[Dict[AnyStr, Any]]) -> PyObject
        raise NotImplementedError

    def openWindowImpl(self, path, params, openAdditional):
        # type: (AnyStr, Dict[AnyStr, Any], bool) -> PyObject
        raise NotImplementedError

    def openWindowInstance(self, path, params=None):
        # type: (AnyStr, Optional[Dict[AnyStr, Any]]) -> PyObject
        raise NotImplementedError

    def swapTo(self, name, params):
        # type: (AnyStr, Dict[AnyStr, Any]) -> PyObject
        raise NotImplementedError

    def swapWindow(self, *args):
        # type: (*Any) -> PyObject
        raise NotImplementedError


class ClientDatasetUtilities(Object):
    def __init__(self, app):
        # type: (FPMIApp) -> None
        super(ClientDatasetUtilities, self).__init__()
        print(app)


class ClientSystemUtilities(Object):
    def __init__(self):
        # type: () -> None
        super(ClientSystemUtilities, self).__init__()


class NavUtilities(INavUtilities):
    def centerWindow(self, arg):
        # type: (Union[FPMIWindow, AnyStr]) -> None
        pass

    def closeParentWindow(self, event):
        # type: (EventObject) -> None
        pass

    def closeWindow(self, arg):
        # type: (Union[FPMIWindow, AnyStr]) -> None
        pass

    def getCurrentWindow(self):
        # type: () -> AnyStr
        pass

    def goBack(self):
        # type: () -> PyObject
        pass

    def goForward(self):
        # type: () -> PyObject
        pass

    def goHome(self):
        # type: () -> PyObject
        pass

    def openWindow(self, path, params=None):
        # type: (AnyStr, Optional[Dict[AnyStr, Any]]) -> PyObject
        pass

    def openWindowImpl(self, path, params, openAdditional):
        # type: (AnyStr, Dict[AnyStr, Any], bool) -> PyObject
        pass

    def openWindowInstance(self, path, params=None):
        # type: (AnyStr, Optional[Dict[AnyStr, Any]]) -> PyObject
        pass

    def swapTo(self, name, params):
        # type: (AnyStr, Dict[AnyStr, Any]) -> PyObject
        pass

    def swapWindow(self, *args):
        # type: (*Any) -> PyObject
        pass


class PrintUtilities(Object):
    def __init__(self, app):
        # type: (Any) -> None
        super(PrintUtilities, self).__init__()
        print(self, app)

    def createImage(self, c):
        # type: (Component) -> BufferedImage
        print(self, c)
        width = height = imageType = 1
        return BufferedImage(width, height, imageType)

    def createPrintJob(self, c):
        # type: (Component) -> PrintUtilities.JythonPrintJob
        pass

    def printToImage(self, c, fileName=None):
        # type: (Component, Optional[str]) -> None
        pass

    class ComponentPrinter(Object):
        def __init__(self, c, fit, zoom):
            # type: (Component, bool, float) -> None
            super(PrintUtilities.ComponentPrinter, self).__init__()
            print(c, fit, zoom)

        def print(self, g, pageFormat, pageIndex):
            # type: (Graphics, PageFormat, int) -> int
            pass

    class JythonPrintJob(Object):
        def __init__(self, c):
            # type: (Component) -> None
            super(PrintUtilities.JythonPrintJob, self).__init__()
            print(c)

        def getBottomMargin(self):
            # type: () -> float
            pass

        def getLeftMargin(self):
            # type: () -> float
            pass

        def getOrientation(self):
            # type: () -> int
            pass

        def getPageHeight(self):
            # type: () -> float
            pass

        def getPageWidth(self):
            # type: () -> float
            pass

        def getPrinterName(self):
            # type: () -> AnyStr
            pass

        def getRightMargin(self):
            # type: () -> float
            pass

        def getTopMargin(self):
            # type: () -> float
            pass

        def getZoomFactor(self):
            # type: () -> float
            pass

        def isFitToPage(self):
            # type: () -> bool
            return True

        def isShowPrintDialog(self):
            # type: () -> bool
            return True

        def setBottomMargin(self, bottomMargin):
            # type: (float) -> None
            pass

        def setFitToPage(self, fitToPage):
            # type: (bool) -> None
            pass

        def setLeftMargin(self, leftMargin):
            # type: (float) -> None
            pass

        def setMargins(self, m):
            # type: (float) -> None
            pass

        def setOrientation(self, orientation):
            # type: (int) -> None
            pass

        def setPageHeight(self, pageHeight):
            # type: (float) -> None
            pass

        def setPageWidth(self, pageWidth):
            # type: (float) -> None
            pass

        def setPrinterName(self, printerName):
            # type: (AnyStr) -> None
            pass

        def setRightMargin(self, rightMargin):
            # type: (float) -> None
            pass

        def setShowPrintDialog(self, showPrintDialog):
            # type: (bool) -> None
            pass

        def setZoomFactor(self, zoomFactor):
            # type: (float) -> None
            pass


class WindowUtilities(Object):
    """These are the scripting functions mounted at system.gui.*.

    Changes to this class must be made carefully, as some of the true
    implementations actually reside in the subclass,
    WindowUtilitiesForDesktop.
    """

    ACCL_NONE = 0
    ACCL_CONSTANT = 1
    ACCL_FAST_TO_SLOW = 2
    ACCL_SLOW_TO_FAST = 3
    ACCL_EASE = 4
    COORD_DESIGNER = 1
    COORD_SCREEN = 0

    def chooseColor(self, initialColor, dialogTitle="Choose Color"):
        # type: (Color, Optional[AnyStr]) -> Color
        pass

    def closeDesktop(self, handle):
        # type: (AnyStr) -> None
        pass

    @staticmethod
    def color(*args):
        # type: (*Any) -> Color
        pass

    def confirm(
        self,
        message,  # type: AnyStr
        title="Confirm",  # type: AnyStr
        allowCancel=False,  # type: bool
    ):
        # type: (...) -> Optional[bool]
        pass

    @staticmethod
    def convertPointToScreen(x, y, event):
        # type: (int, int, EventObject) -> Tuple[int, int]
        pass

    @staticmethod
    def createPopupContext():
        # type: () -> WindowUtilities.PopupContext
        pass

    @staticmethod
    def createPopupMenu(key, functions):
        # type: (PySequence, PySequence) -> JPopupMenu
        pass

    def desktop(self, arg):
        # type: (Union[int, AnyStr]) -> WindowUtilities
        pass

    def errorBox(self, message, title="Error"):
        # type: (AnyStr, Optional[AnyStr]) -> None
        pass

    @staticmethod
    def find(component):
        # type: (JComponent) -> WindowUtilities
        pass

    def findWindow(self, path):
        # type: (AnyStr) -> List[PyComponentWrapper]
        pass

    def getCurrentDesktop(self):
        # type: () -> AnyStr
        pass

    def getDesktopHandles(self):
        # type: () -> PySequence
        pass

    def getOpenedWindowNames(self):
        # type: () -> PyTuple
        pass

    def getOpenedWindows(self):
        # type: () -> PyTuple
        pass

    @staticmethod
    def getParentWindow(event):
        # type: (EventObject) -> PyObject
        pass

    def getQuality(self, comp, propertyName):
        # type: (JComponent, AnyStr) -> QualityCode
        pass

    def getScreenIndex(self):
        # type: () -> int
        pass

    @staticmethod
    def getScreens():
        # type: () -> PySequence
        pass

    @staticmethod
    def getSibling(event, name):
        # type: (EventObject, AnyStr) -> PyObject
        pass

    def getWindow(self, name):
        # type: (AnyStr) -> PyObject
        pass

    def getWindowNames(self):
        # type: () -> PyTuple
        pass

    def inputBox(self, message, defaultTxt=""):
        # type: (AnyStr, AnyStr) -> Optional[AnyStr]
        pass

    def isTouchscreenModeEnabled(self):
        # type: () -> bool
        return True

    def messageBox(self, message, title="Information"):
        # type: (AnyStr, AnyStr) -> None
        pass

    def openDesktop(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> JFrame
        pass

    def openDiagnostics(self):
        # type: () -> None
        pass

    def passwordBox(
        self,
        message,  # type:AnyStr
        title="Password",  # type: AnyStr
        echoChar="*",  # type: AnyStr
    ):
        # type: (...) -> Optional[AnyStr]
        pass

    def setTouchScreenModeEnabled(self, b):
        # type: (bool) -> None
        pass

    def showNumericKeyPad(
        self,
        initialValue,  # type: Number
        fontSize=None,  # type: Optional[int]
        usePasswordMode=False,  # type: bool
    ):
        # type: (...) -> Number
        pass

    def showTouchscreenKeyboard(self, initialText, fontSize=None, password=None):
        # type: (AnyStr, Optional[int], Optional[bool]) -> AnyStr
        pass

    def transform(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> PyObject
        pass

    def warningBox(self, message, title="Warning"):
        # type: (AnyStr, AnyStr) -> None
        pass

    class JyPopupMenu(JPopupMenu):
        def actionPerformed(self, e):
            # type: (ActionEvent) -> None
            pass

        def addJyFunction(self, name, fun):
            # type: (AnyStr, PyObject) -> None
            pass

        def show(self, me, *args):
            # type: (Union[ComponentEvent, MouseEvent], *int) -> None
            pass

    class PopupContext(Object):
        def endPopup(self):
            # type: () -> None
            pass

        def startPopup(self):
            # type: () -> None
            pass
