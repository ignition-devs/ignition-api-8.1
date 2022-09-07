__all__ = [
    "Channel",
    "FileChannel",
    "SeekableByteChannel",
    "SelectableChannel",
    "SelectionKey",
    "Selector",
    "SocketChannel",
]

from typing import Any, Optional, Set, TypeVar, Union

from java.lang import AutoCloseable, Object
from java.nio import ByteBuffer, MappedByteBuffer
from java.util.function import Consumer

T = TypeVar("T")


class Channel(AutoCloseable):
    def close(self):
        # type: () -> None
        pass

    def isOpen(self):
        # type: () -> bool
        pass


class ReadableByteChannel(Channel):
    def read(self, dst):
        # type: (ByteBuffer) -> int
        pass


class WriteableByteChannel(Channel):
    def write(self, src):
        # type: (ByteBuffer) -> int
        pass


class FileChannel(Object, Channel):
    def force(self, metaData):
        # type: (bool) -> None
        pass

    def lock(self):
        # type: () -> FileLock
        pass

    def map(self, mode, position, size):
        # type: (FileChannel.MapMode, long, long) -> MappedByteBuffer
        raise NotImplementedError

    @staticmethod
    def open(*args):
        # type: (*Any) -> FileChannel
        pass

    def position(self, newPosition=None):
        # type: (Optional[long]) -> Union[FileChannel, long]
        pass

    def read(self, *args):
        # type: (Any) -> Union[int, long]
        pass

    def size(self):
        # type: () -> long
        pass

    def transferFrom(self, src, position, count):
        # type: (ReadableByteChannel, long, long) -> long
        pass

    def transferTo(self, position, count, target):
        # type: (long, long, WriteableByteChannel) -> long
        pass

    def truncate(self, size):
        # type: (long) -> FileChannel
        pass

    def tryLock(
        self,
        position=None,  # type: Optional[long]
        size=None,  # type: Optional[long]
        shared=None,  # type: Optional[bool]
    ):
        # type: (...) -> FileLock
        pass

    def write(self, *args):
        # type: (Any) -> Union[int, long]
        pass

    class MapMode(Object):
        PRIVATE = None  # type: FileChannel.MapMode
        READ_ONLY = None  # type: FileChannel.MapMode
        READ_WRITE = None  # type: FileChannel.MapMode


class FileLock(Object, AutoCloseable):
    def acquiredBy(self):
        # type: () -> Channel
        pass

    def channel(self):
        # type: () -> FileChannel
        pass

    def close(self):
        # type: () -> None
        pass

    def isShared(self):
        # type: () -> bool
        pass

    def isValid(self):
        # type: () -> bool
        raise NotImplementedError

    def overlaps(self, position, size):
        # type: (long, long) -> bool
        pass

    def position(self):
        # type: () -> long
        pass

    def release(self):
        # type: () -> None
        raise NotImplementedError

    def size(self):
        # type: () -> long
        pass


class SeekableByteChannel(ReadableByteChannel, WriteableByteChannel):
    def position(self, newPosition=None):
        # type: (Optional[long]) -> Union[long, SeekableByteChannel]
        pass

    def size(self):
        # type: () -> long
        pass

    def truncate(self, size):
        # type: (long) -> SeekableByteChannel
        pass


class SelectableChannel(Object, AutoCloseable):
    def close(self):
        # type: () -> None
        pass

    def blockingLock(self):
        # type: () -> Object
        pass

    def configureBlocking(self):
        # type: () -> SelectableChannel
        pass

    def isBlocking(self):
        # type: () -> bool
        pass

    def isRegistered(self):
        # type: () -> bool
        pass

    def keyFor(self, sel):
        # type: (Selector) -> SelectionKey
        pass

    def provider(self):
        # type: () -> Object
        pass

    def register(self, sel, ops, att=None):
        # type: (Selector, int, Optional[Object]) -> SelectionKey
        pass

    def validOps(self):
        # type: () -> int
        pass


class SelectionKey(Object):
    OP_ACCEPT = None  # type: int
    OP_CONNECT = None  # type: int
    OP_READ = None  # type: int
    OP_WRITE = None  # type: int

    def attach(self, ob):
        # type: (Object) -> Object
        pass

    def attachment(self):
        # type: () -> Object
        pass

    def cancel(self):
        # type: () -> None
        pass

    def channel(self):
        # type: () -> SelectableChannel
        pass

    def interestOps(self, ops=None):
        # type: (Optional[int]) -> Union[int, SelectionKey]
        pass

    def interestOpsAnd(self, ops):
        # type: (int) -> int
        pass

    def interestOpsOr(self, ops):
        # type: (int) -> int
        pass

    def isAcceptable(self):
        # type: () -> bool
        pass

    def isConnectable(self):
        # type: () -> bool
        pass

    def isReadable(self):
        # type: () -> bool
        pass

    def isValid(self):
        # type: () -> bool
        pass

    def isWriteable(self):
        # type: () -> bool
        pass

    def readyOps(self):
        # type: () -> int
        pass

    def selector(self):
        # type: () -> Selector
        pass


class Selector(Object, AutoCloseable):
    def close(self):
        # type: () -> None
        pass

    def isOpen(self):
        # type: () -> bool
        pass

    def keys(self):
        # type: () -> Set[SelectionKey]
        pass

    @staticmethod
    def open():
        # type: () -> Selector
        pass

    def provider(self):
        # type: () -> Object
        pass

    def select(self, *args):
        # type: (Any) -> int
        pass

    def selectedKeys(self):
        # type: () -> Set[SelectionKey]
        pass

    def selectNow(self, action=None):
        # type: (Optional[Consumer]) -> int
        pass

    def wakeup(self):
        # type: () -> Selector
        pass


class SocketChannel(SelectableChannel):
    def bind(self, local):
        # type: (Any) -> SocketChannel
        pass

    def connect(self, remote):
        # type: (Any) -> bool
        pass

    def finishConnect(self):
        # type: () -> bool
        pass

    def getLocalAddress(self):
        # type: () -> Any
        pass

    def getRemoteAddress(self):
        # type: () -> Any
        pass

    def isConnected(self):
        # type: () -> bool
        pass

    def isConnectionPending(self):
        # type: () -> bool
        pass

    def open(self, remote=None):
        # type: (Optional[Any]) -> SocketChannel
        pass

    def read(self, *args):
        # type: (Any) -> Union[int, long]
        pass

    def setOption(self, name, value):
        # type: (Any, T) -> SocketChannel
        pass

    def shutdownInput(self):
        # type: () -> SocketChannel
        pass

    def shutdownOutput(self):
        # type: () -> SocketChannel
        pass

    def socket(self):
        # type: () -> Any
        pass

    def write(self, *args):
        # type: (Any) -> Union[int, long]
        pass
