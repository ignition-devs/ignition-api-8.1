# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com
# pylint: disable=C0103

"""Utility Functions
The following functions give you access to view various Gateway and Client data, as well as interact
with other various systems."""

__all__ = [
    'beep',
    'getGatewayAddress',
    'getProjectName',
    'jsonDecode',
    'jsonEncode',
    'setLocale',
    'translate'
]


def beep():
    """Tells the computer to make a "beep" sound."""
    import sys
    platforms = {
        'linux1': 'Linux',
        'linux2': 'Linux',
        'darwin': 'OS X',
        'win32': 'Windows',
    }

    if sys.platform in platforms:
        if platforms[sys.platform] == 'Windows':
            try:
                import winsound
                winsound.MessageBeep()
            except ImportError:
                print('Beep!')
        elif platforms[sys.platform] == 'OS X':
            import os
            os.system('say "beep"')
        elif platforms[sys.platform] == 'Linux':
            # TODO: Make Linux speak.
            print('Beep!')
    else:
        print('Beep!')


def getGatewayAddress():
    """Returns the address of the gateway that the client is currently communicating with.

    Returns:
        str: The address of the Gateway that the client is communicating with.
    """
    return 'http://localhost:8088/main'


def getProjectName():
    """Returns the name of the project that is currently being run.

    Returns:
        str: The name of the currently running project.
    """
    return 'MyProject'


def jsonDecode(jsonString):
    """Takes a json String and converts it into a Python object such as a list or a dict. If the
    input is not valid json, a string is returned.

    Args:
        jsonString (str): The JSON string to decode into a Python object.

    Returns:
        dict: The decoded Python object.
    """
    print(jsonString)
    return {'key': 'value'}


def jsonEncode(pyObj, indentFactor=4):
    """Takes a Python object such as a list or dict and converts into a json string.

    Args:
        pyObj (object): The Python object to encode into JSON such as a Python list or dictionary.
        indentFactor (int): The number of spaces to add to each level of indentation for
            prettyprinting. Optional.

    Returns:
        str: The encoded JSON string.
    """
    print(pyObj, indentFactor)
    return ''


def setLocale(locale):
    """Sets the user's current Locale. Any valid Java locale code (case-insensitive) can be used as
    a parameter, including ones that have not yet been added to the Translation Manager. An invalid
    locale code will cause an Illegal Argument Exception.

    Args:
        locale (str): A locale code, such as 'en_US' for US English.
    """
    print locale


def translate(term):
    """This function allows you to retrieve the global translation of a term from the translation
    database using the current locale.

    Args:
        term (str): The term to look up.

    Returns:
        str: The translated term.
    """
    return term
