from __future__ import print_function, unicode_literals

__all__ = ["BasicUser", "ContactInfo", "PyUser", "User"]

from java.lang import Object


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


class User(object):
    _Badge = "badge"
    _DEFAULT_SCHEDULE_NAME = "Always"
    _FirstName = "John"
    _Language = "en"
    _LastName = "Doe"
    _Notes = "These are some notes."
    _Password = "password"
    _Schedule = "Always"
    _Username = "johdoe"
    _USERNAME_PATTERN = r"[\p{Alnum}][ @\w.\s\-]{1, 49}"

    @property
    def Badge(self):
        return self._Badge

    @property
    def DEFAULT_SCHEDULE_NAME(self):
        return self._DEFAULT_SCHEDULE_NAME

    @property
    def FirstName(self):
        return self._FirstName

    @property
    def Language(self):
        return self._Language

    @property
    def LastName(self):
        return self._LastName

    @property
    def Notes(self):
        return self._Notes

    @property
    def Password(self):
        return self._Password

    @property
    def Schedule(self):
        return self._Schedule

    @property
    def Username(self):
        return self._Username

    @property
    def USERNAME_PATTERN(self):
        return self._USERNAME_PATTERN

    def getContactInfo(self):
        raise NotImplementedError

    def getId(self):
        raise NotImplementedError

    def getPath(self):
        raise NotImplementedError

    def getProfileName(self):
        raise NotImplementedError

    def getRoles(self):
        raise NotImplementedError

    def getScheduleAdjustments(self):
        raise NotImplementedError


class BasicUser(User):
    def __init__(self, profileName, id, roles, contactInfo=None):
        self.profileName = profileName
        self.id = id
        self.roles = roles
        self.contactInfo = contactInfo

    def getContactInfo(self):
        pass

    def getId(self):
        pass

    def getPath(self):
        pass

    def getProfileName(self):
        pass

    def getRoles(self):
        pass

    def getScheduleAdjustments(self):
        pass


class PyUser(User):
    """A User implementation that delegates to another user object, but
    has some methods that are more scripting friendly.
    """

    _user = None

    def __init__(self, user=None):
        self._user = user

    def addContactInfo(self, *args):
        print(self, args)

    def addRole(self, role):
        print(self, role)

    def addRoles(self, roles):
        print(self, roles)

    def addScheduleAdjustment(self, start, end, available=True, note=None):
        print(self, start, end, available, note)

    def addScheduleAdjustments(self, scheduleAdjustments):
        print(self, scheduleAdjustments)

    def contains(self, prop):
        pass

    def get(self, propertyName):
        print(self)
        return propertyName

    def getContactInfo(self):
        ci_email = ContactInfo("email", "johdoe@mycompany.com")
        ci_phone = ContactInfo("phone", "+1 5551324567")
        ci_sms = ContactInfo("sms", "+1 5557654321")
        return [ci_email, ci_phone, ci_sms]

    def getCount(self):
        print(self)
        return 1

    def getId(self):
        pass

    def getOrDefault(self, prop):
        print(self, prop)

    def getOrElse(self, property, value):
        pass

    def getPath(self):
        pass

    def getProfileName(self):
        pass

    def getProperties(self):
        pass

    def getRoles(self):
        return ["Administrator", "Developer"]

    def getScheduleAdjustments(self):
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

    def removeScheduleAdjustment(self, start, end, available=True, note=None):
        pass

    def set(self, *args):
        pass

    def setContactInfo(self, contactInfo):
        pass

    def setRoles(self, roles):
        pass

    def setScheduleAdjustments(self, scheduleAdjustments):
        pass
