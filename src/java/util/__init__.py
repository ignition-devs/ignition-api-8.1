"""Contains the collections framework, legacy collection classes, event
model, date and time facilities, internationalization, and miscellaneous
utility classes (a string tokenizer, a random-number generator, and a
bit array).
"""

__all__ = ["Date", "EventObject", "Locale"]

from java.lang import Object


class Date(Object):
    """The class Date represents a specific instant in time, with
    millisecond precision.
    """

    def __init__(self, date=None):
        print(self, date)

    def after(self, when):
        pass

    def before(self, when):
        pass

    def compareTo(self, anotherDate):
        pass


class EventObject(Object):
    """The root class from which all event state objects shall be
    derived.

    All Events are constructed with a reference to the object, the
    "source", that is logically deemed to be the object upon which the
    Event in question initially occurred upon.
    """

    def __init__(self, source):
        self.source = source

    def getSource(self):
        return self.source


class ClassProperty(property):
    def __get__(self, cls, owner):
        return classmethod(self.fget).__get__(None, owner)()


class Locale(Object):
    """A Locale object represents a specific geographical, political, or
    cultural region. An operation that requires a Locale to perform its
    task is called locale-sensitive and uses the Locale to tailor
    information for the user. For example, displaying a number is a
    locale-sensitive operation; the number should be formatted according
    to the customs and conventions of the user's native country, region,
    or culture.
    """

    def __init__(self, language, country=None, variant=None):
        self.language = language
        self.country = country
        self.variant = variant

    def __repr__(self):
        return "{!r}".format(self.__str__())

    def __str__(self):
        ret = self.language
        if self.country:
            ret += "_{}".format(self.country)
        if self.variant:
            ret += "_{}".format(self.variant)
        return unicode(ret)

    @ClassProperty
    def CANADA(self):
        return Locale("en", "CA")

    @ClassProperty
    def CANADA_FRENCH(self):
        return Locale("fr", "CA")

    @ClassProperty
    def CHINA(self):
        return Locale("zh", "CN")

    @ClassProperty
    def CHINESE(self):
        return Locale("zh")

    @ClassProperty
    def ENGLISH(self):
        return Locale("en")

    @ClassProperty
    def FRANCE(self):
        return Locale("fr", "FR")

    @ClassProperty
    def FRENCH(self):
        return Locale("fr")

    @ClassProperty
    def GERMAN(self):
        return Locale("de")

    @ClassProperty
    def GERMANY(self):
        return Locale("de", "DE")

    @ClassProperty
    def ITALIAN(self):
        return Locale("it")

    @ClassProperty
    def ITALY(self):
        return Locale("it", "IT")

    @ClassProperty
    def JAPAN(self):
        return Locale("ja", "JP")

    @ClassProperty
    def JAPANESE(self):
        return Locale("ja")

    @ClassProperty
    def KOREA(self):
        return Locale("ko", "KR")

    @ClassProperty
    def KOREAN(self):
        return Locale("ko")

    @ClassProperty
    def PRC(self):
        return self.CHINA

    @ClassProperty
    def SIMPLIFIED_CHINESE(self):
        return self.CHINA

    @ClassProperty
    def TAIWAN(self):
        return Locale("zh", "TW")

    @ClassProperty
    def TRADITIONAL_CHINESE(self):
        return Locale("zh", "TW")

    @ClassProperty
    def UK(self):
        return Locale("en", "GB")

    @ClassProperty
    def US(self):
        return Locale("en", "US")
