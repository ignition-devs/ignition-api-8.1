from __future__ import print_function

__all__ = [
    "Icon",
    "JComponent",
    "JDesktopPane",
    "JFrame",
    "JInternalFrame",
    "JLabel",
    "JLayeredPane",
    "JOptionPane",
    "JPanel",
    "JPopupMenu",
    "JTextField",
]

from typing import Any, List, Optional, Union

from java.awt import Container, Frame
from java.lang import String
from javax.swing.text import JTextComponent


class Icon(object):
    def getIconHeight(self):
        raise NotImplementedError

    def getIconWidth(self):
        raise NotImplementedError

    def paintIcon(self, c, g, x, y):
        raise NotImplementedError


class JComponent(Container):
    """The base class for all Swing components except top-level
    containers.
    """

    def __init__(self):
        # type: () -> None
        pass


class JFrame(Frame):
    """An extended version of java.awt.Frame that adds support for the
    JFC/Swing component architecture.
    """

    def __init__(self, *args):
        # type: (Any) -> None
        pass


class JInternalFrame(JComponent):
    """A lightweight object that provides many of the features of a
    native frame, including dragging, closing, becoming an icon,
    resizing, title display, and support for a menu bar.
    """

    def __init__(
        self,
        title=None,  # type: Optional[String]
        resizable=None,  # type: Optional[bool]
        closable=None,  # type: Optional[bool]
        maximizable=None,  # type: Optional[bool]
        iconifiable=None,  # type: Optional[bool]
    ):
        # type: (...) -> None
        super(JInternalFrame, self).__init__()
        print(title, resizable, closable, maximizable, iconifiable)


class JLabel(JComponent):
    """A display area for a short text string or an image, or both."""

    def __init__(self, *args):
        # type: (Any) -> None
        super(JLabel, self).__init__()
        print(args)


class JLayeredPane(JComponent):
    DEFAULT_LAYER = 0
    DRAG_LAYER = 400
    FRAME_CONTENT_LAYER = -30000
    LAYER_PROPERTY = "layeredContainerLayer"
    MODAL_LAYER = 200
    PALETTE_LAYER = 100
    POPUP_LAYER = 300

    def __init__(self):
        # type: () -> None
        super(JLayeredPane, self).__init__()

    def getComponentCountInLayer(self, layer):
        pass

    def getLayer(self, c):
        pass

    def highestLayer(self):
        pass

    def lowestLayer(self):
        pass

    def setPosition(self, c, position):
        pass


class JDesktopPane(JLayeredPane):
    def __init__(self):
        # type: () -> None
        super(JDesktopPane, self).__init__()

    def getAllFrames(self):
        pass

    def getAllFramesInLayer(self):
        pass

    def getDesktopManager(self):
        pass

    def getDragMode(self):
        pass

    def getSelectedFrame(self):
        pass

    def getUI(self):
        pass

    def getUIClassID(self):
        pass

    def updateUI(self):
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
        parentComponent,  # type: Optional[Any]
        message,  # type: Any
        title=None,  # type: Optional[String]
        optionType=None,  # type: Optional[int]
        messageType=None,  # type: Optional[int]
        icon=None,  # type: Optional[Icon]
    ):
        # type: (...) -> int
        print(parentComponent, message, title, optionType, messageType, icon)
        return JOptionPane.YES_OPTION

    @staticmethod
    def showInputDialog(
        parentComponent,  # type: Optional[Any]
        message,  # type: Any
        title=None,  # type: Optional[String]
        messageType=None,  # type: Optional[int]
        icon=None,  # type: Optional[Icon]
        selectionValues=None,  # type: Optional[List[Any]]
        initialSelectionValue=None,  # type: Optional[Any]
    ):
        # type: (...) -> String
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
        parentComponent,  # type: Optional[Any]
        message,  # type: Any
        title=None,  # type: Optional[String]
        messageType=None,  # type: Optional[int]
        icon=None,  # type: Optional[Icon]
    ):
        # type: (...) -> None
        print(parentComponent, message, title, messageType, icon)

    @staticmethod
    def showOptionDialog(
        parentComponent,  # type: Optional[Any]
        message,  # type: Any
        title=None,  # type: Optional[String]
        optionType=None,  # type: Optional[int]
        messageType=None,  # type: Optional[int]
        icon=None,  # type: Optional[Icon]
        options=None,  # type: Optional[List[Any]]
        initialValue=None,  # type: Optional[Any]
    ):
        # type: (...) -> int
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
    def __init__(self, *args):
        # type: (Any) -> None
        super(JPanel, self).__init__()
        print(args)


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

    def __init__(self, label=None):
        # type: (Optional[String]) -> None
        super(JPopupMenu, self).__init__()
        print(label)

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
        # type: (Any) -> None
        pass
