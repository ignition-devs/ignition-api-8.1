"""GUI Functions.

The following functions allow you to control windows and create popup
interfaces.
"""

from __future__ import print_function

__all__ = [
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

from java.awt import Color
from java.lang import Object
from java.util import EventObject
from javax.swing import (
    JComponent,
    JFrame,
    JInternalFrame,
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


class FPMIWindow(JInternalFrame):
    """FPMIWindow object."""

    # Fields.
    CACHE_ALWAYS = 2
    CACHE_AUTO = 0
    CACHE_NEVER = 1
    DOCK_EAST = 2
    DOCK_FLOAT = 0
    DOCK_NORTH = 2
    DOCK_SOUTH = 4
    DOCK_WEST = 3
    PARENT_WINDOW_NAME = "_parent"
    SHOW_ALWAYS = 0
    SHOW_NEVER = 1
    SHOW_MAXIMIZED = 2

    _path = "Path/To/Window"

    def __init__(self, name):
        self.name = name

    def getPath(self):
        return self._path

    def getRootContainer(self):
        print(self)


class WindowUtilities(Object):
    """WindowUtilities object."""

    def confirm(self, *args):
        pass

    def errorBox(self, *args):
        pass

    def inputBox(self, *args):
        pass

    def messageBox(self, *args):
        pass

    def passwordBox(self, *args):
        pass

    def warningBox(self, *args):
        pass


def _dummy(message, title):
    print(message, title)


def chooseColor(initialColor, dialogTitle="Choose Color"):
    """Prompts the user to pick a color using the default color-chooser
    dialog box.

    Args:
        initialColor (Color): A color to use as a starting point in the
            color choosing popup.
        dialogTitle (str): The title for the color choosing popup.
            Defaults to "Choose Color". Optional.

    Returns:
        Color: The new color chosen by the user.
    """
    print(initialColor, dialogTitle)
    return Color()


def closeDesktop(handle="primary"):
    """Allows you to close any of the open desktops associated with the
    current client.

    Args:
        handle (str): The handle for the desktop to close. The screen
            index cast as a string may be used instead of the handle. If
            omitted, this will default to the Primary Desktop.
            Alternatively, the handle "primary" can be used to refer to
            the Primary Desktop.
    """
    print(handle)


def color(*args):
    """Creates a new color object, either by parsing a string or by
    having the RGB[A] channels specified explicitly. See toColor to see
    a list of available color names.

    Args:
        args: Variable-length argument list.

    Returns:
        Color: The newly created color.
    """
    print(args)


def confirm(message, title="Confirm", allowCancel=False):
    """Displays a confirmation dialog box to the user with "Yes", "No"
    and "Cancel" options, and a custom message.

    Args:
        message (str): The message to show in the confirmation dialog.
        title (str): The title for the confirmation dialog. Optional.
        allowCancel (bool): Show a cancel button in the dialog.
            Optional.

    Returns:
        bool: True (1) if the user selected "Yes", False (0) if the user
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
    """Converts a pair of coordinates that are relative to the
    upper-left corner of some component to be relative to the upper-left
    corner of the entire screen.

    Args:
        x (int): The X-coordinate, relative to the component that fired
            the event.
        y (int): The Y-coordinate, relative to the component that fired
            the event.
        event (EventObject): An event object for a component event.

    Returns:
        tuple: A tuple of (x,y) in screen coordinates.
    """
    print(x, y, event)
    return x, y


def createPopupMenu(itemNames, itemFunctions):
    """Creates a new popup menu, which can then be shown over a
    component on a mouse event.

    Args:
        itemNames (list[str]): A list of names to create popup menu
            items with.
        itemFunctions (list[object]): A list of functions to match up
            with the names.

    Returns:
        JPopupMenu: The javax.swing.JPopupMenu that was created.
    """
    print(itemNames, itemFunctions)
    return JPopupMenu()


def desktop(handle="primary"):
    """Allows for invoking system.gui functions on a specific desktop.

    Args:
        handle (str): The handle for the desktop to use. The screen
            index cast as a string may be used instead of the handle. If
            omitted, this will default to the Primary Desktop.
            Alternatively, the handle "primary" can be used to refer to
            the Primary Desktop.

    Returns:
        WindowUtilities: A copy of system.gui that will be relative to
            the desktop named by the given handle.
    """
    print(handle)
    return WindowUtilities()


def errorBox(message, title="Error"):
    """Displays an error-style message box to the user.

    Args:
        message (str): The message to display in an error box.
        title (str): The title for the error box. Optional.
    """
    JOptionPane.showMessageDialog(
        None, message, title, JOptionPane.ERROR_MESSAGE
    )


def findWindow(path):
    """Finds and returns a list of windows with the given path.

    If the window is not open, an empty list will be returned. Useful
    for finding all instances of an open window that were opened with
    system.gui.openWindowInstance.

    Args:
        path (str): The path of the window to search for.

    Returns:
        list[object]: A list of window objects. May be empty if window
            is not open, or have more than one entry if multiple windows
            are open.
    """
    print(path)
    return []


def getCurrentDesktop():
    """Returns the handle of the desktop this function was called from.

    Commonly used with the system.gui.desktop and system.nav.desktop
    functions.

    Returns:
        str: The handle of the current desktop.
    """
    return "primary"


def getDesktopHandles():
    """Gets a list of all secondary handles of the open desktops
    associated with the current client.

    In this case, secondary means any desktop frame opened by the
    original client frame.

    Example:
        If the original client opened 2 new frames ('left client' and
        'right client'), then this function would return ['left client',
        'right client'].

    Returns:
        list[str]: A list of window handles of all secondary Desktop
            frames.
    """
    return ["left client", "right client"]


def getOpenedWindowNames():
    """Finds all of the currently open windows, returning a tuple of
    their paths.

    Returns:
        tuple: A tuple of strings, representing the path of each window
            that is open.
    """
    return "window_1", "window_2", "window_n"


def getOpenedWindows():
    """Finds all of the currently open windows, returning a tuple of
    references to them.

    Returns:
         tuple: A tuple of the opened windows. Not their names, but the
            actual window objects themselves.
    """
    return [FPMIWindow("Main Window")]


def getParentWindow(event):
    """Finds the parent (enclosing) window for the component that fired
    an event, returning a reference to it.

    Args:
        event (EventObject): A component event object.

    Returns:
        object: The window that contains the component that fired the
            event.
    """
    print(event)
    return object


def getQuality(component, propertyName):
    """Returns the data quality for the property of the given component
    as an integer.

    This function can be used to check the quality of a Tag binding on a
    component in the middle of the script so that alternative actions
    can be taken in the event of device disconnections.

    Args:
        component (JComponent): The component whose property is being
            checked.
        propertyName (str): The name of the property as a string value.

    Returns:
        int: The data quality of the given property as an integer.
    """
    print(component, propertyName)
    return 192


def getScreenIndex():
    """Returns the returns an integer value representing the current
    screen index based on the screen this function was called from.

    Returns:
        int: The screen that the function was called from.
    """
    return 0


def getScreens():
    """Get a list of all the monitors on the computer this client is
    open on.

    Use with system.gui.setScreenIndex() to move the client.

    Returns:
        list[tuple]: A sequence of tuples of the form (index, width,
            height) for each screen device (monitor) available.
    """
    return [(0, 1024, 768), (1, 3840, 2160)]


def getSibling(event, name):
    """Given a component event object, looks up a sibling component.

    Shortcut for event.source.parent.getComponent("siblingName"). If no
    such sibling is found, the special value None is returned.

    Args:
        event (EventObject): A component event object.
        name (str): The name of the sibling component.

    Returns:
        object: The sibling component itself.
    """
    print(event, name)
    return FPMIWindow("Sibling")


def getWindow(name):
    """Finds a reference to an open window with the given name.

    Throws a ValueError if the named window is not open or not found.

    Args:
        name (str): The path to the window to field.

    Returns:
        FPMIWindow: A reference to the window, if it was open. Use
            .getRootContainer() to grab the root container of the
            window.
    """
    print(name)
    return FPMIWindow("Main Window")


def getWindowNames():
    """Returns a list of the paths of all windows in the current
    project, sorted alphabetically.

    Returns:
        tuple[str]: A tuple of strings, representing the path of each
            window defined in the current project.
    """
    return "Main Window", "Main Window 1", "Main Window 2"


def inputBox(message, defaultText=None):
    """Opens up a popup input dialog box.

    This dialog box will show a prompt message, and allow the user to
    type in a string. When the user is done, they can press "OK" or
    "Cancel". If OK is pressed, this function will return with the value
    that they typed in. If Cancel is pressed, this function will return
    the value None.

    Args:
        message (str): The message to display for the input box. Will
            accept html formatting.
        defaultText (str): The default text to initialize the input box
            with. Optional.

    Returns:
        str: The string value that was entered in the input box.
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
    """Checks whether or not the running client's touchscreen mode is
    currently enabled.

    Returns:
         bool: True(1) if the client currently has touchscreen mode
            activated.
    """
    return False


def messageBox(message, title="Information"):
    """Displays an informational-style message popup box to the user.

    Args:
        message (str): The message to display. Will accept html
            formatting.
        title (str): The title for the message box. Optional.
    """
    JOptionPane.showMessageDialog(
        None, message, title, JOptionPane.INFORMATION_MESSAGE
    )


def openDesktop(
    screen=0,
    handle=None,
    title=None,
    width=None,
    height=None,
    x=0,
    y=0,
    windows=None,
):
    """Creates an additional Desktop in a new frame.

    Args:
        screen (int): The screen index of which screen to place the new
            frame on. If omitted, screen 0 will be used.
        handle (str): A name for the desktop. If omitted, the screen
            index will be used.
        title (str): The title for the new frame. If omitted, the index
            handle will be used. If the handle and title are omitted,
            the screen index will be used.
        width (int): The width for the new Desktop's frame. If omitted,
            frame will become maximized on the specified monitor.
        height (int): The width for the new desktop's frame. If omitted,
            frame will become maximized on the specified monitor.
        x (int): The X coordinate for the new desktop's frame. Only used
            if both width and height are specified. If omitted, defaults
            to 0.
        y (int): The Y coordinate for the new desktop's frame. Only used
            if both width and height are specified. If omitted, defaults
            to 0.
        windows (list[str]): A list of window paths to open in the new
            Desktop frame.

    Returns:
        JFrame: A reference to the new Desktop frame.
    """
    print(screen, handle, title, width, height, x, y, windows)
    return JFrame()


def openDiagnostics():
    """Opens the client runtime diagnostics window, which provides
    information regarding performance, logging, active threads,
    connection status, and the console.

    This provides an opportunity to open the diagnostics window in
    situations where the menu bar in the client is hidden, and the
    keyboard shortcut can not be used.
    """
    pass


def passwordBox(message, title="Password", echoChar="*"):
    """Pops up a special input box that uses a password field, so the
    text isn't echoed back in clear-text to the user.

    Returns the text they entered, or None if they canceled the dialog
    box.

    Args:
        message (str): The message for the password prompt. Will accept
            html formatting.
        title (str): A title for the password prompt. Optional.
        echoChar (str): A custom echo character. Defaults to: *.
            Optional.

    Returns:
        str: The password that was entered, or None if the prompt was
            canceled.
    """
    print(message, title, echoChar)
    return "password"


def setScreenIndex(index):
    """Moves an open client to a specific monitor.

    Use with system.gui.getScreens() to identify monitors before moving.

    Args:
        index (int): The new monitor index for this client to move to. 0
            based.
    """
    print(index)


def setTouchscreenModeEnabled(enabled):
    """Alters a running client's touchscreen mode on the fly.

    Args:
        enabled (bool): The new value for touchscreen mode being
            enabled.
    """
    print(enabled)


def showNumericKeypad(initialValue=None, fontSize=None, usePasswordMode=False):
    """Displays a modal on-screen numeric keypad, allowing for arbitrary
    numeric entry using the mouse, or a finger on a touchscreen monitor.

    Returns the number that the user entered.

    Args:
        initialValue (object): The value to start the on-screen keypad
            with.
        fontSize (int): The font size to display in the keypad.
            Optional.
        usePasswordMode (bool): If True, display a * for each digit.
            Optional.

    Returns:
        object: The value that was entered in the keypad.
    """
    print(initialValue, fontSize, usePasswordMode)
    return 43


def showTouchscreenKeyboard(
    initialText=None, fontSize=None, passwordMode=False
):
    """Displays a modal on-screen keyboard, allowing for arbitrary text
    entry using the mouse, or a finger on a touchscreen monitor.

    Returns the text that the user "typed".

    Args:
        initialText: The text to start the on-screen keyboard with.
        fontSize (int): The font size to display in the keypad.
            Optional.
        passwordMode (bool): True (1) to activate password mode, where
            the text entered isn't echoed back clear-text. Optional.

    Returns:
        str: The text that was "typed" in the on-screen keyboard.
    """
    print(initialText, fontSize, passwordMode)
    return ""


def transform(
    component,
    newX=None,
    newY=None,
    newWidth=None,
    newHeight=None,
    duration=0,
    callback=None,
    framesPerSecond=60,
    acceleration=None,
    coordSpace=None,
):
    """Sets a component's position and size at runtime.

    Additional arguments for the duration, framesPerSecond, and
    acceleration of the operation exist for animation. An optional
    callback argument will be executed when the transformation is
    complete.

    Note: The transformation is performed in Designer coordinate space
    on components which are centered or have more than 2 anchors.

    Args:
        component (JComponent): The component to move or resize.
        newX (int): An optional x-coordinate to move to, relative to the
            upper-left corner of the component's parent container.
        newY (int): An optional y-coordinate to move to, relative to the
            upper-left corner of the component's parent container.
        newWidth (int): An optional width for the component.
        newHeight (int):An optional height for the component.
        duration (int): An optional duration over which the
            transformation will take place. If omitted or 0, the
            transform will take place immediately.
        callback (object): An optional function to be called when the
            transformation is complete.
        framesPerSecond (int): An optional frame rate argument which
            dictates how often the transformation updates over the given
            duration. The default is 60 frames per second.
        acceleration (int): An optional modifier to the acceleration of
            the transformation over the given duration. See system.gui
            constants for valid arguments.
        coordSpace (int): The coordinate space to use. When the default
            Screen Coordinates are used, the given size and position are
            absolute, as they appear in the client at runtime. When
            Designer Coordinates are used, the given size and position
            are pre-runtime adjusted values, as they would appear in the
            Designer. See system.gui constants for valid arguments.

    Returns:
        object: An animation object that the script can use to pause(),
            resume(), or cancel() the transformation.
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


def warningBox(message, title="Warning"):
    """Displays a message to the user in a warning style pop-up dialog.

    Args:
        message (str): The message to display in the warning box. Will
            accept html formatting.
        title (str): The title for the warning box. Optional.
    """
    JOptionPane.showMessageDialog(
        None, message, title, JOptionPane.WARNING_MESSAGE
    )
