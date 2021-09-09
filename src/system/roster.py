"""Roster Functions.

Functions that provide roster manipulation, including adding and remove
users from a roster.
"""

from __future__ import print_function

__all__ = [
    "addUsers",
    "createRoster",
    "deleteRoster",
    "getRosters",
    "removeUsers",
]

from system.user import PyUser


def addUsers(rosterName, users):
    """Adds a list of users to an existing roster.

    Users are always appended to the end of the roster.

    Args:
        rosterName (str): The name of the roster to modify.
        users (list[PyUser]): A list of User objects that will be added
            to the end of the roster. User objects can be created with
            the system.user.getUser and system.user.addUser functions.
            These users must exist before being added to the roster.
    """
    print(rosterName)
    for user in users:
        print(user.Username)


def createRoster(name, description):
    """Creates a roster with the given name and description, if it does
    not already exist.

    This function was designed to run in the Gateway and in Perspective
    sessions. If creating rosters from Vision clients, use
    system.alarm.createRoster instead.

    Args:
        name (str): The name of the roster to create.
        description (str): The description for the roster. May be None,
            but the parameter is mandatory.
    """
    print(name, description)


def deleteRoster(rosterName):
    """Deletes a roster with the given name.

    Args:
        rosterName (str): The name of the roster to delete.
    """
    print(rosterName)


def getRosters():
    """Returns a dictionary of rosters, where the key is the name of the
    roster, and the value is an array list of string user names.

    This function was designed to run in the Gateway and in Perspective
    sessions. If creating rosters from Vision clients, use
    system.alarm.getRosters instead.

    Returns:
        dict: A python dictionary of rosters. Refer to the list of User
            objects.
    """
    return {}


def removeUsers(rosterName, users):
    """Removes one or more users from an existing roster.

    Args:
        rosterName (str): The name of the roster to modify.
        users (list[PyUser]): A list of user objects that will be added
            to the end of the roster. User objects can be created with
            the system.user.getUser and system.user.addUser functions.
    """
    print(rosterName)
    for user in users:
        print(user.Username)
