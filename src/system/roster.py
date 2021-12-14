"""Roster Functions.

Functions that provide roster manipulation, including adding and remove
users from a roster.
"""

from __future__ import print_function

__all__ = ["addUsers", "createRoster", "deleteRoster", "getRosters", "removeUsers"]

from typing import Dict, List

from com.inductiveautomation.ignition.common.user import PyUser
from java.lang import String


def addUsers(rosterName, users):
    # type: (String, List[PyUser]) -> None
    """Adds a list of users to an existing roster.

    Users are always appended to the end of the roster.

    Args:
        rosterName: The name of the roster to modify.
        users: A list of User objects that will be added to the end of
            the roster. User objects can be created with the
            system.user.getUser and system.user.addUser functions. These
            users must exist before being added to the roster.
    """
    print(rosterName)
    for user in users:
        print(user.Username)


def createRoster(name, description):
    # type: (String, String) -> None
    """Creates a roster with the given name and description, if it does
    not already exist.

    This function was designed to run in the Gateway and in Perspective
    sessions. If creating rosters from Vision clients, use
    system.alarm.createRoster instead.

    Args:
        name: The name of the roster to create.
        description: The description for the roster. May be None, but
            the parameter is mandatory.
    """
    print(name, description)


def deleteRoster(rosterName):
    # type: (String) -> None
    """Deletes a roster with the given name.

    Args:
        rosterName: The name of the roster to delete.
    """
    print(rosterName)


def getRosters():
    # type: () -> Dict[String, List[String]]
    """Returns a dictionary of rosters, where the key is the name of the
    roster, and the value is an array list of string user names.

    This function was designed to run in the Gateway and in Perspective
    sessions. If creating rosters from Vision clients, use
    system.alarm.getRosters instead.

    Returns:
        A dictionary that maps roster names to a list of usernames in
        the roster. The list of usernames may be empty if no users have
        been added to the roster.
    """
    return {}


def removeUsers(rosterName, users):
    # type: (String, List[PyUser]) -> None
    """Removes one or more users from an existing roster.

    Args:
        rosterName: The name of the roster to modify.
        users: A list of user objects that will be added to the end of
            the roster. User objects can be created with the
            system.user.getUser and system.user.addUser functions.
    """
    print(rosterName)
    for user in users:
        print(user.Username)
