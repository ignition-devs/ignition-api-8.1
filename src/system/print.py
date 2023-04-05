"""Print Functions.

The following functions allow you to send to a printer.
"""

from __future__ import print_function

__all__ = [
    "LANDSCAPE",
    "PORTRAIT",
    "createImage",
    "createPrintJob",
    "getDefaultPrinterName",
    "getPrinterNames",
    "printToImage",
]

from typing import List, Optional

from com.inductiveautomation.factorypmi.application.script.builtin import PrintUtilities
from dev.thecesrom.helper.types import AnyStr
from java.awt import Component
from java.awt.image import BufferedImage

LANDSCAPE = 0
PORTRAIT = 1


def createImage(component):
    # type: (Component) -> BufferedImage
    """Takes a snapshot of a component and creates a Java BufferedImage
    out of it.

    You can use javax.imageio. to turn this into bytes that can be saved
    to a file or a BLOB field in a database.

    Args:
        component: The component to render.

    Returns:
        A java.awt.image.BufferedImage representing the component.
    """
    return PrintUtilities("app").createImage(component)


def createPrintJob(component):
    # type: (Component) -> PrintUtilities.JythonPrintJob
    """Provides a general printing facility for printing the contents of
    a window or component to a printer.

    The general workflow for this function is that you create the print
    job, set the options you'd like on it, and then call print() on the
    job. For printing reports or tables, use those components' dedicated
    print() functions.

    Args:
        component: The component that you'd like to print.

    Returns:
        A print job that can then be customized and started. To start
        the print job, use .print().
    """
    return PrintUtilities.JythonPrintJob(component)


def getDefaultPrinterName():
    # type: () -> Optional[unicode]
    """Obtains the local default printer.

    Returns:
        A string that represents the default printer. Returns null if
        there is no default printer.
    """
    return unicode("Default Printer")


def getPrinterNames():
    # type: () -> List[unicode]
    """Lists the available local printers.

    Returns:
        A list of strings that contain the names of local printers.
        Returns an empty list if there are no available local printers.
    """
    printer = getDefaultPrinterName()
    return [] if printer is None else [printer]


def printToImage(component, filename=None):
    # type: (Component, Optional[AnyStr]) -> None
    """This function prints the given component (such as a graph,
    container, entire window, etc.) to an image file, and saves the file
    where ever the operating system deems appropriate.

    A filename and path may be provided to determine the name and
    location of the saved file.

    While not required, it is highly recommended to pass in a filename
    and path. The script may fail if the function attempts to save to a
    directory that the client does not have access rights to.

    Args:
        component: The component to render.
        filename: A filename to save the image as. Optional.
    """
    print(component, filename)
