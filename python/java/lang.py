# Copyright (C) 2019
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Provides classes that are fundamental to the design of the Java
programming language."""

__all__ = [
    'Exception',
    'System'
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
        nonexistent or unknown. (The cause is the throwable that
        caused this throwable to get thrown.)

        Returns:
            str: The cause of this throwable or null if the cause is
                nonexistent or unknown.
        """
        return self.cause


class System(object):
    """The System class contains several useful class fields and
    methods. It cannot be instantiated.

    Among the facilities provided by the System class are standard
    input, standard output, and error output streams; access to
    externally defined properties and environment variables; a means
    of loading files and libraries; and a utility method for quickly
    copying a portion of an array.
    """

    @staticmethod
    def currentTimeMillis():
        """Returns the current time in milliseconds. Note that while
        the unit of time of the return value is a millisecond, the
        granularity of the value depends on the underlying operating
        system and may be larger. For example, many operating systems
        measure time in units of tens of milliseconds.

        Returns:
             long: The difference, measured in milliseconds, between
                the current time and midnight, January 1, 1970 UTC.
        """
        import system.date
        return system.date.toMillis(system.date.now())
