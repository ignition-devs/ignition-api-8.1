# Copyright (C) 2018-2021
# Author: Cesar Roman
# Contact: cesar@thecesrom.dev

"""User Functions.

The following functions give you access to view and edit users in the
Gateway.
"""

from __future__ import print_function

__all__ = [
    "PyUser",
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

from abc import ABCMeta, abstractmethod

import system.date
from java.lang import Object
from java.util import Date, Locale


class ContactInfo(Object):
    def __init__(self, contactType=None, value=None):
        self.contactType = contactType
        self.value = value

    def getContactType(self):
        pass

    def getValue(self):
        pass

    def setContactType(self, contactType):
        pass

    def setValue(self, value):
        pass


class HolidayModel(Object):
    """HolidayModel object."""

    def __init__(self, name, date, repeatAnnually):
        """Constructs a new HolidayModel.

        Args:
            name (str): The name.
            date (Date): The date.
            repeatAnnually (bool): Repeat annually.
        """
        self.name = name
        self.date = date
        self.repeatAnnually = repeatAnnually

    def getDate(self):
        return self.date

    def getName(self):
        return self.name

    def isRepeatedAnnually(self):
        return self.repeatAnnually


class ScheduleAdjustment(Object):
    def contains(self, timestamp):
        pass

    def getEnd(self):
        pass

    def getNote(self):
        pass

    def getStart(self):
        pass

    def isAvailable(self):
        pass

    def setAvailable(self, available):
        pass

    def setEnd(self, end):
        pass

    def setNoe(self, note):
        pass

    def setStart(self, start):
        pass


class ScheduleModel(Object):
    def deselectDayOfWeek(self, day):
        pass

    def getEveryHour(self):
        pass

    def getHour(self):
        pass

    def getMinute(self):
        pass

    def getSelectedDays(self):
        pass

    def isAlldays(self):
        pass

    def isDaySelected(self, day):
        pass

    def isEveryHourEnabled(self):
        pass

    def isEveryMinuteEnabled(self):
        pass

    def isHourEnabled(self):
        pass

    def isMinuteEnabled(self):
        pass

    def selectDayOfWeek(self, day):
        pass

    def setAllDays(self, allDays):
        pass

    def setEveryHour(self, everyHour):
        pass

    def setHour(self, hour):
        pass

    def setHourEnabled(self, hourEnabled):
        pass

    def setMinute(self, minute):
        pass

    def setMinuteEnabled(self, minuteEnabled):
        pass

    def setSelectedDays(self, selectedDays):
        pass

    def toCronString(self):
        pass


class UIResponse(Object):
    def __init__(self, locale):
        self.locale = locale

    def attempt(self, method):
        pass

    def error(self, message, args):
        pass

    def getErrors(self):
        pass

    def getInfos(self):
        pass

    def getLocale(self):
        pass

    def getWarns(self):
        pass

    def info(self, message, args):
        pass

    def warn(self, message, args):
        pass

    def wrap(self, locale, fx):
        pass


class User(ABCMeta):
    """User Interface."""

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def getContactInfo(cls):
        pass

    @abstractmethod
    def getId(cls):
        pass

    @abstractmethod
    def getPath(cls):
        pass

    @abstractmethod
    def getProfileName(cls):
        pass

    @abstractmethod
    def getRoles(cls):
        pass

    @abstractmethod
    def getScheduleAdjustments(cls):
        pass


class PyUser(User):
    """A User implementation that delegates to another user object, but
    has some methods that are more scripting friendly.
    """

    Badge = "badge"
    DEFAULT_SCHEDULE_NAME = "Always"
    FirstName = "John"
    Language = "en_US"
    LastName = "Doe"
    Notes = "These are some notes."
    Password = "password"
    Schedule = "Always"
    Username = "johdoe"
    USERNAME_PATTERN = r"[\p{Alnum}][ @\w.\s\-]{1, 49}"

    def addContactInfo(cls, *args):
        """Convenience method for scripting to add a new contactInfo
        easily.

        Usage:
            1. addContactInfo(contactType: str, value: str)
            2. addContactInfo(dict: contactDictionary)

        Args:
            args: Variable length argument list.
        """
        print(cls, args)

    def addRole(cls, role):
        """Convenience method for scripting to add a new role easily.

        Only works if user type supports roles.

        Args:
            role (str): A new role to add. If empty or null, no
                effect.
        """
        print(cls, role)

    def addRoles(cls, roles):
        """Adds the provided roles to this user."""
        print(cls, roles)

    def addScheduleAdjustment(cls, start, end, available=True, note=None):
        """Convenience method for scripting to add a new schedule
        adjustment easily.

        Args:
            start (Date): Date to start the schedule adjustment. Not
                null.
            end (Date): Date to end start the schedule adjustment.
                Not null.
            available (bool): True if the employee is available during
                this period. Optional.
            note (str): May be null or empty. Optional.
        """
        print(cls, start, end, available, note)

    def addScheduleAdjustments(cls, scheduleAdjustments):
        """Add Schedule Adjustments.

        Args:
            scheduleAdjustments (ScheduleAdjustment): ScheduleAdjustment
                object.
        """
        print(cls, scheduleAdjustments)

    def contains(cls, prop):
        """Returns if this users contains a given property."""
        print(cls, prop)
        return True

    def get(cls, propertyName):
        """Returns a the value of the requested item.

        Args:
            propertyName (str): The user property to retrieve.

        Returns:
            str: The value of the requested property.
        """
        print(cls)
        return propertyName

    def getContactInfo(cls):
        """Returns a sequence of ContactInfo objects.

        Each of these objects will have a contactType and value property
        representing the contact information, both strings.

        Returns:
            list[ContactInfo]: A sequence of ContactInfo objects.
        """
        print(cls)
        ci_email = ContactInfo("email", "johdoe@mycompany.com")
        ci_phone = ContactInfo("phone", "+1 5551324567")
        ci_sms = ContactInfo("sms", "+1 5557654321")
        return [ci_email, ci_phone, ci_sms]

    def getCount(cls):
        """Get count."""
        print(cls)
        return 1

    def getId(cls):
        """An opaque identifier that can be used to identify this
        user.
        """
        pass

    def getOrDefault(cls, prop):
        """Returns a default value if the requested item is not
        present.

        Args:
            prop (Property): The user property to retrieve.

        Returns:
            object: The value of the requested property.
        """
        print(cls, prop)

    def getOrElse(cls, property, value):
        """Get the value for a given Property, or else fall back to
        value if it's not present.
        """
        pass

    def getPath(cls):
        """Generate an path that unambiguously references this user."""
        pass

    def getProfileName(cls):
        """The name of the user management profile this user was
        retrieved from.
        """
        pass

    def getProperties(cls):
        """Returns all properties for this user."""
        pass

    def getRoles(cls):
        """Returns all of the roles this user is a has."""
        return ["Administrator", "Developer"]

    def getScheduleAdjustments(cls):
        """Returns all of this user's upcoming schedule adjustments."""
        pass

    def getValues(cls):
        """Returns the opaque PropertyValue objects."""
        pass

    def isExtended(cls, prop):
        """Returns whether this property set contains a value for the
        prop, and the prop was actually inherited.
        """
        pass

    def isInherited(cls, prop):
        """Indicates whether the property was inherited from a parent
        type.
        """
        pass

    def iterator(cls):
        """Property iterator."""
        pass

    def merge(cls, other, localOnly):
        """Merges the values from other collection into this one."""
        pass

    def remove(cls, prop):
        """Remove a property for this user."""
        pass

    def removeContactInfo(cls, contactType, value):
        """Remove contact information for this user."""
        pass

    def removeRole(cls, role):
        """Remove a role for this user."""
        pass

    def removeScheduleAdjustment(cls, start, end, available=True, note=None):
        """Remove schedule adjustment for this user."""
        pass

    def set(cls, *args):
        """Set a property for this user."""
        pass

    def setContactInfo(cls, contactInfo):
        """Set contact information for this user."""
        pass

    def setRoles(cls, roles):
        """Set roles for this user."""
        pass

    def setScheduleAdjustments(cls, scheduleAdjustments):
        """Set schedule adjustments for this user."""
        pass


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
