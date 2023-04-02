"""Provides the classes for implementing networking applications."""

from __future__ import print_function

__all__ = [
    "CookieHandler",
    "CookieManager",
    "CookiePolicy",
    "CookieStore",
    "FileNameMap",
    "HttpCookie",
    "InetAddress",
    "InetSocketAddress",
    "Proxy",
    "Socket",
    "SocketAddress",
    "SocketImpl",
    "SocketImplFactory",
    "SocketOption",
    "URI",
]

from typing import Any, List, Mapping, Optional, Set

from dev.thecesrom.helper.types import AnyStr
from java.io import Closeable, InputStream, OutputStream
from java.lang import Class, Enum, Object
from java.nio.channels import SocketChannel


class SocketAddress(Object):
    def __init__(self):
        # type: () -> None
        super(SocketAddress, self).__init__()


class CookiePolicy(object):
    def shouldAccept(self, uri, cookie):
        # type: (URI, HttpCookie) -> bool
        raise NotImplementedError


class CookieStore(object):
    def add(self, uri, cookie):
        # type: (URI, HttpCookie) -> None
        raise NotImplementedError

    def get(self, uri):
        # type: (URI) -> List[HttpCookie]
        raise NotImplementedError

    def getCookies(self):
        # type: () -> List[HttpCookie]
        raise NotImplementedError

    def getURIs(self):
        # type: () -> List[URI]
        raise NotImplementedError

    def remove(self, uri, cookie):
        # type: (URI, HttpCookie) -> bool
        raise NotImplementedError

    def removeAll(self):
        # type: () -> bool
        raise NotImplementedError


class FileNameMap(object):
    def getContentTypeFor(self, fileName):
        # type: (AnyStr) -> AnyStr
        raise NotImplementedError


class SocketImplFactory(object):
    def createSocketImpl(self):
        # type: () -> SocketImpl
        raise NotImplementedError


class SocketOption(object):
    def name(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def type(self):
        # type: () -> Class
        raise NotImplementedError


class CookieHandler(Object):
    def __init__(self):
        # type: () -> None
        super(CookieHandler, self).__init__()

    def get(
        self,
        uri,  # type: URI
        requestHeaders,  # type: Mapping[AnyStr, List[AnyStr]]
    ):
        # type: (...) -> Mapping[AnyStr, List[AnyStr]]
        raise NotImplementedError

    @staticmethod
    def getDefault():
        # type: () -> CookieHandler
        pass

    def put(
        self,
        uri,  # type: URI
        responseHeaders,  # type: Mapping[AnyStr, List[AnyStr]]
    ):
        # type: (...) -> Mapping[AnyStr, List[AnyStr]]
        raise NotImplementedError

    @staticmethod
    def setDefault(cHandler):
        # type: (CookieHandler) -> None
        pass


class CookieManager(CookieHandler):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(CookieManager, self).__init__()
        print(args)

    def get(
        self,
        uri,  # type: URI
        requestHeaders,  # type: Mapping[AnyStr, List[AnyStr]]
    ):
        # type: (...) -> Mapping[AnyStr, List[AnyStr]]
        pass

    def getCookieStore(self):
        # type: () -> CookieStore
        pass

    def put(
        self,
        uri,  # type: URI
        responseHeaders,  # type: Mapping[AnyStr, List[AnyStr]]
    ):
        # type: (...) -> Mapping[AnyStr, List[AnyStr]]
        pass

    def setCookiePolicy(self, cookiePolicy):
        # type: (CookiePolicy) -> None
        pass


class HttpCookie(Object):
    def __init__(self, name, value):
        # type: (AnyStr, AnyStr) -> None
        super(HttpCookie, self).__init__()
        print(name, value)


class InetAddress(Object):
    def getAddress(self):
        # type: () -> bytearray
        pass

    @staticmethod
    def getAllByName(host):
        # type: (AnyStr) -> List[InetAddress]
        pass

    @staticmethod
    def getByAddress(*args):
        # type: (*Any) -> InetAddress
        pass

    @staticmethod
    def getByName(host):
        # type: (AnyStr) -> InetAddress
        pass

    def getCanonicalHostName(self):
        # type: () -> AnyStr
        pass

    def getHostAddress(self):
        # type: () -> AnyStr
        pass

    def getHostName(self):
        # type: () -> AnyStr
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
        super(InetSocketAddress, self).__init__()
        print(args)

    @staticmethod
    def createUnresolved(host, port):
        # type: (AnyStr, int) -> InetSocketAddress
        return InetSocketAddress(host, port)

    def getAddress(self):
        # type: () -> InetAddress
        pass

    def getHostname(self):
        # type: () -> AnyStr
        pass

    def getHostString(self):
        # type: () -> AnyStr
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
        super(Proxy, self).__init__()
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
        super(Socket, self).__init__()
        print(args)

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
        # type: (SocketOption) -> Any
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
        # type: (SocketOption, Any) -> Socket
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
        super(SocketImpl, self).__init__()


class URI(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(URI, self).__init__()
        print(args)
