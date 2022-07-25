from __future__ import print_function

__all__ = ["BasicUser", "ContactInfo", "PyUser", "User", "UserSourceMeta"]

from typing import Any, Iterable, List, Optional, Union

from com.inductiveautomation.ignition.common import QualifiedPath
from com.inductiveautomation.ignition.common.config import (
    BasicProperty,
    Property,
    PropertySet,
    PropertyValue,
)
from com.inductiveautomation.ignition.common.user.schedule import ScheduleAdjustment
from java.lang import Object, String
from java.util import Date


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
    Badge = BasicProperty("badge", str)  # type: BasicProperty
    DEFAULT_SCHEDULE_NAME = "Always"
    FirstName = BasicProperty("firstname", str)  # type: BasicProperty
    Language = BasicProperty("language", str, "en")  # type: BasicProperty
    LastName = BasicProperty("firstname", str)  # type: BasicProperty
    Notes = BasicProperty("notes", str)  # type: BasicProperty
    Password = BasicProperty("password", str)  # type: BasicProperty
    Schedule = BasicProperty("schedule", str, "Always")  # type: BasicProperty
    Username = BasicProperty("username", str)  # type: BasicProperty
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
        # type: (Any) -> None
        print(self, args)

    def addRole(self, role):
        # type: (String) -> None
        print(self, role)

    def addRoles(self, roles):
        # type: (List[String]) -> None
        print(self, roles)

    def addScheduleAdjustment(self, start, end, available, note):
        # type: (Date, Date, bool, String) -> None
        print(self, start, end, available, note)

    def addScheduleAdjustments(self, scheduleAdjustments):
        # type: (List[ScheduleAdjustment]) -> None
        print(self, scheduleAdjustments)

    def contains(self, prop):
        # type: (Property) -> bool
        pass

    def get(self, propertyName):
        # type: (Union[Property, String]) -> Any
        pass

    def getContactInfo(self):
        # type: () -> List[ContactInfo]
        ci_email = ContactInfo("email", "johdoe@mycompany.com")
        ci_phone = ContactInfo("phone", "+1 5551324567")
        ci_sms = ContactInfo("sms", "+1 5557654321")
        return [ci_email, ci_phone, ci_sms]

    def getCount(self):
        # type: () -> int
        print(self)
        return 1

    def getId(self):
        # type: () -> Any
        pass

    def getOrDefault(self, prop):
        # type: (Property) -> Any
        print(self, prop)

    def getOrElse(self, property, value):
        # type: (Property, Any) -> Any
        pass

    def getPath(self):
        # type: () -> QualifiedPath
        pass

    def getProfileName(self):
        # type: () -> String
        pass

    def getProperties(self):
        # type: () -> List[Property]
        pass

    def getRoles(self):
        # type: () -> List[String]
        return ["Administrator", "Developer"]

    def getScheduleAdjustments(self):
        # type: () -> List[ScheduleAdjustment]
        pass

    def getValues(self):
        # type: () -> List[PropertyValue]
        pass

    def isExtended(self, prop):
        # type: (Property) -> bool
        pass

    def isInherited(self, prop):
        # type: (Property) -> bool
        pass

    def iterator(self):
        # type: () -> Iterable[Property]
        pass

    def merge(self, other, localOnly):
        # type: (PropertySet, bool) -> None
        pass

    def remove(self, prop):
        # type: (Property) -> None
        pass

    def removeContactInfo(self, contactType, value):
        # type: (String, String) -> None
        pass

    def removeRole(self, role):
        # type: (String) -> None
        pass

    def removeScheduleAdjustment(self, start, end, available, note):
        # type: (Date, Date, bool, String) -> None
        pass

    def set(self, *args):
        # type: (Any) -> None
        pass

    def setContactInfo(self, contactInfo):
        # type: (List[ContactInfo]) -> None
        pass

    def setRoles(self, roles):
        # type: (List[String]) -> None
        pass

    def setScheduleAdjustments(self, scheduleAdjustments):
        # type: (List[ScheduleAdjustment]) -> None
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
