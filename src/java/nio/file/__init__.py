__all__ = [
    "CopyOption",
    "DirectoryStream",
    "FileStore",
    "FileVisitOption",
    "Files",
    "LinkOption",
    "OpenOption",
    "Path",
    "Paths",
    "StandardCopyOption",
    "WatchEvent",
    "WatchKey",
    "Watchable",
]

from typing import Any, Iterator, List, Optional, Set, TypeVar, Union

from java.io import BufferedReader, BufferedWriter, InputStream, OutputStream
from java.lang import AutoCloseable, CharSequence, Class, Enum, Object, String
from java.nio.channels import SeekableByteChannel
from java.nio.charset import Charset
from java.nio.file.attribute import (
    BasicFileAttributes,
    FileAttribute,
    FileAttributeView,
    FileStoreAttributeView,
    FileTime,
    PosixFilePermission,
    UserPrincipal,
)
from java.util.function import BiPredicate
from java.util.stream import Stream

T = TypeVar("T")


class CopyOption(object):
    pass


class DirectoryStream(AutoCloseable):
    def close(self):
        # type: () -> None
        pass


class OpenOption(object):
    pass


class Watchable(object):
    def register(self, *args):
        # type: (Any) -> WatchKey
        raise NotImplementedError


class FileStore(Object):
    def getAttribute(self, attribute):
        raise NotImplementedError

    def getBlockSize(self):
        # type: () -> long
        pass

    def getFileStoreAttributeView(self, type):
        # type: (Class) -> FileStoreAttributeView
        raise NotImplementedError

    def getTotalSpace(self):
        # type: () -> long
        raise NotImplementedError

    def getUnallocatedSpace(self):
        # type: () -> long
        raise NotImplementedError

    def getUsableSpace(self):
        # type: () -> long
        raise NotImplementedError

    def isReadOnly(self):
        # type: () -> bool
        raise NotImplementedError

    def name(self):
        # type: () -> String
        raise NotImplementedError

    def supportsFileAttributeView(self, type):
        # type: (Class) -> bool
        raise NotImplementedError

    def type(self):
        # type: () -> String
        raise NotImplementedError


class FileVisitOption(Enum):
    FOLLOW_LINKS = None  # type: FileVisitOption

    @staticmethod
    def values():
        # type: () -> List[FileVisitOption]
        pass


class Files(Object):
    @staticmethod
    def copy(*args):
        # type: (*Any) -> Union[long, Path]
        pass

    @staticmethod
    def createDirectories(dir, *attrs):
        # type: (Path, *FileAttribute) -> Path
        pass

    @staticmethod
    def createDirectory(dir, *attrs):
        # type: (Path, *FileAttribute) -> Path
        pass

    @staticmethod
    def createFile(path, *attrs):
        # type: (Path, *FileAttribute) -> Path
        pass

    @staticmethod
    def createLink(link, existing):
        # type: (Path, Path) -> Path
        pass

    @staticmethod
    def createSymbolicLink(link, target, *attrs):
        # type: (Path, Path, FileAttribute) -> Path
        pass

    @staticmethod
    def createTempDirectory(*args):
        # type: (*Any) -> Path
        pass

    @staticmethod
    def createTempFile(*args):
        # type: (*Any) -> Path
        pass

    @staticmethod
    def delete(path):
        # type: (Path) -> None
        pass

    @staticmethod
    def deleteIfExists(path):
        # type: (Path) -> bool
        pass

    @staticmethod
    def exists(path, *options):
        # type: (Path, *LinkOption) -> bool
        pass

    @staticmethod
    def find(start, maxDepth, matcher, *options):
        # type: (Path, int, BiPredicate, *FileVisitOption) -> Stream
        pass

    @staticmethod
    def getAttribute(path, attribute, *options):
        # type: (Path, String, *LinkOption) -> Object
        pass

    @staticmethod
    def getFileAttributeView(path, type, *options):
        # type: (Path, Class, *LinkOption) -> FileAttributeView
        pass

    @staticmethod
    def getFileStore(path):
        # type: (Path) -> FileStore
        pass

    @staticmethod
    def getLastModifiedTime(path, *options):
        # type: (Path, *LinkOption) -> FileTime
        pass

    @staticmethod
    def getOwner(path, *options):
        # type: (Path, *LinkOption) -> UserPrincipal
        pass

    @staticmethod
    def getPosixFilePermissions(path, *options):
        # type: (Path, *LinkOption) -> Set[PosixFilePermission]
        pass

    @staticmethod
    def isDirectory(path, *options):
        # type: (Path, *LinkOption) -> bool
        pass

    @staticmethod
    def isExecutable(path):
        # type: (Path) -> bool
        pass

    @staticmethod
    def isHidden(path):
        # type: (Path) -> bool
        pass

    @staticmethod
    def isReadable(path):
        # type: (Path) -> bool
        pass

    @staticmethod
    def isRegularFile(path, *options):
        # type: (Path, *LinkOption) -> bool
        pass

    @staticmethod
    def isSameFile(path, path2):
        # type: (Path, Path) -> bool
        pass

    @staticmethod
    def isSymbolicLink(path):
        # type: (Path) -> bool
        pass

    @staticmethod
    def isWritable(path):
        # type: (Path) -> bool
        pass

    @staticmethod
    def lines(path, cs=None):
        # type: (Path, Optional[Charset]) -> Stream
        pass

    @staticmethod
    def list(path):
        # type: (Path) -> Stream
        pass

    @staticmethod
    def move(source, target, *options):
        # type: (Path, Path, *CopyOption) -> Path
        pass

    @staticmethod
    def newBufferedReader(path, cs=None):
        # type: (Path, Optional[Charset]) -> BufferedReader
        pass

    @staticmethod
    def newBufferedWriter(path, *args):
        # type: (Path, *Any) -> BufferedWriter
        pass

    @staticmethod
    def newByteChannel(path, *args):
        # type: (Path, *Any) -> SeekableByteChannel
        pass

    @staticmethod
    def newDirectoryStream(dir, *args):
        # type: (Path, *Any) -> DirectoryStream
        pass

    @staticmethod
    def newInputStream(path, *options):
        # type: (Path, *OpenOption) -> InputStream
        pass

    @staticmethod
    def newOutputStream(path, *options):
        # type: (Path, *OpenOption) -> OutputStream
        pass

    @staticmethod
    def notExists(path, *options):
        # type: (Path, *LinkOption) -> bool
        pass

    @staticmethod
    def probeContentType(path):
        # type: (Path) -> String
        pass

    @staticmethod
    def readAllBytes(path):
        # type: (Path) -> bytearray
        pass

    @staticmethod
    def readAllLines(path, cs=None):
        # type: (Path, Optional[Charset]) -> List[String]
        pass

    @staticmethod
    def readAttributes(path, *args):
        # type: (Path, *Any) -> BasicFileAttributes
        pass

    @staticmethod
    def readString(path, cs=None):
        # type: (Path, Optional[Charset]) -> String
        pass

    @staticmethod
    def readSymbolicLink(link):
        # type: (Path) -> Path
        pass

    @staticmethod
    def setAttribute(path, attribute, value, *options):
        # type: (Path, String, Object, *LinkOption) -> Path
        pass

    @staticmethod
    def setLastModifiedTime(path, time):
        # type: (Path, FileTime) -> Path
        pass

    @staticmethod
    def setOwner(path, owner):
        # type: (Path, UserPrincipal) -> Path
        pass

    @staticmethod
    def setPosixFilePermissions(path, perms):
        # type: (Path, Set[PosixFilePermission]) -> Path
        pass

    @staticmethod
    def size(path):
        # type: (Path) -> long
        pass

    @staticmethod
    def walk(path, *args):
        # type: (Path, *Any) -> Stream
        pass

    @staticmethod
    def walkFileTree(path, *args):
        # type: (Path, *Any) -> Path
        pass

    @staticmethod
    def write(path, *args):
        # type: (Path, *Any) -> Path
        pass

    @staticmethod
    def writeString(path, csq, *args):
        # type: (Path, CharSequence, *Any) -> Path
        pass


class LinkOption(Enum, CopyOption, OpenOption):
    NOFOLLOW_LINKS = None  # type: LinkOption

    @staticmethod
    def values():
        # type: () -> List[LinkOption]
        pass


class Path(Watchable):
    def compareTo(self, other):
        # type: (Path) -> int
        pass

    def endsWith(self, other):
        # type: (Union[Object, Path, String]) -> bool
        pass

    def equals(self, other):
        # type: (Object) -> bool
        pass

    def getFileName(self):
        # type: () -> Path
        pass

    def getName(self, index):
        # type: (int) -> Path
        pass

    def getNameCount(self):
        # type: () -> int
        pass

    def getParent(self):
        # type: () -> Path
        pass

    def getRoot(self):
        # type: () -> Path
        pass

    def hashCode(self):
        # type: () -> int
        pass

    def isAbsolute(self):
        # type: () -> bool
        pass

    def iterator(self):
        # type: () -> Iterator[Path]
        pass

    def normalize(self):
        # type: () -> Path
        pass

    @staticmethod
    def of(*args):
        # type: (Any) -> Path
        pass

    def register(self, *args):
        # type: (Any) -> WatchKey
        pass

    def relativize(self, other):
        # type: (Path) -> Path
        pass

    def resolve(self, other):
        # type: (Union[Path, String]) -> Path
        pass

    def resolveSibling(self, other):
        # type: (Path) -> Path
        pass

    def startsWith(self, other):
        # type: (Path) -> bool
        pass

    def subpath(self, beginIndex, endIndex):
        # type: (int, int) -> Path
        pass

    def toAbsolutePath(self):
        # type: () -> Path
        pass

    def toFile(self):
        # type: () -> Any
        pass

    def toRealPath(self, *args):
        # type: (LinkOption) -> Path
        pass

    def toString(self):
        # type: () -> String
        pass

    def toUri(self):
        # type: () -> Any
        pass


class Paths(Object):
    @staticmethod
    def get(*args):
        # type: (*Any) -> Path
        pass


class StandardCopyOption(Enum, CopyOption, OpenOption):
    ATOMIC_MOVE = None  # type: StandardCopyOption
    COPY_ATTRIBUTES = None  # type: StandardCopyOption
    REPLACE_EXISTING = None  # type: StandardCopyOption

    @staticmethod
    def values():
        # type: () -> List[StandardCopyOption]
        pass


class WatchEvent(object):
    def context(self):
        # type: () -> T
        raise NotImplementedError

    def count(self):
        # type: () -> int
        raise NotImplementedError

    def kind(self):
        # type: () -> WatchEvent.Kind
        raise NotImplementedError

    class Kind(object):
        def name(self):
            # type: () -> String
            raise NotImplementedError

        def type(self):
            # type: () -> Class
            raise NotImplementedError

    class Modifier(object):
        def name(self):
            # type: () -> String
            raise NotImplementedError


class WatchKey(object):
    def cancel(self):
        # type: () -> None
        raise NotImplementedError

    def isValid(self):
        # type: () -> bool
        raise NotImplementedError

    def pollEvents(self):
        # type: () -> List[WatchEvent]
        raise NotImplementedError

    def reset(self):
        # type: () -> bool
        raise NotImplementedError

    def watchable(self):
        # type: () -> Watchable
        raise NotImplementedError
