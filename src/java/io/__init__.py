"""Provides for system input and output through data streams,
serialization and the file system. Unless otherwise noted, passing a
null argument to a constructor or method in any class or interface in
this package will cause a NullPointerException to be thrown.
"""

from __future__ import print_function

__all__ = [
    "DataOutputStream",
    "FileDescriptor",
    "FileOutputStream",
    "FilterOutputStream",
    "OutputStream",
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
    _out = None

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
