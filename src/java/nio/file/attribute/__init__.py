__all__ = [
    "AttributeView",
    "BasicFileAttributes",
    "FileAttribute",
    "FileAttributeView",
    "FileStoreAttributeView",
    "FileTime",
    "PosixFilePermission",
    "UserPrincipal",
]

from typing import Any, List

from dev.thecesrom.helper.types import AnyStr
from java.lang import Enum, Object
from java.security import Principal
from java.time import Instant
from java.util.concurrent import TimeUnit


class AttributeView(object):
    def name(self):
        # type: () -> AnyStr
        raise NotImplementedError


class BasicFileAttributes(object):
    def creationTime(self):
        # type: () -> FileTime
        raise NotImplementedError

    def fileKey(self):
        # type: () -> Object
        raise NotImplementedError

    def isDirectory(self):
        # type: () -> bool
        raise NotImplementedError

    def isOther(self):
        # type: () -> bool
        raise NotImplementedError

    def isRegularFile(self):
        # type: () -> bool
        raise NotImplementedError

    def isSymbolicLink(self):
        # type: () -> bool
        raise NotImplementedError

    def lastAccessTime(self):
        # type: () -> FileTime
        raise NotImplementedError

    def lastModifiedTime(self):
        # type: () -> FileTime
        raise NotImplementedError

    def size(self):
        # type: () -> long
        raise NotImplementedError


class FileAttribute(object):
    def name(self):
        # type: () -> AnyStr
        pass

    def value(self):
        # type: () -> Any
        pass


class FileAttributeView(AttributeView):
    def name(self):
        # type: () -> AnyStr
        pass


class FileTime(Object):
    def compareTo(self, other):
        # type: (FileTime) -> int
        pass

    @staticmethod
    def fromMillis(value):
        # type: (long) -> FileTime
        pass

    def to(self, unit):
        # type: (TimeUnit) -> long
        pass

    def toInstant(self):
        # type: () -> Instant
        pass

    def toMillis(self):
        # type: () -> long
        pass


class PosixFilePermission(Enum):
    GROUP_EXECUTE = None  # type: PosixFilePermission
    GROUP_READ = None  # type: PosixFilePermission
    GROUP_WRITE = None  # type: PosixFilePermission
    OTHERS_EXECUTE = None  # type: PosixFilePermission
    OTHERS_READ = None  # type: PosixFilePermission
    OTHERS_WRITE = None  # type: PosixFilePermission
    OWNER_EXECUTE = None  # type: PosixFilePermission
    OWNER_READ = None  # type: PosixFilePermission
    OWNER_WRITE = None  # type: PosixFilePermission

    @staticmethod
    def values():
        # type: () -> List[PosixFilePermission]
        pass


class UserPrincipal(Principal):
    def equals(self, another):
        # type: (Object) -> bool
        return True

    def getName(self):
        # type: () -> AnyStr
        pass

    def hashCode(self):
        # type: () -> int
        pass

    def toString(self):
        # type: () -> AnyStr
        pass


class FileStoreAttributeView(AttributeView):
    def name(self):
        # type: () -> AnyStr
        pass
