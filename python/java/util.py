# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Contains the collections framework, legacy collection classes,
event model, date and time facilities, internationalization, and
miscellaneous utility classes (a string tokenizer, a random-number
generator, and a bit array)."""

__all__ = [
    'Date',
    'EventObject',
    'Locale'
]

from java.lang import Object


class Date(Object):
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
        return (system.date.now()
                if date is None
                else system.date.fromMillis(date))


class EventObject(Object):
    """The root class from which all event state objects shall be
    derived.

    All Events are constructed with a reference to the object, the
    "source", that is logically deemed to be the object upon which the
    Event in question initially occurred upon."""

    def __init__(self, source):
        self.source = source

    def getSource(self):
        return self.source


class Locale(Object):
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

    def Builder(self):
        pass

    @property
    def CANADA(self):
        return self.__init__('en', 'CA')

    @property
    def CANADA_FRENCH(self):
        return self.__init__('fr', 'CA')

    @property
    def CHINA(self):
        return self.__init__('zh', 'CN')

    @property
    def CHINESE(self):
        return self.__init__('zh')

    @property
    def ENGLISH(self):
        return self.__init__('en')

    @property
    def FRANCE(self):
        return self.__init__('fr', 'FR')

    @property
    def FRENCH(self):
        return self.__init__('fr')

    @property
    def GERMAN(self):
        return self.__init__('de')

    @property
    def GERMANY(self):
        return self.__init__('de', 'DE')

    @property
    def ITALIAN(self):
        return self.__init__('it')

    @property
    def ITALY(self):
        return self.__init__('it', 'IT')

    @property
    def JAPAN(self):
        return self.__init__('jp', 'JP')

    @property
    def JAPANESE(self):
        return self.__init__('jp')

    @property
    def KOREA(self):
        return self.__init__('ko', 'KR')

    @property
    def KOREAN(self):
        return self.__init__('ko')

    @property
    def PRC(self):
        return self.CHINA

    @property
    def SIMPLIFIED_CHINESE(self):
        return self.CHINA

    @property
    def TAIWAN(self):
        return self.__init__('zh', 'TW')

    @property
    def TRADITIONAL_CHINESE(self):
        return self.__init__('zh', 'TW')

    @property
    def UK(self):
        return self.__init__('en', 'GB')

    @property
    def US(self):
        return self.__init__('en', 'US')
