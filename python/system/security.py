# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103

"""Security Functions
The following functions give you access to interact with the users and roles in the Gateway."""

__all__ = [
    'getRoles',
    'getUsername',
    'getUserRoles',
    'validateUser'
]


def getRoles():
    """Finds the roles that the currently logged in user has, returns them as a Python tuple of
    strings.

    Returns:
        tuple[str]: A list of the roles (strings) that are assigned to the current user.
    """
    return 'Administrator', 'Developer'


def getUsername():
    """Returns the currently logged-in username.

    Returns:
        str: The current username.
    """
    return 'johdoe'


def getUserRoles(username, password, authProfile='', timeout=60000):
    """Fetches the roles for a user from the Gateway. This may not be the currently logged in user.
    Requires the password for that user. If the authentication profile name is omitted, then the
    current project's default authentication profile is used.

    Args:
        username (str): The username to fetch roles for.
        password (str): The password for the user.
        authProfile (str): The name of the authentication profile to run against. Optional.
            Leaving this out will use the project's default profile.
        timeout (int): Timeout for client-to-gateway communication. Optional. (default: 60,000ms)

    Returns:
        tuple[str]: A list of the roles that this user has, if the user authenticates successfully.
            Otherwise, returns None.
    """
    print(username, password, authProfile, timeout)
    return 'Administrator', 'Developer'


def validateUser(username, password, authProfile='', timeout=60000):
    """Tests credentials (username and password) against an authentication profile. Returns a
    boolean based upon whether or not the authentication profile accepts the credentials. If the
    authentication profile name is omitted, then the current project's default authentication
    profile is used.

    Args:
        username (str): The username to validate.
        password (str): The password for the user.
        authProfile (str): The name of the authentication profile to run against. Optional.
            Leaving this out will use the project's default profile.
        timeout (int): Timeout for client-to-gateway communication. Optional. (default: 60,000ms)
    Returns:
        bool: false(0) if the user failed to authenticate, true(1) if the username/password was a
            valid combination.
    """
    print(username, password, authProfile, timeout)
    return True
