"""Vision Functions.

The following function will allow you to update your Vision Client
project using scripting.
"""

from __future__ import print_function

__all__ = ["getKeyboardLayouts", "updateProject"]

from typing import List

from com.inductiveautomation.ignition.common.i18n.keyboard import KeyboardLayout


def getKeyboardLayouts():
    # type: () -> List[KeyboardLayout]
    """Returns the list of keyboard layouts available on this system.

    Returns:
        A list of KeyboardLayout objects.
    """
    return [
        KeyboardLayout(
            "eac73461-ce82-4583-952a-77c68ab20254", "en_us", "English", "EN", ["en"]
        ),
        KeyboardLayout(
            "ecb36fba-8037-494f-948b-ec5f9beeeb4a",
            "en_us_compat",
            "English (Compatibility)",
            "EN",
            ["en"],
        ),
    ]


def updateProject():
    # type: () -> None
    """Updates the Vision Client project with saved changes.

    This function is intended to be used in conjunction with the "None"
    option of Vision Project update modes in the Project Properties, and
    the Vision Client System Tag ProjectUpdateAvailable.
    """
    pass
