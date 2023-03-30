from __future__ import print_function

__all__ = ["SerialScriptModule"]

from typing import Any

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from org.python.core import PyObject


class SerialScriptModule(Object):
    def __init__(self):
        # type: () -> None
        super(SerialScriptModule, self).__init__()

    @staticmethod
    def setTrialExpired(trialExpired):
        # type: (bool) -> None
        pass

    class PortManager(object):
        def __init__(self, *args):
            # type: (*Any) -> None
            pass

        def __enter__(self):
            # type: () -> None
            print("Enter")

        def __exit__(self, exc_type, exc_val, exc_tb):
            # type: (object, object, object) -> None
            print("Exit")

    class SerialConfigurator(object):
        def setBitRate(self, value):
            # type: (int) -> SerialScriptModule.SerialConfigurator
            pass

        def setDataBits(self, value):
            # type: (int) -> SerialScriptModule.SerialConfigurator
            pass

        def setFlowControl(self, value):
            # type: (bool) -> SerialScriptModule.SerialConfigurator
            pass

        def setHandshake(self, value):
            # type: (int) -> SerialScriptModule.SerialConfigurator
            pass

        def setHardwareFlowControl(self, value):
            # type: (int) -> SerialScriptModule.SerialConfigurator
            pass

        def setParity(self, value):
            # type: (int) -> SerialScriptModule.SerialConfigurator
            pass

        def setStopBits(self, value):
            # type: (int) -> SerialScriptModule.SerialConfigurator
            pass

    class SerialPortWrapper(PyObject):
        def __init__(self, port, serialPort):
            # type: (AnyStr, Any) -> None
            super(SerialScriptModule.SerialPortWrapper, self).__init__()
            self._port = port
            self._serialPort = serialPort

        def readBytes(self, port, numberOfBytes, timeout=5000):
            # type: (AnyStr, int, int) -> bytearray
            pass

        def readBytesAsString(
            self, port, numberOfBytes, timeout=5000, encoding="utf-8"
        ):
            # type: (AnyStr, int, int, AnyStr) -> AnyStr
            pass

        def readLine(self, port, timeout=5000, encoding="utf-8", crlfRequired=False):
            # type: (AnyStr, int, AnyStr, bool) -> AnyStr
            pass

        def readUntil(self, port, delimiter, includeDelimiter, timeout=5000):
            # type: (AnyStr, str, bool, int) -> AnyStr
            pass

        def sendBreak(self, port, millis):
            # type: (AnyStr, long) -> None
            pass

        def write(self, port, toWrite, encoding="utf-8"):
            # type: (AnyStr, bytearray, AnyStr) -> None
            pass

        def writeBytes(self, port, toWrite, timeout=5000):
            # type: (AnyStr, bytearray, int) -> None
            pass
