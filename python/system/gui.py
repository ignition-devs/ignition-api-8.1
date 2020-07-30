# Copyright (C) 2019
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""GUI Functions
The following functions allow you to control windows and create popup
interfaces."""

__all__ = [
    'chooseColor',
    'closeDesktop',
    'color',
    'confirm',
    'convertPointToScreen',
    'errorBox',
    'messageBox',
]

from java.awt import Color

# Constants
ACCL_NONE = 0
ACCL_CONSTANT = 1
ACCL_FAST_TO_SLOW = 2
ACCL_SLOW_TO_FAST = 3
ACCL_EASE = 4
COORD_SCREEN = 0
COORD_DESIGNER = 1


def chooseColor(initialColor, dialogTitle="Choose Color"):
    """Prompts the user to pick a color using the default
    color-chooser dialog box.

    Args:
        initialColor (Color): A color to use as a starting point in
            the color choosing popup.
        dialogTitle (str): The title for the color choosing popup.
            Defaults to "Choose Color". Optional.

    Returns:
        Color: The new color chosen by the user.
    """
    print(initialColor, dialogTitle)
    return Color()


def closeDesktop(handle='primary'):
    """Allows you to close any of the open desktops associated with
    the current client. See the Multi-Monitor Clients page for more
    details about using multiple monitors.

    Args:
        handle (str): The handle for the desktop to close. The screen
            index cast as a string may be used instead of the handle.
            If omitted, this will default to the Primary Desktop.
            Alternatively, the handle "primary" can be used to refer
            to the Primary Desktop.
    """
    print handle


def color(*args):
    """Creates a new color object, either by parsing a string or by
    having the RGB[A] channels specified explicitly. See toColor to
    see a list of available color names.

    Args:
        args: Variable-length argument list.

    Returns:
        Color: The newly created color.
    """
    print args


def confirm(message, title=None, allowCancel=False):
    """Displays a confirmation dialog box to the user with "Yes", "No"
    and "Cancel" options, and a custom message.

    Args:
        message (str): The message to show in the confirmation dialog.
        title (str): The title for the confirmation dialog. Optional.
        allowCancel (bool): Show a cancel button in the dialog.
            Optional.

    Returns:
        bool: True (1) if the user selected "Yes", False (0) if the
            user selected "No", None if the user selected "Cancel".
    """
    print(message, title, allowCancel)
    return True


def convertPointToScreen(x, y, event):
    """Converts a pair of coordinates that are relative to the
    upper-left corner of some component to be relative to the
    upper-left corner of the entire screen.

    Args:
        x (int): The X-coordinate, relative to the component that
            fired the event.
        y (int): The Y-coordinate, relative to the component that
            fired the event.
        event (object): An event object for a component event.

    Returns:
        tuple: A tuple of (x,y) in screen coordinates.
    """
    print(x, y, event)
    return tuple([x, y])


def _dummy(message, title):
    print(message, title)


def errorBox(message, title=None):
    """Displays an error-style message box to the user.

    Args:
        message (str): The message to display in an error box.
        title (str): The title for the error box. Optional.
    """
    _dummy(message, title)


def messageBox(message, title=None):
    """Displays an informational-style message popup box to the user.

    Args:
        message (str): The message to display in an error box.
        title (str): The title for the error box. Optional.
    """
    _dummy(message, title)
