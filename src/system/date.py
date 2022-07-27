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

from datetime import datetime
from time import localtime, mktime

from typing import Optional

from java.lang import String
from java.util import Date, Locale


def _now():
    # type: () -> datetime
    """Get current datetime.

    Returns:
        Now.
    """
    return datetime.now()


def addDays(date, value):
    # type: (Date, int) -> Date
    """Add or subtract an amount of days to a given date and time.

    Args:
        date: The starting date.
        value: The number of units to add, or subtract if the value is
            negative.

    Returns:
        A new date object offset by the integer passed to the function.
    """
    print(date, value)
    return Date()


def addHours(date, value):
    # type: (Date, int) -> Date
    """Add or subtract an amount of hours to a given date and time.

    Args:
        date: The starting date.
        value: The number of units to add, or subtract if the value is
            negative.

    Returns:
        A new date object offset by the integer passed to the function.
    """
    print(date, value)
    return Date()


def addMillis(date, value):
    # type: (Date, int) -> Date
    """Add or subtract an amount of milliseconds to a given date and
    time.

    Args:
        date: The starting date.
        value: The number of units to add, or subtract if the value is
            negative.

    Returns:
        A new date object offset by the integer passed to the function.
    """
    print(date, value)
    return Date()


def addMinutes(date, value):
    # type: (Date, int) -> Date
    """Add or subtract an amount of minutes to a given date and time.

    Args:
        date: The starting date.
        value: The number of units to add, or subtract if the value is
            negative.

    Returns:
        A new date object offset by the integer passed to the function.
    """
    print(date, value)
    return Date()


def addMonths(date, value):
    # type: (Date, int) -> Date
    """Add or subtract an amount of months to a given date and time.

    This function is unique since each month can have a variable number
    of days. For example, if the date passed in is March 31st, and we
    add one month, April does not have a 31st day, so the returned date
    will be the proper number of months rounded down to the closest
    available day, in this case April 30th.

    Args:
        date: The starting date.
        value: The number of units to add, or subtract if the value is
            negative.

    Returns:
        A new date object offset by the integer passed to the function.
    """
    print(date, value)
    return Date()


def addSeconds(date, value):
    # type: (Date, int) -> Date
    """Add or subtract an amount of seconds to a given date and time.

    Args:
        date: The starting date.
        value: The number of units to add, or subtract if the value is
            negative.

    Returns:
        A new date object offset by the integer passed to the function.
    """
    print(date, value)
    return Date()


def addWeeks(date, value):
    # type: (Date, int) -> Date
    """Add or subtract an amount of weeks to a given date and time.

    Args:
        date: The starting date.
        value: The number of units to add, or subtract if the value is
            negative.

    Returns:
        A new date object offset by the integer passed to the function.
    """
    print(date, value)
    return Date()


def addYears(date, value):
    # type: (Date, int) -> Date
    """Add or subtract an amount of years to a given date and time.

    Args:
        date: The starting date.
        value: The number of units to add, or subtract if the value is
            negative.

    Returns:
        A new date object offset by the integer passed to the function.
    """
    print(date, value)
    return Date()


def daysBetween(date_1, date_2):
    # type: (Date, Date) -> int
    """Calculates the number of whole days between two dates.

    Daylight Saving Time changes are taken into account.

    Args:
        date_1: The first date to use.
        date_2: The second date to use.

    Returns:
        An integer that is representative of the difference between two
        dates.
    """
    print(date_1, date_2)
    return 1


def format(date, format="yyyy-MM-dd HH:mm:ss"):
    # type: (Date, String) -> unicode
    """Returns the given date as a string, formatted according to a
    pattern.

    The pattern is a format that is full of various placeholders that
    display different parts of the date. These are case-sensitive. These
    placeholders can be repeated for a different effect. For example, M
    will give you 1-12, MM will give you 01-12, MMM will give you
    Jan-Dec, MMMM will give you January-December.

    Note:
        The functions above are based off the Java class
        `SimpleDateFormat` internally. The functions will accept any
        valid format string for that class.

    Args:
        date: The date to format.
        format: A format string such as "yyyy-MM-dd HH:mm:ss". The
            format argument is optional. The default is
            "yyyy-MM-dd HH:mm:ss". Optional.

    Returns:
        A string representing the formatted datetime.
    """
    print(date, format)
    _date = _now()
    _format = format
    _format = _format.replace("a", "%p")
    _format = _format.replace("D", "%j")
    _format = _format.replace("dd", "{:02}".format(_date.day))
    _format = _format.replace("d", "{}".format(_date.day))
    _format = _format.replace("EEEE", "%A")
    _format = _format.replace("E", "%a")
    _format = _format.replace("F", "{}".format(_date.isocalendar()[2]))
    _format = _format.replace("G", "AD")
    _format = _format.replace("hh", "%I")
    _format = _format.replace("h", "%-I")
    _format = _format.replace("HH", "{:02}".format(_date.hour))
    _format = _format.replace("H", "%-H")
    _format = _format.replace("k", "%H")
    _format = _format.replace("K", "%-I")
    _format = _format.replace("MMMM", "%B")
    _format = _format.replace("MMM", "%b")
    _format = _format.replace("MM", "{:02}".format(_date.month))
    _format = _format.replace("M", "{}".format(_date.month))
    _format = _format.replace("mm", "%M")
    _format = _format.replace("m", "%-M")
    _millis = _date.microsecond % 1000
    _format = _format.replace("SSS", "{:03}".format(_millis))
    _format = _format.replace("SS", "{:02}".format(_millis))
    _format = _format.replace("S", "{:01}".format(_millis))
    _format = _format.replace("ss", "%S")
    _format = _format.replace("s", "%-S")
    _format = _format.replace("w", "{}".format(_date.isocalendar()[1] + 1))
    _format = _format.replace("u", "%w")
    _format = _format.replace(
        "W",
        "{}".format(_date.isocalendar()[1] - _date.replace(day=1).isocalendar()[1] + 1),
    )

    _format = _format.replace("XXX", "{:03.0f}:00".format(getTimezoneOffset()))
    _format = _format.replace("XX", "{:03.0f}00".format(getTimezoneOffset()))
    _format = _format.replace("X", "{:03.0f}".format(getTimezoneOffset()))
    _format = _format.replace("yyyy", "{}".format(_date.year))
    _format = _format.replace("yy", str(_date.year)[-2:])
    _format = _format.replace("Y", "%Y")
    _format = _format.replace("y", "%Y")
    _format = _format.replace("Z", "{:03.0f}00".format(getTimezoneOffset()))
    _format = _format.replace("z", "PDT")
    return unicode(_date.strftime(_format))


def fromMillis(millis):
    # type: (int) -> Date
    """Creates a date object given a millisecond value.

    Args:
        millis: The number of milliseconds elapsed since January 1,
            1970, 00:00:00 UTC (GMT).

    Returns:
        A new date object.
    """
    return Date(millis)


def getAMorPM(date):
    # type: (Date) -> int
    """Returns a 0 if the time is before noon, and a 1 if the time is
    after noon.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    return 1 if _now().hour >= 12 else 0


def getDate(year, month, day):
    # type: (int, int, int) -> Date
    """Creates a new Date object given a year, month and a day.

    The time will be set to midnight of that day.

    Args:
        year: The year for the new date.
        month: The month of the new date. January is month 0.
        day: The day of the month for the new date. The first day
            of the month is day 1.

    Returns:
        A new date, set to midnight of that day.
    """
    print(year, month, day)
    return Date()


def getDayOfMonth(date):
    # type: (Date) -> int
    """Extracts the day of the month from a date.

    The first day of the month is day 1.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    return _now().day


def getDayOfWeek(date):
    # type: (Date) -> int
    """Extracts the day of the week from a date.

    Sunday is day 1, Saturday is day 7.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    _dow = [2, 3, 4, 5, 6, 7, 1]
    return _dow[_now().weekday()]


def getDayOfYear(date):
    # type: (Date) -> int
    """Extracts the day of the year from a date.

    The first day of the year is day 1.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    return _now().timetuple().tm_yday


def getHour12(date):
    # type: (Date) -> int
    """Extracts the hour from a date.

    Uses a 12 hour clock, so noon and midnight are returned as 0.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    return _now().hour - 12 if _now().hour >= 12 else _now().hour


def getHour24(date):
    # type: (Date) -> int
    """Extracts the hour from a date.

    Uses a 24 hour clock, so midnight is zero.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    return _now().hour


def getMillis(date):
    # type: (Date) -> int
    """Extracts the milliseconds from a date, ranging from 0-999.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    return _now().microsecond // 1000


def getMinute(date):
    # type: (Date) -> int
    """Extracts the minutes from a date, ranging from 0-59.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    return _now().minute


def getMonth(date):
    # type: (Date) -> int
    """Extracts the month from a date, where January is month 0.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    return _now().month


def getQuarter(date):
    # type: (Date) -> int
    """Extracts the quarter from a date, ranging from 1-4.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    return ((_now().month - 1) // 3) + 1


def getSecond(date):
    # type: (Date) -> int
    """Extracts the seconds from a date, ranging from 0-59.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    return _now().second


def getTimezone():
    # type: () -> String
    """Returns the ID of the current timezone.

    Returns:
        A representation of the current timezone.
    """
    return "America/Tijuana"


def getTimezoneOffset(date=None):
    # type: (Optional[Date]) -> float
    """Returns the current timezone's offset versus UTC for a given
    instant, taking Daylight Saving Time into account.

    Args:
        date: The instant in time for which to calculate the offset.
            Uses now() if omitted. Optional.

    Returns:
        The timezone offset compared to UTC, in hours.
    """
    return -7.0 if isDaylightTime(date) else -8.0


def getTimezoneRawOffset():
    # type: () -> float
    """Returns the current timezone offset versus UTC, not taking
    Daylight Saving Time into account.

    Returns:
         The timezone offset.
    """
    return float(0)


def getYear(date):
    # type: (Date) -> int
    """Extracts the year from a date.

    Args:
        date: The date to use.

    Returns:
        An integer that is representative of the extracted value.
    """
    print(date)
    return _now().year


def hoursBetween(date_1, date_2):
    # type: (Date, Date) -> int
    """Calculates the number of whole hours between two dates.

    Args:
        date_1: The first date to use.
        date_2: The second date to use.

    Returns:
        An integer that is representative of the difference between two
        dates.
    """
    print(date_1, date_2)
    return 1


def isAfter(date_1, date_2):
    # type: (Date, Date) -> bool
    """Compares two dates to see if date_1 is after date_2.

    Args:
        date_1: The first date.
        date_2: The second date.

    Returns:
        True if date_1 is after date_2, False otherwise.
    """
    print(date_1, date_2)
    return True


def isBefore(date_1, date_2):
    # type: (Date, Date) -> bool
    """Compares to dates to see if date_1 is before date_2.

    Args:
        date_1: The first date.
        date_2: The second date.

    Returns:
        True if date_1 is before date_2, False otherwise.
    """
    print(date_1, date_2)
    return False


def isBetween(target_date, start_date, end_date):
    # type: (Date, Date, Date) -> bool
    """Compares two dates to see if a target date is between two other
    dates.

    Args:
        target_date: The date to compare.
        start_date: The start of a date range.
        end_date: The end of a date range. This date must be after the
            start date.

    Returns:
        True if target_date is >= start_date and target_date <=
        end_date, False otherwise.
    """
    print(target_date, start_date, end_date)
    return True


def isDaylightTime(date=None):
    # type: (Optional[Date]) -> bool
    """Checks to see if the current timezone is using Daylight Saving
    Time during the date specified.

    Args:
        date: The date you want to check if the current timezone is
            observing Daylight Saving Time. Uses now() if omitted.
            Optional.

    Returns:
        True if date is observing Daylight Saving Time in the
        current timezone, False otherwise.
    """
    print(date)
    _date = _now()
    time_tuple = (
        _date.year,
        _date.month,
        _date.day,
        _date.hour,
        _date.minute,
        _date.second,
        _date.weekday(),
        0,
        0,
    )
    stamp = mktime(time_tuple)
    time_tuple = localtime(stamp)
    return time_tuple.tm_isdst > 0


def midnight(date):
    # type: (Date) -> Date
    """Returns a copy of a date with the hour, minute, second, and
    millisecond fields set to zero.

    Args:
        date: The starting date.

    Returns:
        A new date, set to midnight of the day provided.
    """
    print(date)
    return Date()


def millisBetween(date_1, date_2):
    # type: (Date, Date) -> long
    """Calculates the number of whole milliseconds between two dates.

    Args:
        date_1: The first date to use.
        date_2: The second date to use.

    Returns:
        An integer that is representative of the difference between two
        dates.
    """
    print(date_2, date_1)
    return long(1)


def minutesBetween(date_1, date_2):
    # type: (Date, Date) -> int
    """Calculates the number of whole minutes between two dates.

    Args:
        date_1: The first date to use.
        date_2: The second date to use.

    Returns:
        An integer that is representative of the difference between two
        dates.
    """
    print(date_2, date_1)
    return 1


def monthsBetween(date_1, date_2):
    # type: (Date, Date) -> int
    """Calculates the number of whole months between two dates.

    Daylight Saving Time changes are taken into account.

    Args:
        date_1: The first date to use.
        date_2: The second date to use.

    Returns:
        An integer that is representative of the difference between two
        dates.
    """
    print(date_1, date_2)
    return 0


def now():
    # type: () -> Date
    """Returns a java.util.Date object that represents the current time
    according to the local system clock.

    Returns:
        A new date, set to the current date and time.
    """
    return Date()


def parse(dateString, formatString="yyyy-MM-dd HH:mm:ss", locale=Locale.ENGLISH):
    # type: (String, Optional[String], Optional[Locale]) -> Date
    """Attempts to parse a string and create a Date.

    Causes ParseException if the date dateString parameter is in an
    unrecognized format.

    Args:
        dateString: The string to parse into a date.
        formatString: Format string used by the parser. Default is
            "yyyy-MM-dd HH:mm:ss". Optional.
        locale: Locale used for parsing. Can be the locale name
            such as 'fr', or the Java Locale such as 'Locale.FRENCH'.
            Default is 'Locale.ENGLISH'. Optional.

    Returns:
        The parsed date.
    """
    print(dateString, formatString, locale)
    return Date()


def secondsBetween(date_1, date_2):
    # type: (Date, Date) -> int
    """Calculates the number of whole seconds between two dates.

    Args:
        date_1: The first date to use.
        date_2: The second date to use.

    Returns:
        An integer that is representative of the difference between two
        dates.
    """
    print(date_2, date_1)
    return 0


def setTime(date, hour, minute, second):
    # type: (Date, int, int, int) -> Date
    """Takes in a date, and returns a copy of it with the time fields
    set as specified.

    Args:
        date: The starting date.
        hour: The hours (0-23) to set.
        minute: The minutes (0-59) to set.
        second: The seconds (0-59) to set.

    Returns:
        A new date, set to the appropriate time.
    """
    print(date, hour, minute, second)
    return Date()


def toMillis(date):
    # type: (Date) -> long
    """Converts a Date object to its millisecond value elapsed since
    January 1, 1970, 00:00:00 UTC (GMT).

    Args:
        date: The date object to convert.

    Returns:
        An 8-byte integer representing the number of millisecond elapsed
        since January 1, 1970, 00:00:00 UTC (GMT).
    """
    print(date)
    _date = _now()
    millis = mktime(_date.timetuple()) * 1000 + _date.microsecond // 1000
    return long(millis)


def weeksBetween(date_1, date_2):
    # type: (Date, Date) -> int
    """Calculates the number of whole weeks between two dates.

    Args:
        date_1: The first date to use.
        date_2: The second date to use.

    Returns:
        An integer that is representative of the difference between two
        dates.
    """
    print(date_1, date_2)
    return 0


def yearsBetween(date_1, date_2):
    # type: (Date, Date) -> int
    """Calculates the number of whole years between two dates.

    Daylight Saving Time changes are taken into account.

    Args:
        date_1: The first date to use.
        date_2: The second date to use.

    Returns:
        An integer that is representative of the difference between two
        dates.
    """
    print(date_1, date_2)
    return 0
