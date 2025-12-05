from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.modules.serial.scripting import SerialScriptModule

BIT_RATE_110: int
BIT_RATE_150: int
BIT_RATE_300: int
BIT_RATE_600: int
BIT_RATE_1200: int
BIT_RATE_2400: int
BIT_RATE_4800: int
BIT_RATE_9600: int
BIT_RATE_19200: int
BIT_RATE_38400: int
BIT_RATE_57600: int
BIT_RATE_115200: int
BIT_RATE_230400: int
BIT_RATE_460800: int
BIT_RATE_921600: int
DATA_BITS_5: int
DATA_BITS_6: int
DATA_BITS_7: int
DATA_BITS_8: int
HANDSHAKE_CTS_DTR: int
HANDSHAKE_CTS_RTS: int
HANDSHAKE_DSR_DTR: int
HANDSHAKE_HARD_IN: int
HANDSHAKE_HARD_OUT: int
HANDSHAKE_NONE: int
HANDSHAKE_SOFT_IN: int
HANDSHAKE_SOFT_OUT: int
HANDSHAKE_SPLIT_MASK: int
HANDSHAKE_XON_XOFF: int
PARITY_EVEN: int
PARITY_ODD: int
PARITY_MARK: int
PARITY_SPACE: int
PARITY_NONE: int
STOP_BITS_1: int
STOP_BITS_2: int

def closeSerialPort(port: Union[str, unicode]) -> None: ...
def configureSerialPort(
    port: Union[str, unicode],
    bitRate: Optional[int] = ...,
    dataBits: Optional[int] = ...,
    handshake: Optional[int] = ...,
    hardwareFlowControl: Optional[bool] = ...,
    parity: Optional[int] = ...,
    stopBits: Optional[int] = ...,
) -> SerialScriptModule.SerialConfigurator: ...
def openSerialPort(port: Union[str, unicode]) -> None: ...
def port(
    port: Union[str, unicode],
    bitRate: Optional[int] = ...,
    dataBits: Optional[int] = ...,
    handshake: Optional[int] = ...,
    hardwareFlowControl: Optional[bool] = ...,
    parity: Optional[int] = ...,
    stopBits: Optional[int] = ...,
) -> SerialScriptModule.PortManager: ...
def readBytes(
    port: Union[str, unicode], numberOfBytes: int, timeout: Optional[int] = ...
) -> List[Any]: ...
def readBytesAsString(
    port: Union[str, unicode],
    numberOfBytes: int,
    timeout: int = ...,
    encoding: Union[str, unicode] = ...,
) -> Union[str, unicode]: ...
def readLine(
    port: Union[str, unicode],
    timeout: int = ...,
    encoding: Union[str, unicode] = ...,
    crlfRequired: bool = ...,
) -> Union[str, unicode]: ...
def readUntil(
    port: Union[str, unicode],
    delimiter: Union[str, unicode],
    includeDelimiter: bool,
    timeout: int = ...,
) -> Union[str, unicode]: ...
def sendBreak(port: Union[str, unicode], millis: int) -> None: ...
def write(
    port: Union[str, unicode],
    toWrite: Union[str, unicode],
    timeout: int = ...,
    encoding: Union[str, unicode] = ...,
) -> None: ...
def writeBytes(
    port: Union[str, unicode], toWrite: Any, timeout: Optional[int] = ...
) -> None: ...
