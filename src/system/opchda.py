"""OPC HDA Functions.

The following functions give you access to interact with the HDA types
of OPC servers.
"""

from __future__ import print_function

__all__ = [
    "browse",
    "getAggregates",
    "getAttributes",
    "getServers",
    "insert",
    "insertReplace",
    "isServerAvailable",
    "readAttributes",
    "readProcessed",
    "readRaw",
    "replace",
]

from typing import Any, List

from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import QualityCode
from com.inductiveautomation.ignition.common.sqltags.history import AggregateInfo
from java.lang import String
from java.util import Date


def browse(root):
    # type: (String) -> List[Results]
    """Performs a browse at the given root.

    Args:
        root: The root at which to browse. Needs to be a qualified path.

    Returns:
        The results of the browse operation from the given root.
    """
    print(root)
    return [Results()]


def getAggregates(serverName):
    # type: (String) -> List[AggregateInfo]
    """Will query the Server for aggregates that it supports.

    Args:
        serverName: The name of the defined OPC-HDA Server to query.

    Returns:
        A list of supported Aggregate objects. Each object has 'id',
        'name', and 'desc' properties defined.
    """
    print(serverName)
    return [AggregateInfo()]


def getAttributes(serverName):
    # type: (String) -> List[AggregateInfo]
    """Queries the given Server for the item attributes that are
    available with system.opchda.readAttributes().

    Args:
        serverName: The name of the defined OPC-HDA Server to query.

    Returns:
        A list of supported Aggregate objects. Each object has 'id',
        'name', and 'desc' properties defined.
    """
    print(serverName)
    return [AggregateInfo()]


def getServers():
    # type: () -> List[String]
    """Returns a list of the OPC-HDA servers configured on the system.

    This call will return all configured and enabled servers, including
    those that are not currently connected.

    Returns:
        A list of the string names of servers.
    """
    return []


def insert(serverName, itemId, value, date, quality):
    # type: (String, String, Any, Any, int) -> QualityCode
    """Insert values on the OPC-HDA Server if the given item ID does not
    exist.

    Args:
        serverName: The name of the defined OPC-HDA Server.
        itemId: The item ID on which to perform the operation.
        value: The value to insert.
        date: The date to insert.
        quality: The quality to insert.

    Returns:
        The result of the insert.
    """
    print(serverName, itemId, value, date, quality)
    return QualityCode()


def insertReplace(serverName, itemId, value, date, quality):
    # type: (String, String, Any, Date, int) -> QualityCode
    """Will insert values on the OPC-HDA Server, or replace them if they
    already exist.

    Args:
        serverName: The name of the defined OPC-HDA Server.
        itemId: The item ID on which to perform the operation.
        value: The value to insert or replace.
        date: The date to insert or replace.
        quality: The quality to insert or replace.

    Returns:
        The items quality form the operation.
    """
    print(serverName, itemId, value, date, quality)
    return QualityCode()


def isServerAvailable(serverName):
    # type: (String) -> bool
    """Checks to see if the specified OPC-HDA Server is defined,
    enabled, and connected.

    Args:
        serverName: The name of the OPC-HDA Server to check.

    Returns:
        True if the Server is available and can be queried, False if
        not.
    """
    print(serverName)
    return True


def readAttributes(serverName, itemId, attributeIds, startDate, endDate):
    # type: (String, String, String, Date, Date) -> List[Any]
    """Reads the specified attributes for the given item over a time
    range.

    Attributes and their IDs are defined in the OPC-HDA specification,
    and can be discovered by calling system.opchda.getAttributes().

    Args:
        serverName: The name of the defined OPC-HDA Server to read.
        itemId: The itemID to retrieve attributes for.
        attributeIds: The integer IDs of the attributes to read. The
            attribute ids are defined in the OPC-HDA specification. The
            attributes can also be obtained by calling
            system.opchda.getAttributes(). Some servers may not support
            all attributes.
        startDate: The starting date/time of the query.
        endDate: The ending date/time of the query.

    Returns:
        A list of read results which is one-to-one with the requested
        attributes. The ReadResult object has a 'serviceResult' quality
        property that indicates whether the call was successful, and is
        itself a list of QualifiedValues.
    """
    print(serverName, itemId, attributeIds, startDate, endDate)
    return []


def readProcessed(
    serverName,  # type: String
    itemIds,  # type: List[String]
    startDate,  # type: Date
    endDate,  # type: Date
    resampleIntervalMS,  # type: int
    aggregates,  # type: List[Any]
):
    # type: (...) -> List[Any]
    """Reads processed values from the OPC-HDA Server.

    Processed values are calculated values, based on the aggregate
    function requested for each item. The list of aggregates can be
    obtained by calling system.opchda.getAggregates().

    Args:
        serverName: The name of the defined OPC-HDA Server to read.
        itemIds: A list of item ids to read.
        startDate: The starting date/time of the query.
        endDate: The ending date/time of the query.
        resampleIntervalMS: The interval, in milliseconds, that each
            value should cover.
        aggregates: A list which should be one-to-one with the item ids
            requested, specifying the integer id of the aggregation
            function to use. The aggregation ids are defined in the
            OPC-HDA specification. The list of aggregates can also be
            obtained by calling system.opchda.getAggregates().

    Returns:
        A list of read results which is one-to-one with the item IDs
        passed in. The ReadResult object has a 'serviceResult' quality
        property that indicates whether the call was successful, and is
        itself a list of QualifiedValues.
    """
    print(
        serverName,
        itemIds,
        startDate,
        endDate,
        resampleIntervalMS,
        aggregates,
    )
    return []


def readRaw(
    serverName,  # type: String
    itemIds,  # type: List[String]
    startDate,  # type: Date
    endDate,  # type: Date
    maxValues,  # type: int
    boundingValues,  # type: bool
):
    # type: (...) -> List[Any]
    """Reads raw values from the OPC-HDA Server.

    Args:
        serverName: The name of the defined OPC-HDA Server to read.
        itemIds: A list of item ids to read.
        startDate: The starting date/time of the query.
        endDate: The ending date/time of the query.
        maxValues: The maximum number of values to return. 0 or less
            means unlimited.
        boundingValues: A boolean indicating whether or not the
            "bounding values" should be included in the result set. The
            bounding values provide a value exactly at the start and end
            dates, but may be resource-intensive to retrieve.

    Returns:
        A list of read results which is one-to-one with the item IDs
        passed in. The ReadResult object has a 'serviceResult' quality
        property that indicates whether the call was successful, and is
        itself a list of QualifiedValues.
    """
    print(serverName, itemIds, startDate, endDate, maxValues, boundingValues)
    return []


def replace(serverName, itemId, value, date, quality):
    # type: (String, String, Any, Date, int) -> QualityCode
    """Replaces values on the OPC-HDA Server if the given item ID
    exists.

    Args:
        serverName: The name of the defined OPC-HDA Server.
        itemId: The item ID to perform the operation on.
        value: The value to replace.
        date: The date to replace.
        quality: The quality to replace.

    Returns:
        The items quality resulting from the operation.
    """
    print(serverName, itemId, value, date, quality)
    return QualityCode()
