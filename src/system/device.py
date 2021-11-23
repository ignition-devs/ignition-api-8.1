"""Device Functions.

The following functions give you access to view and edit device
connections in the Gateway.
"""

from __future__ import print_function, unicode_literals

__all__ = [
    "addDevice",
    "getDeviceHostname",
    "listDevices",
    "refreshBrowse",
    "removeDevice",
    "setDeviceEnabled",
    "setDeviceHostname",
]

from typing import Any, Dict, Optional, Union

from com.inductiveautomation.ignition.common import BasicDataset


def addDevice(
    deviceType,  # type: Union[str, unicode]
    deviceName,  # type: Union[str, unicode]
    deviceProps,  # type: Dict[Union[str, unicode], Any]
    description,  # type: Optional[Union[str, unicode]]
):
    # type: (...) -> None
    """Adds a new device connection in Ignition.

    Accepts a dictionary of parameters to configure the connection.
    Acceptable parameters differ by device type: i.e., a Modbus/TCP
    connection requires a hostname and port, but a simulator doesn't
    require any parameters.

    Args:
        deviceType: The device driver type. Possible values are listed
            in the Device Types table below.
        deviceName: The name that will be given to the the new device
            connection.
        deviceProps: A dictionary of device connection properties and
            values. Each deviceType has different properties, but most
            require at least a hostname. Keys in the dictionary are
            case-insensitive, spaces are omitted, and the names of the
            properties that appear when manually creating a device
            connection.
        description: The description that will be given to the new
            device connection. Optional.
    """
    print(deviceType, deviceName, deviceProps, description)


def getDeviceHostname(deviceName):
    # type: (Union[str, unicode]) -> Union[str, unicode]
    """Gets the hostname of a device.

    Args:
        deviceName: The name of the device in Ignition.

    Returns:
        The hostname of the device. Null if device doesn't have a
        hostname.
    """
    print(deviceName)
    return ""


def listDevices():
    # type: () -> BasicDataset
    """Returns a dataset of information about each configured device.

    Each row represents a single device.

    Returns:
        A dataset, where each row represents a device. Contains 4
        columns Name, Enabled, State, and Driver.
    """
    return BasicDataset()


def refreshBrowse(deviceName):
    # type: (Union[str, unicode]) -> None
    """Forces Ignition to browse the controller.

    Only works for Allen-Bradley controllers.

    Args:
        deviceName: The name of the device in Ignition.
    """
    print(deviceName)


def removeDevice(deviceName):
    # type: (Union[str, unicode]) -> None
    """Removes a given device from Ignition.

    Args:
        deviceName: The name of the device in Ignition.
    """
    print(deviceName)


def setDeviceEnabled(deviceName, enabled):
    # type: (Union[str, unicode], bool) -> None
    """Enables/disables a device in Ignition.

    Args:
        deviceName: The name of the device in Ignition.
        enabled: The enabled status of the device.
    """
    print(deviceName, enabled)


def setDeviceHostname(deviceName, hostname):
    # type: (Union[str, unicode], Union[str, unicode]) -> None
    """Changes the hostname of a device.

    Used for all ethernet based drivers.

    Args:
        deviceName: The name of the device in Ignition.
        hostname: The new IP address or hostname.
    """
    print(deviceName, hostname)
