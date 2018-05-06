# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Incendium Exceptions module."""

__all__ = [
    'ApplicationError',
    'TagError'
]

UNEXPECTED_ERROR = 'An unexpected error occurred in %s. \n%s'
UNEXPECTED_ERROR_CAUSED_BY = 'An unexpected error occurred in %s. \n%s\nCaused by: %s'


class ApplicationError(Exception):
    """Application Error class."""

    def __init__(self,
                 message,
                 inner_exception,
                 cause=None):
        """Application Error initializer.

        Args:
            message (str): The error message.
            inner_exception (object): The inner Exception.
            cause (str): The cause of the Exception. Optional. Defaults to None.
        """
        super(ApplicationError, self).__init__(message)
        self.inner_exception = inner_exception
        self.cause = cause

    def __repr__(self):
        return "%s(%r, %r, %r)" % (
            self.__class__.__name__,
            repr(self.message),
            self.inner_exception.__repr__(),
            repr(self.cause)
        )

    def __str__(self):
        return repr(self.message)


class TagError(Exception):
    def __init__(self,
                 message):
        super(TagError, self).__init__(message)

    def __repr__(self):
        return "%s(%r)" % (
            self.__class__.__name__,
            repr(self.message)
        )

    def __str__(self):
        return repr(self.message)
