__all__ = [
    "Channel",
    "SelectableChannel",
    "SelectionKey",
    "Selector",
    "SocketChannel",
]

from typing import Any, Optional, Set, TypeVar, Union

from java.io import Closeable
from java.lang import Object
from java.util.function import Consumer

T = TypeVar("T")


class Channel(Closeable):
    def close(self):
        # type: () -> None
        pass

    def isOpen(self):
        # type: () -> bool
        pass


class SelectableChannel(Object, Closeable):
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


class Selector(Object, Closeable):
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
