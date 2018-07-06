# Copyright (C) 2018
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Provides classes that are fundamental to the design of the Java
programming language."""

__all__ = [
    'Exception'
]


class Exception(object):
    """The class Exception and its subclasses are a form of Throwable
    that indicates conditions that a reasonable application might want
    to catch.

    The class Exception and any subclasses that are not also subclasses
    of RuntimeException are checked exceptions. Checked exceptions need
    to be declared in a method or constructor's throws clause if they
    can be thrown by the execution of the method or constructor and
    propagate outside the method or constructor boundary.
    """

    # Static elements
    cause = ''

    def getCause(self):
        """Returns the cause of this throwable or null if the cause is
        nonexistent or unknown. (The cause is the throwable that caused
        this throwable to get thrown.)

        Returns:
            str: The cause of this throwable or null if the cause is
                nonexistent or unknown.
        """
        return self.cause
