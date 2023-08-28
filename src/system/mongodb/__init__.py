"""MongoDB Functions.

The following functions allow users to interact with a MongoDB instance.
These functions require the MongoDB connector.
"""

from __future__ import print_function

__all__ = [
    "aggregate",
    "deleteMany",
    "deleteOne",
    "find",
    "findOne",
    "insertMany",
    "insertOne",
    "listCollectionNames",
    "listConnectorInfo",
    "replaceOne",
    "updateMany",
    "updateOne",
]

from typing import Any, Dict, List, Optional, Union

from dev.thecesrom.helper.types import AnyStr
from org.python.core import PyObject


def aggregate(
    connector,  # type: AnyStr
    collection,  # type: AnyStr
    aggregate,  # type: List[Dict[AnyStr, Any]]
    collation=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> List[Dict[AnyStr, Any]]
    """Returns a list of aggregate results.

    Args:
        connector: The name of connector (case-insensitive).
        collection: The name of collection (case-sensitive).
        aggregate: A list of PyDictionaries to specify an aggregate
            pipeline.
        collation: A PyDictionary of items to specify language-specific
            rules. Optional.

    Returns:
        A list of PyDictionary results containing aggregation results.
    """
    print(connector, collection, aggregate, collation)
    return [{}]


def deleteMany(
    connector,  # type: AnyStr
    collection,  # type: AnyStr
    filter,  # type: Dict[AnyStr, Any]
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> Dict[AnyStr, Any]
    """Removes documents from the collection that match the filter.

    Args:
        connector: The name of connector (case-insensitive).
        collection: The name of collection (case-sensitive).
        filter: A PyDictionary for specifying matching key value pair
            criteria when querying a collection.
        options: A PyDictionary for including additional replace
            configurations. Optional.

    Returns:
        Result of delete action formatted as a PyDictionary with keys
        'acknowledged' and 'deleteCount'.
    """
    print(connector, collection, filter, options)
    return {"acknowledged": True, "deleteCount": 42}


def deleteOne(
    connector,  # type: AnyStr
    collection,  # type: AnyStr
    filter,  # type: Dict[AnyStr, Any]
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> Dict[AnyStr, Any]
    """Removes a document from the collection that matches the filter.

    Args:
        connector: The name of connector (case-insensitive).
        collection: The name of collection (case-sensitive).
        filter: A PyDictionary for specifying matching key value pair
            criteria when querying a collection.
        options: A PyDictionary for including additional replace
            configurations. Optional.

    Returns:
        Result of delete action formatted as a PyDictionary with keys
        'acknowledged' and 'deleteCount'.
    """
    print(connector, collection, filter, options)
    return {"acknowledged": True, "deleteCount": 1}


def find(
    connector,  # type: AnyStr
    collection,  # type: AnyStr
    filter,  # type: Dict[AnyStr, Any]
    project=None,  # type: Optional[Dict[AnyStr, Any]]
    sort=None,  # type: Optional[Dict[AnyStr, Any]]
    collation=None,  # type: Optional[Dict[AnyStr, Any]]
    limit=None,  # type: Optional[int]
    skip=None,  # type: Optional[int]
):
    # type: (...) -> List[Dict[AnyStr, Any]]
    """Returns a list of PyDictionaries that matches the criteria
    specified on the filter parameter.

    Args:
        connector: The name of connector (case-insensitive).
        collection: The name of collection (case-insensitive).
        filter: A PyDictionary for specifying matching key value pair
            criteria when querying a collection.
        project: A PyDictionary for including or omitting specific key
            value pairs in the query result. Optional.
        sort: A PyDictionary of specified items to sort returned
            results. Optional.
        collation: A PyDictionary of items to specify language-specific
            rules. Optional.
        limit: The maximum number of PyDictionaries that will be
            returned. Optional.
        skip: The number of PyDictionaries to skip before returning
            results. Optional.

    Returns:
        A list of PyDictionary results.
    """
    print(connector, collection, filter, project, sort, collation, limit, skip)
    return [{}]


def findOne(
    connector,  # type: AnyStr
    collection,  # type: AnyStr
    filter,  # type: Dict[AnyStr, Any]
    project=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> Dict[AnyStr, Any]
    """Returns a single PyDictionary that matches the criteria specified
    on the filter parameter.

    Args:
        connector: The name of connector (case-insensitive).
        collection: The name of collection (case-insensitive).
        filter: A PyDictionary for specifying matching key value pair
            criteria when querying a collection.
        project: A PyDictionary for including or omitting specific key
            value pairs in the query result. Optional.

    Returns:
        A single PyDictionary as a result.
    """
    print(connector, collection, filter, project, collection)
    return {}


def insertMany(
    connector,  # type: AnyStr
    collection,  # type: AnyStr
    document,  # type: List[Dict[AnyStr, Any]]
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> List[PyObject]
    """Inserts a list of PyDictionaries into a specified collection.

    Args:
        connector: The name of connector (case-insensitive).
        collection: The name of collection (case-insensitive).
        document: A list of PyDictionaries that will represent new
            records being added to the collection.
        options: A PyDictionary for including additional insert
            configurations.

    Returns:
        Keys representing the inserted documents. The keys will usually
        be BSON document ObjectId, unless a different key type is
        specified.
    """
    print(connector, collection, document, options)
    return [PyObject()]


def insertOne(
    connector,  # type: AnyStr
    collection,  # type: AnyStr
    document,  # type: Dict[AnyStr, Any]
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> PyObject
    """Inserts a single PyDictionary into a specified collection.

    Args:
        connector: The name of connector (case-insensitive).
        collection: The name of collection (case-insensitive).
        document: A PyDictionary of specified fields that will represent
            a record being added to the collection.
        options: A PyDictionary for including additional insert
            configurations.

    Returns:
        Key of inserted document. This will usually be BSON document
        ObjectId, unless a different key type is specified.
    """
    print(connector, collection, document, options)
    return PyObject()


def listCollectionNames(connector):
    # type: (AnyStr) -> List[AnyStr]
    """Returns a list of all collection names.

    Args:
        connector: Name of connector (case-insensitive).

    Returns:
        A List of all collection names.
    """
    print(connector)
    return ["collection"]


def listConnectorInfo():
    # type: () -> List[Dict[AnyStr, Any]]
    """Returns a list of PyDictionary descriptors of all MongoDB
    Connectors.

    Returns:
        A list of PyDictionaries containing MongoDB Connector
        descriptors. Descriptor contains keys for 'name', 'description',
        'status', and 'error' (if present).
    """
    return [
        {
            "name": "name",
            "description": "This is the description.",
            "status": "The status.",
            "error": None,
        }
    ]


def replaceOne(
    connector,  # type: AnyStr
    collection,  # type: AnyStr
    replacement,  # type: Dict[AnyStr, Any]
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> Dict[AnyStr, Any]
    """Replaces a document in the collection that matches the filter.

    Args:
        connector: The name of connector (case-insensitive).
        collection: The name of collection (case-insensitive).
        replacement: A PyDictionary for specifying matching key value
            pair criteria when querying a collection.
        options: A PyDictionary for including additional replace
            configurations.

    Returns:
        Result of replace action formatted as a PyDictionary with keys
        'acknowledged', 'modifiedCount', 'matchedCount', and
        'upsertedId'.
    """
    print(connector, collection, replacement, options)
    return {
        "acknowledged": True,
        "modifiedCount": 1,
        "matchedCount": 1,
        "upsertedId": 1,
    }


def updateMany(
    connector,  # type: AnyStr
    collection,  # type: AnyStr
    filter,  # type: Dict[AnyStr, Any]
    updates,  # type: Union[Dict[AnyStr, Any], List[Dict[AnyStr, Any]]]
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> Dict[AnyStr, Any]
    """Updates all documents in the collection that match the filter.

    Args:
        connector: The name of connector (case-insensitive).
        collection: The name of collection (case-insensitive).
        filter: A PyDictionary for specifying matching key value pair
            criteria when querying a collection.
        updates: Changes to apply to specific document fields.
        options: A PyDictionary for including additional update
            configurations. Optional.

    Returns:
         Result of update action formatted as a PyDictionary with keys
         'acknowledged', 'modifiedCount', 'matchedCount', and
         'upsertedId'.
    """
    print(connector, collection, filter, updates, options)
    return {
        "acknowledged": True,
        "modifiedCount": 1,
        "matchedCount": 1,
        "upsertedId": 1,
    }


def updateOne(
    connector,  # type: AnyStr
    collection,  # type: AnyStr
    filter,  # type: Dict[AnyStr, Any]
    updates,  # type: Union[Dict[AnyStr, Any], List[Dict[AnyStr, Any]]]
    options=None,  # type: Optional[Dict[AnyStr, Any]]
):
    # type: (...) -> Dict[AnyStr, Any]
    """Updates a document in the collection that matches the filter.

    Args:
        connector: The name of connector (case-insensitive).
        collection: The name of collection (case-insensitive).
        filter: A PyDictionary for specifying matching key value pair
            criteria when querying a collection.
        updates: Changes to apply to specific document fields.
        options: A PyDictionary for including additional update
            configurations. Optional.

    Returns:
        Result of update action formatted as a PyDictionary with keys
        'acknowledged', 'modifiedCount', 'matchedCount', and
        'upsertedId'.
    """
    print(connector, collection, filter, updates, options)
    return {
        "acknowledged": True,
        "modifiedCount": 1,
        "matchedCount": 1,
        "upsertedId": 1,
    }
