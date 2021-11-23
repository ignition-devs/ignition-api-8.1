from __future__ import print_function, unicode_literals

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


class JToolTip(JComponent):
    def getAccessibleContext(self):
        pass

    def getComponent(self):
        print(self)
        return JComponent()

    def getTipText(self):
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

    def addAncestorListener(self, listener):
        pass

    def addNotify(self):
        pass

    def createToolTip(self):
        print(self)
        return JToolTip()

    @staticmethod
    def getDefaultLocale():
        pass

    @staticmethod
    def isLightweightComponent(c):
        pass

    @staticmethod
    def setDefaultLocale(l):
        pass


class JTextField(JTextComponent):
    """JTextField is a lightweight component that allows the editing of
    a single line of text.
    """

    def __init__(self, *args):
        pass
