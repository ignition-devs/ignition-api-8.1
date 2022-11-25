"""Provides the classes for implementing networking applications."""

from __future__ import print_function

__all__ = [
    "InetAddress",
    "InetSocketAddress",
    "Socket",
    "SocketAddress",
    "SocketChannel",
    "SocketImpl",
    "SocketImplFactory",
    "SocketOption",
]

from typing import Any, List, Optional, Set, TypeVar

from java.io import Closeable, InputStream, OutputStream
from java.lang import Class, Enum, Object, String
from java.nio.channels import SocketChannel

T = TypeVar("T")


class SocketAddress(Object):
    def __init__(self):
        # type: () -> None
        pass


class FileNameMap(object):
    def getContentTypeFor(self, fileName):
        # type: (String) -> String
        raise NotImplementedError


class SocketImplFactory(object):
    def createSocketImpl(self):
        # type: () -> SocketImpl
        raise NotImplementedError


class SocketOption(object):
    def name(self):
        # type: () -> String
        raise NotImplementedError

    def type(self):
        # type: () -> Class
        raise NotImplementedError


class InetAddress(Object):
    def getAddress(self):
        # type: () -> bytearray
        pass

    @staticmethod
    def getAllByName(host):
        # type: (String) -> List[InetAddress]
        pass

    @staticmethod
    def getByAddress(*args):
        # type: (*Any) -> InetAddress
        pass

    @staticmethod
    def getByName(host):
        # type: (String) -> InetAddress
        pass

    def getCanonicalHostName(self):
        # type: () -> String
        pass

    def getHostAddress(self):
        # type: () -> String
        pass

    def getHostName(self):
        # type: () -> String
        pass

    @staticmethod
    def getLocalHost():
        # type: () -> InetAddress
        pass

    @staticmethod
    def getLoopbackAddress():
        # type: () -> InetAddress
        pass

    def isAnyLocalAddress(self):
        # type: () -> bool
        return True

    def isLinkLocalAddress(self):
        # type: () -> bool
        return True

    def isLoopbackAddress(self):
        # type: () -> bool
        return True

    def isMCGlobal(self):
        # type: () -> bool
        return True

    def isMCLinkLocal(self):
        # type: () -> bool
        return True

    def isMCNodeLocal(self):
        # type: () -> bool
        return True

    def isMCOrgLocal(self):
        # type: () -> bool
        return True

    def isMCSiteLocal(self):
        # type: () -> bool
        return True

    def isMulticastAddress(self):
        # type: () -> bool
        return True

    def isReachable(self, *args):
        # type: (*Any) -> bool
        return True

    def isSiteLocalAddress(self):
        # type: () -> bool
        return True


class InetSocketAddress(SocketAddress):
    def __init__(self, *args):
        # type: (*Any) -> None
        print(args)
        super(InetSocketAddress, self).__init__()

    @staticmethod
    def createUnresolved(host, port):
        # type: (String, int) -> InetSocketAddress
        return InetSocketAddress(host, port)

    def getAddress(self):
        # type: () -> InetAddress
        pass

    def getHostname(self):
        # type: () -> String
        pass

    def getHostString(self):
        # type: () -> String
        pass

    def getPort(self):
        # type: () -> int
        pass

    def isUnresolved(self):
        # type: () -> bool
        return True


class Proxy(Object):
    NO_PROXY = None  # type: Proxy

    def __init__(self, type_, sa):
        # type: (Proxy.Type, SocketAddress) -> None
        print(type_, sa)

    def address(self):
        # type: () -> SocketAddress
        pass

    def type(self):
        # type: () -> Proxy.Type
        pass

    class Type(Enum):
        DIRECT = None  # type: Proxy.Type
        HTTP = None  # type: Proxy.Type
        SOCKS = None  # type: Proxy.Type

        @staticmethod
        def values():
            # type: () -> List[Proxy.Type]
            pass


class Socket(Object, Closeable):
    def __init__(self, *args):
        # type: (*Any) -> None
        pass

    def bind(self, bindpoint):
        # type: (SocketAddress) -> None
        pass

    def close(self):
        # type: () -> None
        pass

    def connect(self, endpoint, timeout=None):
        # type: (SocketAddress, Optional[int]) -> None
        pass

    def getChannel(self):
        # type: () -> SocketChannel
        pass

    def getInetAddress(self):
        # type: () -> InetAddress
        pass

    def getInputStream(self):
        # type: () -> InputStream
        pass

    def getKeepAlive(self):
        # type: () -> bool
        return True

    def getLocalAddress(self):
        # type: () -> InetAddress
        pass

    def getLocalPort(self):
        # type: () -> int
        pass

    def getLocalSocketAddress(self):
        # type: () -> SocketAddress
        pass

    def getOOBInline(self):
        # type: () -> bool
        return True

    def getOption(self, name):
        # type: (SocketOption) -> T
        pass

    def getOutputStream(self):
        # type: () -> OutputStream
        pass

    def getPort(self):
        # type: () -> int
        pass

    def getReceiveBufferSize(self):
        # type: () -> int
        pass

    def getRemoteSocketAddress(self):
        # type: () -> SocketAddress
        pass

    def getReuseAddress(self):
        # type: () -> bool
        return True

    def getSendBufferSize(self):
        # type: () -> int
        pass

    def getSoLinger(self):
        # type: () -> int
        pass

    def getSoTimeout(self):
        # type: () -> int
        pass

    def getTcpNoDelay(self):
        # type: () -> bool
        return True

    def getTrafficClass(self):
        # type: () -> int
        pass

    def isBound(self):
        # type: () -> bool
        return True

    def isClosed(self):
        # type: () -> bool
        return True

    def isConnected(self):
        # type: () -> bool
        return True

    def isInputShutdown(self):
        # type: () -> bool
        return True

    def isOutputShutdown(self):
        # type: () -> bool
        return True

    def sendUrgentData(self, data):
        # type: (int) -> None
        pass

    def setKeepAlive(self, on):
        # type: (bool) -> None
        pass

    def setOOBInline(self, on):
        # type: (bool) -> None
        pass

    def setOption(self, name, value):
        # type: (SocketOption, T) -> Socket
        pass

    def setPerformancePreferences(self, connectionTime, latency, bandwidth):
        # type: (int, int, int) -> None
        pass

    def setReceiveBufferSize(self, size):
        # type: (int) -> None
        pass

    def setReuseAddress(self, on):
        # type: (bool) -> None
        pass

    def setSendBufferSize(self, size):
        # type: (int) -> None
        pass

    @staticmethod
    def setSocketImplFactory(fac):
        # type: (SocketImplFactory) -> None
        pass

    def setSoLinger(self, on, linger):
        # type: (bool, int) -> None
        pass

    def setSoTimeout(self, timeout):
        # type: (int) -> None
        pass

    def setTcpNoDelay(self, on):
        # type: (bool) -> None
        pass

    def setTrafficClass(self, tc):
        # type: (int) -> None
        pass

    def shutdownInput(self):
        # type: () -> None
        pass

    def shutdownOutput(self):
        # type: () -> None
        pass

    def supportedOptions(self):
        # type: () -> Set[SocketOption]
        pass


class SocketImpl(Object):
    def __init__(self):
        # type: () -> None
        pass
