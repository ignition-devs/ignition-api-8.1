from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.script.builtin import (
    DatasetUtilities,
    SProcCall,
)
from java.util import Date
from javax.swing import JComponent

BIT: int
REAL: int
LONGVARCHAR: int
LONGVARBINARY: int
TINYINT: int
DOUBLE: int
DATE: int
NULL: int
SMALLINT: int
NUMERIC: int
TIME: int
ROWID: int
INTEGER: int
DECIMAL: int
TIMESTAMP: int
CLOB: int
BIGINT: int
CHAR: int
BINARY: int
NCLOB: int
FLOAT: int
VARCHAR: int
VARBINARY: int
BLOB: int
NCHAR: int
NVARCHAR: int
LONGNVARCHAR: int
BOOLEAN: int
ORACLE_CURSOR: int
DISTINCT: int
STRUCT: int
REF: int
JAVA_OBJECT: int
SQLXML: int
ARRAY: int
DATALINK: int
OTHER: int
READ_COMMITTED: int
READ_UNCOMMITTED: int
REPEATABLE_READ: int
SERIALIZABLE: int

def addDatasource(
    jdbcDriver: Union[str, unicode],
    name: Union[str, unicode],
    description: Union[str, unicode] = ...,
    connectUrl: Union[str, unicode, None] = ...,
    username: Union[str, unicode, None] = ...,
    password: Union[str, unicode, None] = ...,
    props: Union[str, unicode, None] = ...,
    validationQuery: Union[str, unicode, None] = ...,
    maxConnections: int = ...,
) -> None: ...
def beginNamedQueryTransaction(*args: Any, **kwargs: Any) -> Union[str, unicode]: ...
def beginTransaction(
    database: Union[str, unicode] = ...,
    isolationLevel: Optional[int] = ...,
    timeout: Optional[int] = ...,
) -> Union[str, unicode]: ...
def clearAllNamedQueryCaches(project: Union[str, unicode, None] = ...) -> None: ...
def clearNamedQueryCache(
    *args: Union[str, unicode], **kwargs: Union[str, unicode]
) -> None: ...
def closeTransaction(tx: Union[str, unicode]) -> None: ...
def commitTransaction(tx: Union[str, unicode]) -> None: ...
def createSProcCall(
    procedureName: Union[str, unicode],
    database: Union[str, unicode] = ...,
    tx: Union[str, unicode, None] = ...,
    skipAudit: bool = ...,
) -> SProcCall: ...
def dateFormat(
    date: Date, formatPattern: Union[str, unicode]
) -> Union[str, unicode]: ...
def execSProcCall(callContext: SProcCall) -> None: ...
def getConnectionInfo(name: Union[str, unicode, None] = ...) -> BasicDataset: ...
def getConnections() -> BasicDataset: ...
def refresh(component: JComponent, propertyName: Union[str, unicode]) -> bool: ...
def removeDatasource(name: Union[str, unicode]) -> None: ...
def rollbackTransaction(tx: Union[str, unicode]) -> None: ...
def runNamedQuery(*args: Any, **kwargs: Any) -> Any: ...
def runPrepQuery(
    query: Union[str, unicode],
    args: List[Any],
    database: Union[str, unicode] = ...,
    tx: Union[str, unicode, None] = ...,
) -> DatasetUtilities.PyDataSet: ...
def runPrepUpdate(
    query: Union[str, unicode],
    args: List[Any],
    database: Union[str, unicode] = ...,
    tx: Union[str, unicode, None] = ...,
    getKey: bool = ...,
    skipAudit: bool = ...,
) -> int: ...
def runQuery(
    query: Union[str, unicode],
    database: Union[str, unicode] = ...,
    tx: Union[str, unicode, None] = ...,
) -> DatasetUtilities.PyDataSet: ...
def runSFNamedQuery(*args: Any, **kwargs: Any) -> bool: ...
def runSFPrepUpdate(
    query: Union[str, unicode], args: List[Any], datasources: List[Union[str, unicode]]
) -> bool: ...
def runSFUpdateQuery(
    query: Union[str, unicode], datasources: List[Union[str, unicode]]
) -> bool: ...
def runScalarPrepQuery(
    query: Union[str, unicode],
    args: List[Any],
    database: Union[str, unicode] = ...,
    tx: Union[str, unicode, None] = ...,
) -> Any: ...
def runScalarQuery(
    query: Union[str, unicode],
    database: Union[str, unicode] = ...,
    tx: Union[str, unicode, None] = ...,
) -> Any: ...
def runUpdateQuery(
    query: Union[str, unicode],
    database: Union[str, unicode] = ...,
    tx: Union[str, unicode, None] = ...,
    getKey: bool = ...,
    skipAudit: bool = ...,
) -> int: ...
def setDatasourceConnectURL(
    name: Union[str, unicode], connectUrl: Union[str, unicode]
) -> None: ...
def setDatasourceEnabled(name: Union[str, unicode], enabled: bool) -> None: ...
def setDatasourceMaxConnections(
    name: Union[str, unicode], maxConnections: int
) -> None: ...
