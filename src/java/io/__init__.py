"""Provides for system input and output through data streams,
serialization and the file system. Unless otherwise noted, passing a
null argument to a constructor or method in any class or interface in
this package will cause a NullPointerException to be thrown.
"""

from __future__ import print_function

__all__ = [
    "Closeable",
    "DataOutputStream",
    "FileDescriptor",
    "FileOutputStream",
    "FilterOutputStream",
    "Flushable",
    "InputStream",
    "OutputStream",
    "PrintStream",
    "PrintWriter",
    "Writer",
]

from typing import Any, Union

from java.lang import Appendable, AutoCloseable, CharSequence, Object


class Closeable(AutoCloseable):
    def close(self):
        # type: () -> None
        raise NotImplementedError


class FileDescriptor(Object):
    def sync(self):
        pass

    def valid(self):
        pass


class OutputStream(Object):
    def close(self):
        pass

    def flush(self):
        pass

    @staticmethod
    def nullOutputStream():
        return OutputStream()

    def write(self, *args):
        pass


class FileOutputStream(OutputStream):
    def __init__(self, *args):
        pass

    def getChannel(self):
        pass

    def getFD(self):
        print(self)
        return FileDescriptor()


class FilterOutputStream(OutputStream):
    _out = OutputStream()

    def __init__(self, out):
        # type: (OutputStream) -> None
        self._out = out


class DataOutputStream(FilterOutputStream):
    out = None  # type: OutputStream
    written = 0  # type: int

    def __init__(self, out):
        self.out = out
        super(DataOutputStream, self).__init__(out)

    def size(self):
        pass

    def writeBoolean(self, v):
        pass

    def writeByte(self, v):
        pass

    def writeBytes(self, s):
        pass

    def writeChar(self, v):
        pass

    def writeChars(self, s):
        pass

    def writeDouble(self, v):
        pass

    def writeFloat(self, v):
        pass

    def writeInt(self, v):
        pass

    def writeLong(self, v):
        pass

    def writeShort(self, v):
        pass

    def writeUTF(self, s):
        pass


class PrintStream(FilterOutputStream):
    _out = OutputStream()

    def __init__(self, *args):
        print(args)
        super(PrintStream, self).__init__(self._out)

    def append(self, *args):
        pass

    def checkError(self):
        pass

    def clearError(self):
        pass

    def format(self, *args):
        pass

    def print(self, arg):
        pass

    def printf(self, *args):
        pass

    def println(self, arg):
        pass

    def setError(self):
        pass


class Flushable(object):
    def flush(self):
        raise NotImplementedError


class InputStream(Object):
    def available(self):
        pass

    def close(self):
        pass

    def mark(self, readlimit):
        pass

    def markSupported(self):
        pass

    def nullInputStream(self):
        pass

    def read(self, *args):
        pass

    def readAllBytes(self):
        pass

    def readNBytes(self, *args):
        pass

    def reset(self):
        pass

    def skip(self, n):
        pass

    def transferTo(self, out):
        pass


class Writer(Object, Appendable, Closeable, Flushable):
    def append(self, c_csq, start=0, end=-1):
        # type: (Union[CharSequence, str], int, int) -> Writer
        pass

    def close(self):
        # type: () -> None
        pass

    def flush(self):
        # type: () -> None
        pass

    @staticmethod
    def nullWriter():
        # type: () -> Writer
        pass

    def write(self, *args):
        # type: (Any) -> None
        pass


class PrintWriter(Writer):
    def __init__(self, *args):
        # type: (Any) -> None
        pass

    def append(self, c_csq, start=0, end=-1):
        # type: (Union[CharSequence, str], int, int) -> PrintWriter
        pass

    def checkError(self):
        # type: () -> bool
        pass

    def format(self, *args):
        # type: (Any) -> PrintWriter
        pass

    def print(self, arg):
        # type: (Any) -> None
        pass

    def printf(self, *args):
        # type: (Any) -> PrintWriter
        pass

    def println(self, arg):
        # type: (Any) -> None
        pass

    def write(self, *args):
        # type: (Any) -> None
        pass
