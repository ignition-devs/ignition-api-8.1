# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Exceptions module."""

__all__ = [
    'ApplicationError',
    'TagError'
]


class ApplicationError(Exception):
    """Application Error class."""

    def __init__(self,
                 message,
                 inner_exception=None,
                 cause=None):
        """Application Error initializer.

        Args:
            message (str): The error message.
            inner_exception (object): The inner Exception. Optional.
            cause (str): The cause of the Exception. Optional.
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
