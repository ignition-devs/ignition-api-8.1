from __future__ import print_function

__all__ = ["AbstractOPCUtilities", "DatasetUtilities", "SProcCall", "SystemUtilities"]

from typing import Any, Dict, List, Optional, Tuple, Union

from com.inductiveautomation.ignition.common import BasicDataset, Dataset
from com.inductiveautomation.ignition.common.model.values import QualityCode
from com.inductiveautomation.ignition.common.opc import BrowseElementType
from com.inductiveautomation.ignition.common.script.abc import AbstractJythonSequence
from com.inductiveautomation.ignition.common.script.message import Request
from java.lang import Class
from java.lang import Exception as JavaException
from java.lang import Object, String
from java.util import Locale
from org.python.core import PyFunction, PyObject
from org.slf4j import Logger


class AbstractOPCUtilities(Object):
    def browseServer(self, opcServer, nodeId):
        # type: (String, String) -> List[AbstractOPCUtilities.PyOPCTag]
        return [
            AbstractOPCUtilities.PyOPCTag(opcServer, nodeId, "", BrowseElementType())
        ]

    def getServers(self):
        pass

    def getServerState(self, opcServer):
        pass

    def isServerEnabled(self, serverName):
        pass

    def readValue(self, opcServer, itemPath):
        pass

    def readValues(self, opcServer, itemPaths):
        pass

    def setServerEnabled(self, serverName, enabled):
        pass

    def writeValue(self, *args, **kwargs):
        pass

    def writeValues(self, *args, **kwargs):
        pass

    class PyOPCTag(PyObject):
        displayName = None  # type: String
        elementType = None  # type: BrowseElementType
        nodeId = None  # type: String
        serverName = None  # type: String

        def __init__(self, serverName, nodeId, displayName, elementType):
            # type: (String, String, String, BrowseElementType) -> None
            self.serverName = serverName
            self.nodeId = nodeId
            self.displayName = displayName
            self.elementType = elementType
            super(AbstractOPCUtilities.PyOPCTag, self).__init__()

        def __findattr_ex__(self, name):
            # type: (String) -> PyObject
            pass

        def getDisplayName(self):
            # type: () -> String
            return self.displayName

        def getElementType(self):
            # type: () -> BrowseElementType
            return self.elementType

        def getNodeId(self):
            # type: () -> String
            return self.nodeId

        def getServerName(self):
            # type: () -> String
            return self.serverName


class DatasetUtilities(Object):
    @staticmethod
    def addColumn(*args):
        pass

    @staticmethod
    def addRow(*args):
        pass

    @staticmethod
    def addRows(*args):
        pass

    @staticmethod
    def appendDataset(ds1, ds2):
        pass

    @staticmethod
    def clearDataset(ds):
        pass

    @staticmethod
    def dataSetToExcel(headerRow, datasets):
        pass

    @staticmethod
    def dataSetToExcelBytes(headerRow, objects, nullsEmpty, sheetNames):
        pass

    @staticmethod
    def dataSetToExcelStreaming(headerRow, objects, out, nullsEmpty):
        pass

    @staticmethod
    def dataSetToHTML(headerRow, ds, title):
        pass

    @staticmethod
    def dataSetToHTMLStreaming(headerRow, ds, title, fw):
        pass

    @staticmethod
    def deleteRow(ds, row):
        pass

    @staticmethod
    def deleteRows(ds, rows):
        pass

    @staticmethod
    def filterColumns(dataset, columns):
        pass

    @staticmethod
    def formatDates(dataset, format, locale=Locale.US):
        pass

    @staticmethod
    def fromCSV(csv):
        pass

    @staticmethod
    def fromCSVJava(csv):
        pass

    @staticmethod
    def getColumnHeaders(ds):
        pass

    @staticmethod
    def insertColumn(*args):
        pass

    @staticmethod
    def insertRow(*args):
        pass

    @staticmethod
    def setValue(*args):
        pass

    @staticmethod
    def sort(
        ds,  # type: BasicDataset
        keyColumn,  # type: Union[int, String]
        ascending=None,  # type: Optional[bool]
        naturalOrdering=None,  # type: Optional[bool]
    ):
        # type: (...) -> BasicDataset
        pass

    @staticmethod
    def toCSV(*args, **kwargs):
        pass

    @staticmethod
    def toCSVJava(ds, showHeaders, forExport, localized=False):
        pass

    @staticmethod
    def toCSVJavaStreaming(ds, showHeaders, forExport, sw, localized):
        pass

    @staticmethod
    def toDataSet(*args):
        pass

    @staticmethod
    def toExcel(*args, **kwargs):
        pass

    @staticmethod
    def toJSONObject(data):
        pass

    @staticmethod
    def toPyDataSet(dataset):
        # type: (Dataset) -> PyDataSet
        pass

    @staticmethod
    def updateRow(ds, row, changes):
        pass

    class PyDataSet(Dataset, AbstractJythonSequence):
        def __init__(self, ds=None):
            # type: (Optional[Dataset]) -> None
            pass

        def getColumnCount(self):
            # type: () -> int
            """Returns the number of columns in the dataset.

            Returns:
                The number of columns in the dataset.
            """
            pass

        def getColumnIndex(self, colName):
            # type: (String) -> int
            """Returns the index of the column with the name colName.

            Args:
                colName: The name of the column.

            Returns:
                The index of the column with the name colName.
            """
            pass

        def getColumnName(self, col):
            # type: (int) -> String
            """Returns the name of the column at the index colIndex.

            Args:
                col: The column number. Zero-indexed.

            Returns:
                The name of the column at the index colIndex.
            """
            pass

        def getColumnNames(self):
            # type: () -> List[String]
            """Returns a list with the names of all the columns.

            Returns:
                A list with the names of all the columns.
            """
            pass

        def getColumnType(self, col):
            # type: (int) -> Class
            """Returns the type of the column at the index.

            Args:
                col: The column number. Zero-indexed.

            Returns:
                The type of the column at the index.
            """
            pass

        def getColumnTypes(self):
            # type: () -> List[Class]
            """Returns a list with the types of all the columns.

            Returns:
                A list with the types of all the columns.
            """
            pass

        def getPrimitiveValueAt(self, row, col):
            # type: (int, int) -> float
            """If the given column is a numeric type or a Date, then the
            value will be returned as a double.

            Args:
                row: The row index. Zero-based index.
                col: The column index. Zero-based index.

            Raises:
                IllegalArgumentException: if the value at row, col is
                    not a number or Date.
                UnsupportedOperationException: If the Dataset
                    implementation declines to implement this operation.
            """
            pass

        def getQualityAt(self, row, col):
            # type: (int, int) -> QualityCode
            """Returns the quality of the value at the given location.

            Args:
                row: The row index. Zero-based index.
                col: The column index. Zero-based index.

            Raises:
                ArrayIndexOutOfBoundsException: If the given row, col is
                    out of range and hasQualityData() returns true.
            """
            pass

        def getRowCount(self):
            # type: () -> int
            """Returns the number of rows in the dataset.

            Returns:
                The number of rows in the dataset.
            """
            pass

        def getValueAt(self, row, col):
            # type: (int, Union[int, String]) -> Any
            """Returns the value at the specified row index and column
            name or index.

            Args:
                row: The row number. Zero-indexed.
                col: The column number (zero-indexed) or name.

            Returns:
                The value found at the row and column.
            """
            pass

        def setData(self, data):
            # type: (Dataset) -> None
            """Used for serialization only."""
            pass


class SProcCall(Object):
    callFinished = False  # type: bool
    datasource = ""  # type: String
    params = None  # type: Dict[SProcCall.SProcArgKey, SProcCall.SProcArg]
    procedureName = None  # type: String
    resultset = None  # type: Dataset
    returnParam = None  # type: SProcCall.SProcArg
    skipAudit = None  # type: bool
    txId = None  # type: String
    updateCount = None  # type: int

    def getDataSource(self):
        # type: () -> String
        pass

    def getOutParamValue(self, param):
        # type: (Union[int, String]) -> Any
        print(self, param)
        return 0

    def getProcedureName(self):
        # type: () -> String
        pass

    def getResultSet(self):
        # type: () -> BasicDataset
        print(self)
        return BasicDataset()

    def getReturnValue(self):
        # type: () -> Any
        print(self)
        return 0

    def getTxId(self):
        # type: () -> String
        return "transaction_id"

    def getUpdateCount(self):
        # type: () -> int
        print(self)
        return 1

    def isSkipAudit(self):
        # type: () -> bool
        print(self)
        return False

    def registerInParam(self, param, typeCode, value):
        # type: (Union[int, String], int, Any) -> None
        print(self, param, typeCode, value)

    def registerOutParam(self, param, typeCode):
        # type: (Union[int, String], int) -> None
        print(self, param, typeCode)

    def registerReturnParam(self, typeCode):
        # type: (int) -> None
        print(self, typeCode)

    def setSkipAudit(self, skipAudit):
        # type: (bool) -> None
        pass

    def setTxId(self, txId):
        # type: (String) -> None
        pass

    class SProcArg(Object):
        outParam = False  # type: bool
        inParam = False  # type: bool
        paramType = None  # type: int
        value = None  # type: Object

        def getParamType(self):
            # type: () -> int
            pass

        def getValue(self):
            # type: () -> Any
            pass

        def isInParam(self):
            # type: () -> bool
            pass

        def isOutParam(self):
            # type: () -> bool
            pass

        def setParamType(self, paramType):
            # type: (int) -> None
            pass

        def setValue(self, value):
            # type: (Object) -> None
            pass

    class SProcArgKey(Object):
        index = -1  # type: int
        name = None  # type: String

        def getParamIndex(self):
            # type: () -> int
            pass

        def getParamName(self):
            # type: () -> String
            pass

        def isNamedParam(self):
            # type: () -> bool
            pass


class SystemUtilities(Object):
    @staticmethod
    def logger(loggerName):
        # type: (String) -> Logger
        pass

    @staticmethod
    def parseTranslateArguments(*args, **kwargs):
        # type: (PyObject, String) -> Tuple[String, String, bool]
        pass

    class RequestImpl(Object, Request):
        timeout = None  # type: int

        def __init__(self, timeout):
            # type: (int) -> None
            self.timeout = timeout

        def cancel(self):
            # type: () -> None
            pass

        def checkTimeout(self):
            # type: () -> None
            pass

        def finishExceptionally(self, e):
            # type: (JavaException) -> None
            pass

        def finishSuccessfully(self, value):
            # type: (Object) -> None
            pass

        def get(self):
            # type: () -> Object
            pass

        def getError(self):
            # type: () -> JavaException
            pass

        def getLongId(self):
            # type: () -> long
            pass

        def onError(self, func):
            # type: (PyFunction) -> None
            pass

        def onSuccess(self, func):
            # type: (PyFunction) -> None
            pass
