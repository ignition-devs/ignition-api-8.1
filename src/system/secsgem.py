"""SECS/GEM Functions.

The following functions allow you to interact with equipment defined by
the SECS/GEM module. Note that the SECS/GEM module must be installed
before these functions will be accessible.
"""

from __future__ import print_function

__all__ = [
    "copyEquipment",
    "deleteToolProgram",
    "enableDisableEquipment",
    "getResponse",
    "getToolProgram",
    "getToolProgramDataset",
    "sendRequest",
    "sendResponse",
    "startSimEventRun",
    "toDataSet",
    "toTreeDataSet",
]

from typing import Any, Dict, List, Optional, Tuple

from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import String
from java.util import Date


def copyEquipment(
    equipmentSource,  # type: String
    newEquipmentName,  # type: String
    enabled,  # type: bool
    activeAddress,  # type: String
    activePort,  # type: int
    passiveAddress,  # type: String
    passivePort,  # type: int
    deviceId,  # type: int
    dbTablePrefix=None,  # type: Optional[String]
    description=None,  # type: Optional[String]
):
    # type: (...) -> None
    """Creates a copy of an equipment connection.

    Common settings can be overridden for the new connection.

    An exception is thrown if the new Equipment Connection cannot be
    created.

    Args:
        equipmentSource: Some new equipment settings will be retrieved
            from this equipment connection. Specify the source equipment
            connection name.
        newEquipmentName: The name of the new equipment connection.
        enabled: If set to False, the new equipment connection will be
            disabled after it is created.
        activeAddress: IP Address of new equipment. Must be specified if
            the SECS/GEM module is used in Active mode. Otherwise, do
            not use this parameter.
        activePort: Port number of new equipment. Must be specified if
            the SECS/GEM module is used in Active mode. Otherwise, do
            not use this parameter.
        passiveAddress: IP Address of new equipment. Must be specified
            if the SECS/GEM module is used in Passive mode. Otherwise,
            do not use this parameter.
        passivePort: Port number of new equipment. Must be specified if
            the SECS/GEM module is used in Passive mode. Otherwise, do
            not use this parameter.
        deviceId: Unique identifier of new equipment. This value must be
            an integer, and is specified within the equipment.
        dbTablePrefix: SECS/GEM database table names will use the
            specified prefix for the new equipment connection. If no
            prefix is specified, the description of the source equipment
            will be used. Optional.
        description: The description for the new equipment connection.
            If no description is specified, the description of the
            source equipment will be used. Optional.
    """
    print(
        equipmentSource,
        newEquipmentName,
        enabled,
        activeAddress,
        activePort,
        passiveAddress,
        passivePort,
        deviceId,
        dbTablePrefix,
        description,
    )


def deleteToolProgram(ppid):
    # type: (String) -> None
    """Deletes a process program from the Gateway.

    Args:
        ppid: The PPID that was sent from the tool when the S7F3 message
            was saved.
    """
    print(ppid)


def enableDisableEquipment(enable, names):
    # type: (bool, Tuple[String, ...]) -> List[unicode]
    """Enables or disables a Tuple of equipment connections from a
    script.

    Args:
        enable: Set to True to enable equipment connections, or set to
            False to disable them.
        names: A Tuple of Strings. Each String should match an Equipment
            Connection configured on the Gateway. If this parameter
            contains the name of an Equipment Connection that does not
            exist, then a message will be included in the List returned
            by this function.

    Returns:
         A List of unicode strings. Each string contains a message about
         an equipment connection that could not be enabled/disabled. If
         the list is empty, then all specified equipment connections
         were successfully modified.
    """
    print(enable)
    for name in names:
        print(name)
    return [unicode("")]


def getResponse(transactionID, equipment, timeout=5, poll=150):
    # type: (int, String, Optional[int], Optional[int]) -> Any
    """Attempts to retrieve a response message from the Gateway.

    The transaction id from the sent message is used to retrieve the
    response.

    Args:
        transactionID: The transactionID of the request and response.
            The transactionID is used to retrieve the response.
            Typically used in conjunction with
            system.secsgem.sendRequest to generate a transactionID.
        equipment: Name of equipment connection.
        timeout: Specifies in seconds how long to wait for a response
            before returning None. If omitted the timeout will be 5
            seconds. Optional.
        poll: Specifies in milliseconds how often to poll the system for
            a response. If omitted the poll will be 150 milliseconds.
            Optional.

    Returns:
        A Python object, typically a dictionary. The actual result is a
        JSON string that's decoded into a python object, as shown on the
        mapping on the system.util.jsonDecode page.
    """
    print(transactionID, equipment, timeout, poll)
    return ""


def getToolProgram(ppid):
    # type: (String) -> Dict[String, Any]
    """Returns a process program from the Gateway that was previously
    sent by a a tool in an S7F3 message.

    Args:
        ppid: The PPID that was sent from the tool when the S7F3 message
            was saved.

    Returns:
        A Python Dictionary containing the following keys: editDate,
        ppbody, bodyFormat.
    """
    print(ppid)
    return {
        "editDate": Date(),
        "ppBody": "program",
        "bodyFormat": "A",
    }


def getToolProgramDataset():
    # type: () -> BasicDataset
    """Returns a Dataset containing information about all stored process
    programs.

    Returns:
         A Dataset containing information about all stored process
         programs. Includes the following columns in order: ppid,
         editDate, bodyFormat.
    """
    return BasicDataset()


def sendRequest(streamFunction, reply, body, equipment):
    # type: (String, bool, Any, String) -> int
    """Sends a JSON-formatted SECS message to a tool.

    An equipment connection must be configured for the tool in the
    Gateway.

    Args:
        streamFunction: The stream and function of the SECS message to
            send. Example: "S1F13"
        reply: Whether or not the SECS message expects a reply message.
        body: This contains the body of a SECS message. The argument can
            be a Python Object or JSON string representing the body of a
            SECS message. If this argument is a string then it will be
            converted to a Python Object using the
            system.util.jsonDecode function.
        equipment: Name of the equipment connection to use.

    Returns:
        The transactionID of the SECS message response.
    """
    print(streamFunction, reply, body, equipment)
    return 0


def sendResponse(transactionID, systemBytes, streamFunction, body, equipment):
    # type: (int, int, String, Any, String) -> None
    """Sends a JSON-formatted SECS response message to a message sent by
    a tool.

    An equipment connection must be configured for the tool in the
    Gateway, and this must be used within a Message Handler to create a
    Custom Message Response Handler.

    Args:
        transactionID: The TxID of the response. The TxID from the
            received request in the payload of the message handler must
            be specified here.
        systemBytes: The SystemBytes of the response. The SystemBytes
            from the received request in the payload of the message
            handler must be specified here.
        streamFunction: The stream and function of the SECS message to
            send. Example: "S1F14".
        body: This contains the body of a SECS response. The argument
            can be a Python Object or JSON string representing the body
            of a SECS message. If this argument is a string then it will
            be converted to a Python Object using the
            system.util.jsonDecode function.
        equipment: Name of the equipment connection to use.
    """
    print(transactionID, systemBytes, streamFunction, body, equipment)


def startSimEventRun(simulatorName, eventRunName):
    # type: (String, String) -> None
    """Starts a configured simulator event run in the Gateway.

    Note, that this function only works with the simulators that come
    included with the SECS/GEM module.

    The function will throw an exception if the specified Event Run
    cannot be started.

    Args:
        simulatorName: The simulator that holds the configured event
            run. Will throw an exception if the specified simulator
            can't be found.
        eventRunName: The event run to start. Will throw an exception if
            the specified simulator can't be found.
    """
    print(simulatorName, eventRunName)


def toDataSet(secsObject):
    # type: (Any) -> BasicDataset
    """Converts a SECS message data structure, as returned by the
    system.secsgem.getResponse function, into a dataset and returns it.

    Args:
        secsObject: A Python object, such as Sequence or a Dictionary,
            representing a SECS message to convert to a dataset.

    Returns:
         A Dataset representing a SECS message.
    """
    print(secsObject)
    return BasicDataset()


def toTreeDataSet(dataset):
    # type: (BasicDataset) -> BasicDataset
    """Changes an existing dataset, as returned by the
    system.secsgem.toDataSet function, to make it usable for the Tree
    View component.

    Args:
        dataset: A dataset containing a SECS message. Note that this
            parameter cannot take a JSON message, so the object returned
            by system.secsgem.getResponse must first be processed by
            system.secsgem.toDataSet.

    Returns:
        A dataset containing a SECS message with the following columns,
        as suited for Vision's tree view component: "path", "text",
        "icon", "background", "foreground", "tooltip", "border",
        "selectedText", "selectedIcon", "selectedBackground",
        "selectedForeground", "selectedTooltip", "selectedBorder".
    """
    print(dataset)
    return BasicDataset()
