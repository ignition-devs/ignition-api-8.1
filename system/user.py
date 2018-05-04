# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103,C0111,R0201

"""User Functions
The following functions give you access to view and edit users in the Gateway."""

__all__ = [
    'User',
    'getUsers',
    'getUser'
]


class ContactInfo(object):
    def __init__(self,
                 contactType=None,
                 value=None):
        self.contactType = contactType
        self.value = value


class User(object):
    Username = 'johdoe'
    FirstName = 'John'
    LastName = 'Doe'
    Email = 'johdoe@mycompany.com'
    Notes = 'These are some notes.'
    Roles = ['Administrator', 'Developer']
    Schedule = 'Always'
    Language = 'en_US'

    def get(self, prop):
        """Returns a the value of the requested item.

        Args:
            prop (User property): The user property to retrieve.

        Returns:
            str: The value of the requested property.
        """
        return prop

    def getContactInfo(self):
        """Returns a sequence of ContactInfo objects. Each of these objects will have a contactType
        and valueproperty representing the contact information, both strings.

        Returns:
            list[ContactInfo]: A sequence of ContactInfo objects.
        """
        ci_email = ContactInfo('email', 'johdoe@mycompany.com')
        ci_phone = ContactInfo('phone', '+1 5551324567')
        ci_sms = ContactInfo('sms', '+1 5557654321')
        return [ci_email, ci_phone, ci_sms]

    def getId(self):
        """Returns the internal identifier object that the backing user source needs to identify
        this user.

        Returns:
            str: The internal identifier object that the backing user source needs to identify this
                user.
        """
        return 1

    def getOrDefault(self, prop):
        """Returns a default value if the requested item is not present.

        Args:
            prop (User property): The user property to retrieve.

        Returns:
            str: The value of the requested property.
        """
        return prop

    def getRoles(self):
        """Returns a sequence of strings representing the roles that this user belongs to

        Returns:
             list[str]: Sequence of strings representing the roles that this user belongs to.
        """
        return User.Roles


def getUsers(userSource):
    """Retrieves the list of users in a specific user source. The `User` objects that are returned
    contain all of the information about that user, except for the user's password.

    Args:
        userSource (str): The name of the user source to find the users in.

    Returns:
        list[User] - A list of User objects.
    """
    print userSource
    # You may return more than one User object.
    return [User()]


def getUser(userSource, username):
    """Looks up a specific user in a user source, by username. The full `User` object is returned
    except for the user's password.

    Args:
        userSource (str): The name of the user source to search for the user in.
        username (str): The username of the user to search for.

    Returns:
        User: A User object.
    """
    print(userSource, username)
    return User()
