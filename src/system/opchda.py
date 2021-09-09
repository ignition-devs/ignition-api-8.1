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

from abc import ABCMeta, abstractmethod

from java.lang import Object
from java.util import Date


class Aggregate(ABCMeta):
    """This interface defines an aggregation function used by the
    history query system.

    Different types of history providers may support different Aggregate
    functions, and may define new types of aggregates. The name and
    description are for informational purposes, aggregates are only
    identified by their id (name and description should not be taken
    into account).

    The general implementation class is AggregateInfo. Common or "well
    known" aggregates are defined in the AggregationMode enum. The
    system works like this for historical reasons, previous to 7.7 only
    the AggregationMode aggregates were used. After, with the
    introduction of history providers as an extension point, new
    providers could define any aggregation function.
    """

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def getDesc(cls):
        pass

    @abstractmethod
    def getId(cls):
        pass

    @abstractmethod
    def getName(cls):
        pass


class Results(Object):
    """The results of a browse operation.

    May only represent a partial result set, which can be determined by
    comparing the Total Available Size to the Returned Size. If there is
    a mismatch, the continuation point should be non-null and can be
    used in constructing the subsequent BrowseFilter to continue the
    browse.
    """

    def error(self, result):
        pass

    def getContinuationPoint(self):
        pass

    def getResultQuality(self):
        pass

    def getResults(self):
        pass

    def getReturnedSize(self):
        pass

    def getTotalAvailableSize(self):
        pass

    def of(self, arg):
        pass

    def setContinuationPoint(self, continuationPoint):
        pass

    def setResultQuality(self, value):
        pass

    def setResults(self, results):
        pass

    def setTotalAvailableResults(self, totalAvailableResults):
        pass


def browse(root):
    """Performs a browse at the given root.

    Args:
        root (str): The root at which to browse. Needs to be a qualified
            path.

    Returns:
        list[Results]: The Browse Results that would result for the
            operation at that root. Refer to the list of Results
            objects.
    """
    print(root)
    return [Results()]


def getAggregates(serverName):
    """Will query the server for aggregates that it supports.

    Args:
        serverName (str): The name of the defined OPC-HDA server to
            query.

    Returns:
        list[Aggregate]: A list of supported Aggregate objects. Each
            object has 'id', 'name', and 'desc' properties defined.
    """
    print(serverName)
    return [Aggregate()]


def getAttributes(serverName):
    """Queries the given server for the item attributes that are
    available with system.opchda.readAttributes().

    Args:
        serverName (str): The name of the defined OPC-HDA server to
            query.

    Returns:
        list[Aggregate]: A list of supported Aggregate objects. Each
            object has 'id', 'name', and 'desc' properties defined.
    """
    print(serverName)
    return [Aggregate()]


def getServers():
    """Returns a list of the OPC-HDA servers configured on the system.

    This call will return all configured and enabled servers, including
    those that are not currently connected.

    Returns:
        list[str]: A list of the string names of servers.
    """
    return []


def insert(serverName, itemId, value, date, quality):
    """Insert values on the OPC-HDA server if the given item ID does not
    exist.

    Args:
        serverName (str): The name of the defined OPC-HDA server.
        itemId (str): The item ID to perform the operation on.
        value (object): The value to insert.
        date (object): The date to insert.
        quality (int): The quality to insert.

    Returns:
        int: The items quality form the operation.
    """
    print(serverName, itemId, value, date, quality)
    return 192


def insertReplace(serverName, itemId, value, date, quality):
    """Will insert values on the OPC-HDA server, or replace them if they
    already exist.

    Args:
        serverName (str): The name of the defined OPC-HDA server.
        itemId (str): The item ID to perform the operation on.
        value (object): The value to insert.
        date (object): The date to insert.
        quality (int): The quality to insert.

    Returns:
        int: The items quality form the operation.
    """
    print(serverName, itemId, value, date, quality)
    return 192


def isServerAvailable(serverName):
    """Checks to see if the specified OPC-HDA server is defined,
    enabled, and connected.

    Args:
        serverName (str): The name of the OPC-HDA server to check.

    Returns:
        bool: Will be True if the server is available and can be
            queried, False if not.
    """
    print(serverName)
    return True


def readAttributes(serverName, itemId, attributeIds, startDate, endDate):
    """Reads the specified attributes for the given item over a time
    range.

    Attributes and their IDs are defined in the OPC-HDA specification,
    and can be discovered by calling system.opchda.getAttributes().

    Args:
        serverName (str): The name of the defined OPC-HDA server to
            read.
        itemId (str): The itemID to retrieve attributes for.
        attributeIds (list[int]): The integer IDs of the attributes to
            read. The attribute ids are defined in the OPC-HDA
            specification. The attributes can also be obtained by
            calling system.opchda.getAttributes(). Some servers may not
            support all attributes.
        startDate (Date): The starting date/time of the query.
        endDate (Date): The ending date/time of the query.

    Returns:
        list[ReadResult]: A list of read results which is one-to-one
            with the requested attributes. The ReadResult object has a
            'serviceResult' quality property that indicates whether the
            call was successful, and is itself a list of
            QualifiedValues.
    """
    print(serverName, itemId, attributeIds, startDate, endDate)
    return []


def readProcessed(
    serverName, itemIds, startDate, endDate, resampleIntervalMS, aggregates
):
    """Reads processed values from the OPC-HDA server.

    Processed values are calculated values, based on the aggregate
    function requested for each item. The list of aggregates can be
    obtained by calling system.opchda.getAggregates().

    Args:
        serverName (str): The name of the defined OPC-HDA server to
            read.
        itemIds (list[str]): A list of item ids to read.
        startDate (Date): The starting date/time of the query.
        endDate (Date): The ending date/time of the query.
        resampleIntervalMS (int): The interval, in milliseconds, that
            each value should cover.
        aggregates (list[object]): A list which should be one-to-one
            with the item ids requested, specifying the integer id of
            the aggregation function to use. The aggregation ids are
            defined in the OPC-HDA specification. The list of aggregates
            can also be obtained by calling
            system.opchda.getAggregates().

    Returns:
        list[ReadResult]: A list of read results which is one-to-one
            with the item IDs passed in. The ReadResult object has a
            'serviceResult' quality property that indicates whether the
            call was successful, and is itself a list of
            QualifiedValues.
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
    serverName, itemIds, startDate, endDate, maxValues, boundingValues
):
    """Reads raw values from the OPC-HDA server.

    Args:
        serverName (str): The name of the defined OPC-HDA server to
            read.
        itemIds (list[str]): A list of item ids to read.
        startDate (Date): The starting date/time of the query.
        endDate (Date): The ending date/time of the query.
        maxValues (int): The maximum number of values to return. 0 or
            less means unlimited.
        boundingValues (bool): A boolean indicating whether or not the
            "bounding values" should be included in the result set. The
            bounding values provide a value exactly at the start and end
            dates, but may be resource-intensive to retrieve.

    Returns:
        list[ReadResult]: A list of read results which is one-to-one
            with the item IDs passed in. The ReadResult object has a
            'serviceResult' quality property that indicates whether the
            call was successful, and is itself a list of
            QualifiedValues.
    """
    print(serverName, itemIds, startDate, endDate, maxValues, boundingValues)
    return []


def replace(serverName, itemId, value, date, quality):
    """Replaces values on the OPC-HDA server if the given item ID
    exists.

    Args:
        serverName (str): The name of the defined OPC-HDA server.
        itemId (str): The item ID to perform the operation on.
        value (object): The value to replace.
        date (Date): The date to replace.
        quality (int): The quality to replace.

    Returns:
        int: The item's quality resulting from the operation.
    """
    print(serverName, itemId, value, date, quality)
    return 192
