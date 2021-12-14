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

from typing import Any, Dict, Optional, Union

from com.inductiveautomation.factorypmi.application import FPMIWindow
from com.inductiveautomation.factorypmi.application.script.builtin import NavUtilities
from java.lang import String
from java.util import EventObject


def centerWindow(arg):
    # type: (Union[String, FPMIWindow]) -> None
    """Given a window path, or a reference to a window itself, it will
    center the window.

    The window should be floating and non-maximized. If the window can't
    be found, this function will do nothing.

    Args:
        arg: The path of the window or a reference to the window to
            center.
    """
    print(arg)


def closeParentWindow(event):
    # type: (EventObject) -> None
    """Closes the parent window given a component event object.

    Args:
        event: A component event object. The enclosing window for the
            component will be closed.
    """
    print(event)


def closeWindow(arg):
    # type: (Union[String, FPMIWindow]) -> None
    """Given a window path, or a reference to a window itself, it will
    close the window.

    If the window can't be found, this function will do nothing.

    Args:
        arg: The path of the window or a reference to the window to
            center.
    """
    print(arg)


def desktop(handle="primary"):
    # type: (Optional[String]) -> NavUtilities
    """Allows for invoking system.nav functions on a specific desktop.

    Args:
        handle: The handle for the desktop to use. May be omitted for
            the primary desktop. Optional.

    Returns:
        A copy of system.nav that will alter the desktop named by the
        given handle.
    """
    print(handle)
    return NavUtilities()


def getCurrentWindow():
    # type: () -> String
    """Returns the path of the current "main screen" window, which is
    defined as the maximized window.

    With the typical navigation, there is only ever one maximized window
    at a time.

    Returns:
        The path of the current "main screen" window - the maximized
        window.
    """
    return "Path/To/Maximized Window"


def goBack():
    # type: () -> FPMIWindow
    """When using the typical navigation strategy, this function will
    navigate back to the previous main screen window.

    Returns:
        A reference to window that was navigated to.
    """
    return FPMIWindow("Back")


def goForward():
    # type: () -> FPMIWindow
    """When using the typical navigation strategy, this function will
    navigate "forward" to the last main screen window the user was on
    when they executed a system.nav.goBack().

    Returns:
        A reference to window that was navigated to.
    """
    return FPMIWindow("Forward")


def goHome():
    # type: () -> FPMIWindow
    """When using the typical navigation strategy, this function will
    navigate to the "home" window.

    This is automatically detected as the first main-screen window shown
    in a project.

    Returns:
        A reference to window that was navigated to.
    """
    return FPMIWindow("Home")


def openWindow(path, params=None):
    # type: (String, Optional[Dict[String, Any]]) -> FPMIWindow
    """Opens the window with the given path.

    If the window is already open, brings it to the front. The optional
    params dictionary contains key:value pairs which will be used to set
    the target window's root container's dynamic variables.

    Args:
        path: The path to the window to open.
        params: A dictionary of parameters to pass into the window. The
            keys in the dictionary must match dynamic property names on
            the target window's root container. The values for each key
            will be used to set those properties. Optional.

    Returns:
        A reference to the opened window.
    """
    print(path, params)
    return FPMIWindow("Opened Window")


def openWindowInstance(path, params=None):
    # type: (String, Optional[Dict[String, Any]]) -> FPMIWindow
    """Operates exactly like system.nav.openWindow, except that if the
    named window is already open, then an additional instance of the
    window will be opened.

    There is no limit to the number of additional instances of a window
    that you can open.

    Args:
        path: The path to the window to open.
        params: A dictionary of parameters to pass into the window. The
            keys in the dictionary must match dynamic property names on
            the target window's root container. The values for each key
            will be used to set those properties. Optional.

    Returns:
        A reference to the opened window.
    """
    print(path, params)
    return FPMIWindow("Window Instance")


def swapTo(path, params=None):
    # type: (String, Optional[Dict[String, Any]]) -> FPMIWindow
    """Performs a window swap from the current main screen window to the
    window specified.

    Swapping means that the opened window will take the place of the
    closing window - in this case it will be maximized.

    This function works like system.nav.swapWindow except that you
    cannot specify the source for the swap.

    Args:
        path: The path to the window to open.
        params: A dictionary of parameters to pass into the window. The
            keys in the dictionary must match dynamic property names on
            the target window's root container. The values for each key
            will be used to set those properties. Optional.

    Returns:
        A reference to the swapped-to window.
    """
    print(path, params)
    return FPMIWindow("Swapped To")


def swapWindow(
    arg,  # type: Union[String, EventObject]
    swapToPath,  # type: String
    params=None,  # type: Optional[Dict[String, Any]]
):
    # type: (...) -> FPMIWindow
    """Performs a window swap.

    This means that one window is closed, and another is opened and
    takes its place - assuming its size, floating state, and
    maximization state. This gives a seamless transition; one window
    seems to simply turn into another.

    This function works like system.nav.swapTo except that you can
    specify the source and destination for the swap.

    Args:
        arg: The path of the window to swap from. Must be a currently
            open window, otherwise this will act like an openWindow, or
            a component event (EventObject) whose enclosing window will
            be used as the "swap-from" window.
        swapToPath: The name of the window to swap to.
        params: A dictionary of parameters to pass into the window. The
            keys in the dictionary must match dynamic property names on
            the target window's root container. The values for each key
            will be used to set those properties. Optional.

    Returns:
        A reference to the swapped-to window.
    """
    print(arg, swapToPath, params)
    return FPMIWindow("Swapped To")
