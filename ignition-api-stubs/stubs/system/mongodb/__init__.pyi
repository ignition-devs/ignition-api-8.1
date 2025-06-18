from typing import Any, Dict, List, Optional, Union

from dev.coatl.helper.types import AnyStr
from org.python.core import PyObject

def aggregate(
    connector: AnyStr,
    collection: AnyStr,
    aggregate: List[Dict[AnyStr, Any]],
    collation: Optional[Dict[AnyStr, Any]] = ...,
) -> List[Dict[AnyStr, Any]]: ...
def deleteMany(
    connector: AnyStr,
    collection: AnyStr,
    filter: Dict[AnyStr, Any],
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> Dict[AnyStr, Any]: ...
def deleteOne(
    connector: AnyStr,
    collection: AnyStr,
    filter: Dict[AnyStr, Any],
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> Dict[AnyStr, Any]: ...
def find(
    connector: AnyStr,
    collection: AnyStr,
    filter: Dict[AnyStr, Any],
    project: Optional[Dict[AnyStr, Any]] = ...,
    sort: Optional[Dict[AnyStr, Any]] = ...,
    collation: Optional[Dict[AnyStr, Any]] = ...,
    limit: Optional[int] = ...,
    skip: Optional[int] = ...,
) -> List[Dict[AnyStr, Any]]: ...
def findOne(
    connector: AnyStr,
    collection: AnyStr,
    filter: Dict[AnyStr, Any],
    project: Optional[Dict[AnyStr, Any]] = ...,
) -> Dict[AnyStr, Any]: ...
def insertMany(
    connector: AnyStr,
    collection: AnyStr,
    document: List[Dict[AnyStr, Any]],
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> List[PyObject]: ...
def insertOne(
    connector: AnyStr,
    collection: AnyStr,
    document: Dict[AnyStr, Any],
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> PyObject: ...
def listCollectionNames(connector: AnyStr) -> List[AnyStr]: ...
def listConnectorInfo() -> List[Dict[AnyStr, Any]]: ...
def replaceOne(
    connector: AnyStr,
    collection: AnyStr,
    replacement: Dict[AnyStr, Any],
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> Dict[AnyStr, Any]: ...
def updateMany(
    connector: AnyStr,
    collection: AnyStr,
    filter: Dict[AnyStr, Any],
    updates: Union[Dict[AnyStr, Any], List[Dict[AnyStr, Any]]],
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> Dict[AnyStr, Any]: ...
def updateOne(
    connector: AnyStr,
    collection: AnyStr,
    filter: Dict[AnyStr, Any],
    updates: Union[Dict[AnyStr, Any], List[Dict[AnyStr, Any]]],
    options: Optional[Dict[AnyStr, Any]] = ...,
) -> Dict[AnyStr, Any]: ...
