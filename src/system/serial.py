"""Serial Functions.

The following functions give you access to read and write through serial
ports.
"""

from __future__ import print_function

__all__ = [
    "BIT_RATE_110",
    "BIT_RATE_115200",
    "BIT_RATE_1200",
    "BIT_RATE_150",
    "BIT_RATE_19200",
    "BIT_RATE_230400",
    "BIT_RATE_2400",
    "BIT_RATE_300",
    "BIT_RATE_38400",
    "BIT_RATE_460800",
    "BIT_RATE_4800",
    "BIT_RATE_57600",
    "BIT_RATE_600",
    "BIT_RATE_921600",
    "BIT_RATE_9600",
    "DATA_BITS_5",
    "DATA_BITS_6",
    "DATA_BITS_7",
    "DATA_BITS_8",
    "HANDSHAKE_CTS_DTR",
    "HANDSHAKE_CTS_RTS",
    "HANDSHAKE_DSR_DTR",
    "HANDSHAKE_HARD_IN",
    "HANDSHAKE_HARD_OUT",
    "HANDSHAKE_NONE",
    "HANDSHAKE_SOFT_IN",
    "HANDSHAKE_SOFT_OUT",
    "HANDSHAKE_SPLIT_MASK",
    "HANDSHAKE_XON_XOFF",
    "PARITY_EVEN",
    "PARITY_MARK",
    "PARITY_NONE",
    "PARITY_ODD",
    "PARITY_SPACE",
    "STOP_BITS_1",
    "STOP_BITS_2",
    "closeSerialPort",
    "configureSerialPort",
    "openSerialPort",
    "port",
    "readBytes",
    "readBytesAsString",
    "readLine",
    "readUntil",
    "sendBreak",
    "write",
    "writeBytes",
]

from typing import Any, List, Optional

from com.inductiveautomation.ignition.modules.serial.scripting import SerialScriptModule
from java.lang import String

# Bit rate constants.
BIT_RATE_110 = 110
BIT_RATE_150 = 150
BIT_RATE_300 = 300
BIT_RATE_600 = 600
BIT_RATE_1200 = 1200
BIT_RATE_2400 = 2400
BIT_RATE_4800 = 4800
BIT_RATE_9600 = 9600
BIT_RATE_19200 = 19200
BIT_RATE_38400 = 38400
BIT_RATE_57600 = 57600
BIT_RATE_115200 = 115200
BIT_RATE_230400 = 230400
BIT_RATE_460800 = 460800
BIT_RATE_921600 = 921600

# Data bits constants.
DATA_BITS_5 = 5
DATA_BITS_6 = 6
DATA_BITS_7 = 7
DATA_BITS_8 = 8

# Handshake constants.
HANDSHAKE_CTS_DTR = 4112
HANDSHAKE_CTS_RTS = 17
HANDSHAKE_DSR_DTR = 4352
HANDSHAKE_HARD_IN = 0
HANDSHAKE_HARD_OUT = 0
HANDSHAKE_NONE = 0
HANDSHAKE_SOFT_IN = 65536
HANDSHAKE_SOFT_OUT = 1048576
HANDSHAKE_SPLIT_MASK = 0
HANDSHAKE_XON_XOFF = 1114112

# Parity constants.
PARITY_EVEN = 2
PARITY_ODD = 1
PARITY_MARK = 3
PARITY_SPACE = 4
PARITY_NONE = 0

# Stop bits constants.
STOP_BITS_1 = 1
STOP_BITS_2 = 3


def closeSerialPort(port):
    # type: (String) -> None
    """Closes a previously opened serial port.

    Returns without doing anything if the named serial port is not
    currently open. Will throw an exception if the port is open and
    cannot be closed.

    Args:
        port: The name of the serial port, e.g., "COM1" or "dev/ttyS0".
    """
    print(port)


def configureSerialPort(
    port,  # type: String
    bitRate=None,  # type: Optional[int]
    dataBits=None,  # type: Optional[int]
    handshake=None,  # type: Optional[int]
    hardwareFlowControl=None,  # type: Optional[bool]
    parity=None,  # type: Optional[int]
    stopBits=None,  # type: Optional[int]
):
    # type: (...) -> SerialScriptModule.SerialConfigurator
    """Configure a serial port for use in a later call.

    This only needs to be done once unless the configuration has changed
    after the initial call. All access to constants must be prefixed by
    "system.serial.".

    Args:
        port: The name of the serial port, e.g., "COM1" or "/dev/ttyS0".
            This parameter is required.
        bitRate: Configure the bit rate. Valid values are defined by the
            following constants: BIT_RATE_110, BIT_RATE_150,
            BIT_RATE_300, BIT_RATE_600, BIT_RATE_1200, BIT_RATE_2400,
            BIT_RATE_4800, BIT_RATE_9600, BIT_RATE_19200,
            BIT_RATE_38400, BIT_RATE_57600, BIT_RATE_115200,
            BIT_RATE_230400, BIT_RATE_460800, BIT_RATE_921600. Optional.
        dataBits: Configure the data bits. Valid values are defined by
            the following constants: DATA_BITS_5, DATA_BITS_6,
            DATA_BITS_7, DATA_BITS_8. Optional.
        handshake: Configure the handshake. Valid values are defined by
            the following constants: HANDSHAKE_CTS_DTR,
            HANDSHAKE_CTS_RTS, HANDSHAKE_DSR_DTR, HANDSHAKE_HARD_IN,
            HANDSHAKE_HARD_OUT, HANDSHAKE_NONE, HANDSHAKE_SOFT_IN,
            HANDSHAKE_SOFT_OUT, HANDSHAKE_SPLIT_MASK,
            HANDSHAKE_XON_XOFF. Optional.
        hardwareFlowControl: Configure hardware flow control. On or off.
        parity: Configure parity. Valid values are defined by the
            following constants: PARITY_EVEN, PARITY_ODD, PARITY_MARK,
            PARITY_SPACE, PARITY_NONE. Optional.
        stopBits: Configure stop bits. Valid values are defined by the
            following constants: STOP_BITS_1, STOP_BITS_2. Optional.

    Returns:
        A SerialConfigurator object with exposed functions that can be
        used to configure the serial port instead of, or in addition to,
        the arguments passed to configureSerialPort.
    """
    print(
        port,
        bitRate,
        dataBits,
        handshake,
        hardwareFlowControl,
        parity,
        stopBits,
    )
    return SerialScriptModule.SerialConfigurator()


def openSerialPort(port):
    # type: (String) -> None
    """Opens a previously configured serial port for use.

    Will throw an exception if the serial port cannot be opened.

    Args:
        port: The name of the serial port, e.g., "COM1" or "dev/ttyS0".
    """
    print(port)


def port(
    port,  # type: String
    bitRate=None,  # type: Optional[int]
    dataBits=None,  # type: Optional[int]
    handshake=None,  # type: Optional[int]
    hardwareFlowControl=None,  # type: Optional[bool]
    parity=None,  # type: Optional[int]
    stopBits=None,  # type: Optional[int]
):
    # type: (...) -> SerialScriptModule.PortManager
    """Returns a context manager wrapping a serial port, allowing the
    rest of the system to interact with that port.

    This function effectively combines the
    system.serial.configureSerialPort, system.serial.openSerialPort,
    and system.serial.closeSerialPort functions into a single call.

    Intended to be used with the Python 'with' statement. The object
    aliased in the 'with' statement has special access to all of the
    other system.serial functions, allowing for reads and writes.

    Closing the port happens automatically once the 'with' statement
    ends.

    Accepts the same arguments as configureSerialPort, and access to
    constants must be prefixed by "system.serial." As shown in the
    parameter descriptions.

    Args:
        port: The name of the serial port, e.g., "COM1" or "dev/ttyS0".
        bitRate: Configure the bit rate. Valid values are defined by the
            following constants: BIT_RATE_110, BIT_RATE_150,
            BIT_RATE_300, BIT_RATE_600, BIT_RATE_1200, BIT_RATE_2400,
            BIT_RATE_4800, BIT_RATE_9600, BIT_RATE_19200,
            BIT_RATE_38400, BIT_RATE_57600, BIT_RATE_115200,
            BIT_RATE_230400, BIT_RATE_460800, BIT_RATE_921600. Optional.
        dataBits: Configure the data bits. Valid values are defined by
            the following constants: DATA_BITS_5, DATA_BITS_6,
            DATA_BITS_7, DATA_BITS_8. Optional.
        handshake: Configure the handshake. Valid values are defined by
            the following constants: HANDSHAKE_CTS_DTR,
            HANDSHAKE_CTS_RTS, HANDSHAKE_DSR_DTR, HANDSHAKE_HARD_IN,
            HANDSHAKE_HARD_OUT, HANDSHAKE_NONE, HANDSHAKE_SOFT_IN,
            HANDSHAKE_SOFT_OUT, HANDSHAKE_SPLIT_MASK,
            HANDSHAKE_XON_XOFF. Optional.
        hardwareFlowControl: Configure hardware flow control. On or off.
            Optional.
        parity: Configure parity. Valid values are defined by the
            following constants: PARITY_EVEN, PARITY_ODD, PARITY_MARK,
            PARITY_SPACE, PARITY_NONE. Optional.
        stopBits: Configure stop bits. Valid values are defined by the
            following constants: STOP_BITS_1, STOP_BITS_2. Optional.

    Returns:
        A wrapper around the configured port, that can be entered by
        using a 'with' statement. The port will automatically close on
        exiting the 'with' statement scope.
    """
    print(
        port,
        bitRate,
        dataBits,
        handshake,
        hardwareFlowControl,
        parity,
        stopBits,
    )
    return SerialScriptModule.PortManager()


def readBytes(port, numberOfBytes, timeout=5000):
    # type: (String, int, Optional[int]) -> List[Any]
    """Read numberOfBytes bytes from a serial port.

    Args:
        port: The previously configured serial port to use.
        numberOfBytes: The number of bytes to read.
        timeout: Maximum amount of time, in milliseconds, to block
            before returning. Default is 5,000. Optional.

    Returns:
        A list containing bytes read from the serial port.
    """
    print(port, numberOfBytes, timeout)
    return []


def readBytesAsString(
    port,  # type: String
    numberOfBytes,  # type: int
    timeout=5000,  # type: int
    encoding="utf-8",  # type: String
):
    # type: (...) -> String
    """Read numberOfBytes bytes from a serial port and convert them to a
    String.

    If a specific encoding is needed to match the source of the data,
    use system.serial.readBytes and use the desired encoding to decode
    the byte array returned.

    Args:
        port: The previously configured serial port to use.
        numberOfBytes: The number of bytes to read.
        timeout: Maximum amount of time, in milliseconds, to block
            before returning. Default is 5,000. Optional.
        encoding: Encoding to use when constructing the string. Defaults
            to the platform's default character set. Optional.

    Returns:
        A String created from the bytes read.
    """
    print(port, numberOfBytes, timeout, encoding)
    return ""


def readLine(
    port,  # type: String
    timeout=5000,  # type: int
    encoding="utf-8",  # type: String
    crlfRequired=False,  # type: bool
):
    # type: (...) -> String
    r"""Attempts to read a line from a serial port.

    A "line" is considered to be terminated by either a line feed
    ('\n'), a carriage return ('\r'), or a carriage return followed
    immediately by a line feed.

    The function will wait until the timeout period for a terminator. If
    the timeout is reached before the line is properly terminated, then
    the buffer will be dumped, possibly resulting in data loss.

    Args:
        port: The previously configured serial port to use.
        timeout: Maximum amount of time, in milliseconds, to block
            before returning. Default is 5000. Optional.
        encoding: The String encoding to use. Default is UTF8. Optional.
        crlfRequired: True if both CR and LF are required to delimit a
            line. Optional.

    Returns:
        A line of text.
    """
    print(port, timeout, encoding, crlfRequired)
    return ""


def readUntil(port, delimiter, includeDelimiter, timeout=5000):
    # type: (String, String, bool, Optional[int]) -> String
    """Reads a byte at a time from a serial port until a delimiter
    character is encountered.

    The read will block for up to timeout milliseconds before returning.

    If the delimiter is not found before the timeout period, then the
    buffer will dump, potentially resulting in data loss.

    Args:
        port: The previously configured serial port to use.
        delimiter: The delimiter to read until.
        includeDelimiter: If True, the delimiter will be included in the
            return value.
        timeout: Timeout in milliseconds. Default is 5,000. Optional.

    Returns:
        A String containing all 8-bit ASCII characters read until the
        delimiter was reached, and including the delimiter if the
        "includeDelimiter" parameter was True.
    """
    print(port, delimiter, includeDelimiter, timeout)
    return ""


def sendBreak(port, millis):
    # type: (String, int) -> None
    """Sends a break signal for approximately millis milliseconds.

    Args:
        port: The name of the serial port, e.g., "COM1" or "dev/ttyS0".
        millis: Approximate length of break signal, in milliseconds.
    """
    print(port, millis)


def write(port, toWrite, encoding="utf-8"):
    # type: (String, String, Optional[String]) -> None
    """Write a String to a serial port using the platforms default
    character encoding.

    Args:
        port: The previously configured serial port to use.
        toWrite: The String to write.
        encoding: Encoding to use when constructing the string. Defaults
            to the platform's default character set. Optional.
    """
    print(port, toWrite, encoding)


def writeBytes(port, toWrite, timeout=5000):
    # type: (String, Any, Optional[int]) -> None
    """Write a byte array to a serial port.

    Args:
        port: The previously configured serial port to use.
        toWrite: The byte array to write.
        timeout: Optional timeout in milliseconds. Default is 5,000.
            Optional.
    """
    print(port, toWrite, timeout)
