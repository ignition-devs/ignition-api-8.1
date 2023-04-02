from __future__ import print_function

__all__ = [
    "DesktopManager",
    "Icon",
    "JComponent",
    "JDesktopPane",
    "JFrame",
    "JInternalFrame",
    "JLabel",
    "JLayeredPane",
    "JOptionPane",
    "JPanel",
    "JPasswordField",
    "JPopupMenu",
    "JRootPane",
    "JTextField",
    "JToolTip",
    "RootPaneContainer",
]

import array
import warnings
from typing import Any, List, Optional

from dev.thecesrom.helper.types import AnyStr
from java.awt import Component, Container, Frame, Graphics
from java.util import Locale
from javax.swing.event import AncestorListener
from javax.swing.plaf import DesktopPaneUI
from javax.swing.text import JTextComponent


class DesktopManager(object):
    def activateFrame(self, f):
        # type: (JInternalFrame) -> None
        raise NotImplementedError

    def beginDragginFrame(self, f):
        # type: (JComponent) -> None
        raise NotImplementedError

    def beginResizingFrame(self, f, direction):
        # type: (JComponent, int) -> None
        raise NotImplementedError

    def closeFrame(self, f):
        # type: (JInternalFrame) -> None
        raise NotImplementedError

    def deactivateFrame(self, f):
        # type: (JInternalFrame) -> None
        raise NotImplementedError

    def deiconifyFrame(self, f):
        # type: (JInternalFrame) -> None
        raise NotImplementedError

    def dragFrame(self, f, newX, newY):
        # type: (JComponent, int, int) -> None
        raise NotImplementedError

    def endDraggingFrame(self, f):
        # type: (JComponent) -> None
        raise NotImplementedError

    def endResizing(self, f):
        # type: (JComponent) -> None
        raise NotImplementedError

    def iconifyFrame(self, f):
        # type: (JInternalFrame) -> None
        raise NotImplementedError

    def maximizeFrame(self, f):
        # type: (JInternalFrame) -> None
        raise NotImplementedError

    def minimizeFrame(self, f):
        # type: (JInternalFrame) -> None
        raise NotImplementedError

    def openFrame(self, f):
        # type: (JInternalFrame) -> None
        raise NotImplementedError

    def resizeFrame(self, f, newX, newY, newWidth, newHeight):
        # type: (JComponent, int, int, int, int) -> None
        raise NotImplementedError

    def setBoundsForFrame(self, f, newX, newY, newWidth, newHeight):
        # type: (JComponent, int, int, int, int) -> None
        raise NotImplementedError


class Icon(object):
    def getIconHeight(self):
        # type: () -> int
        raise NotImplementedError

    def getIconWidth(self):
        # type: () -> int
        raise NotImplementedError

    def paintIcon(self, c, g, x, y):
        # type: (Component, Graphics, int, int) -> None
        raise NotImplementedError


class RootPaneContainer(object):
    def getContentPane(self):
        # type: () -> Container
        raise NotImplementedError

    def getGlassPane(self):
        # type: () -> Component
        raise NotImplementedError

    def getLayeredPane(self):
        # type: () -> JLayeredPane
        raise NotImplementedError

    def getRootPane(self):
        # type: () -> JRootPane
        raise NotImplementedError

    def setContentPane(self, contentPane):
        # type: (Container) -> None
        raise NotImplementedError

    def setGlassPane(self, glassPane):
        # type: (Component) -> None
        raise NotImplementedError

    def setLayeredPane(self, rootPane):
        # type: (JLayeredPane) -> None
        raise NotImplementedError


class JComponent(Container):
    TOOL_TIP_TEXT_KEY = None  # type: AnyStr
    UNDEFINED_CONDITION = None  # type: int
    WHEN_ANCESTOR_OF_FOCUSED_COMPONENT = None  # type: int
    WHEN_FOCUSED = None  # type: int
    WHEN_IN_FOCUSED_WINDOW = None  # type: int

    def __init__(self):
        # type: () -> None
        super(JComponent, self).__init__()

    def addAncestorListener(self, listener):
        # type: (AncestorListener) -> None
        pass

    def addNotify(self):
        # type: () -> None
        pass

    def createToolTip(self):
        # type: () -> JToolTip
        pass

    @staticmethod
    def getDefaultLocale():
        # type: () -> Locale
        pass

    @staticmethod
    def isLightweightComponent(c):
        # type: (Component) -> bool
        return True

    @staticmethod
    def setDefaultLocale(l):
        # type: (Locale) -> None
        pass


class JFrame(Frame):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(JFrame, self).__init__(*args)


class JInternalFrame(JComponent):
    def __init__(
        self,
        title=None,  # type: Optional[AnyStr]
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
        # type: (*Any) -> None
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
        # type: (int) -> int
        pass

    def getLayer(self, c):
        # type: (Component) -> int
        pass

    def highestLayer(self):
        # type: () -> int
        pass

    def lowestLayer(self):
        # type: () -> int
        pass

    def setPosition(self, c, position):
        # type: (Component, int) -> None
        pass


class JDesktopPane(JLayeredPane):
    LIVE_DRAG_MODE = None  # type: int
    OUTLINE_DRAG_MODE = None  # type: int

    def __init__(self):
        # type: () -> None
        super(JDesktopPane, self).__init__()

    def getAllFrames(self):
        # type: () -> List[JInternalFrame]
        pass

    def getAllFramesInLayer(self, layer):
        # type: (int) -> List[JInternalFrame]
        pass

    def getDesktopManager(self):
        # type: () -> DesktopManager
        pass

    def getDragMode(self):
        # type: () -> int
        pass

    def getSelectedFrame(self):
        # type: () -> JInternalFrame
        pass

    def getUI(self):
        # type: () -> DesktopPaneUI
        pass

    def getUIClassID(self):
        # type: () -> AnyStr
        pass

    def updateUI(self):
        # type: () -> None
        pass


class JOptionPane(JComponent):
    """JOptionPane makes it easy to pop up a standard dialog box that
    prompts users for a value or informs them of something.

    For information about using JOptionPane, see How to Make Dialogs, a
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
        title=None,  # type: Optional[AnyStr]
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
        title=None,  # type: Optional[AnyStr]
        messageType=None,  # type: Optional[int]
        icon=None,  # type: Optional[Icon]
        selectionValues=None,  # type: Optional[List[Any]]
        initialSelectionValue=None,  # type: Optional[Any]
    ):
        # type: (...) -> AnyStr
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
        title=None,  # type: Optional[AnyStr]
        messageType=None,  # type: Optional[int]
        icon=None,  # type: Optional[Icon]
    ):
        # type: (...) -> None
        print(parentComponent, message, title, messageType, icon)

    @staticmethod
    def showOptionDialog(
        parentComponent,  # type: Optional[Any]
        message,  # type: Any
        title=None,  # type: Optional[AnyStr]
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
        # type: (*Any) -> None
        super(JPanel, self).__init__()
        print(args)


class JToolTip(JComponent):
    def __init__(self):
        # type: () -> None
        super(JToolTip, self).__init__()

    def getComponent(self):
        # type: () -> JComponent
        pass

    def getTipText(self):
        # type: () -> AnyStr
        pass


class JPopupMenu(JComponent):
    """An implementation of a popup menu -- a small window that pops up
    and displays a series of choices.

    A JPopupMenu is used for the menu that appears when the user selects
    an item on the menu bar. It is also used for "pull-right" menu that
    appears when the selects a menu item that activates it. Finally, a
    JPopupMenu can also be used anywhere else you want a menu to appear.
    For example, when the user right-clicks in a specified area.
    """

    def __init__(self, label=None):
        # type: (Optional[AnyStr]) -> None
        super(JPopupMenu, self).__init__()
        print(label)


class JRootPane(JComponent):
    """A lightweight container used behind the scenes by JFrame,
    JDialog, JWindow, JApplet, and JInternalFrame.
    """

    def __init__(self):
        # type: () -> None
        super(JRootPane, self).__init__()


class JTextField(JTextComponent):
    """JTextField is a lightweight component that allows the editing of
    a single line of text.
    """

    def __init__(self, *args):
        # type: (*Any) -> None
        super(JTextField, self).__init__()


class JPasswordField(JTextField):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(JPasswordField, self).__init__(*args)

    def copy(self):
        # type: () -> None
        pass

    def cut(self):
        # type: () -> None
        pass

    def echoCharIsSet(self):
        # type: () -> bool
        pass

    def getEchoChar(self):
        # type: () -> AnyStr
        pass

    def getPassword(self):
        # type: () -> Any
        return array.array("c", "password")

    def getText(self, *args):
        # type: (*int) -> unicode
        warnings.warn(
            "As of Java 2 platform v1.2, replaced by getPassword.",
            DeprecationWarning,
        )
        return unicode("password")

    def getUIClassID(self):
        # type: () -> AnyStr
        pass

    def setEchoChar(self, c):
        # type: (AnyStr) -> None
        pass

    def updateUI(self):
        # type: () -> None
        pass
