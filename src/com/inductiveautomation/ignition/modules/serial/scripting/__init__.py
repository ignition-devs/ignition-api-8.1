from __future__ import print_function

__all__ = ["SerialScriptModule"]

from typing import Any, Union

from java.lang import Object

from org.python.core import PyObject


class SerialScriptModule(Object):

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
            # type: (Union[str, unicode], Any) -> None
            super(SerialScriptModule.SerialPortWrapper, self).__init__()
            self._port = port
            self._serialPort = serialPort

        def readBytes(self, port, numberOfBytes, timeout=5000):
            # type: (Union[str, unicode], int, int) -> bytearray
            pass

        def readBytesAsString(
            self,
            port,  # type: Union[str, unicode]
            numberOfBytes,  # type: int
            timeout=5000,  # type: int
            encoding="utf-8",  # type: Union[str, unicode]
        ):
            # type: (...) -> Union[str, unicode]
            pass

        def readLine(
            self,
            port,  # type: Union[str, unicode]
            timeout=5000,  # type: int
            encoding="utf-8",  # type: Union[str, unicode]
            crlfRequired=False,  # type: bool
        ):
            # type: (...) -> Union[str, unicode]
            pass

        def readUntil(
            self,
            port,  # type: Union[str, unicode]
            delimiter,  # type: Union[str, unicode]
            includeDelimiter,  # type: bool
            timeout=5000,  # type: int
        ):
            # type: (...) -> Union[str, unicode]
            pass

        def sendBreak(self, port, millis):
            # type: (Union[str, unicode], long) -> None
            pass

        def write(
            self,
            port,  # type: Union[str, unicode]
            toWrite,  # type: bytearray
            encoding="utf-8",  # type: Union[str, unicode]
        ):
            # type: (...) -> None
            pass

        def writeBytes(self, port, toWrite, timeout=5000):
            # type: (Union[str, unicode], bytearray, int) -> None
            pass

    def __init__(self):
        # type: () -> None
        super(SerialScriptModule, self).__init__()

    @staticmethod
    def setTrialExpired(trialExpired):
        # type: (bool) -> None
        pass
