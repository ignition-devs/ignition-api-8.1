"""User Functions.

The following functions give you access to view and edit users in the
Gateway.
"""

from __future__ import print_function

__all__ = [
    "addCompositeSchedule",
    "addHoliday",
    "addRole",
    "addSchedule",
    "addUser",
    "createScheduleAdjustment",
    "editHoliday",
    "editRole",
    "editSchedule",
    "editUser",
    "getHoliday",
    "getHolidayNames",
    "getHolidays",
    "getNewUser",
    "getRoles",
    "getSchedule",
    "getScheduleNames",
    "getScheduledUsers",
    "getSchedules",
    "getUser",
    "getUsers",
    "isUserScheduled",
    "removeHoliday",
    "removeRole",
    "removeSchedule",
    "removeUser",
]

import system.date
from com.inductiveautomation.ignition.client.util.gui.scheduling import (
    ScheduleModel,
)
from com.inductiveautomation.ignition.common.messages import UIResponse
from com.inductiveautomation.ignition.common.user import PyUser
from com.inductiveautomation.ignition.common.user.schedule import HolidayModel
from java.util import Date, Locale


def addCompositeSchedule(name, scheduleOne, scheduleTwo, description=None):
    """Allows two schedules to be combined into a composite schedule.

    Args:
        name (str): The name of the new composite schedule.
        scheduleOne (str): The first schedule to combine.
        scheduleTwo (str): The second schedule to combine.
        description (str): Description of the new combined schedule.
            Optional.

    Returns:
        UIResponse: A UIResponse object with lists of warnings, errors,
            and info about the success or failure of the add.
    """
    print(name, scheduleOne, scheduleTwo, description)
    return UIResponse(Locale.ENGLISH)


def addHoliday(holiday):
    """Allows a holiday to be added.

    Args:
        holiday (HolidayModel): The holiday to add, as a HolidayModel
            object.

    Returns:
        UIResponse: A UIResponse object with lists of warnings, errors,
            and info about the success or failure of the add.
    """
    print(holiday)
    return UIResponse(Locale.ENGLISH)


def addRole(userSource, role):
    """Allows a role to the specified user source.

    When altering the Gateway System User Source, the Allow User Admin
    setting must be enabled.

    Args:
        userSource (str): The user source to add a role to. Blank will
            use the default user source.
        role (str): The role to add. Role must not be blank and must not
            already exist.

    Returns:
        UIResponse: A UIResponse object with lists of warnings, errors,
            and info about the success or failure of the add.
    """
    print(userSource, role)
    return UIResponse(Locale.ENGLISH)


def addSchedule(schedule):
    """Allows a schedule to be added.

    Args:
        schedule (ScheduleModel): The schedule to add. Can be a
            BasicScheduleModel or CompositeScheduleModel object (or any
            other class that extends AbstractScheduleModel).

    Returns:
        UIResponse: A UIResponse object with lists of warnings, errors,
            and info about the success or failure of the add.
    """
    print(schedule)
    return UIResponse(Locale.ENGLISH)


def addUser(userSource, user):
    """Adds a new user to a user source.

    Used in combination with getNewUser to create new user.

    Args:
        userSource (str):
        user (PyUser): The user to add, as a User object. Refer also to
            the PyUser class.

    Returns:
        UIResponse: A UIResponse object with lists of warnings, errors,
            and info about the success or failure of the add attempt.
    """
    print(userSource, user)
    return UIResponse(Locale.ENGLISH)


def createScheduleAdjustment(startDate, endDate, isAvailable, note):
    """Creates a schedule adjustment.

    Args:
        startDate (Date): The starting date of the schedule
            adjustment.
        endDate (Date): The ending date of the schedule adjustment.
        isAvailable (bool): True if the user is available during this
            schedule adjustment.
        note (str): A note about the schedule adjustment.

    Returns:
        ScheduleAdjustment: A ScheduleAdjustment object that can be
            added to a user.
    """
    print(startDate, endDate, isAvailable, note)


def editHoliday(holidayName, holiday):
    """Allows a holiday to be edited.

    Args:
        holidayName (str): The name of the holiday to edit. Name is
            case-sensitive.
        holiday (HolidayModel): The edited holiday, as a HolidayModel
            object.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the edit.
    """
    print(holidayName, holiday)
    return UIResponse(Locale.ENGLISH)


def editRole(userSource, oldName, newName):
    """Renames a role in the specified user source.

    When altering the Gateway System User Source, the Allow User Admin
    setting must be enabled.

    Args:
        userSource (str): The user source in which the role is found.
            Blank will use the default user source.
        oldName (str): The role to edit. Role must not be blank and must
            exist.
        newName (str): The new name for the role. Must not be blank.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the edit.
    """
    print(userSource, oldName, newName)
    return UIResponse(Locale.ENGLISH)


def editSchedule(scheduleName, schedule):
    """Allows a schedule to be edited.

    Args:
        scheduleName (str): The name of the schedule to edit. Name is
            case-sensitive.
        schedule (ScheduleModel): The schedule to add. Can be a
            BasicScheduleModel or CompositeScheduleModel object (or any
            other class that extends AbstractScheduleModel).

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the edit.
    """
    print(scheduleName, schedule)
    return UIResponse(Locale.ENGLISH)


def editUser(userSource, user):
    """Alters a specific user in a user source, replacing the previous
    data with the new data passed in.

    Args:
        userSource (str): The user source in which the user is found.
            Blank will use the default user source.
        user (PyUser): The user to update, as a User object. Refer also
            to the PyUser class.

    Returns:
        UIResponse: A UIResponse object with lists of warnings, errors,
            and information returned after the edit attempt.
    """
    print(userSource, user)
    return UIResponse(Locale.ENGLISH)


def getHoliday(holidayName):
    """Returns a specific holiday.

    Args:
        holidayName (str): The name of the holiday to return.
            Case-sensitive.

    Returns:
        HolidayModel: The holiday, as a HolidayModel object, or None if
            not found.
    """
    print(holidayName)


def getHolidayNames():
    """Returns a collection of Strings of all holiday names.

    Returns:
        list[str]: A list of all holiday names, or an empty list if no
            holidays are defined.
    """
    return ["Labor Day", "Groundhog Day"]


def getHolidays():
    """Returns a sequence of all of the holidays available.

    Returns:
        list[HolidayModel]: A list of holidays, as HolidayModel objects.
    """
    return []


def getNewUser(userSource, username):
    """Creates a new user object.

    The user will not be added to the user source until addUser is
    called.

    Args:
        userSource (str): The name of the user source in which to create
            a user.
        username (str): The username for the new user. Does not check if
            username already exists or is valid.

    Returns:
        PyUser: The new user, as a User object. Refer also to the PyUser
            class.
    """
    print(userSource, username)
    return PyUser()


def getRoles(userSource):
    """Returns a sequence of strings representing all of the roles
    configured in a specific user source.

    Args:
        userSource (str): The user source to fetch the roles for.

    Returns:
        list[str]: A List of Strings that holds all the roles in the
            user source.
    """
    print(userSource)


def getSchedule(scheduleName):
    """Returns a specific schedule.

    Args:
        scheduleName (str): The name of the schedule to return.
            Case-sensitive.

    Returns:
         ScheduleModel: The schedule, which can be a BasicScheduleModel
            object, CompositeScheduleModel object, or another type
            registered by a module. If a schedule was not found, the
            function will return None if called from a Vision Client or
            the Designer. if called in from a Perspective Session or
            anywhere else in the Gateway scope, will throw an
            IllegalArgumentException.
    """
    print(scheduleName)


def getScheduleNames():
    """Returns a sequence of strings representing the names of all of
    the schedules available.

    Returns:
        list[str]: A List of Strings that holds the names of all the
            available schedules.
    """
    return ["A", "Always", "B", "C", "Example", "MyComposite", "MySchedule"]


def getScheduledUsers(userSource, date=None):
    """Returns a list of users that are scheduled on.

    If no users are scheduled, it will return an empty list.

    Args:
        userSource (str): The name of the user source to check for
            scheduled users.
        date (object): The date to check schedules for. May be a Java
            Date or Unix Time in ms.. If omitted, the current date and
            time will be used. Optional.

    Returns:
        list[PyUser]: List of all Users scheduled for the given date,
            taking schedule adjustments into account. Refer also to the
            PyUser class.
    """
    date = system.date.now() if date is None else date
    print(userSource, date)


def getSchedules():
    """Returns a sequence of all available schedule models, which can be
    used to return configuration information on the schedule, such as
    time for each day of the week.

    Returns:
        list[ScheduleModel]: A list of schedules. Each schedule can be a
            BasicScheduleModel object, CompositeScheduleModel object, or
            another type registered by a module.
    """
    return [ScheduleModel()]


def getUser(userSource, username):
    """Looks up a specific user in a user source, by username.

    The full User object is returned except for the user's password.

    Args:
        userSource (str): The name of the user source to search for the
            user in. Can be a blank string to use the Vision Client's
            default user source.
        username (str): The username of the user to search for.

    Returns:
        PyUser: The user, as a User object. Refer also to the PyUser
            class.
    """
    print(userSource, username)
    return PyUser()


def getUsers(userSource):
    """Retrieves the list of users in a specific user source.

    The User objects that are returned contain all of the information
    about that user, except for the user's password.

    Args:
        userSource (str): The name of the user source to find the users
            in.

    Returns:
        list[PyUser]: A list of User objects. Refer also to the PyUser
            class.
    """
    print(userSource)
    # You may return more than one User object.
    return [PyUser()]


def isUserScheduled(user, date=None):
    """Will check if a specified User is scheduled currently or on a
    specified date/time.

    Args:
        user (PyUser): The user object to check the schedule for.
        date (object): The date to check schedules for. May be a Java
            Date or Unix Time in ms. If omitted, the current date and
            time will be used. Optional.

    Returns:
        bool: True if the user is scheduled for the specified date,
            False if not.
    """
    date = system.date.now() if date is None else date
    print(user, date)
    return True


def removeHoliday(holidayName):
    """Allows a holiday to be deleted.

    Args:
        holidayName (str): The name of the holiday to delete. Name is
            case-sensitive.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the deletion.
    """
    print(holidayName)
    return UIResponse(Locale.ENGLISH)


def removeRole(userSource, role):
    """Removes a role from the specified user source.

    When altering the Gateway System User Source, the Allow User Admin
    setting must be enabled.

    Args:
        userSource (str): The user source in which the role is found.
            Blank will use the default user source.
        role (str): The role to remove. The role must exist.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the deletion.
    """
    print(userSource, role)
    return UIResponse(Locale.ENGLISH)


def removeSchedule(scheduleName):
    """Allows a schedule to be deleted.

    Note that schedules which are used in Composite Schedules can not be
    deleted until they are removed from the Composite Schedule.

    Args:
        scheduleName (str): The name of the schedule to delete. Name is
            case-sensitive.

    Returns:
        UIResponse: An object with lists of warnings, errors, and info
            about the success or failure of the deletion.
    """
    print(scheduleName)
    return UIResponse(Locale.ENGLISH)


def removeUser(userSource, username):
    """Removes a specific user from the a user source based on username.

    When altering the Gateway System User Source, the Allow User Admin
    setting must be enabled.

    Args:
        userSource (str): The user source in which the user is found.
            Blank will use the default user source.
        username (str): The username of the user to remove.

    Returns:
        UIResponse: An UIResponse object with lists of warnings, errors,
            and information returned after the removal attempt.
    """
    print(userSource, username)
