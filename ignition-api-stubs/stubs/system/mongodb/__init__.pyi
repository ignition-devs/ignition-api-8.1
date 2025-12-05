from typing import Any, Dict, List, Optional, Union

from org.python.core import PyObject

def aggregate(
    connector: Union[str, unicode],
    collection: Union[str, unicode],
    aggregate: List[Dict[Union[str, unicode], Any]],
    collation: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> List[Dict[Union[str, unicode], Any]]: ...
def deleteMany(
    connector: Union[str, unicode],
    collection: Union[str, unicode],
    filter: Dict[Union[str, unicode], Any],
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> Dict[Union[str, unicode], Any]: ...
def deleteOne(
    connector: Union[str, unicode],
    collection: Union[str, unicode],
    filter: Dict[Union[str, unicode], Any],
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> Dict[Union[str, unicode], Any]: ...
def find(
    connector: Union[str, unicode],
    collection: Union[str, unicode],
    filter: Dict[Union[str, unicode], Any],
    project: Optional[Dict[Union[str, unicode], Any]] = ...,
    sort: Optional[Dict[Union[str, unicode], Any]] = ...,
    collation: Optional[Dict[Union[str, unicode], Any]] = ...,
    limit: Optional[int] = ...,
    skip: Optional[int] = ...,
) -> List[Dict[Union[str, unicode], Any]]: ...
def findOne(
    connector: Union[str, unicode],
    collection: Union[str, unicode],
    filter: Dict[Union[str, unicode], Any],
    project: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> Dict[Union[str, unicode], Any]: ...
def insertMany(
    connector: Union[str, unicode],
    collection: Union[str, unicode],
    document: List[Dict[Union[str, unicode], Any]],
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> List[PyObject]: ...
def insertOne(
    connector: Union[str, unicode],
    collection: Union[str, unicode],
    document: Dict[Union[str, unicode], Any],
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> PyObject: ...
def listCollectionNames(
    connector: Union[str, unicode],
) -> List[Union[str, unicode]]: ...
def listConnectorInfo() -> List[Dict[Union[str, unicode], Any]]: ...
def replaceOne(
    connector: Union[str, unicode],
    collection: Union[str, unicode],
    replacement: Dict[Union[str, unicode], Any],
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> Dict[Union[str, unicode], Any]: ...
def updateMany(
    connector: Union[str, unicode],
    collection: Union[str, unicode],
    filter: Dict[Union[str, unicode], Any],
    updates: Union[
        Dict[Union[str, unicode], Any], List[Dict[Union[str, unicode], Any]]
    ],
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> Dict[Union[str, unicode], Any]: ...
def updateOne(
    connector: Union[str, unicode],
    collection: Union[str, unicode],
    filter: Dict[Union[str, unicode], Any],
    updates: Union[
        Dict[Union[str, unicode], Any], List[Dict[Union[str, unicode], Any]]
    ],
    options: Optional[Dict[Union[str, unicode], Any]] = ...,
) -> Dict[Union[str, unicode], Any]: ...
