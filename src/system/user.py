"""User Functions.

The following functions give you access to view and edit users in the
Gateway.
"""

from __future__ import print_function, unicode_literals

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

from typing import List, Optional, Union

from com.inductiveautomation.ignition.client.util.gui.scheduling import ScheduleModel
from com.inductiveautomation.ignition.common.messages import UIResponse
from com.inductiveautomation.ignition.common.user import PyUser
from com.inductiveautomation.ignition.common.user.schedule import (
    AbstractScheduleModel,
    BasicScheduleModel,
    CompositeScheduleModel,
    HolidayModel,
    ScheduleAdjustment,
)
from java.util import Date, Locale


def addCompositeSchedule(
    name,  # type: Union[str, unicode]
    scheduleOne,  # type: Union[str, unicode]
    scheduleTwo,  # type: Union[str, unicode]
    description=None,  # type: Optional[Union[str, unicode]]
):
    # type: (...) -> UIResponse
    """Allows two schedules to be combined into a composite schedule.

    Args:
        name: The name of the new composite schedule.
        scheduleOne: The first schedule to combine.
        scheduleTwo: The second schedule to combine.
        description: Description of the new combined schedule. Optional.

    Returns:
        A UIResponse object with lists of warnings, errors, and info
        about the success or failure of the add.
    """
    print(name, scheduleOne, scheduleTwo, description)
    return UIResponse(Locale.ENGLISH)


def addHoliday(holiday):
    # type: (HolidayModel) -> UIResponse
    """Allows a holiday to be added.

    Args:
        holiday: The holiday to add.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the add.
    """
    print(holiday)
    return UIResponse(Locale.ENGLISH)


def addRole(userSource, role):
    # type: (Union[str, unicode], Union[str, unicode]) -> UIResponse
    """Allows a role to the specified user source.

    When altering the Gateway System User Source, the Allow User Admin
    setting must be enabled.

    Args:
        userSource: The user source to add a role to. Blank will use the
            default user source.
        role: The role to add. Role must not be blank and must not
            already exist.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the add.
    """
    print(userSource, role)
    return UIResponse(Locale.ENGLISH)


def addSchedule(
    schedule,  # type: Union[BasicScheduleModel, CompositeScheduleModel]
):
    # type: (...) -> UIResponse
    """Allows a schedule to be added.

    Args:
        schedule: The schedule to add. Can be a BasicScheduleModel or
            CompositeScheduleModel object (or any other class that
            extends AbstractScheduleModel).

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the add.
    """
    print(schedule)
    return UIResponse(Locale.ENGLISH)


def addUser(userSource, user):
    # type: (Union[str, unicode], PyUser) -> UIResponse
    """Adds a new user to a user source.

    Used in combination with getNewUser to create new user.

    Args:
        userSource: The user source to add a user to. If set to an empty
            string, the function will attempt to use the project's
            default user source (if called from a project).
        user: The user to add, as a User object. Refer also to the
            PyUser class.

    Returns:
        A UIResponse object with lists of warnings, errors, and info
        about the success or failure of the add attempt.
    """
    print(userSource, user)
    return UIResponse(Locale.ENGLISH)


def createScheduleAdjustment(
    startDate,  # type: Date
    endDate,  # type: Date
    isAvailable,  # type: bool
    note,  # type: Union[str, unicode]
):
    # type: (...) -> ScheduleAdjustment
    """Creates a schedule adjustment.

    Args:
        startDate: The starting date of the schedule adjustment.
        endDate: The ending date of the schedule adjustment.
        isAvailable: True if the user is available during this schedule
            adjustment.
        note: A note about the schedule adjustment.

    Returns:
        A ScheduleAdjustment object that can be added to a user.
    """
    print(startDate, endDate, isAvailable, note)
    return ScheduleAdjustment()


def editHoliday(holidayName, holiday):
    # type: (Union[str, unicode], HolidayModel) -> UIResponse
    """Allows a holiday to be edited.

    Args:
        holidayName: The name of the holiday to edit. Name is
            case-sensitive.
        holiday: The edited holiday.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the edit.
    """
    print(holidayName, holiday)
    return UIResponse(Locale.ENGLISH)


def editRole(
    userSource,  # type: Union[str, unicode]
    oldName,  # type: Union[str, unicode]
    newName,  # type: Union[str, unicode]
):
    # type: (...) -> UIResponse
    """Renames a role in the specified user source.

    When altering the Gateway System User Source, the Allow User Admin
    setting must be enabled.

    Args:
        userSource: The user source in which the role is found. Blank
            will use the default user source.
        oldName: The role to edit. Role must not be blank and must
            exist.
        newName: The new name for the role. Must not be blank.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the edit.
    """
    print(userSource, oldName, newName)
    return UIResponse(Locale.ENGLISH)


def editSchedule(
    scheduleName,  # type: Union[str, unicode]
    schedule,  # type: Union[BasicScheduleModel, CompositeScheduleModel]
):
    # type: (...) -> UIResponse
    """Allows a schedule to be edited.

    Args:
        scheduleName: The name of the schedule to edit. Name is
            case-sensitive.
        schedule: The schedule to add. Can be a BasicScheduleModel or
            CompositeScheduleModel object (or any other class that
            extends AbstractScheduleModel).

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the edit.
    """
    print(scheduleName, schedule)
    return UIResponse(Locale.ENGLISH)


def editUser(userSource, user):
    # type: (Union[str, unicode], PyUser) -> UIResponse
    """Alters a specific user in a user source, replacing the previous
    data with the new data passed in.

    Args:
        userSource: The user source in which the user is found. Blank
            will use the default user source.
        user: The user to update, as a User object. Refer also to the
            PyUser class.

    Returns:
        A UIResponse object with lists of warnings, errors, and
        information returned after the edit attempt.
    """
    print(userSource, user)
    return UIResponse(Locale.ENGLISH)


def getHoliday(holidayName):
    # type: (Union[str, unicode]) -> HolidayModel
    """Returns a specific holiday.

    Args:
        holidayName: The name of the holiday to return. Case-sensitive.

    Returns:
        The holiday, or None if not found.
    """
    print(holidayName)
    return HolidayModel(holidayName, Date(), True)


def getHolidayNames():
    # type: () -> List[Union[str, unicode]]
    """Returns a collection of Strings of all holiday names.

    Returns:
        A list of all holiday names, or an empty list if no holidays are
        defined.
    """
    return ["Cinco de mayo", "Labor Day", "Groundhog Day"]


def getHolidays():
    # type: () -> List[HolidayModel]
    """Returns a sequence of all of the holidays available.

    Returns:
        A list of holidays.
    """
    return [HolidayModel("Cinco de mayo", Date(), True)]


def getNewUser(userSource, username):
    # type: (Union[str, unicode], Union[str, unicode]) -> PyUser
    """Creates a new user object.

    The user will not be added to the user source until addUser is
    called.

    Args:
        userSource: The name of the user source in which to create a
            user.
        username: The username for the new user. Does not check if
            username already exists or is valid.

    Returns:
        The new user, as a User object. Refer also to the PyUser class.
    """
    print(userSource, username)
    return PyUser()


def getRoles(userSource):
    # type: (Union[str, unicode]) -> List[Union[str, unicode]]
    """Returns a sequence of strings representing all of the roles
    configured in a specific user source.

    Args:
        userSource: The user source to fetch the roles for.

    Returns:
        A List of Strings that holds all the roles in the user source.
    """
    print(userSource)
    return ["Administrator", "Designer", "Developer"]


def getSchedule(scheduleName):
    # type: (Union[str, unicode]) -> AbstractScheduleModel
    """Returns a specific schedule.

    Args:
        scheduleName: The name of the schedule to return.
            Case-sensitive.

    Returns:
         The schedule, which can be a BasicSchedule, CompositeSchedule,
         or another type registered by a module, or None if not found.
    """
    print(scheduleName)
    return AbstractScheduleModel()


def getScheduleNames():
    # type: () -> List[Union[str, unicode]]
    """Returns a sequence of strings representing the names of all of
    the schedules available.

    Returns:
        A List of Strings that holds the names of all the available
        schedules.
    """
    return ["A", "Always", "B", "C", "Example", "MyComposite", "MySchedule"]


def getScheduledUsers(
    userSource,  # type: Union[str, unicode]
    date=None,  # type: Optional[Union[Date, int]]
):
    # type: (...) -> List[PyUser]
    """Returns a list of users that are scheduled on.

    If no users are scheduled, it will return an empty list.

    Args:
        userSource: The name of the user source to check for scheduled
            users.
        date: The date to check schedules for. May be a Java Date or
            Unix Time in ms.. If omitted, the current date and time will
            be used. Optional.

    Returns:
        List of all Users scheduled for the given date, taking schedule
        adjustments into account.
    """
    print(userSource, date)
    return [PyUser()]


def getSchedules():
    # type: () -> List[ScheduleModel]
    """Returns a sequence of all available schedule models, which can
    be used to return configuration information on the schedule, such as
    time for each day of the week.

    Returns:
        A list of ScheduleModel objects. ScheduleModel objects can be a
        Basic Schedule, Composite Schedule (composed of exactly two
        other schedules), or another type registered by a module.
    """
    return [ScheduleModel()]


def getUser(userSource, username):
    # type: (Union[str, unicode], Union[str, unicode]) -> PyUser
    """Looks up a specific user in a user source, by username.

    The full User object is returned except for the user's password.

    Args:
        userSource: The name of the user source to search for the user
            in.
        username: The username of the user to search for.

    Returns:
        A User object.
    """
    print(userSource, username)
    return PyUser()


def getUsers(userSource):
    # type: (Union[str, unicode]) -> List[PyUser]
    """Retrieves the list of users in a specific user source.

    The User objects that are returned contain all of the information
    about that user, except for the user's password.

    Args:
        userSource: The name of the user source to find the users in.

    Returns:
        A list of User objects.
    """
    print(userSource)
    return [PyUser()]


def isUserScheduled(user, date=None):
    # type: (PyUser, Optional[Union[Date, int]]) -> bool
    """Will check if a specified User is scheduled currently or on a
    specified date/time.

    Args:
        user: The user object to check the schedule for.
        date: The date to check schedules for. May be a Java Date or
            Unix Time in ms. If omitted, the current date and time
            will be used. Optional.

    Returns:
        True if the user is scheduled for the specified date, False if
        not.
    """
    print(user, date)
    return True


def removeHoliday(holidayName):
    # type: (Union[str, unicode]) -> UIResponse
    """Allows a holiday to be deleted.

    Args:
        holidayName: The name of the holiday to delete. Name is
            case-sensitive.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the deletion.
    """
    print(holidayName)
    return UIResponse(Locale.ENGLISH)


def removeRole(userSource, role):
    # type: (Union[str, unicode], Union[str, unicode]) -> UIResponse
    """Removes a role from the specified user source.

    When altering the Gateway System User Source, the Allow User Admin
    setting must be enabled.

    Args:
        userSource: The user source in which the role is found. Blank
            will use the default user source.
        role: The role to remove. The role must exist.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the deletion.
    """
    print(userSource, role)
    return UIResponse(Locale.ENGLISH)


def removeSchedule(scheduleName):
    # type: (Union[str, unicode]) -> UIResponse
    """Allows a schedule to be deleted.

    Note that schedules which are used in Composite Schedules can not be
    deleted until they are removed from the Composite Schedule.

    Args:
        scheduleName: The name of the schedule to delete. Name is
            case-sensitive.

    Returns:
        An object with lists of warnings, errors, and info about the
        success or failure of the deletion.
    """
    print(scheduleName)
    return UIResponse(Locale.ENGLISH)


def removeUser(userSource, username):
    # type: (Union[str, unicode], Union[str, unicode]) -> UIResponse
    """Removes a specific user from the a user source based on username.

    When altering the Gateway System User Source, the Allow User Admin
    setting must be enabled.

    Args:
        userSource: The user source in which the user is found. Blank
            will use the default user source.
        username: The username of the user to remove.

    Returns:
        An UIResponse object with lists of warnings, errors, and
        information returned after the removal attempt.
    """
    print(userSource, username)
    return UIResponse(Locale.ENGLISH)
