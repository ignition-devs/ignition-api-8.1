# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium User module."""

__all__ = [
    'get_sso_user',
    'get_user_first_name',
    'get_user_full_name'
]

import system.security
import system.user


class _User(object):
    """Wrapper class for Ignition's User object."""

    def __init__(self, user):
        """User initializer.

        Args:
            user (User): Ignition's user object.
        """
        self._username = user.get(user.Username)
        self._first_name = user.get(user.FirstName)
        self._last_name = user.get(user.LastName)
        self._locale = user.getOrDefault(user.Language)

    def get_first_name(self):
        """Returns User's first name.

        Returns:
            str: User's first name.
        """
        return self._first_name

    def get_full_name(self):
        """Returns User's full name.

        Returns:
            str: User's full name.
        """
        return ' '.join([self._first_name, self._last_name])

    def get_locale(self):
        """Returns User's preferred language.

        Returns:
            str: User's preferred language.
        """
        return self._locale


def get_user(user_source, failover=None):
    """Looks up the logged-in User in a User Source.

    Args:
        user_source (str): The name of the User Source.
        failover (str): The name of the Failover profile. Optional.

    Returns:
        _User: A User object.
    """
    # Initialize variables
    user = None
    user_obj = None

    # 1 Try User Source
    if sso:
        user = system.user.getUser(user_source, system.security.getUsername())
    # 2 Try Failover
    if not user and failover:
        user = system.user.getUser(failover, system.security.getUsername())

    if user:
        user_obj = _User(user)

    return user_obj
