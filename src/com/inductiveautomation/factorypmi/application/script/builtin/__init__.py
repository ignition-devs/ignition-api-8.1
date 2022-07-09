from __future__ import print_function

__all__ = [
    "INavUtilities",
    "NavUtilities",
    "PrintUtilities",
    "WindowUtilities",
]

from typing import Any, Dict, Optional, Union

from com.inductiveautomation.factorypmi.application import FPMIWindow
from java.awt import Component
from java.awt.image import BufferedImage
from java.lang import Object, String
from java.util import EventObject
from org.python.core import PyObject


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
        # type: (Any) -> PyObject
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
        # type: (Any) -> PyObject
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

    class JythonPrintJob(Object):
        def getBottomMargin(self):
            pass

        def getLeftMargin(self):
            pass

        def getOrientation(self):
            pass

        def getPageHeight(self):
            pass

        def getPageWidth(self):
            pass

        def getPrinterName(self):
            pass

        def getRightMargin(self):
            pass

        def getTopMargin(self):
            pass

        def getZoomFactor(self):
            pass

        def isFitToPage(self):
            pass

        def isShowPrintDialog(self):
            pass

        def setBottomMargin(self, bottomMargin):
            pass

        def setFitToPage(self, fitToPage):
            pass

        def setLeftMargin(self, leftMargin):
            pass

        def setMargins(self, m):
            pass

        def setOrientation(self, orientation):
            pass

        def setPageHeight(self, pageHeight):
            pass

        def setPageWidth(self, pageWidth):
            pass

        def setPrinterName(self, printerName):
            pass

        def setRightMargin(self, rightMargin):
            pass

        def setShowPrintDialog(self, showPrintDialog):
            pass

        def setZoomFactor(self, zoomFactor):
            pass


class WindowUtilities(Object):
    """These are the scripting functions mounted at system.gui.*.
    Changes to this class must be made carefully, as some of the true
    implementations actually reside in the subclass,
    WindowUtilitiesForDesktop.
    """

    def confirm(self, *args):
        pass

    def errorBox(self, *args):
        pass

    def inputBox(self, *args):
        pass

    def messageBox(self, *args):
        pass

    def passwordBox(self, *args):
        pass

    def warningBox(self, *args):
        pass
