"""Provides for system input and output through data streams,
serialization and the file system. Unless otherwise noted, passing a
null argument to a constructor or method in any class or interface in
this package will cause a NullPointerException to be thrown.
"""

from __future__ import print_function, unicode_literals

__all__ = [
    "DataOutputStream",
    "FileDescriptor",
    "FileOutputStream",
    "FilterOutputStream",
    "OutputStream",
    "PrintStream",
]

from java.lang import Object


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
        self._out = out


class DataOutputStream(FilterOutputStream):
    _written = 0

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
