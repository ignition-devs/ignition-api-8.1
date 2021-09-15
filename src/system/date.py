"""Date Functions.

The following functions give you access to test and modify dates.
"""

from __future__ import print_function

__all__ = [
    "addDays",
    "addHours",
    "addMillis",
    "addMinutes",
    "addMonths",
    "addSeconds",
    "addWeeks",
    "addYears",
    "daysBetween",
    "format",
    "fromMillis",
    "getAMorPM",
    "getDate",
    "getDayOfMonth",
    "getDayOfWeek",
    "getDayOfYear",
    "getHour12",
    "getHour24",
    "getMillis",
    "getMinute",
    "getMonth",
    "getQuarter",
    "getSecond",
    "getTimezone",
    "getTimezoneOffset",
    "getTimezoneRawOffset",
    "getYear",
    "hoursBetween",
    "isAfter",
    "isBefore",
    "isBetween",
    "isDaylightTime",
    "midnight",
    "millisBetween",
    "minutesBetween",
    "monthsBetween",
    "now",
    "parse",
    "secondsBetween",
    "setTime",
    "toMillis",
    "weeksBetween",
    "yearsBetween",
]

from calendar import monthrange
from datetime import datetime, timedelta
from time import localtime, mktime

from java.util import Date, Locale


def addDays(date, value):
    """Add or subtract an amount of days to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return date + timedelta(days=value)


def addHours(date, value):
    """Add or subtract an amount of hours to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return date + timedelta(hours=value)


def addMillis(date, value):
    """Add or subtract an amount of milliseconds to a given date and
    time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return date + timedelta(milliseconds=value)


def addMinutes(date, value):
    """Add or subtract an amount of minutes to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return date + timedelta(minutes=value)


def addMonths(date, value):
    """Add or subtract an amount of months to a given date and time.

    This function is unique since each month can have a variable number
    of days. For example, if the date passed in is March 31st, and we
    add one month, April does not have a 31st day, so the returned date
    will be the proper number of months rounded down to the closest
    available day, in this case April 30th.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    month = (date.month + value) % 12
    year = date.year + (date.month + value - 1) // 12
    if not month:
        month = 12
    day = min(date.day, monthrange(year, month)[1])
    return date.replace(day=day, month=month, year=year)


def addSeconds(date, value):
    """Add or subtract an amount of seconds to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return date + timedelta(seconds=value)


def addWeeks(date, value):
    """Add or subtract an amount of weeks to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return date + timedelta(weeks=value)


def addYears(date, value):
    """Add or subtract an amount of years to a given date and time.

    Args:
        date (Date): The starting date.
        value (int): The number of units to add, or subtract if the
            value is negative.

    Returns:
        Date: A new date object offset by the integer passed to the
            function.
    """
    return date.replace(year=date.year + value)


def daysBetween(date_1, date_2):
    """Calculates the number of whole days between two dates.

    Daylight Saving Time changes are taken into account.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference between
            two dates.
    """
    return (date_2 - date_1).days


def format(date, format="yyyy-MM-dd HH:mm:ss"):
    """Returns the given date as a string, formatted according to a
    pattern.

    Note:
        Not all symbols from system.date.format() have a counterpart
        directive on strftime().

    Args:
        date (Date): The date to format.
        format (str): A format string such as "yyyy-MM-dd HH:mm:ss".
            Optional.

    Returns:
        str: A string representing the formatted datetime
    """
    _format = format.replace("yyyy", "%Y")
    _format = _format.replace("yy", "%y")
    _format = _format.replace("MMMM", "%B")
    _format = _format.replace("MMM", "%b")
    _format = _format.replace("MM", "%m")
    _format = _format.replace("dd", "%d")
    _format = _format.replace("HH", "%H")
    _format = _format.replace("hh", "%I")
    _format = _format.replace("mm", "%M")
    _format = _format.replace("S", "%f")
    _format = _format.replace("ss", "%S")
    _format = _format.replace("z", "%Z")
    _format = _format.replace("Z", "%z")
    _format = _format.replace("a", "%p")
    _format = _format.replace("w", "%U")
    _format = _format.replace("D", "%j")
    return date.strftime(_format)


def fromMillis(millis):
    """Creates a date object given a millisecond value.

    Args:
        millis (long): The number of milliseconds elapsed since
            January 1, 1970, 00:00:00 UTC (GMT).

    Returns:
        Date: A new date object.
    """
    seconds = millis // 1000
    micro = (millis % 1000) * 1000
    _date = datetime.fromtimestamp(seconds)
    return datetime(
        _date.year,
        _date.month,
        _date.day,
        _date.hour,
        _date.minute,
        _date.second,
        micro,
    )


def getAMorPM(date):
    """Returns a 0 if the time is before noon, and a 1 if the time is
    after noon.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return 1 if date.hour >= 12 else 0


def getDate(year, month, day):
    """Creates a new Date object given a year, month and a day.

    The time will be set to midnight of that day.

    Args:
        year (int): The year for the new date.
        month (int): The month of the new date. January is month 0.
        day (int): The day of the month for the new date. The first day
            of the month is day 1.

    Returns:
        Date: A new date, set to midnight of that day.
    """
    _jan = datetime(year, 1, day)
    return addMonths(_jan, month)


def getDayOfMonth(date):
    """Extracts the day of the month from a date. The first day of the
    month is day 1.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return date.day


def getDayOfWeek(date):
    """Extracts the day of the week from a date.

    Sunday is day 1, Saturday is day 7.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    _dow = [2, 3, 4, 5, 6, 7, 1]
    return _dow[date.weekday()]


def getDayOfYear(date):
    """Extracts the day of the year from a date. The first day of the
    year is day 1.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return date.timetuple().tm_yday


def getHour12(date):
    """Extracts the hour from a date. Uses a 12 hour clock, so noon and
    midnight are returned as 0.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return date.hour - 12 if date.hour >= 12 else date.hour


def getHour24(date):
    """Extracts the hour from a date. Uses a 24 hour clock, so midnight
    is zero.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return date.hour


def getMillis(date):
    """Extracts the milliseconds from a date, ranging from 0-999.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return date.microsecond // 1000


def getMinute(date):
    """Extracts the minutes from a date, ranging from 0-59.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return date.minute


def getMonth(date):
    """Extracts the month from a date, where January is month 0.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return date.month - 1


def getQuarter(date):
    """Extracts the quarter from a date, ranging from 1-4.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return ((date.month - 1) // 3) + 1


def getSecond(date):
    """Extracts the seconds from a date, ranging from 0-59.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return date.second


def getTimezone():
    """Returns the ID of the current timezone.

    Returns:
        str: A representation of the current timezone.
    """
    return "America/Tijuana"


def getTimezoneOffset(date=datetime.now()):
    """Returns the current timezone's offset versus UTC for a given
    instant, taking Daylight Saving Time into account.

    Args:
        date (Date): The instant in time for which to calculate the
            offset. Uses now() if omitted. Optional.

    Returns:
        float: The timezone offset compared to UTC, in hours.
    """
    return -7.0 if isDaylightTime(date) else -8.0


def getTimezoneRawOffset():
    """Returns the current timezone offset versus UTC, not taking
    Daylight Saving Time into account.

    Returns:
         float: The timezone offset.
    """
    offset = -1.0 if isDaylightTime() else 0.0
    return float(hoursBetween(datetime.utcnow(), datetime.now())) + offset


def getYear(date):
    """Extracts the year from a date.

    Args:
        date (Date): The date to use.

    Returns:
        int: An integer that is representative of the extracted value.
    """
    return date.year


def hoursBetween(date_1, date_2):
    """Calculates the number of whole hours between two dates.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference between
            two dates.
    """
    diff = date_2 - date_1
    days, seconds, _ = diff.days, diff.seconds, diff.microseconds
    return days * 24 + seconds // 3600


def isAfter(date_1, date_2):
    """Compares two dates to see if date_1 is after date_2.

    Args:
        date_1 (Date): The first date.
        date_2 (Date): The second date.

    Returns:
        bool: True (1) if date_1 is after date_2, False (0) otherwise.
    """
    return date_1 > date_2


def isBefore(date_1, date_2):
    """Compares to dates to see if date_1 is before date_2.

    Args:
        date_1 (Date): The first date.
        date_2 (Date): The second date.

    Returns:
        bool: True (1) if date_1 is before date_2, False (0) otherwise.
    """
    return date_1 < date_2


def isBetween(target_date, start_date, end_date):
    """Compares two dates to see if a target date is between two other
    dates.

    Args:
        target_date (Date): The date to compare.
        start_date (Date): The start of a date range.
        end_date (Date): The end of a date range. This date must be
            after the start date.

    Returns:
        bool: True (1) if target_date is >= start_date and
            target_date <= end_date, False (0) otherwise.
    """
    return start_date <= target_date <= end_date


def isDaylightTime(date=datetime.now()):
    """Checks to see if the current timezone is using Daylight Saving
    Time during the date specified.

    Args:
        date (Date): The date you want to check if the current
            timezone is observing Daylight Saving Time. Uses now() if
            omitted. Optional.

    Returns:
        bool: True (1) if date is observing Daylight Saving Time in the
            current timezone, False (0) otherwise.
    """
    time_tuple = (
        date.year,
        date.month,
        date.day,
        date.hour,
        date.minute,
        date.second,
        date.weekday(),
        0,
        0,
    )
    stamp = mktime(time_tuple)
    time_tuple = localtime(stamp)
    return time_tuple.tm_isdst > 0


def midnight(date):
    """Returns a copy of a date with the hour, minute, second, and
    millisecond fields set to zero.

    Args:
        date (Date): The starting date.

    Returns:
        Date: A new date, set to midnight of the day provided.
    """
    return date.replace(hour=0, minute=0, second=0, microsecond=0)


def millisBetween(date_1, date_2):
    """Calculates the number of whole milliseconds between two dates.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        long: An integer that is representative of the difference
            between two dates.
    """
    diff = date_2 - date_1
    days, seconds, microseconds = diff.days, diff.seconds, diff.microseconds
    return days * 86400 * 1000 + seconds * 1000 + microseconds // 1000


def minutesBetween(date_1, date_2):
    """Calculates the number of whole minutes between two dates.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference between
            two dates.
    """
    diff = date_2 - date_1
    days, seconds, _ = diff.days, diff.seconds, diff.microseconds
    return days * 1440 + seconds // 60


def monthsBetween(date_1, date_2):
    """Calculates the number of whole months between two dates. Daylight
    Saving Time changes are taken into account.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference between
            two dates.
    """
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
    """Returns a java.util.Date object that represents the current time
    according to the local system clock.

    Returns:
        Date: A new date, set to the current date and time.
    """
    return datetime.now()


def parse(
    dateString, formatString="yyyy-MM-dd HH:mm:ss", locale=Locale.ENGLISH
):
    """Attempts to parse a string and create a Date. Causes
    ParseException if the date dateString parameter is in an
    unrecognized format.

    Args:
        dateString (str): The string to parse into a date.
        formatString (str): Format string used by the parser. Default is
            "yyyy-MM-dd HH:mm:ss". Optional.
        locale (object): Locale used for parsing. Can be the locale name
            such as 'fr', or the Java Locale such as 'Locale.French'.
            Default is 'Locale.English'. Optional.

    Returns:
        Date: The parsed date.
    """
    print(dateString, formatString, locale)
    return now()


def secondsBetween(date_1, date_2):
    """Calculates the number of whole seconds between two dates.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference between
            two dates.
    """
    diff = date_2 - date_1
    days, seconds, _ = diff.days, diff.seconds, diff.microseconds
    return days * 86400 + seconds


def setTime(date, hour, minute, second):
    """Takes in a date, and returns a copy of it with the time fields
    set as specified.

    Args:
        date (Date): The starting date.
        hour (int): The hours (0-23) to set.
        minute(int): The minutes (0-59) to set.
        second (int): The seconds (0-59) to set.

    Returns:
        Date: A new date, set to the appropriate time.
    """
    return date.replace(hour=hour, minute=minute, second=second, microsecond=0)


def toMillis(date):
    """Converts a Date object to its millisecond value elapsed since
    January 1, 1970, 00:00:00 UTC (GMT).

    Args:
        date (Date): The date object to convert.

    Returns:
        int: 8-byte integer representing the number of millisecond
            elapsed since January 1, 1970, 00:00:00 UTC (GMT).
    """
    millis = mktime(date.timetuple()) * 1000 + date.microsecond // 1000
    return int(millis)


def weeksBetween(date_1, date_2):
    """Calculates the number of whole weeks between two dates.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference between
            two dates.
    """
    diff = date_2 - date_1
    return diff.days // 7


def yearsBetween(date_1, date_2):
    """Calculates the number of whole years between two dates. Daylight
    Saving Time changes are taken into account.

    Args:
        date_1 (Date): The first date to use.
        date_2 (Date): The second date to use.

    Returns:
        int: An integer that is representative of the difference between
            two dates.
    """
    return monthsBetween(date_1, date_2) // 12
