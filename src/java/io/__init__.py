"""Provides for system input and output through data streams,
serialization and the file system. Unless otherwise noted, passing a
null argument to a constructor or method in any class or interface in
this package will cause a NullPointerException to be thrown.
"""

from __future__ import print_function

__all__ = [
    "BufferedReader",
    "BufferedWriter",
    "Closeable",
    "DataOutputStream",
    "File",
    "FileDescriptor",
    "FileOutputStream",
    "FilterOutputStream",
    "Flushable",
    "IOException",
    "InputStream",
    "OutputStream",
    "PrintStream",
    "PrintWriter",
    "Reader",
    "Writer",
]

from typing import Any, Optional, Union

from java.lang import (
    Appendable,
    AutoCloseable,
    CharSequence,
    Exception,
    Object,
    String,
    Throwable,
)


class Closeable(AutoCloseable):
    def close(self):
        # type: () -> None
        raise NotImplementedError


class Flushable(object):
    def flush(self):
        # type: () -> None
        raise NotImplementedError


class File(Object):
    pathSeparator = None  # type: String
    pathSeparatorChar = None  # type: String
    separator = None  # type: String
    separatorChar = None  # type: String

    def __init__(self, *args):
        # type: (Any) -> None
        pass


class FileDescriptor(Object):
    def sync(self):
        # type: () -> None
        pass

    def valid(self):
        # type: () -> bool
        pass


class OutputStream(Object, Closeable, Flushable):
    def close(self):
        # type: () -> None
        pass

    def flush(self):
        # type: () -> None
        pass

    @staticmethod
    def nullOutputStream():
        # type: () -> OutputStream
        pass

    def write(self, *args):
        # type: (Any) -> None
        pass


class FileOutputStream(OutputStream):
    def __init__(self, *args):
        # type: (Any) -> None
        pass

    def getChannel(self):
        # type: () -> Any
        pass

    def getFD(self):
        # type: () -> FileDescriptor
        pass


class FilterOutputStream(OutputStream):
    _out = None  # type: OutputStream

    def __init__(self, out):
        # type: (OutputStream) -> None
        self._out = out


class DataOutputStream(FilterOutputStream):
    out = None  # type: OutputStream

    def __init__(self, out):
        # type: (OutputStream) -> None
        self.out = out
        super(DataOutputStream, self).__init__(out)

    def size(self):
        # type: () -> int
        pass

    def writeBoolean(self, v):
        # type: (bool) -> None
        pass

    def writeByte(self, v):
        # type: (int) -> None
        pass

    def writeBytes(self, s):
        # type: (String) -> None
        pass

    def writeChar(self, v):
        # type: (int) -> None
        pass

    def writeChars(self, s):
        # type: (String) -> None
        pass

    def writeDouble(self, v):
        # type: (float) -> None
        pass

    def writeFloat(self, v):
        # type: (float) -> None
        pass

    def writeInt(self, v):
        # type: (int) -> None
        pass

    def writeLong(self, v):
        # type: (long) -> None
        pass

    def writeShort(self, v):
        # type: (int) -> None
        pass

    def writeUTF(self, s):
        # type: (String) -> None
        pass


class PrintStream(FilterOutputStream):
    _out = OutputStream()

    def __init__(self, *args):
        # type: (Any) -> None
        print(args)
        super(PrintStream, self).__init__(self._out)

    def append(self, *args):
        # type: (Any) -> PrintStream
        pass

    def checkError(self):
        # type: () -> bool
        pass

    def format(self, *args):
        # type: (Any) -> PrintStream
        pass

    def print(self, arg):
        # type: (Any) -> None
        pass

    def printf(self, *args):
        # type: (Any) -> None
        pass

    def println(self, arg):
        # type: (Any) -> None
        pass


class InputStream(Object, Closeable):
    def available(self):
        # type: () -> int
        pass

    def close(self):
        # type: () -> None
        pass

    def mark(self, readlimit):
        # type: (int) -> None
        pass

    def markSupported(self):
        # type: () -> bool
        pass

    @staticmethod
    def nullInputStream():
        # type: () -> InputStream
        pass

    def read(self, *args):
        # type: (Any) -> int
        pass

    def readAllBytes(self):
        # type: () -> bytearray
        pass

    def readNBytes(self, *args):
        # type: (Any) -> int
        pass

    def reset(self):
        # type: () -> None
        pass

    def skip(self, n):
        # type: (long) -> long
        pass

    def transferTo(self, out):
        # type: (OutputStream) -> long
        pass


class IOException(Exception):
    def __init__(self, message=None, cause=None):
        # type: (Optional[str], Optional[Throwable]) -> None
        super(IOException, self).__init__(message, cause)


class Reader(Object, AutoCloseable):
    def close(self):
        # type: () -> None
        raise NotImplementedError

    def mark(self, readAheadLimit):
        # type: (int) -> None
        pass

    def markSupported(self):
        # type: () -> bool
        pass

    @staticmethod
    def nullReader():
        # type: () -> Reader
        pass

    def read(self, *args):
        # type: (Any) -> int
        pass

    def ready(self):
        # type: () -> bool
        pass

    def reset(self):
        # type: () -> None
        pass

    def skip(self, n):
        # type: (long) -> long
        pass

    def transferTo(self, out):
        # type: (Writer) -> long
        pass


class BufferedReader(Reader):
    def __init__(self, in_, sz=None):
        # type: (Reader, Optional[int]) -> None
        print(in_, sz)

    def close(self):
        # type: () -> None
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


class BufferedWriter(Writer):
    def __init__(self, out, sz=None):
        # type: (Writer, Optional[int]) -> None
        print(out, sz)


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
