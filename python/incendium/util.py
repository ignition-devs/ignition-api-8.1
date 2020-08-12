# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium Utility module."""

__all__ = [
    'get_function_name',
    'get_timer',
    'set_locale',
    'validate_form'
]

import traceback

import system.date
import system.util
from incendium import constants


def get_function_name():
    """Returns the name of the function last called.

    Returns:
        str: Function's name.
    """
    return traceback.extract_stack(None, 2)[0][2]


def get_timer(date):
    """Returns a timer with the time elapsed from value until now in
    the form of hh:mm:ss.

    Args:
        date: A date or a date represented in milliseconds.

    Returns:
         str: Time elapsed.
    """
    # Initialize Variables
    from java.util import Date
    h = m = s = 0

    try:
        a = date if isinstance(date, Date) else system.date.fromMillis(date)
        b = system.date.now()
        seconds = system.date.secondsBetween(a, b)
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
    finally:
        return '%02d:%02d:%02d' % (h, m, s)


def set_locale(user):
    """Sets the Locale to the user's default Language. If none is
    configured, the default will be English (US).

    Args:
        user (User): The User.
    """
    locale = constants.DEFAULT_LANGUAGE

    if user is not None and user.get_locale() is not None:
        locale = user.get_locale()

    system.util.setLocale(locale)


def validate_form(strings=None, numbers=None, collections=None):
    """Performs a form validation.

    Args:
        strings (dict): A dictionary containing all strings which must
            not be empty. Optional.
        numbers (dict): A dictionary containing all numbers which must
            be greater than zero. Optional.
        collections (dict): A dictionary containing all collections
            which must at least contain an element. Optional.

    Returns:
        tuple: A tuple containing:
            is_valid (bool): True if all validation tests have passed,
                False otherwise.
            error_message (str): Error message in case any validation
                test has failed.
    """
    # Initialize variables.
    is_valid = True
    error_message = constants.EMPTY_STRING
    counter = 0

    if strings:
        for key, value in strings.iteritems():
            if not value:
                counter += 1
                error_message += (constants.TABBED_LINE + key
                                  if counter == 1 else
                                  constants.NEW_TABBED_LINE + key)
                is_valid = False
    if numbers:
        for key, value in numbers.iteritems():
            if value is None or value <= 0:
                counter += 1
                error_message += (constants.TABBED_LINE + key
                                  if counter == 1 else
                                  constants.NEW_TABBED_LINE + key)
                is_valid = False
    if collections:
        for key, value in collections.iteritems():
            if value is None or value <= 0:
                counter += 1
                error_message += (constants.TABBED_LINE + key
                                  if counter == 1 else
                                  constants.NEW_TABBED_LINE + key)
                is_valid = False

    return is_valid, error_message
