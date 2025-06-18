from typing import Any, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.script.builtin import (
    DatasetUtilities,
    SProcCall,
)
from dev.coatl.helper.types import AnyStr
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
    jdbcDriver: AnyStr,
    name: AnyStr,
    description: AnyStr = ...,
    connectUrl: Optional[AnyStr] = ...,
    username: Optional[AnyStr] = ...,
    password: Optional[AnyStr] = ...,
    props: Optional[AnyStr] = ...,
    validationQuery: Optional[AnyStr] = ...,
    maxConnections: int = ...,
) -> None: ...
def beginNamedQueryTransaction(*args: Any, **kwargs: Any) -> AnyStr: ...
def beginTransaction(
    database: Optional[AnyStr] = ...,
    isolationLevel: Optional[int] = ...,
    timeout: Optional[int] = ...,
) -> AnyStr: ...
def clearAllNamedQueryCaches(project: Optional[AnyStr] = ...) -> None: ...
def clearNamedQueryCache(*args: AnyStr, **kwargs: AnyStr) -> None: ...
def closeTransaction(tx: AnyStr) -> None: ...
def commitTransaction(tx: AnyStr) -> None: ...
def createSProcCall(
    procedureName: AnyStr,
    database: AnyStr = ...,
    tx: Optional[AnyStr] = ...,
    skipAudit: bool = ...,
) -> SProcCall: ...
def dateFormat(date: Date, formatPattern: AnyStr) -> AnyStr: ...
def execSProcCall(callContext: SProcCall) -> None: ...
def getConnectionInfo(name: Optional[AnyStr] = ...) -> BasicDataset: ...
def getConnections() -> BasicDataset: ...
def refresh(component: JComponent, propertyName: AnyStr) -> bool: ...
def removeDatasource(name: AnyStr) -> None: ...
def rollbackTransaction(tx: AnyStr) -> None: ...
def runNamedQuery(*args: Any, **kwargs: Any) -> Any: ...
def runPrepQuery(
    query: AnyStr, args: List[Any], database: AnyStr = ..., tx: Optional[AnyStr] = ...
) -> DatasetUtilities.PyDataSet: ...
def runPrepUpdate(
    query: AnyStr,
    args: List[Any],
    database: AnyStr = ...,
    tx: Optional[AnyStr] = ...,
    getKey: bool = ...,
    skipAudit: bool = ...,
) -> int: ...
def runQuery(
    query: AnyStr, database: AnyStr = ..., tx: Optional[AnyStr] = ...
) -> DatasetUtilities.PyDataSet: ...
def runSFNamedQuery(*args: Any, **kwargs: Any) -> bool: ...
def runSFPrepUpdate(
    query: AnyStr, args: List[Any], datasources: List[AnyStr]
) -> bool: ...
def runSFUpdateQuery(query: AnyStr, datasources: List[AnyStr]) -> bool: ...
def runScalarPrepQuery(
    query: AnyStr, args: List[Any], database: AnyStr = ..., tx: Optional[AnyStr] = ...
) -> Any: ...
def runScalarQuery(
    query: AnyStr, database: Optional[AnyStr] = ..., tx: Optional[AnyStr] = ...
) -> Any: ...
def runUpdateQuery(
    query: AnyStr,
    database: AnyStr = ...,
    tx: Optional[AnyStr] = ...,
    getKey: bool = ...,
    skipAudit: bool = ...,
) -> int: ...
def setDatasourceConnectURL(name: AnyStr, connectUrl: AnyStr) -> None: ...
def setDatasourceEnabled(name: AnyStr, enabled: bool) -> None: ...
def setDatasourceMaxConnections(name: AnyStr, maxConnections: int) -> None: ...
