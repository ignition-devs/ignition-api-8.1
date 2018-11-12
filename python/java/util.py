# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Contains the collections framework, legacy collection classes,
event model, date and time facilities, internationalization, and
miscellaneous utility classes (a string tokenizer, a random-number
generator, and a bit array)."""

__all__ = [
    'Date',
    'Locale'
]


class Date(object):
    """The class Date represents a specific instant in time, with
    millisecond precision.
    """

    def __new__(cls, date=None):
        """Allocates a Date object and initializes it...

        1) so that it represents the time at which it was allocated,
        measured to the nearest millisecond.

        2) to represent the specified number of milliseconds since the
        standard base time known as "the epoch", namely January 1,
        1970, 00:00:00 GMT.

        1) java.util.Date()
        2) java.util.Date(date)

        Args:
            date (long): The milliseconds since January 1, 1970,
                00:00:00 GMT. Optional.

        Returns:
            datetime: A new Date instance.
        """
        import system.date
        if date is None:
            self = system.date.now()
        else:
            self = system.date.fromMillis(date)
        return self


class Locale(object):
    """A Locale object represents a specific geographical, political,
    or cultural region. An operation that requires a Locale to perform
    its task is called locale-sensitive and uses the Locale to tailor
    information for the user. For example, displaying a number is a
    locale-sensitive operation; the number should be formatted
    according to the customs and conventions of the user's native
    country, region, or culture.
    """

    def __init__(self,
                 language,
                 country=None,
                 variant=None):
        """Locale initializer.

        Args:
            language (str): Language code.
            country (str): Country code.
            variant (str): Variant code.
        """
        self.language = language
        self.country = country
        self.variant = variant

    @property
    def English(self):
        return self.__init__('eng')
