"""Security Functions.

The following functions give you access to interact with the users and
roles in the Gateway.
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


def getRoles():
    """Finds the roles that the currently logged in user has, returns
    them as a Python tuple of strings.

    Returns:
        tuple[str]: A list of the roles (strings) that are assigned to
            the current user.
    """
    return "Administrator", "Developer"


def getUserRoles(username, password, authProfile="", timeout=60000):
    """Fetches the roles for a user from the Gateway.

    This may not be the currently logged in user. Requires the password
    for that user. If the authentication profile name is omitted, then
    the current project's default authentication profile is used.

    Args:
        username (str): The username to fetch roles for.
        password (str): The password for the user.
        authProfile (str): The name of the authentication profile to run
            against. Optional. Leaving this out will use the project's
            default profile.
        timeout (int): Timeout for client-to-gateway communication.
            Optional. (default: 60,000ms)

    Returns:
        tuple[str]: A list of the roles that this user has, if the user
            authenticates successfully. Otherwise, returns None.
    """
    print(username, password, authProfile, timeout)
    return "Administrator", "Developer"


def getUsername():
    """Returns the currently logged-in username.

    Returns:
        str: The current username.
    """
    return getpass.getuser()


def isScreenLocked():
    """Returns whether or not the screen is currently locked.

    Returns:
        bool: A flag indication whether or not the screen is currently
            locked.
    """
    return False


def lockScreen(obscure=False):
    """Used to put a running client in lock-screen mode.

    The screen can be unlocked by the user with the proper credentials,
    or by scripting via the system.security.unlockScreen() function.

    Args:
        obscure (bool): If True(1), the locked screen will be opaque,
            otherwise it will be partially visible. Optional.
    """
    print(obscure)


def logout():
    """Logs out of the client for the current user and brings the client
    to the login screen.
    """
    pass


def switchUser(username, password, event, hideError=False):
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
        username (str): The username to try and switch to.
        password (str): The password to authenticate with.
        event (object): If specified, the enclosing window for this
            event's component will be closed in the switch user process.
        hideError (bool): If True (1), no error will be shown if the
            switch user function fails. (default: 0)

    Returns:
        bool: False(0) if the switch user operation failed, True (1)
            otherwise.
    """
    print(username, password, event, hideError)
    return True


def unlockScreen():
    """Unlocks the client, if it is currently in lock-screen mode."""
    pass


def validateUser(username, password, authProfile="", timeout=60000):
    """Tests credentials (username and password) against an
    authentication profile.

    Returns a boolean based upon whether or not the authentication
    profile accepts the credentials. If the authentication profile name
    is omitted, then the current project's default authentication
    profile is used.

    Args:
        username (str): The username to validate.
        password (str): The password for the user.
        authProfile (str): The name of the authentication profile to run
            against. Optional. Leaving this out will use the project's
            default profile.
        timeout (int): Timeout for client-to-gateway communication.
            Optional. (default: 60,000ms)

    Returns:
        bool: False(0) if the user failed to authenticate, True(1) if
            the username/password was a valid combination.
    """
    print(username, password, authProfile, timeout)
    return True
