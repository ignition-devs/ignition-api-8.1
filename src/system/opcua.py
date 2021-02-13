# Copyright (C) 2018-2021
# Author: Cesar Roman
# Contact: cesar@thecesrom.dev
"""OPC - UA Functions
The following functions allow you to interact directly with an OPC-UA
server.
"""

__all__ = ["callMethod"]


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
    return None, None, None
