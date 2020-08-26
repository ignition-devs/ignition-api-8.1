# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""Provides classes that are fundamental to the design of the Java
programming language."""

__all__ = [
    'Exception',
    'IllegalArgumentException',
    'Object',
    'RuntimeException',
    'Thread',
    'Throwable'
]

from __builtin__ import Exception as PyException


class Object(object):
    """Class Object is the root of the class hierarchy. Every class
    has Object as a superclass. All objects, including arrays,
    implement the methods of this class."""

    def clone(self):
        """Creates and returns a copy of this object.

        Returns:
            object: A copy of this object.
        """
        import copy
        return copy.deepcopy(self)

    def equals(self, obj):
        """Indicates whether some other object is "equal to" this one.

        The equals method implements an equivalence relation on
        non-null object references:

            - It is reflexive: for any non-null reference value x,
            x.equals(x) should return true.
            - It is symmetric: for any non-null reference values x and
            y, x.equals(y) should return true if and only if
            y.equals(x) returns true.
            - It is transitive: for any non-null reference values x,
            y, and z, if x.equals(y) returns true and y.equals(z)
            returns true, then x.equals(z) should return true.
            - It is consistent: for any non-null reference values x
            and y, multiple invocations of x.equals(y) consistently
            return true or consistently return false, provided no
            information used in equals comparisons on the objects is
            modified.
            - For any non-null reference value x, x.equals(null)
            should return false.

        The equals method for class Object implements the most
        discriminating possible equivalence relation on objects; that
        is, for any non-null  reference values x and y, this method
        returns true if and only if x and y refer to the same object
        (x == y has the value true).

        Note that it is generally necessary to override the hashCode
        method whenever this method is overridden, so as to maintain
        the general contract for the hashCode method, which states
        that equal objects must have equal hash codes.

        Args:
            obj (object): The reference object with which to compare.

        Returns:
            bool: true if this object is the same as the obj argument;
                false otherwise.
        """
        print(self, obj)
        return True

    def finalize(self):
        pass

    def getClass(self):
        pass

    def hashCode(self):
        pass

    def notify(self):
        pass

    def notifyAll(self):
        pass

    def toString(self):
        """Returns a string representation of the object. In general,
        the toString method returns a string that "textually
        represents" this object. The result should be a concise but
        informative representation that is easy for a person to read.
        It is recommended that all subclasses override this method.

        Returns:
             str: A string representation of the object.
        """
        return repr(self)

    def wait(self, *args):
        pass


class Throwable(Object, PyException):
    """The Throwable class is the superclass of all errors and
    exceptions in the Java language."""

    def __init__(self, message=None, cause=None):
        """Constructs a new throwable.

        Args:
            message (str): The detail message (which is saved for
                later retrieval by the getMessage() method).
            cause (Throwable): The cause (which is saved for later
                retrieval by the getCause() method). (A null value is
                permitted, and indicated that the cause is nonexistent
                or unknown.).
        """
        PyException.__init__(self, message)
        self._cause = cause

    @property
    def cause(self):
        return self._cause

    def addSuppressed(self, exception):
        pass

    def fillInStackTrace(self):
        pass

    def getCause(self):
        return self.cause

    def getLocalizedMessage(self):
        return self.message

    def getMessage(self):
        return self.message

    def getStackTrace(self):
        pass

    def getSuppressed(self):
        pass

    def initCause(self):
        pass

    def printStackTrace(self):
        pass

    def setStackTrace(self):
        pass

    def toString(self):
        return 'A short description of this throwable.'


class Exception(Throwable):
    """The class Exception and its subclasses are a form of Throwable
    that indicates conditions that a reasonable application might want
    to catch.

    The class Exception and any subclasses that are not also
    subclasses of RuntimeException are checked exceptions. Checked
    exceptions need to be declared in a method or constructor's throws
    clause if they can be thrown by the execution of the method or
    constructor and propagate outside the method or constructor
    boundary."""

    # Static elements
    cause = ''

    def __init__(self, *args):
        super(Exception, self).__init__(*args)

    def getCause(self):
        """Returns the cause of this throwable or null if the cause is
        nonexistent or unknown. (The cause is the throwable that
        caused this throwable to get thrown.)

        Returns:
            str: The cause of this throwable or null if the cause is
                nonexistent or unknown.
        """
        return self.cause


class RuntimeException(Exception):
    """RuntimeException is the superclass of those exceptions that can
    be thrown during the normal operation of the Java Virtual Machine.

    RuntimeException and its subclasses are unchecked exceptions.
    Unchecked exceptions do not need to be declared in a method or
    constructor's throws clause if they can be thrown by the execution
    of the method or constructor and propagate outside the method or
    constructor boundary."""

    def __init__(self, *args):
        super(RuntimeException, self).__init__(*args)


class IllegalArgumentException(RuntimeException):
    """Thrown to indicate that a method has been passed an illegal or
    inappropriate argument."""

    def __init__(self, *args):
        super(IllegalArgumentException, self).__init__(*args)


class Thread(Object):
    """A thread is a thread of execution in a program. The Java
    Virtual Machine allows an application to have multiple threads of
    execution running concurrently.

    Every thread has a name for identification purposes. More than one
    thread may have the same name. If a name is not specified when a
    thread is created, a new name is generated for it.

    Unless otherwise noted, passing a null argument to a constructor
    or method in this class will cause a NullPointerException to be
    thrown.
    """

    @staticmethod
    def sleep(millis):
        """Causes the currently executing thread to sleep (temporarily
        cease execution) for the specified number of milliseconds,
        subject to the precision and accuracy of system timers and
        schedulers. The thread does not lose ownership of any
        monitors.

        Args:
            millis (long): the length of time to sleep in milliseconds.
        """
        import time
        time.sleep(millis // 1000)
