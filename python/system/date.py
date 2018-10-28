# Copyright (C) 2017
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Ignition date module."""

__all__ = [
    'daysBetween',
    'fromMillis',
    'getDayOfYear',
    'hoursBetween',
    'millisBetween',
    'minutesBetween',
    'monthsBetween',
    'now',
    'parse',
    'secondsBetween',
    'weeksBetween',
    'yearsBetween'
]

from datetime import datetime, timedelta

from java.util import Locale


def daysBetween(date_1, date_2):
    """Calculates the number of whole days between two dates.
    Daylight savings changes are taken into account.

    Args:
        date_1 (datetime): The first date to use.
        date_2 (datetime): The second date to use.

    Returns:
        int: An integer that is representative of the difference
            between two dates.
    """
    return (date_2 - date_1).days


def fromMillis(millis):
    """Creates a date object given a millisecond value.

    Args:
        millis (long): The number of milliseconds elapsed since
        January 1, 1970, 00:00:00 UTC (GMT).

    Returns:
        Date: A new date object.
    """
    return datetime.utcfromtimestamp(float(millis))


def getDayOfYear(date):
    """Extracts the day of the year from a date. The first day of the
    year is day 1.

    Args:
        date (datetime): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return date.timetuple().tm_yday


def hoursBetween(date_1, date_2):
    """Calculates the number of whole hours between two dates.

    Args:
        date_1 (datetime): The first date to use.
        date_2 (datetime): The second date to use.

    Returns:
        int: An integer that is representative of the difference
            between two dates.
    """
    diff = date_2 - date_1
    d, s, micro = diff.days, diff.seconds, diff.microseconds
    return d * 24 + s // 3600


def millisBetween(date_1, date_2):
    """Calculates the number of whole milliseconds between two dates.

    Args:
        date_1 (datetime): The first date to use.
        date_2 (datetime): The second date to use.

    Returns:
        long: An integer that is representative of the difference
            between two dates.
    """
    diff = date_2 - date_1
    d, s, micro = diff.days, diff.seconds, diff.microseconds
    return d * 86400 * 1000 + s * 1000 + micro // 1000


def minutesBetween(date_1, date_2):
    """Calculates the number of whole minutes between two dates.

    Args:
        date_1 (datetime): The first date to use.
        date_2 (datetime): The second date to use.

    Returns:
        int: An integer that is representative of the difference
            between two dates.
    """
    diff = date_2 - date_1
    d, s, micro = diff.days, diff.seconds, diff.microseconds
    return d * 1440 + s // 60


def monthsBetween(date_1, date_2):
    """Calculates the number of whole months between two dates.
    Daylight savings changes are taken into account.

    Args:
        date_1 (datetime): The first date to use.
        date_2 (datetime): The second date to use.

    Returns:
        int: An integer that is representative of the difference
            between two dates.
    """
    from calendar import monthrange
    delta = 0
    while True:
        mdays = monthrange(date_1.year, date_2.month)[1]
        date_1 += timedelta(days=mdays)
        if date_1 <= date_2:
            delta += 1
        else:
            break
    return delta


def now():
    """Returns a java.util.Date object that represents the current
    time according to the local system clock.

    Returns:
        Date: A new date, set to the current date and time.
    """
    return datetime.now()


def parse(dateString, formatString='yyyy-MM-dd HH:mm:ss', locale=Locale.English):
    """Attempts to parse a string and create a Date. Causes
    ParseException if the date dateString parameter is in an
    unrecognized format.

    Args:
        dateString (str): The string to parse into a date.
        formatString (str): Format string used by the parser. Default
            is "yyyy-MM-dd HH:mm:ss". Optional.
        locale (object): Locale used for parsing. Can be the locale
            name such as 'fr', or the Java Locale such as
            'Locale.French'. Default is 'Locale.English'. Optional.

    Retuns:
        Date: The parsed date.
    """
    print dateString, formatString, locale
    return now()


def secondsBetween(date_1, date_2):
    """Calculates the number of whole * between two dates.

    Args:
        date_1 (datetime): The first date to use.
        date_2 (datetime): The second date to use.

    Returns:
        int: An integer that is representative of the difference
            between two dates.
    """
    diff = date_2 - date_1
    d, s, micro = diff.days, diff.seconds, diff.microseconds
    return d * 86400 + s


def weeksBetween(date_1, date_2):
    """Calculates the number of whole weeks between two dates.

    Args:
        date_1 (datetime): The first date to use.
        date_2 (datetime): The second date to use.

    Returns:
        int: An integer that is representative of the difference
            between two dates.
    """
    diff = date_2 - date_1
    return diff.days // 7


def yearsBetween(date_1, date_2):
    """Calculates the number of whole years between two dates.
    Daylight savings changes are taken into account.

    Args:
        date_1 (datetime): The first date to use.
        date_2 (datetime): The second date to use.

    Returns:
        int: An integer that is representative of the difference
            between two dates.
    """
    return monthsBetween(date_1, date_2) // 12
