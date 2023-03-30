"""IEC 61850 Functions.

The following functions give you access to interact with IEC 61850
devices.
"""

from __future__ import print_function

__all__ = [
    "cancel",
    "getControlParams",
    "listFiles",
    "operate",
    "readFile",
    "select",
    "writeFile",
]

from typing import Any, Dict, List, Optional

from dev.thecesrom.helper.types import AnyStr


def cancel(deviceName, mapParams):
    # type: (AnyStr, Dict[AnyStr, Any]) -> None
    """Cancels the selection of an SBO type control on a configured IEC
    81650 device to prevent the operate command from performing.

    Args:
        deviceName: Name of the configured IEC 61850 device.
        mapParams: Control parameters dictionary that requires the
            following keys to be specified: name, T, orCat, orIdent,
            Check, and Test. These keys must match the params from the
            select function. If you do not know the required key value
            pairs, they can be found using the getControlParams
            function.
    """
    print(deviceName, mapParams)


def getControlParams(deviceName):
    # type: (AnyStr) -> List[Dict[AnyStr, Any]]
    """This function returns a list of report control names and their
    attributes contained in the configured IEC 61850 device.

    Args:
        deviceName: The name of the configured IEC 61850 device driver.

    Returns:
        A list of PyDictionaries.
    """
    print(deviceName)
    return [
        {
            "name": "SSSA_52AFA_FPRCTRL/CBCSWI1.Mod",
            "ctlModel": 1,
            "T": 1,
            "ctlNumb": 0,
            "orCat": 0,
            "orIdent": "not-supported",
            "Test": False,
        }
    ]


def listFiles(deviceName, remoteFilePath=None):
    # type: (AnyStr, Optional[AnyStr]) -> List[AnyStr]
    """This function returns a list of filenames from a remote path for
    the configured IEC 61850 device.

    Args:
        deviceName: The name of the configured IEC 61850 device.
        remoteFilePath: The remote file path on the server of the
            configured IEC 61850 device for the file to read. Optional.

    Returns:
        A list of filenames.
    """
    print(deviceName, remoteFilePath)
    return ["COMFEDE.ced"]


def operate(deviceName, mapParams, controlValue):
    # type: (AnyStr, Dict[AnyStr, Any], float) -> None
    """This function operates on the IEC 61850 device control
    immediately, such as to change the position of a switch. This can be
    done directly, or following a select command.

    Args:
        deviceName: Name of the configured IEC 61850 device.
        mapParams: Control parameters dictionary that requires the
            following keys to be specified: name, T, orCat, orIdent,
            Check, and Test. Use the same params as the select function
            when operating on an SBO type control. If you do not know
            the required key value pairs, they can be found using the
            getControlParams function.
        controlValue: Control value (32-bit float).
    """
    print(deviceName, mapParams, controlValue)


def readFile(deviceName, remoteFilePath, localFilePath):
    # type: (AnyStr, AnyStr, AnyStr) -> None
    """This function downloads remote files from the configured IEC
    61850 device to an identified local path.

    Args:
        deviceName: The name of the configured IEC 61850 device.
        remoteFilePath: The remote file path on the server of the file
            to read.
        localFilePath: The local file path on client to store the file
            contents.
    """
    print(deviceName, remoteFilePath, localFilePath)


def select(deviceName, mapParams, value):
    # type: (AnyStr, Dict[AnyStr, Any], float) -> None
    """Select an SBO type control to prepare it for a subsequent operate
    command for a configured IEC 61850 device. These selections can be
    removed by using the cancel function.

    Args:
        deviceName: Name of the configured IEC 61850 device.
        mapParams: Control parameters dictionary that requires the
            following keys to be specified: name, T, orCat, orIdent,
            Check, and Test. If you do not know the required key value
            pairs, they can be found using the getControlParams
            function.
        value: Control value (32-bit float).
    """
    print(deviceName, mapParams, value)


def writeFile(deviceName, localFilePath, remoteFilePath):
    # type: (AnyStr, AnyStr, AnyStr) -> None
    """This function uploads a file from a  local path to the configured
    IEC 61850 device remote path.

    Args:
        deviceName: The name of the configured IEC 61850 device.
        localFilePath: The local file path on client to pull the file
            contents from.
        remoteFilePath: Remote file path on server of the file to read.
    """
    print(deviceName, localFilePath, remoteFilePath)
