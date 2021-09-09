"""OPC - UA Functions.

The following functions allow you to interact directly with an OPC-UA
server.
"""

from __future__ import print_function

__all__ = ["addConnection", "callMethod", "removeConnection"]


def addConnection(
    name,
    description,
    discoveryUrl,
    endpointUrl,
    securityPolicy,
    securityMode,
    settings,
):
    """Adds a new OPC UA connection.

    Args:
        name (str): Name to assign to the new connection.
        description (str): Description assigned to the new OPC UA
            connection.
        discoveryUrl (str): Endpoint URL to use for discovery
            services.
        endpointUrl (str): Endpoint URL to use for session services.
        securityPolicy (str): The name of the SecurityPolicy to use.
        securityMode (str): The name of the MessageSecurityMode to
            use.
        settings (dict): A dictionary of additional settings to apply
            to the connection.
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


def callMethod(connectionName, objectId, methodId, inputs):
    """Calls a method in an OPC UA server. To make the most of this
    function, you'll need to be familiar with methods in the OPC-UA
    server.

    Args:
        connectionName (str): The name of the OPC-UA connection to the
            server that the method resides in.
        objectId (str): The NodeId of the Object Node the Method is a
            member of.
        methodId (str): The NodeId of the Method Node to call.
        inputs (list[object]): A list of input values expected by the
            method.

    Returns:
        tuple: A tuple containing the following:
            0: Resulting StatusCode for the call
            1: A list of StatusCode objects corresponding to each
                input argument
            2: A list of output values

    """
    print(connectionName, objectId, methodId, inputs)


def removeConnection(name):
    """Removes an OPC UA Connection.

    Args:
        name (str): The name of the OPC UA connection to remove.

    Returns:
        bool: A boolean value representing whether the function was
            able to remove the connection. Returns True if the
            connection was successfully removed. Returns False if the
            connection was not removed.
    """
    print(name)
    return True
