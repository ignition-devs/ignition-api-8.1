from __future__ import print_function

__all__ = ["BasicUser", "ContactInfo", "PyUser", "User", "UserSourceMeta"]

from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common import QualifiedPath
from com.inductiveautomation.ignition.common.user.schedule import ScheduleAdjustment
from java.lang import Object

String = Union[str, unicode]


class ContactInfo(Object):
    contactType = ""  # type: String
    value = ""  # type: String

    def __init__(self, *args):
        # type: (Any) -> None
        if len(args) == 2:
            self.contactType = args[0]
            self.value = args[1]

    def getContactType(self):
        # type: () -> String
        return self.contactType

    def getValue(self):
        # type: () -> String
        return self.value

    def setContactType(self, contactType):
        # type: (String) -> None
        self.contactType = contactType

    def setValue(self, value):
        # type: (String) -> None
        self.value = value


class User(object):
    Badge = "badge"
    DEFAULT_SCHEDULE_NAME = "Always"
    FirstName = "John"
    Language = "en"
    LastName = "Doe"
    Notes = "These are some notes."
    Password = "password"
    Schedule = "Always"
    Username = "johdoe"
    USERNAME_PATTERN = r"[\p{Alnum}][ @\w.\s\-]{1, 49}"

    def getContactInfo(self):
        # type: () -> List[ContactInfo]
        raise NotImplementedError

    def getId(self):
        # type: () -> Any
        raise NotImplementedError

    def getPath(self):
        # type: () -> QualifiedPath
        raise NotImplementedError

    def getProfileName(self):
        # type: () -> String
        raise NotImplementedError

    def getRoles(self):
        # type: () -> List[String]
        raise NotImplementedError

    def getScheduleAdjustments(self):
        # type: () -> List[ScheduleAdjustment]
        raise NotImplementedError


class BasicUser(User):
    contactInfo = None  # type: Optional[List[ContactInfo]]
    id = None  # type: Any
    profileName = None  # type: String
    roles = None  # type: List[String]
    scheduleAdjustments = None  # type: List[ScheduleAdjustment]

    def __init__(
        self,
        profileName,  # type: String
        id_,  # type: Any
        roles,  # type: List[String]
        contactInfo=None,  # type: Optional[List[ContactInfo]]
    ):
        # type: (...) -> None
        self.profileName = profileName
        self.id = id_
        self.roles = roles
        self.contactInfo = contactInfo

    def getContactInfo(self):
        # type: () -> List[ContactInfo]
        pass

    def getId(self):
        # type: () -> Any
        pass

    def getPath(self):
        # type: () -> QualifiedPath
        pass

    def getProfileName(self):
        # type: () -> String
        pass

    def getRoles(self):
        # type: () -> List[String]
        pass

    def getScheduleAdjustments(self):
        # type: () -> List[ScheduleAdjustment]
        pass


class PyUser(User):
    """A User implementation that delegates to another user object, but
    has some methods that are more scripting friendly.
    """

    _user = None

    def __init__(self, user=None):
        # type: (Optional[User]) -> None
        self._user = user

    def addContactInfo(self, *args):
        print(self, args)

    def addRole(self, role):
        print(self, role)

    def addRoles(self, roles):
        print(self, roles)

    def addScheduleAdjustment(self, start, end, available, note):
        print(self, start, end, available, note)

    def addScheduleAdjustments(self, scheduleAdjustments):
        print(self, scheduleAdjustments)

    def contains(self, prop):
        pass

    def get(self, propertyName):
        print(self)
        return propertyName

    def getContactInfo(self):
        # type: () -> List[ContactInfo]
        ci_email = ContactInfo("email", "johdoe@mycompany.com")
        ci_phone = ContactInfo("phone", "+1 5551324567")
        ci_sms = ContactInfo("sms", "+1 5557654321")
        return [ci_email, ci_phone, ci_sms]

    def getCount(self):
        print(self)
        return 1

    def getId(self):
        # type: () -> Any
        pass

    def getOrDefault(self, prop):
        print(self, prop)

    def getOrElse(self, property, value):
        pass

    def getPath(self):
        # type: () -> QualifiedPath
        pass

    def getProfileName(self):
        # type: () -> String
        pass

    def getProperties(self):
        pass

    def getRoles(self):
        # type: () -> List[String]
        return ["Administrator", "Developer"]

    def getScheduleAdjustments(self):
        # type: () -> List[ScheduleAdjustment]
        pass

    def getValues(self):
        pass

    def isExtended(self, prop):
        pass

    def isInherited(self, prop):
        pass

    def iterator(self):
        pass

    def merge(self, other, localOnly):
        pass

    def remove(self, prop):
        pass

    def removeContactInfo(self, contactType, value):
        pass

    def removeRole(self, role):
        pass

    def removeScheduleAdjustment(self, start, end, available, note):
        pass

    def set(self, *args):
        pass

    def setContactInfo(self, contactInfo):
        pass

    def setRoles(self, roles):
        pass

    def setScheduleAdjustments(self, scheduleAdjustments):
        pass


class UserSourceMeta(Object):
    description = None  # type: String
    name = None  # type: String
    type = None  # type: String

    def __init__(self, name, description, type_):
        # type: (String, String, String) -> None
        self.name = name
        self.description = description
        self.type = type_

    def getName(self):
        # type: () -> String
        return self.name

    def getDescription(self):
        # type: () -> String
        return self.description

    def getType(self):
        # type: () -> String
        return self.type
