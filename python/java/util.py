# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Contains the collections framework, legacy collection classes,
event model, date and time facilities, internationalization, and
miscellaneous utility classes (a string tokenizer, a random-number
generator, and a bit array)."""

__all__ = [
    'Locale'
]


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
