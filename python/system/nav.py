# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Navigation Functions
The following functions allow you to open and close windows in the
client."""

__all__ = [
    'centerWindow',
    'closeParentWindow',
    'closeWindow',
    'desktop',
    'getCurrentWindow',
    'goBack',
    'goForward',
    'goHome',
    'openWindow',
    'openWindowInstance',
    'swapTo',
    'swapWindow'
]

from . import EventObject, FPMIWindow, INavUtilities


def centerWindow(windowPath):
    """Given a window path, or a reference to a window itself, it will
    center the window. The window should be floating an non-maximized.
    If the window can't be found, this function will do nothing.

    Args:
        windowPath (str): The path of the window to center.

    Returns:
        FPMIWindow: A reference to the window to center.
    """
    print windowPath
    return FPMIWindow()


def closeParentWindow(event):
    """Closes the parent window given a component event object.

    Args:
        event (EventObject): A component event object. The enclosing
            window for the component will be closed.
    """
    print event


def closeWindow(arg):
    """Given a window path, or a reference to a window itself, it will
    close the window. If the window can't be found, this function will
    do nothing.

    Args:
        arg (object): A reference to the window to close as an
            FPMIWindow instance or the path of the window to close as
            a String.
    """
    print arg


def desktop(handle='primary'):
    """Allows for invoking system.nav functions on a specific desktop.

    Args:
        handle (str): The handle for the desktop to use. The screen
            index casted as a string may be used instead of the
            handle. If omitted, this will default to the Primary
            Desktop. Alternatively, the handle "primary" can be used
            to refer to the Primary Desktop.

    Returns:
        INavUtilities: A copy of system.nav that will alter the
            desktop named by the given handle.
    """
    print handle
    return INavUtilities()


def getCurrentWindow():
    """Returns the path of the current "main screen" window, which is
    defined as the maximized window. With the Typical Navigation
    Strategy, there is only ever one maximized window at a time.

    Eeturns:
        str: The path of the current "main screen" window - the
            maximized window.
    """
    return 'Path/To/Maximized Window'


def goBack():
    """When using the Typical Navigation Strategy, this function will
    navigate back to the previous main screen window.

    Returns:
        FPMIWindow: The window that was returned to.
    """
    return FPMIWindow()


def goForward():
    """When using the Typical Navigation Strategy, this function will
    navigate "forward" to the last main-screen window the user was on
    when they executed a system.nav.goBack().

    Returns:
        FPMIWindow: The window that was returned to.
    """
    return FPMIWindow()


def goHome():
    """When using the Typical Navigation Strategy, this function will
    navigate to the "home" window. This is automatically detected as
    the first main-screen window shown in a project.

    Returns:
        FPMIWindow: The window that was returned to.
    """
    return FPMIWindow()


def openWindow(path, params=None):
    """Opens the window with the given path. If the window is already
    open, brings it to the front. The optional params dictionary
    contains key:value pairs which will be used to set the target
    window's root container's dynamic variables.

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
    return FPMIWindow()


def openWindowInstance(path, params=None):
    """Operates exactly like system.nav.openWindow, except that if the
    named window is already open, then an additional instance of the
    window will be opened. There is no limit to the number of
    additional instances of a window that you can open.

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
    return FPMIWindow()


def swapTo(path, params=None):
    """Performs a window swap from the current main screen window to
    the window specified. Swapping means that the opened window will
    take the place of the closing window - in this case it will be
    maximized. See also: Navigation Strategies.

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
    return FPMIWindow()


def swapWindow(swapFromPath, swapToPath, params=None):
    """Performs a window swap. This means that one window is closed,
    and another is opened and takes its place - assuming its size,
    floating state, and maximization state. This gives a seamless
    transition - one window seems to simply turn into another.

    Args:
        swapFromPath (str): The path of the window to swap from. Must
            be a currently open window, or this will act like an
            openWindow.
        swapToPath (str): The name of the window to swap to.
        params (dict): A dictionary of parameters to pass into the
            window. The keys in the dictionary must match dynamic
            property names on the target window's root container. The
            values for each key will be used to set those properties.
            Optional.

    Returns:
        FPMIWindow: A reference to the swapped-to window.
    """
    print(swapFromPath, swapToPath, params)
    return FPMIWindow()
