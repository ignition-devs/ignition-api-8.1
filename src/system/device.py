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
    "setDeviceEnabled",
    "setDeviceHostname",
]

from system.dataset import Dataset


def addDevice(deviceType, deviceName, deviceProps, description=None):
    """Adds a new device connection in Ignition.

    Accepts a dictionary of parameters to configure the connection.
    Acceptable parameters differ by device type: i.e., a Modbus/TCP
    connection requires a hostname and port, but a simulator doesn't
    require any parameters.

    Args:
        deviceType (str): The device driver type. Possible values are
            listed in the Device Types table below.
        deviceName (str): The name that will be given to the the new
            device connection.
        deviceProps (dict): A dictionary of device connection properties
            and values. Each deviceType has different properties, but
            most require at least a hostname. Keys in the dictionary are
            case-insensitive, spaces are omitted, and the names of the
            properties that appear when manually creating a device
            connection.
        description (str): The description that will be given to the
            new device connection. Optional.
    """
    print(deviceType, deviceName, deviceProps, description)


def getDeviceHostname(deviceName):
    """Gets the hostname of a device.

    Args:
        deviceName (str): The name of the device in Ignition.

    Returns:
        str: The hostname of the device. Null if device doesn't have a
            hostname.
    """
    print(deviceName)


def listDevices():
    """Returns a dataset of information about each configured device.

    Each row represents a single device.

    Returns:
        Dataset: A dataset, where each row represents a device. Contains
            4 columns Name, Enabled, State, and Driver.
    """
    return Dataset()


def refreshBrowse(deviceName):
    """Forces Ignition to browse the controller.

    Only works for Allen-Bradley controllers.

    Args:
        deviceName (str): The name of the device in Ignition.
    """
    print(deviceName)


def removeDevice(deviceName):
    """Removes a given device from Ignition.

    Args:
        deviceName (str): The name of the device in Ignition.
    """
    print(deviceName)


def setDeviceEnabled(deviceName, enabled):
    """Enables/disables a device in Ignition.

    Args:
        deviceName (str): The name of the device in Ignition.
        enabled (bool): The enabled status of the device.
    """
    print(deviceName, enabled)


def setDeviceHostname(deviceName, hostname):
    """Changes the hostname of a device.

    Used for all ethernet based drivers.

    Args:
        deviceName (str): The name of the device in Ignition.
        hostname (str): The new IP address or hostname.
    """
    print(deviceName, hostname)
