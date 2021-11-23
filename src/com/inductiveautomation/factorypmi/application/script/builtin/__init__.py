from __future__ import print_function, unicode_literals

__all__ = [
    "INavUtilities",
    "NavUtilities",
    "PrintUtilities",
    "WindowUtilities",
]

from java.awt.image import BufferedImage
from java.lang import Object


class INavUtilities(object):
    """Parent interface to coordinate the functions between NavUtilities
    and NavUtilitiesDispatcher.
    """

    def centerWindow(self, arg):
        raise NotImplementedError

    def closeParentWindow(self, event):
        raise NotImplementedError

    def closeWindow(self, arg):
        raise NotImplementedError

    def getCurrentWindow(self):
        raise NotImplementedError

    def goBack(self):
        raise NotImplementedError

    def goForward(self):
        raise NotImplementedError

    def goHome(self):
        raise NotImplementedError

    def openWindow(self, *args):
        raise NotImplementedError

    def openWindowImpl(self, path, params, openAdditional):
        raise NotImplementedError

    def openWindowInstance(self, *args):
        raise NotImplementedError

    def swapTo(self, *args):
        raise NotImplementedError

    def swapWindow(self, *args):
        raise NotImplementedError


class NavUtilities(INavUtilities):
    def centerWindow(self, arg):
        pass

    def closeParentWindow(self, event):
        pass

    def closeWindow(self, arg):
        pass

    def getCurrentWindow(self):
        pass

    def goBack(self):
        pass

    def goForward(self):
        pass

    def goHome(self):
        pass

    def openWindow(self, *args):
        pass

    def openWindowImpl(self, path, params, openAdditional):
        pass

    def openWindowInstance(self, *args):
        pass

    def swapTo(self, *args):
        pass

    def swapWindow(self, *args):
        pass


class PrintUtilities(Object):
    def __init__(self, app):
        print(self, app)

    def createImage(self, c):
        print(self, c)
        width = height = imageType = 1
        return BufferedImage(width, height, imageType)

    def createPrintJob(self, c):
        pass

    def printToImage(self, c, fileName=None):
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
