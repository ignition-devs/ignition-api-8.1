"""Device Functions.

The following functions give you access to view and edit device
connections in the Gateway.
"""

from __future__ import print_function

__all__ = [
    "addDevice",
    "getDeviceHostname",
    "listDevices",
    "refreshBrowse",
    "removeDevice",
    "restart",
    "setDeviceEnabled",
    "setDeviceHostname",
]

from typing import Any, Dict, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import String


def addDevice(
    deviceType,  # type: String
    deviceName,  # type: String
    deviceProps,  # type: Dict[String, Any]
    description=None,  # type: Optional[String]
):
    # type: (...) -> None
    """Adds a new device connection in Ignition.

    Accepts a dictionary of parameters to configure the connection.
    Acceptable parameters differ by device type: i.e., a Modbus/TCP
    connection requires a hostname and port, but a simulator doesn't
    require any parameters. When using this function, the arguments must
    be passed in as keyword arguments.

    Args:
        deviceType: The device driver type.
        deviceName: The name that will be given to the new device
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
    # type: (String) -> String
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
    # type: (String) -> None
    """Forces Ignition to browse the controller.

    Only works for Allen-Bradley controllers.

    Args:
        deviceName: The name of the device in Ignition.
    """
    print(deviceName)


def removeDevice(deviceName):
    # type: (String) -> None
    """Removes a given device from Ignition.

    Args:
        deviceName: The name of the device in Ignition.
    """
    print(deviceName)


def restart(deviceName):
    # type: (String) -> None
    """Restarts the named device connection.

    Args:
        deviceName: The name of the device connection to restart. The
            function will throw an error if the specified deviceName
            does not exist on the host gateway.
    """
    print(deviceName)


def setDeviceEnabled(deviceName, enabled):
    # type: (String, bool) -> None
    """Enables/disables a device in Ignition.

    Args:
        deviceName: The name of the device in Ignition.
        enabled: Specifies whether the device connection will be set to
            enabled or disabled state.
    """
    print(deviceName, enabled)


def setDeviceHostname(deviceName, hostname):
    # type: (String, String) -> None
    """Changes the hostname of a device.

    Used for all Ethernet based drivers.

    Args:
        deviceName: The name of the device in Ignition.
        hostname: The new IP address or hostname.
    """
    print(deviceName, hostname)
