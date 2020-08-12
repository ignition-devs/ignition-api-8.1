# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""GUI module."""

__all__ = [
    'confirm',
    'error',
    'info',
    'input',
    'warning'
]

import system.gui
import system.util
from incendium import constants
from javax.swing import JOptionPane

# Cursor codes.
CURSOR_DEFAULT = 0
CURSOR_CROSSHAIR = 1
CURSOR_TEXT = 2
CURSOR_WAIT = 3
CURSOR_HAND = 4
CURSOR_MOVE = 5
CURSOR_SW_RESIZE = 6
CURSOR_SE_RESIZE = 7
CURSOR_NW_RESIZE = 8
CURSOR_NE_RESIZE = 9
CURSOR_N_RESIZE = 10
CURSOR_S_RESIZE = 11
CURSOR_W_RESIZE = 12
CURSOR_E_RESIZE = 13


def confirm(message, title, show_cancel=False):
    """Displays a confirmation dialog box to the user with "Yes", "No"
    and "Cancel" options, and a custom message.

    Args:
        message (str): The message to display. This will be translated
            to the selected Locale.
        title (str): A title for the message box. This will be
            translated to the selected Locale.
        show_cancel (bool): Show a cancel button in the dialog.
            Optional.

    Returns:
        bool: True if the user selected "Yes", False if the user
            selected "No", None if the user selected "Cancel" or
            closes the dialog.
    """
    options = [
        system.util.translate(constants.YES_TEXT),
        system.util.translate(constants.NO_TEXT)
    ]

    if show_cancel:
        options.append(system.util.translate(constants.CANCEL_TEXT))

    choice = JOptionPane.showOptionDialog(
        None,
        system.util.translate(message),
        system.util.translate(title),
        JOptionPane.YES_NO_CANCEL_OPTION,
        JOptionPane.QUESTION_MESSAGE,
        None,
        options,
        options[0]
    )

    return (
        not bool(choice)
        if choice in [JOptionPane.YES_OPTION, JOptionPane.NO_OPTION]
        else None
    )


def error(message, title, detail=None):
    """Displays an error-style message box to the user.

    Args:
        message (str): The message to display in an error box. This
            will be translated to the selected Locale.
        title (str): A title for the error box. This will be
            translated to the selected Locale.
        detail (str): Additional text to display. This will be
            translated to the selected Locale. Optional.
    """
    if detail is None:
        msg = system.util.translate(message)
    else:
        msg = '\n'.join([system.util.translate(message),
                         system.util.translate(detail)])
    JOptionPane.showMessageDialog(
        None,
        msg,
        system.util.translate(title),
        JOptionPane.ERROR_MESSAGE
    )


def info(message, title, detail=None):
    """Displays an informational-style message popup box to the user.

    Args:
        message (str): The message to display. This will be translated
            to the selected Locale. Will accept html formatting.
        title (str): A title for the message box. This will be
            translated to the selected Locale.
        detail (str): Additional text to display. This will be
            translated to the selected Locale. Optional.
    """
    if detail is None:
        msg = system.util.translate(message)
    else:
        msg = '\n'.join([system.util.translate(message),
                         system.util.translate(detail)])
    JOptionPane.showMessageDialog(
        None,
        msg,
        system.util.translate(title),
        JOptionPane.INFORMATION_MESSAGE
    )


def input(message, title=None):
    """Opens up a popup input dialog box. This dialog box will show a
    prompt message, and allow the user to type in a string. When the
    user is done, they can press "OK" or "Cancel". If OK is pressed,
    this function will return with the value that they typed in. If
    Cancel is pressed, this function will return the value None.

    Args:
        message (str): The message to display. This will be translated
            to the selected Locale. Will accept html formatting.
        title (str): A title for the message box. This will be
            translated to the selected Locale.

    Returns:
        str: The string value that was entered in the input box.
    """
    return JOptionPane.showInputDialog(
        None,
        system.util.translate(message),
        system.util.translate(title),
        JOptionPane.PLAIN_MESSAGE,
        None,
        None,
        ''
    )


def warning(message, title, detail=None):
    """Displays a message to the user in a warning style pop-up
    dialog.

    Args:
        message (str): The message to display in an warning box. This
            will be translated to the selected Locale.
        title (str): A title for the warning box. This will be
            translated to the selected Locale.
        detail (str): Additional text to display. This will be
            translated to the selected Locale. Optional.
    """
    if detail is None:
        msg = system.util.translate(message)
    else:
        msg = '\n'.join([system.util.translate(message),
                         system.util.translate(detail)])
    JOptionPane.showMessageDialog(
        None,
        msg,
        system.util.translate(title),
        JOptionPane.WARNING_MESSAGE
    )
