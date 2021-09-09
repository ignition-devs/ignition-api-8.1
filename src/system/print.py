"""Print Functions.

The following functions allow you to send to a printer.
"""

from __future__ import print_function

__all__ = ["createImage", "createPrintJob", "printToImage"]

from java.awt import Component
from java.awt.image import BufferedImage
from java.lang import Object


class JythonPrintJob(Object):
    """JythonPrintJob object."""

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

    def print(self):
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


def createImage(component):
    """Takes a snapshot of a component and creates a Java BufferedImage
    out of it.

    You can use javax.imageio.ImageIO to turn this into bytes that can
    be saved to a file or a BLOB field in a database.

    Args:
        component (Component): The component to render.

    Returns:
        BufferedImage: A java.awt.image.BufferedImage representing the
            component.
    """
    print(component)
    width = height = imageType = 1
    return BufferedImage(width, height, imageType)


def createPrintJob(component):
    """Provides a general printing facility for printing the contents of
    a window or component to a printer.

    The general workflow for this function is that you create the print
    job, set the options you'd like on it, and then call print() on the
    job. For printing reports or tables, use those components' dedicated
    print() functions.

    Args:
        component (Component): The component that you'd like to print.

    Returns:
        JythonPrintJob: A print job that can then be customized and
            started. To start the print job, use .print().
    """
    print(component)
    return JythonPrintJob()


def printToImage(component, filename=None):
    """This function prints the given component (such as a graph,
    container, entire window, etc) to an image file, and saves the file
    where ever the operating system deems appropriate.

    A filename and path may be provided to determine the name and
    location of the saved file.

    While not required, it is highly recommended to pass in a filename
    and path. The script may fail if the function attempts to save to a
    directory that the client does not have access rights to.

    Args:
        component (Component): The component to render.
        filename (str): A filename to save the image as. Optional.
    """
    print(component, filename)
