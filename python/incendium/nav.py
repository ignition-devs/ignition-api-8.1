# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium Navigation module."""

__all__ = [
    'swap_windows'
]

import system.nav
from incendium import (constants, gui)


def swap_windows(from_path, to_path, input_windows, params=None):
    """Performs a window swap after asking the user to save their changes on all input windows.

    Args:
        from_path (str): The path of the window to swap from. Must be a currently open window, or
            this will act like an openWindow.
        to_path (str): The name of the window to swap to.
        input_windows (list[str]):  A list of paths that includes all input windows.
        params (dict): A dictionary of parameters to pass into the window. The keys in the
            dictionary must match dynamic property names on the target window's root container.
            The values for each key will be used to set those properties. Optional.
    """
    if to_path != from_path:
        if from_path in input_windows:
            if gui.confirm(constants.PROCEED_WITHOUT_SAVING_CHANGES, constants.CONFIRM):
                system.nav.swapWindow(from_path, to_path, params)
        else:
            system.nav.swapWindow(from_path, to_path, params)
