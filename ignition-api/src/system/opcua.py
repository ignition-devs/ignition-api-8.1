"""OPC - UA Functions.

The following functions allow you to interact directly with an OPC UA
Server.
"""

from __future__ import print_function

__all__ = ["addConnection", "callMethod", "removeConnection"]

from typing import Any, Dict, List, Tuple

from dev.coatl.helper.types import AnyStr


def addConnection(
    name,  # type: AnyStr
    description,  # type: AnyStr
    discoveryUrl,  # type: AnyStr
    endpointUrl,  # type: AnyStr
    securityPolicy,  # type: AnyStr
    securityMode,  # type: AnyStr
    settings,  # type: Dict[AnyStr, Any]
):
    # type: (...) -> None
    """Adds a new OPC UA connection.

    Args:
        name: Name to assign to the new connection.
        description: Description assigned to the new OPC UA connection.
        discoveryUrl: Endpoint URL to use for discovery services.
        endpointUrl: Endpoint URL to use for session services.
        securityPolicy: The name of the SecurityPolicy to use.
        securityMode: The name of the MessageSecurityMode to use.
        settings: A dictionary of additional settings to apply to the
            connection.
    """
    print(
        name,
        description,
        discoveryUrl,
        endpointUrl,
        securityPolicy,
        securityMode,
        settings,
    )


def callMethod(
    connectionName,  # type: AnyStr
    objectId,  # type: AnyStr
    methodId,  # type: AnyStr
    inputs,  # type: List[Any]
):
    # type: (...) -> Tuple[Any, Any, Any]
    """Calls a method in an OPC UA Server.

    To make the most of this n, you'll need to be familiar with methods
    in the OPC UA Server.

    Args:
        connectionName: The name of the OPC UA connection to the Server
            that the method resides in.
        objectId: The NodeId of the Object Node the Method is a member
            of.
        methodId: The NodeId of the Method Node to call.
        inputs: A list of input values expected by the method.

    Returns:
        A tuple containing the following:
            0: Resulting StatusCode for the call
            1: A list of StatusCode objects corresponding to each
                input argument
            2: A list of output values
    """
    print(connectionName, objectId, methodId, inputs)
    return None, None, None


def removeConnection(name):
    # type: (AnyStr) -> bool
    """Removes an OPC UA Connection.

    Args:
        name: The name of the OPC UA connection to remove.

    Returns:
        A boolean value representing whether the function was able to
        remove the connection. Returns True if the connection was
        successfully removed, False if the connection was not removed.
    """
    print(name)
    return True
