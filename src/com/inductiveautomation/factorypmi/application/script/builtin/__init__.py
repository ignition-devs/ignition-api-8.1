from __future__ import print_function

__all__ = [
    "INavUtilities",
    "NavUtilities",
    "PrintUtilities",
    "WindowUtilities",
]

from typing import Any, Dict, List, Optional, Tuple, Union

from com.inductiveautomation.factorypmi.application import FPMIWindow
from com.inductiveautomation.factorypmi.application.script import PyComponentWrapper
from com.inductiveautomation.ignition.common.model.values import QualityCode
from java.awt import Color, Component, Graphics
from java.awt.event import ActionEvent, ComponentEvent, MouseEvent
from java.awt.image import BufferedImage
from java.awt.print import PageFormat
from java.lang import Number, Object, String
from java.util import EventObject
from javax.swing import JComponent, JFrame, JPopupMenu
from org.python.core import PyObject, PySequence, PyTuple


class INavUtilities(object):
    """Parent interface to coordinate the functions between NavUtilities
    and NavUtilitiesDispatcher.
    """

    def centerWindow(self, arg):
        # type: (Union[FPMIWindow, String]) -> None
        raise NotImplementedError

    def closeParentWindow(self, event):
        # type: (EventObject) -> None
        raise NotImplementedError

    def closeWindow(self, arg):
        # type: (Union[FPMIWindow, String]) -> None
        raise NotImplementedError

    def getCurrentWindow(self):
        # type: () -> String
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
        # type: (String, Optional[Dict[String, Any]]) -> PyObject
        raise NotImplementedError

    def openWindowImpl(self, path, params, openAdditional):
        # type: (String, Dict[String, Any], bool) -> PyObject
        raise NotImplementedError

    def openWindowInstance(self, path, params=None):
        # type: (String, Optional[Dict[String, Any]]) -> PyObject
        raise NotImplementedError

    def swapTo(self, name, params):
        # type: (String, Dict[String, Any]) -> PyObject
        raise NotImplementedError

    def swapWindow(self, *args):
        # type: (*Any) -> PyObject
        raise NotImplementedError


class NavUtilities(INavUtilities):
    def centerWindow(self, arg):
        # type: (Union[FPMIWindow, String]) -> None
        pass

    def closeParentWindow(self, event):
        # type: (EventObject) -> None
        pass

    def closeWindow(self, arg):
        # type: (Union[FPMIWindow, String]) -> None
        pass

    def getCurrentWindow(self):
        # type: () -> String
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
        # type: (String, Optional[Dict[String, Any]]) -> PyObject
        pass

    def openWindowImpl(self, path, params, openAdditional):
        # type: (String, Dict[String, Any], bool) -> PyObject
        pass

    def openWindowInstance(self, path, params=None):
        # type: (String, Optional[Dict[String, Any]]) -> PyObject
        pass

    def swapTo(self, name, params):
        # type: (String, Dict[String, Any]) -> PyObject
        pass

    def swapWindow(self, *args):
        # type: (*Any) -> PyObject
        pass


class PrintUtilities(Object):
    def __init__(self, app):
        # type: (Any) -> None
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
            pass

        def print(self, g, pageFormat, pageIndex):
            # type: (Graphics, PageFormat, int) -> int
            pass

    class JythonPrintJob(Object):
        def __init__(self, c):
            # type: (Component) -> None
            pass

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
            # type: () -> String
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
            # type: (String) -> None
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
        # type: (Color, Optional[String]) -> Color
        pass

    def closeDesktop(self, handle):
        # type: (String) -> None
        pass

    @staticmethod
    def color(*args):
        # type: (*Any) -> Color
        pass

    def confirm(
        self,
        message,  # type: String
        title="Confirm",  # type: String
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
        # type: (Union[int, String]) -> WindowUtilities
        pass

    def errorBox(self, message, title="Error"):
        # type: (String, Optional[String]) -> None
        pass

    @staticmethod
    def find(component):
        # type: (JComponent) -> WindowUtilities
        pass

    def findWindow(self, path):
        # type: (String) -> List[PyComponentWrapper]
        pass

    def getCurrentDesktop(self):
        # type: () -> String
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
        # type: (JComponent, String) -> QualityCode
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
        # type: (EventObject, String) -> PyObject
        pass

    def getWindow(self, name):
        # type: (String) -> PyObject
        pass

    def getWindowNames(self):
        # type: () -> PyTuple
        pass

    def inputBox(self, message, defaultTxt=""):
        # type: (String, String) -> Optional[String]
        pass

    def isTouchscreenModeEnabled(self):
        # type: () -> bool
        return True

    def messageBox(self, message, title="Information"):
        # type: (String, String) -> None
        pass

    def openDesktop(self, *args, **kwargs):
        # type: (*PyObject, **String) -> JFrame
        pass

    def openDiagnostics(self):
        # type: () -> None
        pass

    def passwordBox(
        self,
        message,  # type:String
        title="Password",  # type: String
        echoChar="*",  # type: String
    ):
        # type: (...) -> Optional[String]
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
        # type: (String, Optional[int], Optional[bool]) -> String
        pass

    def transform(self, *args, **kwargs):
        # type: (*PyObject, **String) -> PyObject
        pass

    def warningBox(self, message, title="Warning"):
        # type: (String, String) -> None
        pass

    class JyPopupMenu(JPopupMenu):
        def actionPerformed(self, e):
            # type: (ActionEvent) -> None
            pass

        def addJyFunction(self, name, fun):
            # type: (String, PyObject) -> None
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
