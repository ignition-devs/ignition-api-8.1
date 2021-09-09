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

from abc import ABCMeta, abstractmethod

from java.lang import Object


class OPCBrowseTag(Object):
    """BrowseTag class."""

    def __init__(
        self,
        opcServer=None,
        type=None,
        displayName=None,
        displayPath=None,
        dataType=None,
        opcItemPath=None,
    ):
        super(OPCBrowseTag, self).__init__()
        self.opcServer = opcServer
        self.type = type
        self.displayName = displayName
        self.displayPath = displayPath
        self.dataType = dataType
        self.opcItemPath = opcItemPath

    def getDataType(self):
        return self.dataType

    def getDisplayName(self):
        return self.displayName

    def getDisplayPath(self):
        return self.displayPath

    def getOpcItemPath(self):
        return self.opcItemPath

    def getOpcServer(self):
        return self.opcServer

    def getType(self):
        return self.type


class QualifiedValue(ABCMeta):
    """Represents a value with a DataQuality & timestamp attached to
    it.
    """

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def getQuality(self):
        pass

    @abstractmethod
    def getTimestamp(self):
        pass

    @abstractmethod
    def getValue(self):
        pass


class Quality(ABCMeta):
    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def getDescription(self):
        pass

    def getLevel(self):
        pass

    @abstractmethod
    def getName(self):
        pass

    def getQualityCode(self):
        pass

    def isGood(self):
        pass


def browse(opcServer, device, folderPath, opcItemPath):
    """Allows browsing of the OPC servers in the runtime, returning a
    list of tags.

    Args:
        opcServer (str): The name of the OPC server to browse.
        device (str): The name of the device to browse.
        folderPath (str): Filters on a folder path. Use * as a wildcard
            for any number of characters and a ? for a single character.
        opcItemPath (str): Filters on a OPC item path. Use * as a
            wildcard for any number of characters and a ? for a single
            character.

    Returns:
        list[OPCBrowseTag]: An array of OPCBrowseTag objects.
            OPCBrowseTag has the following functions: getOpcServer(),
            getOpcItemPath(), getType(), getDisplayName(),
            getDisplayPath(), getDataType().
    """
    print(opcServer, device, folderPath, opcItemPath)
    return [OPCBrowseTag()]


def browseServer(opcServer, nodeId):
    """When called from a Vision Client, returns a list of
    OPCBrowseElement objects for the given server.

    Otherwise returns a list of PyOPCTag.

    Args:
        opcServer (str): The name of the OPC server connection.
        nodeId (str): The node ID to browse.

    Returns:
        object: A list of OPCBrowseElement/PyOPCTag objects.
    """
    print(opcServer, nodeId)
    return []


def browseSimple(opcServer, device, folderPath, opcItemPath):
    """Allows browsing of OPC servers in the runtime returning a list of
    tags.

    browseSimple() takes mandatory parameters, which can be null,
    while browse() uses keyword-style arguments.

    Args:
        opcServer (str): The name of the OPC server to browse.
        device (str): The name of the device to browse.
        folderPath (str): Filters on a folder path. Use * as a wildcard
            for any number of characters and a ? for a single character.
        opcItemPath (str): Filters on a OPC item path. Use * as a
            wildcard for any number of characters and a ? for a single
            character.

    Returns:
        list[OPCBrowseTag]: An array of OPCBrowseTag objects.
            OPCBrowseTag has the following functions: getOpcServer(),
            getOpcItemPath(), getType(), getDisplayName(),
            getDisplayPath(), getDataType().
    """
    print(opcServer, device, folderPath, opcItemPath)
    return [OPCBrowseTag()]


def getServerState(opcServer):
    """Retrieves the current state of the given OPC server connection.

    If the given server is not found, the return value will be None.
    Otherwise, the return value will be one of these strings:
        - UNKNOWN
        - FAULTED
        - CONNECTING
        - CLOSED
        - CONNECTED
        - DISABLED

    Args:
        opcServer (str): The name of an OPC server connection.

    Returns:
        str: A string representing the current state of the connection,
            or None if the connection doesn't exist.
    """
    print(opcServer)
    return "CONNECTED"


def getServers(includeDisabled=False):
    """Returns a list of server names.

    Args:
        includeDisabled (bool): If set to True, enabled and disabled
            servers will be returned. If set to False, only enabled
            servers will be returned. Defaults to False. Optional.

    Returns:
        list[str]: A list of server name strings. If no servers are
            found, returns an empty list.
    """
    print(includeDisabled)
    return []


def isServerEnabled(serverName):
    """Checks if an OPC server connection is enabled or disabled.

    Args:
        serverName (str): The name of an OPC server connection.

    Returns:
        bool: True if the connection is enabled, False if the connection
            is disabled.
    """
    print(serverName)
    return True


def readValue(opcServer, itemPath):
    """Reads a single value directly from an OPC server connection.

    The address is specified as a string, for example,
    [MyDevice]N11/N11:0. The object returned from this function has
    three attributes: value, quality, and timestamp. The value attribute
    represents the current value for the address specified.

    The quality attribute is an OPC-UA status code. You can easily check
    a good quality vs a bad quality by calling the isGood() function on
    the quality object. The timestamp attribute is Date object that
    represents the time that the value was retrieved at.

    Args:
        opcServer (str): The name of the OPC server connection in which
            the item resides.
        itemPath (str): The item path, or address, to read from.

    Returns:
        QualifiedValue: An object that contains the value, quality, and
            timestamp returned from the OPC server for the address
            specified.
    """
    print(opcServer, itemPath)
    return QualifiedValue()


def readValues(opcServer, itemPaths):
    """This function is equivalent to the system.opc.readValue function,
    except that it can operate in bulk.

    You can specify a list of multiple addresses to read from, and you
    will receive a list of the same length, where each entry is the
    qualified value object for the corresponding address.

    Args:
        opcServer (str): The name of the OPC server connection in which
            the items reside.
        itemPaths (list[str]): A list of strings, each representing an
            item path, or address to read from.

    Returns:
        list[QualifiedValue]: A sequence of objects, one for each
            address specified, in order. Each object will contains the
            value, quality, and timestamp returned from the OPC server
            for the corresponding address.
    """
    print(opcServer, itemPaths)
    return [QualifiedValue()]


def setServerEnabled(serverName, enabled):
    """Enables or disables an OPC server connection.

    Args:
        serverName (str): The name of an OPC server connection.
        enabled (bool): The new state the connection should be set to:
            True to enable the connection, False to disable.
    """
    print(serverName, enabled)


def writeValue(opcServer, itemPath, value):
    """Writes a value directly through an OPC server connection
    synchronously.

    Will return an OPC-UA status code object. You can quickly check if
    the write succeeded by calling isGood() on the return value from
    this function.

    Args:
        opcServer (str): The name of the OPC server connection in which
            the item resides.
        itemPath (str): The item path, or address, to write to.
        value (object): The value to write to the OPC item.

    Returns:
        Quality: The status of the write. Use returnValue.isGood() to
            check if the write succeeded.
    """
    print(opcServer, itemPath, value)
    return Quality()


def writeValues(opcServer, itemPaths, values):
    """This function is a bulk version of system.opc.writeValue.

    It takes a list of addresses and a list of objects, which must be
    the same length. It will write the corresponding object to the
    corresponding address in bulk. It will return a list of status codes
    representing the individual write success or failure for each
    corresponding address.

    Args:
        opcServer (str): The name of the OPC server connection in which
            the items reside.
        itemPaths (list[str]): A list of item paths, or addresses, to
            write to.
        values (list[object]): A list of values to write to each address
            specified.

    Returns:
        list[Quality]: An array of Quality objects, each entry
            corresponding in order to the addresses specified.
    """
    print(opcServer, itemPaths, values)
    return [Quality()]
