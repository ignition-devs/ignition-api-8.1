"""GUI Functions.

The following functions allow you to control windows and create popup
interfaces.
"""

from __future__ import print_function

__all__ = [
    "ACCL_CONSTANT",
    "ACCL_EASE",
    "ACCL_FAST_TO_SLOW",
    "ACCL_NONE",
    "ACCL_SLOW_TO_FAST",
    "COORD_DESIGNER",
    "COORD_SCREEN",
    "chooseColor",
    "closeDesktop",
    "color",
    "confirm",
    "convertPointToScreen",
    "createPopupMenu",
    "desktop",
    "errorBox",
    "findWindow",
    "getCurrentDesktop",
    "getDesktopHandles",
    "getOpenedWindowNames",
    "getOpenedWindows",
    "getParentWindow",
    "getQuality",
    "getScreenIndex",
    "getScreens",
    "getSibling",
    "getWindow",
    "getWindowNames",
    "inputBox",
    "isTouchscreenModeEnabled",
    "messageBox",
    "openDesktop",
    "openDiagnostics",
    "passwordBox",
    "setScreenIndex",
    "setTouchscreenModeEnabled",
    "showNumericKeypad",
    "showTouchscreenKeyboard",
    "transform",
    "warningBox",
]

from typing import Any, Callable, List, Optional, Tuple, Union

from com.inductiveautomation.factorypmi.application import FPMIWindow
from com.inductiveautomation.factorypmi.application.script.builtin import (
    WindowUtilities,
)
from java.awt import Color
from java.lang import String
from java.org.jdesktop.core.animation.timing import Animator
from java.util import EventObject
from javax.swing import (
    JComponent,
    JFrame,
    JLabel,
    JOptionPane,
    JPanel,
    JPopupMenu,
    JTextField,
)

# Constants
ACCL_NONE = 0
ACCL_CONSTANT = 1
ACCL_FAST_TO_SLOW = 2
ACCL_SLOW_TO_FAST = 3
ACCL_EASE = 4
COORD_SCREEN = 0
COORD_DESIGNER = 1


def chooseColor(initialColor, dialogTitle="Choose Color"):
    # type: (Color, Optional[String]) -> Color
    """Prompts the user to pick a color using the default color-chooser
    dialog box.

    Args:
        initialColor: A color to use as a starting point in the color
            choosing popup.
        dialogTitle: The title for the color choosing popup. Defaults to
            "Choose Color". Optional.

    Returns:
        The new color chosen by the user.
    """
    print(initialColor, dialogTitle)
    return Color()


def closeDesktop(handle):
    # type: (String) -> None
    """Allows you to close any of the open desktops associated with the
    current client.

    Args:
        handle: The handle for the desktop to close. The screen index
            cast as a string may be used instead of the handle. If
            omitted, this will default to the Primary Desktop.
            Alternatively, the handle "primary" can be used to refer to
            the Primary Desktop.
    """
    print(handle)


def color(*args):
    # type: (*Any) -> Color
    """Creates a new color object, either by parsing a string or by
    having the RGB[A] channels specified explicitly.

    Args:
        args: Variable-length argument list.

    Returns:
        The newly created color.
    """
    print(args)
    return Color(*args)


def confirm(message, title="Confirm", allowCancel=False):
    # type: (String, Optional[String], Optional[bool]) -> Optional[bool]
    """Displays a confirmation dialog box to the user with "Yes", "No"
    options, and a custom message.

    Args:
        message: The message to show in the confirmation dialog.
        title: The title for the confirmation dialog. Optional.
        allowCancel: Show a cancel button in the dialog. Optional.

    Returns:
        True if the user selected "Yes", False if the user
        selected "No", None if the user selected "Cancel".
    """
    options = ["Yes", "No"]

    if allowCancel:
        options.append("Cancel")

    choice = JOptionPane.showOptionDialog(
        None,
        message,
        title,
        JOptionPane.YES_NO_CANCEL_OPTION,
        JOptionPane.QUESTION_MESSAGE,
        None,
        options,
        options[0],
    )

    return (
        not bool(choice)
        if choice in [JOptionPane.YES_OPTION, JOptionPane.NO_OPTION]
        else None
    )


def convertPointToScreen(x, y, event):
    # type: (int, int, EventObject) -> Tuple[int, int]
    """Converts a pair of coordinates that are relative to
    the upper-left corner of some component to be relative to the
    upper-left corner of the entire screen.

    Args:
        x: The X-coordinate, relative to the component that fired the
            event.
        y: The Y-coordinate, relative to the component that fired the
            event.
        event: An event object for a component event.

    Returns:
        A tuple of (x,y) in screen coordinates.
    """
    print(x, y, event)
    return x, y


def createPopupMenu(itemNames, itemFunctions):
    # type: (List[String], List[Callable[..., Any]]) -> JPopupMenu
    """Creates a new popup menu, which can then be shown over a
    component on a mouse event.

    Args:
        itemNames: A list of names to create popup menu items with.
        itemFunctions: A list of functions to match up with the names.

    Returns:
        The javax.swing.JPopupMenu that was created.
    """
    print(itemNames, itemFunctions)
    return JPopupMenu()


def desktop(handle):
    # type: (String) -> WindowUtilities
    """Allows for invoking system.gui functions on a specific desktop.

    Args:
        handle: The handle for the desktop to use. The screen index cast
            as a string may be used instead of the handle. If omitted,
            this will default to the Primary Desktop. Alternatively, the
            handle "primary" can be used to refer to the primary
            desktop.

    Returns:
        A copy of system.gui that will be relative to the desktop named
        by the given handle.
    """
    print(handle)
    return WindowUtilities()


def errorBox(message, title="Error"):
    # type: (String, Optional[String]) -> None
    """Displays an error-style message box to the user.

    Args:
        message: The message to display in an error box.
        title: The title for the error box. Optional.
    """
    JOptionPane.showMessageDialog(None, message, title, JOptionPane.ERROR_MESSAGE)


def findWindow(path):
    # type: (String) -> List[FPMIWindow]
    """Finds and returns a list of windows with the given path.

    If the window is not open, an empty list will be returned. Useful
    for finding all instances of an open window that were opened with
    system.gui.openWindowInstance.

    Args:
        path: The path of the window to search for.

    Returns:
        A list of window objects. May be empty if window is not open, or
        have more than one entry if multiple windows are open.
    """
    print(path)
    return [FPMIWindow("Window")]


def getCurrentDesktop():
    # type: () -> String
    """Returns the handle of the desktop this function was called from.

    Commonly used with the system.gui.desktop and system.nav.desktop
    functions.

    Returns:
        The handle of the current desktop.
    """
    return "primary"


def getDesktopHandles():
    # type: () -> List[String]
    """Gets a list of all secondary handles of the open desktops
    associated with the current client.

    In this case, secondary means any desktop frame opened by the
    original client frame.

    Example:
        If the original client opened 2 new frames ('left client' and
        'right client'), then this function would return ['left client',
        'right client'].

    Returns:
        A list of window handles of all secondary Desktop frames.
    """
    return ["left client", "right client"]


def getOpenedWindowNames():
    # type: () -> Tuple[String, ...]
    """Finds all of the currently open windows and returns a tuple of
    their paths.

    Returns:
        A tuple of strings, representing the path of each window that is
        open.
    """
    return "window_1", "window_2", "window_n"


def getOpenedWindows():
    # type: () -> Tuple[FPMIWindow, ...]
    """Finds all of the currently open windows, returning a tuple of
    references to them.

    Returns:
         A tuple of the opened windows. Not their names, but the actual
         window objects themselves.
    """
    return FPMIWindow("Main Window"), FPMIWindow("Other Window")


def getParentWindow(event):
    # type: (EventObject) -> FPMIWindow
    """Finds the parent (enclosing) window for the component that fired
    an event, returning a reference to it.

    Args:
        A component event object.

    Returns:
        The window that contains the component that fired the event.
    """
    print(event)
    return FPMIWindow("Parent Window")


def getQuality(component, propertyName):
    # type: (JComponent, String) -> int
    """Returns the data quality for the property of the given component
    as an integer.

    This function can be used to check the quality of a Tag binding on a
    component in the middle of the script so that alternative actions
    can be taken in the event of device disconnections.

    Args:
        component: The component whose property is being checked.
        propertyName: The name of the property as a string value.

    Returns:
        The data quality of the given property as an integer.
    """
    print(component, propertyName)
    return 192


def getScreenIndex():
    # type: () -> int
    """Returns the returns an integer value representing the current
    screen index based on the screen from which this function was
    called.

    Returns:
        The screen from which the function was called.
    """
    return 0


def getScreens():
    # type: () -> List[Tuple[String, int, int]]
    """Get a list of all the monitors on the computer this client is
    open on.

    Use with system.gui.setScreenIndex() to move the client.

    Returns:
        A sequence of tuples of the form (index, width, height) for each
        screen device (monitor) available.
    """
    return [("primary", 1440, 900), ("secondary", 1920, 1080)]


def getSibling(event, name):
    # type: (EventObject, String) -> FPMIWindow
    """Given a component event object, looks up a sibling component.

    Shortcut for event.source.parent.getComponent("siblingName"). If no
    such sibling is found, the special value None is returned.

    Args:
        event: A component event object.
        name: The name of the sibling component.

    Returns:
        The sibling component itself.
    """
    print(event, name)
    return FPMIWindow("Sibling")


def getWindow(name):
    # type: (String) -> FPMIWindow
    """Finds a reference to an open window with the given name.

    Throws a ValueError if the named window is not open or not found.

    Args:
        name: The path to the window to field.

    Returns:
        A reference to the window, if it was open.
    """
    print(name)
    return FPMIWindow("Main Window")


def getWindowNames():
    # type: () -> Tuple[String, ...]
    """Returns a list of the paths of all windows in the current
    project, sorted alphabetically.

    Returns:
        A tuple of strings, representing the path of each window defined
        in the current project.
    """
    return "Main Window", "Main Window 1", "Main Window 2"


def inputBox(message, defaultText=""):
    # type: (String, String) -> Optional[String]
    """Opens up a popup input dialog box.

    This dialog box will show a prompt message, and allow the user to
    type in a string. When the user is done, they can press "OK" or
    "Cancel". If OK is pressed, this function will return with the value
    that they typed in. If Cancel is pressed, this function will return
    the value None.

    Args:
        message: The message to display for the input box. Will accept
            HTML formatting.
        defaultText: The default text to initialize the input box with.
            Optional.

    Returns:
        The string value that was entered in the input box.
    """
    options = ["OK", "Cancel"]

    panel = JPanel()
    label = JLabel("{}: ".format(message))
    panel.add(label)
    text_field = JTextField(25)
    text_field.setText(defaultText)
    panel.add(text_field)

    choice = JOptionPane.showOptionDialog(
        None,
        panel,
        "Input",
        JOptionPane.OK_CANCEL_OPTION,
        JOptionPane.QUESTION_MESSAGE,
        None,
        options,
        options[0],
    )

    return text_field.getText() if choice == JOptionPane.OK_OPTION else None


def isTouchscreenModeEnabled():
    # type: () -> bool
    """Checks whether or not the running client's touchscreen mode is
    currently enabled.

    Returns:
         True if the Client currently has Touch Screen mode activated.
    """
    return False


def messageBox(message, title="Information"):
    # type: (String, String) -> None
    """Displays an informational-style message popup box to the user.

    Args:
        message: The message to display. Will accept HTML formatting.
        title: The title for the message box. Optional.
    """
    JOptionPane.showMessageDialog(None, message, title, JOptionPane.INFORMATION_MESSAGE)


def openDesktop(
    screen=0,  # type: int
    handle=None,  # type: Optional[String]
    title=None,  # type: Optional[String]
    width=None,  # type: Optional[int]
    height=None,  # type: Optional[int]
    x=0,  # type: int
    y=0,  # type: int
    windows=None,  # type: Optional[List[String]]
):
    # type: (...) -> JFrame
    """Creates an additional Desktop in a new frame.

    Args:
        screen: The screen index of which screen to place the new frame
            on. If omitted, screen 0 will be used. Optional.
        handle: A name for the desktop. If omitted, the screen index
            will be used. Optional.
        title: The title for the new frame. If omitted, the index handle
            will be used. If the handle and title are omitted, the
            screen index will be used. Optional.
        width: The width for the new Desktop's frame. If omitted, frame
            will become maximized on the specified monitor. Optional.
        height: The width for the new desktop's frame. If omitted, frame
            will become maximized on the specified monitor. Optional.
        x: The X coordinate for the new desktop's frame. Only used if
            both width and height are specified. If omitted, defaults to
            0. Optional.
        y: The Y coordinate for the new desktop's frame. Only used if
            both width and height are specified. If omitted, defaults to
            0. Optional.
        windows: A list of window paths to open in the new Desktop
            frame. If omitted, the desktop will open without any opened
            windows. Optional.

    Returns:
        A reference to the new Desktop frame object.
    """
    print(screen, handle, title, width, height, x, y, windows)
    return JFrame()


def openDiagnostics():
    # type: () -> None
    """Opens the client runtime diagnostics window, which provides
    information regarding performance, logging, active threads,
    connection status, and the console.

    This provides an opportunity to open the diagnostics window in
    situations where the menu bar in the client is hidden, and the
    keyboard shortcut can not be used.
    """
    pass


def passwordBox(
    message,  # type:String
    title="Password",  # type: String
    echoChar="*",  # type: String
):
    # type: (...) -> Optional[String]
    """Pops up a special input box that uses a password field, so the
    text isn't echoed back in clear-text to the user.

    Returns the text they entered, or None if they canceled the dialog
    box.

    Args:
        message: The message for the password prompt. Will accept HTML
            formatting.
        title: A title for the password prompt. Optional.
        echoChar: A custom echo character. Defaults to: *. Optional.

    Returns:
        The password that was entered, or None if the prompt was
        canceled.
    """
    print(message, title, echoChar)
    return "password"


def setScreenIndex(index):
    # type: (int) -> None
    """Moves an open client to a specific monitor.

    Use with system.gui.getScreens() to identify monitors before moving.

    Args:
        index: The new monitor index for this client to move to. 0
            based.
    """
    print(index)


def setTouchscreenModeEnabled(enabled):
    # type: (bool) -> None
    """Alters a running Client's Touch Screen mode on the fly.

    Args:
        enabled: The new value for Touch Screen mode being enabled.
    """
    print(enabled)


def showNumericKeypad(
    initialValue,  # type: Union[float, int]
    fontSize=None,  # type: Optional[int]
    usePasswordMode=False,  # type: bool
):
    # type: (...) -> Union[float, int]
    """Displays a modal on-screen numeric keypad, allowing for arbitrary
    numeric entry using the mouse, or a finger on a touchscreen monitor.

    Returns the number that the user entered.

    Args:
        initialValue: The value to start the on-screen keypad with.
        fontSize: The font size to display in the keypad. Optional.
        usePasswordMode: If True, display a * for each digit. Optional.

    Returns:
        The value that was entered in the keypad.
    """
    print(initialValue, fontSize, usePasswordMode)
    return 43


def showTouchscreenKeyboard(initialText, fontSize=None, passwordMode=False):
    # type: (String, Optional[int], Optional[bool]) -> String
    """Displays a modal on-screen keyboard, allowing for arbitrary text
    entry using the mouse, or a finger on a touchscreen monitor.

    Returns the text that the user entered.

    Args:
        initialText: The text to start the on-screen keyboard with.
        fontSize: The font size to display in the keypad. Optional.
        passwordMode: True to activate password mode, where the text
            entered isn't echoed back clear-text. Optional.

    Returns:
        The text that was entered in the on-screen keyboard.
    """
    print(initialText, fontSize, passwordMode)
    return ""


def transform(
    component,  # type: JComponent
    newX=None,  # type: Optional[int]
    newY=None,  # type: Optional[int]
    newWidth=None,  # type: Optional[int]
    newHeight=None,  # type: Optional[int]
    duration=0,  # type: int
    callback=None,  # type: Optional[Callable[..., Any]]
    framesPerSecond=60,  # type: int
    acceleration=None,  # type: Optional[int]
    coordSpace=None,  # type: Optional[int]
):
    # type: (...) -> Animator
    """Sets a component's position and size at runtime.

    Additional arguments for the duration, framesPerSecond, and
    acceleration of the operation exist for animation. An optional
    callback argument will be executed when the transformation is
    complete.

    Note:
        The transformation is performed in Designer coordinate space on
        components which are centered or have more than two anchors.

    Args:
        component: The component to move or resize.
        newX: An optional x-coordinate to move to, relative to the
            upper-left corner of the component's parent container.
        newY: An optional y-coordinate to move to, relative to the
            upper-left corner of the component's parent container.
        newWidth: An optional width for the component.
        newHeight: An optional height for the component.
        duration: An optional duration over which the transformation
            will take place. If omitted or 0, the transform will take
            place immediately.
        callback: An optional function to be called when the
            transformation is complete.
        framesPerSecond: An optional frame rate argument which dictates
            how often the transformation updates over the given
            duration. The default is 60 frames per second.
        acceleration: An optional modifier to the acceleration of the
            transformation over the given duration. See system.gui
            constants for valid arguments.
        coordSpace: The coordinate space to use. When the default Screen
            Coordinates are used, the given size and position are
            absolute, as they appear in the client at runtime. When
            Designer Coordinates are used, the given size and position
            are pre-runtime adjusted values, as they would appear in the
            Designer. See system.gui constants for valid arguments.

    Returns:
        An object that contains pause(), resume(), and cancel() methods,
        allowing for a script to interrupt the animation.
    """
    print(
        component,
        newX,
        newY,
        newWidth,
        newHeight,
        duration,
        callback,
        framesPerSecond,
        acceleration,
        coordSpace,
    )
    return Animator()


def warningBox(message, title="Warning"):
    # type: (String, String) -> None
    """Displays a message to the user in a warning style popup dialog.

    Args:
        message: The message to display in the warning box. Will accept
            HTML formatting.
        title: The title for the warning box. Optional.
    """
    JOptionPane.showMessageDialog(None, message, title, JOptionPane.WARNING_MESSAGE)
