"""Provides classes that are fundamental to the design of the Java
programming language.
"""

from __future__ import print_function

__all__ = [
    "Class",
    "Enum",
    "Exception",
    "IllegalArgumentException",
    "Iterable",
    "Object",
    "RuntimeException",
    "StackTraceElement",
    "Thread",
    "Throwable",
]

import __builtin__ as builtins
import copy
import time


class Object(object):
    """Class Object is the root of the class hierarchy. Every class has
    Object as a superclass. All objects, including arrays, implement the
    methods of this class.
    """

    def clone(self):
        return copy.deepcopy(self)

    def equals(self, obj):
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
        return repr(self)

    def wait(self, timeoutMillis=0, nanos=0):
        # type: (long, int) -> None
        pass


class Class(Object):
    def asSubClass(self, clazz):
        pass

    def cast(self, obj):
        pass


class Enum(Object):
    def compareTo(self, o):
        pass

    def getDeclaringClass(self):
        pass

    def name(self):
        pass

    def ordinal(self):
        pass

    def valueOf(self, enumType, name):
        pass


class Iterable(object):
    """Implementing this interface allows an object to be the target of
    the enhanced for statement (sometimes called the "for-each loop"
    statement).
    """

    def __iter__(self):
        pass

    def forEach(self, action):
        pass

    def iterator(self):
        raise NotImplementedError

    def spliterator(self):
        pass


class StackTraceElement(Object):
    def __init__(self, *args):
        pass

    def getClassLoaderName(self):
        # type: () -> str
        pass

    def getClassName(self):
        # type: () -> str
        pass

    def getFileName(self):
        # type: () -> str
        pass

    def getLineNumber(self):
        # type: () -> int
        pass

    def getMethodName(self):
        # type: () -> str
        pass

    def getModuleName(self):
        # type: () -> str
        pass

    def getModuleVersion(self):
        # type: () -> str
        pass

    def isNativeMethod(self):
        # type: () -> bool
        pass


class Throwable(Object, builtins.Exception):
    """The Throwable class is the superclass of all errors and
    exceptions in the Java language.
    """

    def __init__(self, message=None, cause=None):
        # type: (str, Throwable) -> None
        self._cause = cause
        self._message = message
        builtins.Exception.__init__(self, message)

    @property
    def cause(self):
        # type: () -> Throwable
        pass

    def addSuppressed(self, exception):
        # type: (Throwable) -> None
        pass

    def fillInStackTrace(self):
        # type: () -> Throwable
        pass

    def getCause(self):
        # type: () -> Throwable
        return self.cause

    def getLocalizedMessage(self):
        # type: () -> str
        return self.message

    def getMessage(self):
        # type: () -> str
        pass

    def getStackTrace(self):
        pass

    def getSuppressed(self):
        pass

    def initCause(self, cause=None):
        # type: (Throwable) -> None
        pass

    @property
    def message(self):
        # type: () -> str
        pass

    def printStackTrace(self, *args):
        pass

    def setStackTrace(self, stackTrace):
        pass

    def toString(self):
        return "A short description of this throwable."


class Exception(Throwable):
    """The class Exception and its subclasses are a form of Throwable
    that indicates conditions that a reasonable application might want
    to catch.

    The class Exception and any subclasses that are not also subclasses
    of RuntimeException are checked exceptions. Checked exceptions need
    to be declared in a method or constructor's throws clause if they
    can be thrown by the execution of the method or constructor and
    propagate outside the method or constructor boundary.
    """

    def __init__(self, message=None, cause=None):
        # type: (str, Throwable) -> None
        super(Exception, self).__init__(message, cause)


class RuntimeException(Exception):
    """RuntimeException is the superclass of those exceptions that can
    be thrown during the normal operation of the Java Virtual Machine.

    RuntimeException and its subclasses are unchecked exceptions.
    Unchecked exceptions do not need to be declared in a method or
    constructor's throws clause if they can be thrown by the execution
    of the method or constructor and propagate outside the method or
    constructor boundary.
    """

    def __init__(self, message=None, cause=None):
        # type: (str, Throwable) -> None
        super(RuntimeException, self).__init__(message, cause)


class IllegalArgumentException(RuntimeException):
    """Thrown to indicate that a method has been passed an illegal or
    inappropriate argument.
    """

    def __init__(self, message=None, cause=None):
        # type: (str, Throwable) -> None
        super(IllegalArgumentException, self).__init__(message, cause)


class NullPointerException(RuntimeException):
    """Thrown when an application attempts to use null in a case where
    an object is required.
    """

    def __init__(self, message=None, cause=None):
        # type: (str, Throwable) -> None
        super(NullPointerException, self).__init__(message, cause)


class Thread(Object):
    """A thread is a thread of execution in a program. The Java Virtual
    Machine allows an application to have multiple threads of execution
    running concurrently.

    Every thread has a name for identification purposes. More than one
    thread may have the same name. If a name is not specified when a
    thread is created, a new name is generated for it.

    Unless otherwise noted, passing a null argument to a constructor or
    method in this class will cause a NullPointerException to be thrown.
    """

    @staticmethod
    def sleep(millis):
        time.sleep(millis // 1000)
