# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium Utility module."""

__all__ = [
    'confirm',
    'error',
    'get_function_name',
    'info',
    'set_locale',
    'validate_form'
]

import traceback

import system.util

# Global variables.
DEFAULT_LANGUAGE = 'en_US'
EMPTY_STRING = ''
ERROR_WINDOW_TITLE = 'Error'
NEW_LINE = '\n'
NEW_TABBED_LINE = '\n    - '


def confirm(message, title):
    """Displays a confirmation dialog box to the user with "Yes" and "No" options, and a custom
    message.

    Args:
        message (str): The message to display. This will be translated to the selected Locale.
        title (str): A title for the message box. This will be translated to the selected Locale.

    Returns:
        bool: True if the user selected "Yes", False if the user selected "No", None if the user
            selected "Cancel".
    """
    return system.gui.confirm(system.util.translate(message), system.util.translate(title))


def error(message):
    """Displays an error-style message box to the user.

    Args:
        message (str): The message to display in an error box. This will be translated to the
            selected Locale.
    """
    if message:
        system.gui.errorBox(system.util.translate(message),
                            system.util.translate(ERROR_WINDOW_TITLE))


def get_function_name():
    """Returns the name of the function last called.

    Returns:
        str: Function's name.
    """
    return traceback.extract_stack(None, 2)[0][2]


def info(message, title, detail=None):
    """Displays an informational-style message popup box to the user.

    Args:
        message (str): The message to display. This will be translated to the selected Locale.
        title (str): A title for the message box. This will be translated to the selected Locale.
        detail (str): Additional text to display. This will be translated to the selected Locale.
            Optional.
    """
    if detail is None:
        system.gui.messageBox(system.util.translate(message), system.util.translate(title))
    else:
        msg = system.util.translate(message) + ' ' + system.util.translate(detail)
        system.gui.messageBox(msg, system.util.translate(title))


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


def validate_form(strings=None, numbers=None, collections=None):
    """Performs a form validation.

    Args:
        strings (dict): A dictionary containing all strings which must not be empty. Optional.
        numbers (dict): A dictionary containing all numbers which must be greater than zero.
            Optional.
        collections (dict): A dictionary containing all collections which must at least contain
            an element. Optional.

    Returns:
        tuple: A tuple containing:
            is_valid (bool): True if all validation tests have passed, False otherwise.
            error_message (str): Error message in case any validation test has failed.
    """
    # Initialize variables.
    is_valid = True
    error_message = EMPTY_STRING

    if strings:
        for key, value in strings.iteritems():
            if not value:
                error_message += NEW_TABBED_LINE + key
                is_valid = False
    if numbers:
        for key, value in numbers.iteritems():
            if not value or value <= 0:
                error_message += NEW_TABBED_LINE + key
                is_valid = False
    if collections:
        for key, value in collections.iteritems():
            if not value or value <= 0:
                error_message += NEW_TABBED_LINE + key
                is_valid = False

    return is_valid, error_message
