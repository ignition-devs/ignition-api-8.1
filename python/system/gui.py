# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103

"""GUI Functions
The following functions allow you to control windows and create popup interfaces."""

__all__ = [
    'confirm',
    'errorBox',
    'messageBox'
]

# Constants
ACCL_NONE = 0
ACCL_CONSTANT = 1
ACCL_FAST_TO_SLOW = 2
ACCL_SLOW_TO_FAST = 3
ACCL_EASE = 4
COORD_SCREEN = 0
COORD_DESIGNER = 1


def confirm(message, title=None, allowCancel=False):
    """Displays a confirmation dialog box to the user with "Yes" and "No" options, and a custom
    message.

    Args:
        message (str): The message to show in the confirmation dialog.
        title (str): The title for the confirmation dialog. Optional.
        allowCancel (bool): Show a cancel button in the dialog. Optional.

    Returns:
        bool: True (1) if the user selected "Yes", false (0) if the user selected "No", None if the
            user selected "Cancel".
    """
    print(message, title, allowCancel)
    return True


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
