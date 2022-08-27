"""OPC Functions.

The following functions allow you to read, write and browser OPC
servers.
"""

from __future__ import print_function

__all__ = [
    "browse",
    "browseServer",
    "browseSimple",
    "getServerState",
    "getServers",
    "isServerEnabled",
    "readValue",
    "readValues",
    "setServerEnabled",
    "writeValue",
    "writeValues",
]

from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common.model.values import (
    BasicQualifiedValue,
    QualityCode,
)
from com.inductiveautomation.ignition.common.opc import BasicOPCBrowseElement
from com.inductiveautomation.ignition.common.script.builtin import AbstractOPCUtilities
from com.inductiveautomation.ignition.common.script.builtin.ialabs import OPCBrowseTag
from java.lang import String

BrowseServerResult = List[Union[BasicOPCBrowseElement, AbstractOPCUtilities.PyOPCTag]]


def browse(opcServer, device, folderPath, opcItemPath):
    # type: (String, String, String, String) -> List[OPCBrowseTag]
    """Allows browsing of the OPC Servers in the runtime, returning a
    list of Tags.

    Args:
        opcServer: The name of the OPC Server to browse.
        device: The name of the device to browse.
        folderPath: Filters on a folder path. Use * as a wildcard for
            any number of characters and a ? for a single character.
        opcItemPath: Filters on a OPC item path. Use * as a wildcard for
            any number of characters and a ? for a single character.

    Returns:
        An array of OPCBrowseTag objects.
    """
    print(opcServer, device, folderPath, opcItemPath)
    return [OPCBrowseTag()]


def browseServer(
    opcServer,  # type: String
    nodeId,  # type: String
):
    # type: (...) -> BrowseServerResult
    """When called from a Vision Client, returns a list of
    OPCBrowseElement objects for the given Server. Otherwise, returns a
    list of PyOPCTag.

    Args:
        opcServer: The name of the OPC Server connection.
        nodeId: The node ID to browse.

    Returns:
        A list of OPCBrowseElement/PyOPCTag objects.
    """
    print(opcServer, nodeId)
    return [BasicOPCBrowseElement()]


def browseSimple(opcServer, device, folderPath, opcItemPath):
    # type: (String, String, String, String) -> List[OPCBrowseTag]
    """Allows browsing of OPC servers in the runtime returning a list of
    tags.

    browseSimple() takes mandatory parameters, which can be null, while
    browse() uses keyword-style arguments.

    Note:
        The spelling on the opcServer and device parameters must be
        exact.

    Args:
        opcServer: The name of the OPC Server to browse.
        device: The name of the device to browse.
        folderPath: Filters on a folder path. Use * as a wildcard for
            any number of characters and a ? for a single character.
        opcItemPath: Filters on a OPC item path. Use * as a wildcard for
            any number of characters and a ? for a single character.

    Returns:
        An array of OPCBrowseTag objects.
    """
    print(opcServer, device, folderPath, opcItemPath)
    return [OPCBrowseTag()]


def getServerState(opcServer):
    # type: (String) -> Optional[String]
    """Retrieves the current state of the given OPC Server connection.

    If the given Server is not found, the return value will be None.
    Otherwise, the return value will be one of these strings:
        - UNKNOWN
        - FAULTED
        - CONNECTING
        - CLOSED
        - CONNECTED
        - DISABLED

    Args:
        opcServer: The name of an OPC Server connection.

    Returns:
        A string representing the current state of the connection, or
        None if the connection doesn't exist.
    """
    print(opcServer)
    return "CONNECTED"


def getServers(includeDisabled=False):
    # type: (Optional[bool]) -> List[String]
    """Returns a list of Server names.

    Args:
        includeDisabled: If set to True, enabled and disabled servers
            will be returned. If set to False, only enabled servers will
            be returned. Defaults to False. Optional.

    Returns:
        A list of Server name strings. If no servers are found, returns
        an empty list.
    """
    print(includeDisabled)
    return ["serverName"]


def isServerEnabled(serverName):
    # type: (String) -> bool
    """Checks if an OPC Server connection is enabled or disabled.

    Args:
        serverName: The name of an OPC Server connection.

    Returns:
        True if the connection is enabled, False if the connection is
        disabled.
    """
    print(serverName)
    return True


def readValue(opcServer, itemPath):
    # type: (String, String) -> BasicQualifiedValue
    """Reads a single value directly from an OPC Server connection.

    The address is specified as a string, for example,
    [MyDevice]N11/N11:0. The object returned from this function has
    three attributes: value, quality, and timestamp. The value attribute
    represents the current value for the address specified.

    The quality attribute is an OPC-UA status code. You can easily check
    a good quality vs a bad quality by calling the isGood() function on
    the quality object. The timestamp attribute is Date object that
    represents the time that the value was retrieved at.

    Args:
        opcServer: The name of the OPC Server connection in which the
            item resides.
        itemPath: The item path, or address, to read from.

    Returns:
        An object that contains the value, quality, and timestamp
        returned from the OPC Server for the address specified.
    """
    print(opcServer, itemPath)
    return BasicQualifiedValue()


def readValues(opcServer, itemPaths):
    # type: (String, List[String]) -> List[BasicQualifiedValue]
    """This function is equivalent to the system.opc.readValue function,
    except that it can operate in bulk.

    You can specify a list of multiple addresses to read from, and you
    will receive a list of the same length, where each entry is the
    qualified value object for the corresponding address.

    Args:
        opcServer: The name of the OPC Server connection in which the
            items reside.
        itemPaths: A list of strings, each representing an item path, or
            address to read from.

    Returns:
        A sequence of objects, one for each address specified, in order.
        Each object will contain the value, quality, and timestamp
        returned from the OPC Server for the corresponding address.
    """
    print(opcServer, itemPaths)
    return [BasicQualifiedValue() for _ in itemPaths]


def setServerEnabled(serverName, enabled):
    # type: (String, bool) -> None
    """Enables or disables an OPC Server connection.

    Args:
        serverName: The name of an OPC Server connection.
        enabled: The new state the connection should be set to: True to
            enable the connection, False to disable.
    """
    print(serverName, enabled)


def writeValue(opcServer, itemPath, value):
    # type: (String, String, Any) -> QualityCode
    """Writes a value directly through an OPC Server connection
    synchronously.

    Will return an OPC-UA status code object. You can quickly check if
    the write succeeded by calling isGood() on the return value from
    this function.

    Args:
        opcServer: The name of the OPC Server connection in which the
            item resides.
        itemPath: The item path, or address, to write to.
        value: The value to write to the OPC item.

    Returns:
        The status of the write. Use returnValue.isGood() to check if
        the write succeeded.
    """
    print(opcServer, itemPath, value)
    return QualityCode()


def writeValues(opcServer, itemPaths, values):
    # type: (String, List[String], List[Any]) -> List[QualityCode]
    """This function is a bulk version of system.opc.writeValue.

    It takes a list of addresses and a list of objects, which must be
    the same length. It will write the corresponding object to the
    corresponding address in bulk. It will return a list of status codes
    representing the individual write success or failure for each
    corresponding address.

    Args:
        opcServer: The name of the OPC Server connection in which the
            items reside.
        itemPaths: A list of item paths, or addresses, to write to.
        values: A list of values to write to each address specified.

    Returns:
        An array of Quality objects, each entry corresponding in order
        to the addresses specified.
    """
    print(opcServer, itemPaths, values)
    return [QualityCode() for _ in itemPaths]
