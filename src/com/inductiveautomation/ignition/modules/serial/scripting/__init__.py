from __future__ import print_function

__all__ = ["SerialScriptModule"]

from typing import Any

from java.lang import Object


class SerialScriptModule(Object):
    def __init__(self):
        pass

    def setTrialExpired(self, arg):
        pass

    class PortManager(object):
        def __init__(self, *args):
            # type: (Any) -> None
            pass

        def __enter__(self):
            print("Enter")

        def __exit__(self, exc_type, exc_val, exc_tb):
            print("Exit")

    class SerialConfigurator(object):
        def setBitRate(self, value):
            pass

        def setDataBits(self, value):
            pass

        def setFlowControl(self, value):
            pass

        def setHandshake(self, value):
            pass

        def setHardwareFlowControl(self, value):
            pass

        def setParity(self, value):
            pass

        def setStopBits(self, value):
            pass

    class SerialPortWrapper(object):
        def readBytes(self, port, numberOfBytes, timeout=5000):
            pass

        def readBytesAsString(
            self, port, numberOfBytes, timeout=5000, encoding="utf-8"
        ):
            pass

        def readLine(self, port, timeout=5000, encoding="utf-8", crlfRequired=False):
            pass

        def readUntil(self, port, delimiter, includeDelimiter, timeout=5000):
            pass

        def sendBreak(self, port, millis):
            pass

        def write(self, port, toWrite, encoding="utf-8"):
            pass

        def writeBytes(self, port, toWrite, timeout=5000):
            pass
