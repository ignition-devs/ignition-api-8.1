# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103

"""Navigation Functions
The following functions allow you to open and close windows in the client."""

__all__ = [
    'swapWindow'
]


def swapWindow(swapFromPath, swapToPath, params=None):
    """Performs a window swap. This means that one window is closed, and another is opened and
    takes its place - assuming its size, floating state, and maximization state. This gives a
    seamless transition - one window seems to simply turn into another.

    Args:
        swapFromPath (str): The path of the window to swap from. Must be a currently open window,
            or this will act like an openWindow.
        swapToPath (str): The name of the window to swap to.
        params (dict): A dictionary of parameters to pass into the window. The keys in the
            dictionary must match dynamic property names on the target window's root container.
            The values for each key will be used to set those properties. Optional.

    Returns:
        object: A reference to the swapped-to window.
    """
    print(swapFromPath, swapToPath, params)
