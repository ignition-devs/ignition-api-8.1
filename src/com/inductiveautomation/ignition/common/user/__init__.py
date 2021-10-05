from __future__ import print_function

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
        """Convenience method for scripting to add a new contactInfo
        easily.

        Usage:
            1. addContactInfo(contactType: str, value: str)
            2. addContactInfo(dict: contactDictionary)

        Args:
            args: Variable length argument list.
        """
        print(self, args)

    def addRole(self, role):
        """Convenience method for scripting to add a new role easily.

        Only works if user type supports roles.

        Args:
            role (str): A new role to add. If empty or null, no
                effect.
        """
        print(self, role)

    def addRoles(self, roles):
        """Adds the provided roles to this user.

        Args:
            roles (list[str]): A list of roles.
        """
        print(self, roles)

    def addScheduleAdjustment(self, start, end, available=True, note=None):
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
        print(self, start, end, available, note)

    def addScheduleAdjustments(self, scheduleAdjustments):
        """Add Schedule Adjustments.

        Args:
            scheduleAdjustments (ScheduleAdjustment): ScheduleAdjustment
                object.
        """
        print(self, scheduleAdjustments)

    def contains(self, prop):
        """Returns if this users contains a given property."""
        pass

    def get(self, propertyName):
        """Returns a the value of the requested item.

        Args:
            propertyName (str): The user property to retrieve.

        Returns:
            str: The value of the requested property.
        """
        print(self)
        return propertyName

    def getContactInfo(self):
        """Returns a sequence of ContactInfo objects.

        Each of these objects will have a contactType and value property
        representing the contact information, both strings.

        Returns:
            list[ContactInfo]: A sequence of ContactInfo objects.
        """
        ci_email = ContactInfo("email", "johdoe@mycompany.com")
        ci_phone = ContactInfo("phone", "+1 5551324567")
        ci_sms = ContactInfo("sms", "+1 5557654321")
        return [ci_email, ci_phone, ci_sms]

    def getCount(self):
        """Get count."""
        print(self)
        return 1

    def getId(self):
        """An opaque identifier that can be used to identify this
        user.
        """
        pass

    def getOrDefault(self, prop):
        """Returns a default value if the requested item is not
        present.

        Args:
            prop (Property): The user property to retrieve.

        Returns:
            object: The value of the requested property.
        """
        print(self, prop)

    def getOrElse(self, property, value):
        """Get the value for a given Property, or else fall back to
        value if it's not present.
        """
        pass

    def getPath(self):
        """Generate an path that unambiguously references this user."""
        pass

    def getProfileName(self):
        """The name of the user management profile this user was
        retrieved from.
        """
        pass

    def getProperties(self):
        """Returns all properties for this user."""
        pass

    def getRoles(self):
        """Returns all of the roles this user is a has."""
        return ["Administrator", "Developer"]

    def getScheduleAdjustments(self):
        """Returns all of this user's upcoming schedule adjustments."""
        pass

    def getValues(self):
        """Returns the opaque PropertyValue objects."""
        pass

    def isExtended(self, prop):
        """Returns whether this property set contains a value for the
        prop, and the prop was actually inherited.
        """
        pass

    def isInherited(self, prop):
        """Indicates whether the property was inherited from a parent
        type.
        """
        pass

    def iterator(self):
        """Property iterator."""
        pass

    def merge(self, other, localOnly):
        """Merges the values from other collection into this one."""
        pass

    def remove(self, prop):
        """Remove a property for this user."""
        pass

    def removeContactInfo(self, contactType, value):
        """Remove contact information for this user."""
        pass

    def removeRole(self, role):
        """Remove a role for this user."""
        pass

    def removeScheduleAdjustment(self, start, end, available=True, note=None):
        """Remove schedule adjustment for this user."""
        pass

    def set(self, *args):
        """Set a property for this user."""
        pass

    def setContactInfo(self, contactInfo):
        """Set contact information for this user."""
        pass

    def setRoles(self, roles):
        """Set roles for this user."""
        pass

    def setScheduleAdjustments(self, scheduleAdjustments):
        """Set schedule adjustments for this user."""
        pass
