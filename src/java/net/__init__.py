"""Provides the classes for implementing networking applications."""

from __future__ import print_function, unicode_literals

__all__ = ["InetSocketAddress", "Socket", "SocketAddress"]

from java.lang import Object


class Socket(Object):
    def __init__(self, *args):
        pass

    def bind(self, bindpoint):
        pass

    def close(self):
        pass

    def connect(self, endpoint, timeout):
        pass

    def getChannel(self):
        pass

    def getInetAddress(self):
        pass

    def getInputStream(self):
        pass

    def getKeepAlive(self):
        pass

    def getLocalAddress(self):
        pass

    def getLocalPort(self):
        pass

    def getLocalSocketAddress(self):
        pass

    def getOOBInline(self):
        pass

    def getOption(self, name):
        pass

    def getOutputStream(self):
        pass

    def getPort(self):
        pass

    def getReceiveBufferSize(self):
        pass

    def getRemoteSocketAddress(self):
        pass

    def getReuseAddress(self):
        pass

    def getSendBufferSize(self):
        pass

    def getSoLinger(self):
        pass

    def getSoTimeout(self):
        pass

    def getTcpNoDelay(self):
        pass

    def getTrafficClass(self):
        pass

    def isBound(self):
        pass

    def isClosed(self):
        pass

    def isConnected(self):
        pass

    def isInputShutdown(self):
        pass

    def isOutputShutdown(self):
        pass

    def sendUrgentData(self, data):
        pass

    def setKeepAlive(self, on):
        pass

    def setOOBInline(self, on):
        pass

    def setOption(self, name, value):
        pass

    def setPerformancePreferences(self, connectionTime, latency, bandwidth):
        pass

    def setReceiveBufferSize(self, size):
        pass

    def setReuseAddress(self, on):
        pass

    def setSendBufferSize(self, size):
        pass

    @staticmethod
    def setSocketImplFactory(fac):
        pass

    def setSoLinger(self, on, linger):
        pass

    def setSoTimeout(self, timeout):
        pass

    def setTcpNoDelay(self, on):
        pass

    def setTrafficClass(self, tc):
        pass

    def shutdownInput(self):
        pass

    def shutdownOutput(self):
        pass

    def supportedOptions(self):
        pass


class SocketAddress(Object):
    def __init__(self):
        pass


class InetSocketAddress(SocketAddress):
    def __init__(self, *args):
        print(args)
        super(InetSocketAddress, self).__init__()

    @staticmethod
    def createUnresolved(host, port):
        return InetSocketAddress(host, port)

    def getAddress(self):
        pass

    def getHostname(self):
        pass

    def getHostString(self):
        pass

    def getPort(self):
        pass

    def isUnresolved(self):
        pass
