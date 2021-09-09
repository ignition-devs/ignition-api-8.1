"""Navigation Functions.

The following functions allow you to open and close windows in the
client.
"""

from __future__ import print_function

__all__ = [
    "centerWindow",
    "closeParentWindow",
    "closeWindow",
    "desktop",
    "getCurrentWindow",
    "goBack",
    "goForward",
    "goHome",
    "openWindow",
    "openWindowInstance",
    "swapTo",
    "swapWindow",
]

from abc import ABCMeta, abstractmethod

from java.util import EventObject
from javax.swing import JInternalFrame


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


class INavUtilities(ABCMeta):
    """Parent interface to coordinate the functions between NavUtilities
    and NavUtilitiesDispatcher.
    """

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def centerWindow(cls, arg):
        pass

    @abstractmethod
    def closeParentWindow(cls, event):
        pass

    @abstractmethod
    def closeWindow(cls, arg):
        pass

    @abstractmethod
    def getCurrentWindow(cls):
        pass

    @abstractmethod
    def goBack(cls):
        pass

    @abstractmethod
    def goForward(cls):
        pass

    @abstractmethod
    def goHome(cls):
        pass

    @abstractmethod
    def openWindow(cls, *args):
        pass

    @abstractmethod
    def openWindowImpl(cls, path, params, openAdditional):
        pass

    @abstractmethod
    def openWindowInstance(cls, *args):
        pass

    @abstractmethod
    def swapTo(cls, *args):
        pass

    @abstractmethod
    def swapWindow(cls, *args):
        pass


def centerWindow(arg):
    """Given a window path, or a reference to a window itself, it will
    center the window.

    The window should be floating and non-maximized. If the window can't
    be found, this function will do nothing.

    Args:
        arg (object): The path of the window (str) or a reference to the
            window (FPMIWindow) to center.
    """
    print(arg)


def closeParentWindow(event):
    """Closes the parent window given a component event object.

    Args:
        event (EventObject): A component event object. The enclosing
            window for the component will be closed.
    """
    print(event)


def closeWindow(arg):
    """Given a window path, or a reference to a window itself, it will
    close the window.

    If the window can't be found, this function will do nothing.

    Args:
        arg (object): A reference to the window to close as an
            FPMIWindow instance or the path of the window to close as a
            String.
    """
    print(arg)


def desktop(handle="primary"):
    """Allows for invoking system.nav functions on a specific desktop.

    Args:
        handle (str): The handle for the desktop to use. The screen
            index casted as a string may be used instead of the handle.
            If omitted, this will default to the Primary Desktop.
            Alternatively, the handle "primary" can be used to refer to
            the Primary Desktop.

    Returns:
        INavUtilities: A copy of system.nav that will alter the desktop
            named by the given handle.
    """
    print(handle)
    return INavUtilities()


def getCurrentWindow():
    """Returns the path of the current "main screen" window, which is
    defined as the maximized window.

    With the Typical Navigation Strategy, there is only ever one
    maximized window at a time.

    Returns:
        str: The path of the current "main screen" window - the
            maximized window.
    """
    return "Path/To/Maximized Window"


def goBack():
    """When using the Typical Navigation Strategy, this function will
    navigate back to the previous main screen window.

    Returns:
        FPMIWindow: The window that was returned to.
    """
    return FPMIWindow("Back")


def goForward():
    """When using the Typical Navigation Strategy, this function will
    navigate "forward" to the last main-screen window the user was on
    when they executed a system.nav.goBack().

    Returns:
        FPMIWindow: The window that was returned to.
    """
    return FPMIWindow("Forward")


def goHome():
    """When using the Typical Navigation Strategy, this function will
    navigate to the "home" window.

    This is automatically detected as the first main-screen window shown
    in a project.

    Returns:
        FPMIWindow: The window that was returned to.
    """
    return FPMIWindow("Home")


def openWindow(path, params=None):
    """Opens the window with the given path.

    If the window is already open, brings it to the front. The optional
    params dictionary contains key:value pairs which will be used to set
    the target window's root container's dynamic variables.

    Args:
        path (str): The path to the window to open.
        params (dict): A dictionary of parameters to pass into the
            window. The keys in the dictionary must match dynamic
            property names on the target window's root container. The
            values for each key will be used to set those properties.
            Optional.

    Returns:
        FPMIWindow: A reference to the opened window.
    """
    print(path, params)
    return FPMIWindow("Opened Window")


def openWindowInstance(path, params=None):
    """Operates exactly like system.nav.openWindow, except that if the
    named window is already open, then an additional instance of the
    window will be opened.

    There is no limit to the number of additional instances of a window
    that you can open.

    Args:
        path (str): The path to the window to open.
        params (dict): A dictionary of parameters to pass into the
            window. The keys in the dictionary must match dynamic
            property names on the target window's root container. The
            values for each key will be used to set those properties.
            Optional.

    Returns:
        FPMIWindow: A reference to the opened window.
    """
    print(path, params)
    return FPMIWindow("Window Instance")


def swapTo(path, params=None):
    """Performs a window swap from the current main screen window to the
    window specified.

    Swapping means that the opened window will take the place of the
    closing window - in this case it will be maximized.

    This function works like system.nav.swapWindow except that you
    cannot specify the source for the swap.

    Args:
        path (str): The path to the window to open.
        params (dict): A dictionary of parameters to pass into the
            window. The keys in the dictionary must match dynamic
            property names on the target window's root container. The
            values for each key will be used to set those properties.
            Optional.

    Returns:
        FPMIWindow: A reference to the swapped-to window.
    """
    print(path, params)
    return FPMIWindow("Swapped To")


def swapWindow(arg, swapToPath, params=None):
    """Performs a window swap.

    This means that one window is closed, and another is opened and
    takes its place - assuming its size, floating state, and
    maximization state. This gives a seamless transition; one window
    seems to simply turn into another.

    Args:
        arg (object): The path of the window (str) to swap from. Must be
            a currently open window, or this will act like an
            openWindow, or a component event (EventObject) whose
            enclosing window will be used as the "swap-from" window.
        swapToPath (str): The name of the window to swap to.
        params (dict): A dictionary of parameters to pass into the
            window. The keys in the dictionary must match dynamic
            property names on the target window's root container. The
            values for each key will be used to set those properties.
            Optional.

    Returns:
        FPMIWindow: A reference to the swapped-to window.
    """
    print(arg, swapToPath, params)
    return FPMIWindow("Swapped To")
