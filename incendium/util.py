# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium Utility module."""

__all__ = [
    'get_function_name',
    'set_locale'
]

import traceback

import system.util

# Global variables.
DEFAULT_LANGUAGE = 'en_US'


def get_function_name():
    """Returns the name of the function last called.

    Returns:
        str: Function's name.
    """
    return traceback.extract_stack(None, 2)[0][2]


def set_locale(user):
    """Sets the Locale to the user's default Language. If none is configured, the default will be
    English (US).

    Args:
        user (_User): The User.
    """
    locale = DEFAULT_LANGUAGE

    if user and user.get_locale():
        locale = user.get_locale()

    system.util.setLocale(locale)
