"""Provides a set of "lightweight" (all-Java language) components that,
to the maximum degree possible, work the same on all platforms.
"""

from __future__ import print_function

__all__ = [
    "JComponent",
    "JFrame",
    "JInternalFrame",
    "JLabel",
    "JOptionPane",
    "JPanel",
    "JPopupMenu",
    "JTextField",
]

from java.awt import Container, Frame
from javax.swing.text import JTextComponent


class JComponent(Container):
    """The base class for all Swing components except top-level
    containers.
    """

    pass


class JFrame(Frame):
    """An extended version of java.awt.Frame that adds support for the
    JFC/Swing component architecture.
    """

    pass


class JInternalFrame(JComponent):
    """A lightweight object that provides many of the features of a
    native frame, including dragging, closing, becoming an icon,
    resizing, title display, and support for a menu bar.
    """

    pass


class JLabel(JComponent):
    """A display area for a short text string or an image, or both."""

    def __init__(self, *args):
        """Creates a JLabel instance."""
        pass


class JOptionPane(JComponent):
    """JOptionPane makes it easy to pop up a standard dialog box that
    prompts users for a value or informs them of something. For
    information about using JOptionPane, see How to Make Dialogs, a
    section in The Java Tutorial.
    """

    # messageType.
    PLAIN_MESSAGE = -1
    ERROR_MESSAGE = 0
    INFORMATION_MESSAGE = 1
    WARNING_MESSAGE = 2
    QUESTION_MESSAGE = 3

    # optionType.
    DEFAULT_OPTION = -1
    YES_NO_OPTION = 0
    YES_NO_CANCEL_OPTION = 1
    OK_CANCEL_OPTION = 2

    # When one of the showXxxDialog methods returns an integer, the
    # possible values are:
    CLOSED_OPTION = -1
    OK_OPTION = 0
    YES_OPTION = 0
    NO_OPTION = 1
    CANCEL_OPTION = 2

    @staticmethod
    def showConfirmDialog(
        parentComponent,
        message,
        title=None,
        optionType=None,
        messageType=None,
        icon=None,
    ):
        """Asks a confirming question, like yes/no/cancel.

        Args:
            parentComponent (Component): Determines the Frame in which
                the dialog is displayed; if None, or if the
                parentComponent has no Frame, a default Frame is used.
            message (object): The object to display.
            title (str): The title string for the dialog. Optional.
            optionType (int): An int designating the options available
                on the dialog: YES_NO_OPTION, YES_NO_CANCEL_OPTION, or
                OK_CANCEL_OPTION. Optional.
            messageType (int): An integer designating the kind of
                message this is; primarily used to determine the icon
                from the pluggable Look and Feel: ERROR_MESSAGE,
                INFORMATION_MESSAGE, WARNING_MESSAGE, QUESTION_MESSAGE,
                or PLAIN_MESSAGE. Optional.
            icon (Icon): The icon to display in the dialog. Optional.

        Returns:
            int: An integer indicating the option selected by the user.
        """
        print(parentComponent, message, title, optionType, messageType, icon)
        return JOptionPane.YES_OPTION

    @staticmethod
    def showInputDialog(
        parentComponent,
        message,
        title=None,
        messageType=None,
        icon=None,
        selectionValues=None,
        initialSelectionValue=None,
    ):
        """Prompt for some input.

        Args:
            parentComponent (Component): Determines the Frame in which
                the dialog is displayed; if None, or if the
                parentComponent has no Frame, a default Frame is used.
            message (object): The object to display.
            title (str): The title string for the dialog. Optional.
            messageType (int): The type of message to be displayed:
                ERROR_MESSAGE, INFORMATION_MESSAGE, WARNING_MESSAGE,
                QUESTION_MESSAGE, or PLAIN_MESSAGE. Optional.
            icon (Icon): The icon to display in the dialog. Optional.
            selectionValues (object): An array of Objects that gives the
                possible selections. Optional.
            initialSelectionValue (object): The value used to initialize
                the input field. Optional.

        Returns:
            object: An integer indicating the option selected by the
                user.
        """
        print(
            parentComponent,
            message,
            title,
            messageType,
            icon,
            selectionValues,
            initialSelectionValue,
        )
        return "Input"

    @staticmethod
    def showMessageDialog(
        parentComponent, message, title=None, messageType=None, icon=None
    ):
        """Tell the user about something that has happened.

        Args:
            parentComponent (Component): Determines the Frame in which
                the dialog is displayed; if None, or if the
                parentComponent has no Frame, a default Frame is used.
            message (object): The object to display.
            title (str): The title string for the dialog. Optional.
            messageType (int): The type of message to be displayed:
                ERROR_MESSAGE, INFORMATION_MESSAGE, WARNING_MESSAGE,
                QUESTION_MESSAGE, or PLAIN_MESSAGE. Optional.
            icon (Icon): The icon to display in the dialog. Optional.
        """
        print(parentComponent, message, title, messageType, icon)

    @staticmethod
    def showOptionDialog(
        parentComponent,
        message,
        title=None,
        optionType=None,
        messageType=None,
        icon=None,
        options=None,
        initialValue=None,
    ):
        """The Grand Unification of the above three.

        Args:
            parentComponent (Component): Determines the Frame in which
                the dialog is displayed; if None, or if the
                parentComponent has no Frame, a default Frame is used.
            message (object): The object to display.
            title (str): The title string for the dialog. Optional.
            optionType (int): An integer designating the options
                available on the dialog: DEFAULT_OPTION, YES_NO_OPTION,
                YES_NO_CANCEL_OPTION, or OK_CANCEL_OPTION. Optional.
            messageType (int): An integer designating the kind of
                message this is; primarily used to determine the icon
                from the pluggable Look and Feel: ERROR_MESSAGE,
                INFORMATION_MESSAGE, WARNING_MESSAGE, QUESTION_MESSAGE,
                or PLAIN_MESSAGE. Optional.
            icon (Icon): The icon to display in the dialog. Optional.
            options (list): An array of objects indicating the possible
                choices the user can make; if the objects are
                components, they are rendered properly; non-String
                objects are rendered using their toString methods; if
                this parameter is null, the options are determined by
                the Look and Feel. Optional.
            initialValue (object): The object that represents the
                default selection for the dialog; only meaningful if
                options is used; can be null. Optional.

        Returns:
            int: An integer indicating the option chosen by the user, or
                CLOSED_OPTION if the user closed the dialog.
        """
        print(
            parentComponent,
            message,
            title,
            optionType,
            messageType,
            icon,
            options,
            initialValue,
        )
        return JOptionPane.YES_OPTION


class JPanel(JComponent):
    """JPanel is a generic lightweight container."""

    pass


class JPopupMenu(JComponent):
    """An implementation of a popup menu -- a small window that pops up
    and displays a series of choices. A JPopupMenu is used for the menu
    that appears when the user selects an item on the menu bar. It is
    also used for "pull-right" menu that appears when the selects a menu
    item that activates it. Finally, a JPopupMenu can also be used
    anywhere else you want a menu to appear. For example, when the user
    right-clicks in a specified area.
    """

    pass


class JTextField(JTextComponent):
    """JTextField is a lightweight component that allows the editing of
    a single line of text.
    """

    def __init__(self, *args):
        """Constructor."""
        pass
