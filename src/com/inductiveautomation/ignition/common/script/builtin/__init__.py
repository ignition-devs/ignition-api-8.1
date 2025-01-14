from __future__ import print_function

__all__ = ["AbstractOPCUtilities", "DatasetUtilities", "SProcCall", "SystemUtilities"]

from typing import Any, Dict, List, Optional, Tuple, Union

from com.inductiveautomation.ignition.common import BasicDataset, Dataset
from com.inductiveautomation.ignition.common.model.values import (
    QualifiedValue,
    QualityCode,
)
from com.inductiveautomation.ignition.common.opc import BrowseElementType
from com.inductiveautomation.ignition.common.script.abc import AbstractJythonSequence
from com.inductiveautomation.ignition.common.script.message import Request
from dev.coatl.helper.types import AnyStr
from java.io import OutputStream, Writer
from java.lang import Class
from java.lang import Exception as JavaException
from java.lang import Object
from java.util import Locale
from org.json import JSONObject
from org.python.core import PyFunction, PyList, PyObject, PySequence
from org.slf4j import Logger


class AbstractOPCUtilities(Object):
    def browseServer(self, opcServer, nodeId):
        # type: (AnyStr, AnyStr) -> List[AbstractOPCUtilities.PyOPCTag]
        return [
            AbstractOPCUtilities.PyOPCTag(opcServer, nodeId, "", BrowseElementType())
        ]

    def getServers(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> List[AnyStr]
        pass

    def getServerState(self, opcServer):
        # type: (AnyStr) -> AnyStr
        pass

    def isServerEnabled(self, serverName):
        # type: (AnyStr) -> bool
        return True

    def readValue(self, opcServer, itemPath):
        # type: (AnyStr, AnyStr) -> QualifiedValue
        pass

    def readValues(self, opcServer, itemPaths):
        # type: (AnyStr, List[AnyStr]) -> QualifiedValue
        pass

    def setServerEnabled(self, serverName, enabled):
        # type: (AnyStr, bool) -> None
        pass

    def writeValue(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> QualityCode
        pass

    def writeValues(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> List[QualityCode]
        pass

    class PyOPCTag(PyObject):
        displayName = None  # type: AnyStr
        elementType = None  # type: BrowseElementType
        nodeId = None  # type: AnyStr
        serverName = None  # type: AnyStr

        def __init__(self, serverName, nodeId, displayName, elementType):
            # type: (AnyStr, AnyStr, AnyStr, BrowseElementType) -> None
            self.serverName = serverName
            self.nodeId = nodeId
            self.displayName = displayName
            self.elementType = elementType
            super(AbstractOPCUtilities.PyOPCTag, self).__init__()

        def __findattr_ex__(self, name):
            # type: (AnyStr) -> PyObject
            pass

        def getDisplayName(self):
            # type: () -> AnyStr
            return self.displayName

        def getElementType(self):
            # type: () -> BrowseElementType
            return self.elementType

        def getNodeId(self):
            # type: () -> AnyStr
            return self.nodeId

        def getServerName(self):
            # type: () -> AnyStr
            return self.serverName


class DatasetUtilities(Object):
    @staticmethod
    def addColumn(ds, *args):
        # type: (Dataset, *Any) -> Dataset
        pass

    @staticmethod
    def addRow(ds, *args):
        # type: (Dataset, *Any) -> Dataset
        pass

    @staticmethod
    def addRows(ds, *args):
        # type: (Dataset, *Any) -> Dataset
        pass

    @staticmethod
    def appendDataset(ds1, ds2):
        # type: (Dataset, Dataset) -> Dataset
        pass

    @staticmethod
    def clearDataset(ds):
        # type: (Dataset) -> Dataset
        pass

    @staticmethod
    def dataSetToExcel(headerRow, datasets):
        # type: (bool, List[Object]) -> AnyStr
        pass

    @staticmethod
    def dataSetToExcelBytes(headerRow, objects, nullsEmpty, sheetNames):
        # type: (bool, List[Object], bool, List[AnyStr]) -> bytearray
        pass

    @staticmethod
    def dataSetToExcelStreaming(headerRow, objects, out, nullsEmpty):
        # type: (bool, List[Object], OutputStream, bool) -> None
        pass

    @staticmethod
    def dataSetToHTML(headerRow, ds, title):
        # type: (bool, Dataset, AnyStr) -> AnyStr
        pass

    @staticmethod
    def dataSetToHTMLStreaming(headerRow, ds, title, fw):
        # type: (bool, Dataset, AnyStr, Writer) -> None
        pass

    @staticmethod
    def deleteRow(ds, row):
        # type: (Dataset, int) -> Dataset
        pass

    @staticmethod
    def deleteRows(ds, rows):
        # type: (Dataset, List[int]) -> Dataset
        pass

    @staticmethod
    def filterColumns(dataset, columns):
        # type: (Dataset, PySequence) -> Dataset
        pass

    @staticmethod
    def formatDates(dataset, format, locale=Locale.US):
        # type: (Dataset, AnyStr, Locale) -> Dataset
        pass

    @staticmethod
    def fromCSV(csv):
        # type: (AnyStr) -> Dataset
        pass

    @staticmethod
    def fromCSVJava(csv):
        # type: (AnyStr) -> Dataset
        pass

    @staticmethod
    def getColumnHeaders(ds):
        # type: (Dataset) -> PyList
        pass

    @staticmethod
    def insertColumn(ds, *args):
        # type: (Dataset, *Any) -> Dataset
        pass

    @staticmethod
    def insertRow(ds, *args):
        # type: (Dataset, *Any) -> Dataset
        pass

    @staticmethod
    def setValue(
        ds,  # type: Dataset
        row,  # type: int
        col,  # type: Union[int, AnyStr]
        value,  # type: Union[Object, PyObject]
    ):
        # type: (...) -> Dataset
        pass

    @staticmethod
    def sort(
        ds,  # type: Dataset
        keyColumn,  # type: Union[int, AnyStr]
        ascending=None,  # type: Optional[bool]
        naturalOrdering=None,  # type: Optional[bool]
    ):
        # type: (...) -> BasicDataset
        pass

    @staticmethod
    def toCSV(*args, **kwargs):
        # type: (*PyObject, **AnyStr) -> AnyStr
        pass

    @staticmethod
    def toCSVJava(ds, showHeaders, forExport, localized=False):
        # type: (Dataset, bool, bool, bool) -> AnyStr
        pass

    @staticmethod
    def toCSVJavaStreaming(ds, showHeaders, forExport, sw, localized):
        # type: (Dataset, bool, bool, Writer, bool) -> None
        pass

    @staticmethod
    def toDataSet(*args):
        # type: (*Any) -> Dataset
        pass

    @staticmethod
    def toExcel(*args, **kwargs):
        # type: (*PyObject, **AnyStr) -> bytearray
        pass

    @staticmethod
    def toJSONObject(data):
        # type: (Dataset) -> JSONObject
        pass

    @staticmethod
    def toPyDataSet(dataset):
        # type: (Dataset) -> PyDataSet
        pass

    @staticmethod
    def updateRow(ds, row, changes):
        # type: (Dataset, int, Dict[AnyStr, Any]) -> Dataset
        pass

    class PyDataSet(Dataset, AbstractJythonSequence):
        def __init__(self, ds=None):
            # type: (Optional[Dataset]) -> None
            print(ds)
            super(DatasetUtilities.PyDataSet, self).__init__(Class())

        def __add__(self, other):
            # type: (PyObject) -> PyObject
            pass

        def getColumnCount(self):
            # type: () -> int
            """Returns the number of columns in the dataset.

            Returns:
                The number of columns in the dataset.
            """
            pass

        def getColumnIndex(self, colName):
            # type: (AnyStr) -> int
            """Returns the index of the column with the name colName.

            Args:
                colName: The name of the column.

            Returns:
                The index of the column with the name colName.

            Raises:
                ArrayIndexOutOfBoundsException: If the column isn't
                    found.
            """
            pass

        def getColumnName(self, col):
            # type: (int) -> AnyStr
            """Returns the name of the column at the index colIndex.

            Args:
                col: The column number. Zero-indexed.

            Returns:
                The name of the column at the index colIndex.

            Raises:
                ArrayIndexOutOfBoundsException: If the given index is
                    out of range.
            """
            pass

        def getColumnNames(self):
            # type: () -> List[AnyStr]
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

            Raises:
                ArrayIndexOutOfBoundsException: If the given index is
                    out of range.
            """
            pass

        def getColumnTypes(self):
            # type: () -> List[Class]
            """Returns an unmodifiable list of this dataset's column
            types, in order.

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

            Returns:
                If the given column is a numeric type or a Date, then
                    the value will be returned as a double.

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

            Returns:
                The quality of the value at the given location.

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
            # type: (int, Union[int, AnyStr]) -> Any
            """Returns the value at the specified row index and column
            name or index.

            Args:
                row: The row number. Zero-indexed.
                col: The column number (zero-indexed) or name.

            Returns:
                The value found at the row and column.

            Raises:
                ArrayIndexOutOfBoundsException: If the column isn't
                    found.
            """
            print(row, col)
            return True

        def setData(self, data):
            # type: (Dataset) -> None
            """Used for serialization only."""
            pass


class SProcCall(Object):
    callFinished = False  # type: bool
    datasource = ""  # type: AnyStr
    params = None  # type: Dict[SProcCall.SProcArgKey, SProcCall.SProcArg]
    procedureName = None  # type: AnyStr
    resultset = None  # type: Dataset
    returnParam = None  # type: SProcCall.SProcArg
    skipAudit = None  # type: bool
    txId = None  # type: AnyStr
    updateCount = None  # type: int

    def getDataSource(self):
        # type: () -> AnyStr
        pass

    def getOutParamValue(self, param):
        # type: (Union[int, AnyStr]) -> Any
        print(self, param)
        return 0

    def getProcedureName(self):
        # type: () -> AnyStr
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
        # type: () -> AnyStr
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
        # type: (Union[int, AnyStr], int, Any) -> None
        print(self, param, typeCode, value)

    def registerOutParam(self, param, typeCode):
        # type: (Union[int, AnyStr], int) -> None
        print(self, param, typeCode)

    def registerReturnParam(self, typeCode):
        # type: (int) -> None
        print(self, typeCode)

    def setSkipAudit(self, skipAudit):
        # type: (bool) -> None
        pass

    def setTxId(self, txId):
        # type: (AnyStr) -> None
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
            return True

        def isOutParam(self):
            # type: () -> bool
            return True

        def setParamType(self, paramType):
            # type: (int) -> None
            pass

        def setValue(self, value):
            # type: (Object) -> None
            pass

    class SProcArgKey(Object):
        index = -1  # type: int
        name = None  # type: AnyStr

        def getParamIndex(self):
            # type: () -> int
            pass

        def getParamName(self):
            # type: () -> AnyStr
            pass

        def isNamedParam(self):
            # type: () -> bool
            return True


class SystemUtilities(Object):
    @staticmethod
    def logger(loggerName):
        # type: (AnyStr) -> Logger
        pass

    @staticmethod
    def parseTranslateArguments(*args, **kwargs):
        # type: (*PyObject, **AnyStr) -> Tuple[AnyStr, AnyStr, bool]
        pass

    class RequestImpl(Object, Request):
        timeout = None  # type: int

        def __init__(self, timeout):
            # type: (int) -> None
            super(SystemUtilities.RequestImpl, self).__init__()
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
