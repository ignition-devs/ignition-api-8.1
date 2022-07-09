"""Security Functions.

The following functions give you access to interact with the users and
roles in the Gateway. These functions require the Vision module, as
these functions can only be used with User Sources and their interaction
with Vision Clients.
"""

from __future__ import print_function

__all__ = [
    "getRoles",
    "getUserRoles",
    "getUsername",
    "isScreenLocked",
    "lockScreen",
    "logout",
    "switchUser",
    "unlockScreen",
    "validateUser",
]

import getpass

from typing import Optional, Tuple

from java.lang import String
from java.util import EventObject


def getRoles():
    # type: () -> Tuple[String, ...]
    """Finds the roles that the currently logged in user has, returns
    them as a Python tuple of strings.

    Returns:
        A list of the roles (strings) that are assigned to the current
        user.
    """
    return "Administrator", "Developer"


def getUserRoles(
    username,  # type: String
    password,  # type: String
    authProfile="",  # type: String
    timeout=60000,  # type: int
):
    # type: (...) -> Optional[Tuple[String, ...]]
    """Fetches the roles for a user from the Gateway.

    This may not be the currently logged in user. Requires the password
    for that user. If the authentication profile name is omitted, then
    the current project's default authentication profile is used.

    Args:
        username: The username to fetch roles for.
        password: The password for the user.
        authProfile: The name of the authentication profile to run
            against. Leaving this out will use the project's default
            profile. Optional.
        timeout: Timeout for Client-to-Gateway communication. Default is
            60,000ms. Optional.


    Returns:
        A list of the roles that this user has, if the user
        authenticates successfully. Otherwise, returns None.
    """
    print(username, password, authProfile, timeout)
    return "Administrator", "Developer"


def getUsername():
    # type: () -> String
    """Returns the currently logged-in username.

    Returns:
        The current username.
    """
    return getpass.getuser()


def isScreenLocked():
    # type: () -> bool
    """Returns whether or not the screen is currently locked.

    Returns:
        A flag indication whether or not the screen is currently locked.
    """
    return False


def lockScreen(obscure=False):
    # type: (Optional[bool]) -> None
    """Used to put a running Client in lock-screen mode.

    The screen can be unlocked by the user with the proper credentials,
    or by scripting via the system.security.unlockScreen() function.

    Args:
        obscure: If True, the locked screen will be opaque, otherwise
            it will be partially visible. Optional.
    """
    print(obscure)


def logout():
    # type: () -> None
    """Logs out of the Client for the current user and brings the Client
    to the login screen.
    """
    pass


def switchUser(username, password, event, hideError=False):
    # type: (String, String, EventObject, Optional[bool]) -> bool
    """Attempts to switch the current user on the fly.

    If the given username and password fail, this function will return
    False. If it succeeds, then all currently opened windows are closed,
    the user is switched, and windows are then re-opened in the states
    that they were in.

    If an event object is passed to this function, the parent window of
    the event object will not be re-opened after a successful user
    switch. This is to support the common case of having a switch-user
    screen that you want to disappear after the switch takes place.

    Args:
        username: The username to try and switch to.
        password: The password to authenticate with.
        event: If specified, the enclosing window for this event's
            component will be closed in the switch user process.
        hideError: If True, no error will be shown if the switch
            user function fails. Default is False. Optional.

    Returns:
        False if the switch user operation failed, True
        otherwise.
    """
    print(username, password, event, hideError)
    return True


def unlockScreen():
    # type: () -> None
    """Unlocks the Client, if it is currently in lock-screen mode."""
    pass


def validateUser(username, password, authProfile="", timeout=60000):
    # type: (String, String, Optional[String], Optional[int]) -> bool
    """Tests credentials (username and password) against an
    authentication profile.

    Returns a boolean based upon whether or not the authentication
    profile accepts the credentials. If the authentication profile name
    is omitted, then the current project's default authentication
    profile is used.

    Args:
        username: The username to validate.
        password: The password for the user.
        authProfile: The name of the authentication profile to run
            against. Leaving this out will use the project's default
            profile. Optional.
        timeout: Timeout for Client-to-Gateway communication. Default is
            60,000ms. Optional.

    Returns:
        False if the user failed to authenticate, True if the
        username/password was a valid combination.
    """
    print(username, password, authProfile, timeout)
    return True
