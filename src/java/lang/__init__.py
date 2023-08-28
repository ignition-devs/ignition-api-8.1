"""Provides classes that are fundamental to the design of the Java
programming language.
"""

from __future__ import print_function

__all__ = [
    "Appendable",
    "AutoCloseable",
    "CharSequence",
    "Class",
    "Comparable",
    "Enum",
    "Exception",
    "IllegalArgumentException",
    "NullPointerException",
    "Number",
    "Object",
    "Runnable",
    "RuntimeException",
    "StackTraceElement",
    "String",
    "StringBuffer",
    "StringBuilder",
    "Thread",
    "Throwable",
]

import __builtin__ as builtins
import array
import time
from typing import Any, List, Optional, Union

from dev.thecesrom.helper.types import AnyStr
from java.lang.reflect import Type


class Object(object):
    """Class Object is the root of the class hierarchy.

    Every class has Object as a superclass. All objects, including
    arrays, implement the methods of this class.
    """

    def __init__(self):
        # type: () -> None
        super(Object, self).__init__()

    def __cmp__(self, other):
        # type: (Object) -> bool
        return True

    def __ge__(self, other):
        # type: (Object) -> bool
        return True

    def __gt__(self, other):
        # type: (Object) -> bool
        return True

    def __lt__(self, other):
        # type: (Object) -> bool
        return True

    def equals(self, obj):
        # type: (Object) -> bool
        return True

    def getClass(self):
        # type: () -> Class
        pass

    def hashCode(self):
        # type: () -> int
        return hash(self)

    def notify(self):
        # type: () -> None
        pass

    def notifyAll(self):
        # type: () -> None
        pass

    def toString(self):
        # type: () -> AnyStr
        return repr(self)

    def wait(self, timeoutMillis=0, nanos=0):
        # type: (long, int) -> None
        pass


class Appendable(object):
    def append(self, c_csq, start=0, end=-1):
        # type: (Union[CharSequence, str], int, int) -> Appendable
        raise NotImplementedError


class AutoCloseable(object):
    def close(self):
        # type: () -> None
        raise NotImplementedError


class CharSequence(object):
    def charAt(self, index):
        # type: (int) -> str
        raise NotImplementedError

    def chars(self):  # type: ignore[no-untyped-def]
        pass

    def codePoints(self):  # type: ignore[no-untyped-def]
        pass

    @staticmethod
    def compare(cs1, cs2):
        # type: (CharSequence, CharSequence) -> int
        pass

    def length(self):
        # type: () -> int
        raise NotImplementedError

    def subSequence(self, start, end):
        # type: (int, int) -> CharSequence
        raise NotImplementedError

    def toString(self):
        # type: () -> AnyStr
        raise NotImplementedError


class Comparable(object):
    def compareTo(self, o):
        # type: (Any) -> int
        raise NotImplementedError


class Runnable(object):
    def run(self):
        # type: () -> None
        raise NotImplementedError


class Class(Object, Type):
    def asSubClass(self, clazz):
        # type: (Class) -> Any
        pass

    def cast(self, obj):
        # type: (Object) -> Any
        pass

    def getTypeName(self):
        # type: () -> AnyStr
        pass


class Enum(Object):
    def compareTo(self, o):
        # type: (Enum) -> int
        pass

    def getDeclaringClass(self):
        # type: () -> Class
        pass

    def name(self):
        # type: () -> AnyStr
        pass

    def ordinal(self):
        # type: () -> int
        pass

    @staticmethod
    def valueOf(enumType, name):
        # type: (Class, AnyStr) -> Enum
        pass


class Number(Object):
    def byteValue(self):
        # type: () -> int
        pass

    def doubleValue(self):
        # type: () -> float
        raise NotImplementedError

    def floatValue(self):
        # type: () -> float
        raise NotImplementedError

    def intValue(self):
        # type: () -> int
        raise NotImplementedError

    def longValue(self):
        # type: () -> long
        raise NotImplementedError

    def shortValue(self):
        # type: () -> int
        pass


class StackTraceElement(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(StackTraceElement, self).__init__()
        print(args)

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
        return True


class String(unicode):
    def __new__(cls, *args):
        # type: (Any, *Any) -> Any
        print(args)
        return super(String, cls).__new__(cls, *args)

    def __init__(self, *args):
        # type: (*Any) -> None
        super(String, self).__init__(*args)

    def charAt(self, index):
        # type: (int) -> unicode
        pass

    def chars(self):  # type: ignore[no-untyped-def]
        pass

    def codePointAt(self, index):
        # type: (int) -> int
        pass

    def codePointBefore(self, index):
        # type: (int) -> int
        pass

    def codePointCount(self, beginIndex, endIndex):
        # type: (int, int) -> int
        pass

    def codePoints(self):  # type: ignore[no-untyped-def]
        pass

    @staticmethod
    def compare(cs1, cs2):
        # type: (CharSequence, CharSequence) -> int
        pass

    def compareTo(self, anotherString):
        # type: (String) -> int
        pass

    def compareToIgnoreCase(self, arg):
        # type: (String) -> int
        pass

    def concat(self, arg):
        # type: (String) -> String
        pass

    def contains(self, arg):
        # type: (String) -> bool
        pass

    def contentEquals(self, arg):
        # type: (Union[CharSequence, StringBuffer]) -> bool
        pass

    @staticmethod
    def copyValueOf(*args):
        # type: (*Any) -> String
        pass

    def endsWith(self, suffix):
        # type: (String) -> bool
        return self.endswith(suffix)

    def equals(self, anObject):
        # type: (Object) -> bool
        pass

    def equalsIgnoreCase(self, anotherString):
        # type: (String) -> bool
        pass

    def getBytes(self, *args):
        # type: (*Any) -> Optional[object]
        print(args)
        return array.array("b", self)

    def getChars(self, srcBegin, srcEnd, dst, dstBegin):
        # type: (int, int, object, int) -> None
        pass

    def getClass(self):
        # type: () -> Class
        pass

    def hashCode(self):
        # type: () -> int
        return hash(self)

    def indexOf(self, arg, fromIndex=None):
        # type: (Union[int, String], Optional[int]) -> int
        pass

    def intern(self):
        # type: () -> String
        pass

    def isBlank(self):
        # type: () -> bool
        pass

    def isEmpty(self):
        # type: () -> bool
        pass

    def lastIndexOf(self, arg, fromIndex=None):
        # type: (Union[int, String], Optional[int]) -> int
        pass

    def length(self):
        # type: () -> int
        return len(self)

    def lines(self):  # type: ignore[no-untyped-def]
        pass

    def matches(self, regex):
        # type: (String) -> bool
        pass

    def notify(self):
        # type: () -> None
        pass

    def notifyAll(self):
        # type: () -> None
        pass

    def offsetByCodePoints(self, index, codePointOffset):
        # type: (int, int) -> int
        pass

    def regionMatches(self, *args):
        # type: (*Any) -> bool
        pass

    def repeat(self, count):
        # type: (int) -> String
        pass

    def replaceAll(self, regex, replacement):
        # type: (String, String) -> String
        pass

    def replaceFirst(self, regex, replacement):
        # type: (String, String) -> String
        pass

    def startsWith(self, prefix, offset=0):
        # type: (String, int) -> bool
        return self.startswith(prefix, offset)

    def stripLeading(self):
        # type: () -> String
        pass

    def stripTrailing(self):
        # type: () -> String
        pass

    def subSequence(self, start, end):
        # type: (int, int) -> CharSequence
        pass

    def substring(self, beginIndex, endIndex=None):
        # type: (int, Optional[int]) -> String
        pass

    def toCharArray(self):
        # type: () -> object
        return array.array("c", self)

    def toLowerCase(self, locale=None):
        # type: (Optional[Any]) -> String
        print(locale)
        return String(self.lower())

    def toString(self):
        # type: () -> unicode
        return unicode(self)

    def toUpperCase(self):
        # type: () -> String
        return String(self.upper())

    @staticmethod
    def valueOf(*args):
        # type: (*Any) -> String
        pass

    def wait(self, timeoutMillis=0, nanos=0):
        # type: (long, int) -> None
        pass


class StringBuffer(Object, CharSequence):
    def __init__(self, *args):
        # type: (Any) -> None
        super(StringBuffer, self).__init__()
        print(args)

    def append(self, *args):
        # type: (Any) -> StringBuffer
        pass

    def appendCodePoint(self, codePoint):
        # type: (int) -> StringBuffer
        pass

    def capacity(self):
        # type: () -> int
        pass

    def charAt(self, index):
        # type: (int) -> str
        pass

    def codePointAt(self, index):
        # type: (int) -> int
        pass

    def codePointBefore(self, index):
        # type: (int) -> int
        pass

    def codePointCount(self, beginIndex, endIndex):
        # type: (int, int) -> int
        pass

    def compareTo(self, another):
        # type: (StringBuffer) -> int
        pass

    def delete(self, start, end):
        # type: (int, int) -> StringBuffer
        pass

    def deleteCharAt(self, index):
        # type: (int) -> StringBuffer
        pass

    def ensureCapacity(self, minimumCapacity):
        # type: (int) -> None
        pass

    def getChars(self, srcBegin, srcEnd, dst, dstBegin):
        # type: (int, int, str, int) -> None
        pass

    def indexOf(self, string, fromIndex=0):
        # type: (str, int) -> int
        pass

    def insert(self, *args):
        # type: (Any) -> StringBuffer
        pass

    def lastIndexOf(self, string, fromIndex=0):
        # type: (str, int) -> int
        pass

    def length(self):
        # type: () -> int
        pass

    def offsetByCodePoints(self, index, codePointOffset):
        # type: (int, int) -> int
        pass

    def replace(self, start, end, string):
        # type: (int, int, str) -> StringBuffer
        pass

    def reverse(self):
        # type: () -> StringBuffer
        pass

    def setCharAt(self, index, ch):
        # type: (int, str) -> None
        pass

    def setLength(self, newLength):
        # type: (int) -> None
        pass

    def subSequence(self, start, end):
        # type: (int, int) -> CharSequence
        pass

    def substring(self, start, end=-1):
        # type: (int, int) -> str
        pass

    def trimToSize(self):
        # type: () -> None
        pass


class StringBuilder(Object, CharSequence):
    def __init__(self, *args):
        # type: (Any) -> None
        super(StringBuilder, self).__init__()
        print(args)

    def append(self, *args):
        # type: (Any) -> StringBuilder
        pass

    def capacity(self):
        # type: () -> int
        pass

    def charAt(self, index):
        # type: (int) -> str
        pass

    def codePointAt(self, index):
        # type: (int) -> int
        pass

    def codePointBefore(self, index):
        # type: (int) -> int
        pass

    def codePointCount(self, beginIndex, endIndex):
        # type: (int, int) -> int
        pass

    def compareTo(self, another):
        # type: (StringBuilder) -> int
        pass

    def delete(self, start, end):
        # type: (int, int) -> StringBuilder
        pass

    def deleteCharAt(self, index):
        # type: (int) -> StringBuilder
        pass

    def ensureCapacity(self, minimumCapacity):
        # type: (int) -> None
        pass

    def getChars(self, srcBegin, srcEnd, dst, dstBegin):
        # type: (int, int, str, int) -> None
        pass

    def indexOf(self, str_, fromIndex=0):
        # type: (AnyStr, int) -> int
        pass

    def insert(self, *args):
        # type: (Any) -> StringBuilder
        pass

    def lastIndexOf(self, str_, fromIndex=0):
        # type: (AnyStr, int) -> int
        pass

    def length(self):
        # type: () -> int
        pass

    def offsetByCodePoints(self, index, codePointOffset):
        # type: (int, int) -> int
        pass

    def replace(self, start, end, str_):
        # type: (int, int, int) -> StringBuilder
        pass

    def reverse(self):
        # type: () -> StringBuilder
        pass

    def setCharAt(self, index, ch):
        # type: (int, str) -> None
        pass

    def setLength(self, newLength):
        # type: (int) -> None
        pass

    def subSequence(self, start, end):
        # type: (int, int) -> CharSequence
        pass

    def substring(self, start, end=-1):
        # type: (int, int) -> AnyStr
        pass

    def trimToSize(self):
        # type: () -> None
        pass


class Throwable(Object, builtins.Exception):
    """The Throwable class is the superclass of all errors and
    exceptions in the Java language.
    """

    def __init__(self, message=None, cause=None):
        # type: (Optional[str], Optional[Throwable]) -> None
        super(Throwable, self).__init__()
        self._cause = cause
        self._message = message
        builtins.Exception.__init__(self, message)

    @property
    def cause(self):
        # type: () -> Throwable
        return Throwable()

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
        # type: () -> List[StackTraceElement]
        pass

    def getSuppressed(self):
        # type: () -> List[Throwable]
        pass

    def initCause(self, cause=None):
        # type: (Optional[Throwable]) -> None
        pass

    @property
    def message(self):
        # type: () -> str
        return "message"

    def printStackTrace(self, *args):
        # type: (Any) -> None
        pass

    def setStackTrace(self, stackTrace):
        # type: (List[StackTraceElement]) -> None
        pass

    def toString(self):
        # type: () -> AnyStr
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
        # type: (Optional[str], Optional[Throwable]) -> None
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
        # type: (Optional[str], Optional[Throwable]) -> None
        super(RuntimeException, self).__init__(message, cause)


class IllegalArgumentException(RuntimeException):
    """Thrown to indicate that a method has been passed an illegal or
    inappropriate argument.
    """

    def __init__(self, message=None, cause=None):
        # type: (Optional[str], Optional[Throwable]) -> None
        super(IllegalArgumentException, self).__init__(message, cause)


class NullPointerException(RuntimeException):
    """Thrown when an application attempts to use null in a case where
    an object is required.
    """

    def __init__(self, message=None, cause=None):
        # type: (Optional[str], Optional[Throwable]) -> None
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
        # type: (long) -> None
        time.sleep(millis // 1000)
