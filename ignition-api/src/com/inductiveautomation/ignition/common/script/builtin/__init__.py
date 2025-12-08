from __future__ import print_function

__all__ = ["AbstractOPCUtilities", "DatasetUtilities", "SProcCall", "SystemUtilities"]

from typing import Any, Dict, List, Optional, Tuple, Union

from java.io import OutputStream, Writer
from java.lang import ArrayIndexOutOfBoundsException, Class
from java.lang import Exception as JavaException
from java.lang import IllegalArgumentException, Object, UnsupportedOperationException
from java.util import Locale

from com.inductiveautomation.ignition.common import BasicDataset, Dataset
from com.inductiveautomation.ignition.common.model.values import (
    QualifiedValue,
    QualityCode,
)
from com.inductiveautomation.ignition.common.opc import BrowseElementType
from com.inductiveautomation.ignition.common.script.abc import AbstractJythonSequence
from com.inductiveautomation.ignition.common.script.message import Request
from org.json import JSONObject
from org.python.core import PyFunction, PyList, PyObject, PySequence
from org.slf4j import Logger


class AbstractOPCUtilities(Object):

    class PyOPCTag(PyObject):
        displayName = None  # type: Union[str, unicode]
        elementType = None  # type: BrowseElementType
        nodeId = None  # type: Union[str, unicode]
        serverName = None  # type: Union[str, unicode]

        def __init__(
            self,
            serverName,  # type: Union[str, unicode]
            nodeId,  # type: Union[str, unicode]
            displayName,  # type: Union[str, unicode]
            elementType,  # type: BrowseElementType
        ):
            # type: (...) -> None
            self.serverName = serverName
            self.nodeId = nodeId
            self.displayName = displayName
            self.elementType = elementType
            super(AbstractOPCUtilities.PyOPCTag, self).__init__()

        def __findattr_ex__(self, name):
            # type: (Union[str, unicode]) -> PyObject
            pass

        def getDisplayName(self):
            # type: () -> Union[str, unicode]
            return self.displayName

        def getElementType(self):
            # type: () -> BrowseElementType
            return self.elementType

        def getNodeId(self):
            # type: () -> Union[str, unicode]
            return self.nodeId

        def getServerName(self):
            # type: () -> Union[str, unicode]
            return self.serverName

    def browseServer(
        self,
        opcServer,  # type: Union[str, unicode]
        nodeId,  # type: Union[str, unicode]
    ):
        # type: (...) -> List[AbstractOPCUtilities.PyOPCTag]
        return [
            AbstractOPCUtilities.PyOPCTag(opcServer, nodeId, "", BrowseElementType())
        ]

    def getServers(self, *args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> List[Union[str, unicode]]  # noqa: W505
        pass

    def getServerState(self, opcServer):
        # type: (Union[str, unicode]) -> Union[str, unicode]
        pass

    def isServerEnabled(self, serverName):
        # type: (Union[str, unicode]) -> bool
        return True

    def readValue(
        self,
        opcServer,  # type: Union[str, unicode]
        itemPath,  # type: Union[str, unicode]
    ):
        # type: (...) -> QualifiedValue
        pass

    def readValues(
        self,
        opcServer,  # type: Union[str, unicode]
        itemPaths,  # type: List[Union[str, unicode]]
    ):
        # type: (...) -> QualifiedValue
        pass

    def setServerEnabled(self, serverName, enabled):
        # type: (Union[str, unicode], bool) -> None
        pass

    def writeValue(self, *args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> QualityCode
        pass

    def writeValues(self, *args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> List[QualityCode]
        pass


class DatasetUtilities(Object):

    class PyDataSet(Dataset, AbstractJythonSequence):
        def __init__(self, ds=None):
            # type: (Optional[Dataset]) -> None
            print(ds)
            super(DatasetUtilities.PyDataSet, self).__init__(Class())

        def getColumnCount(self):
            # type: () -> int
            """Returns the number of columns in the dataset.

            Returns:
                The number of columns in the dataset.
            """
            pass

        def getColumnIndex(self, colName):
            # type: (Union[str, unicode]) -> int
            """Returns the index of the column with the name colName.

            Args:
                colName: The name of the column.

            Returns:
                The index of the column with the name colName.

            Raises:
                ArrayIndexOutOfBoundsException: If the column isn't
                    found.
            """
            if not colName:
                raise ArrayIndexOutOfBoundsException()
            return 0

        def getColumnName(self, col):
            # type: (int) -> Union[str, unicode]
            """Returns the name of the column at the index colIndex.

            Args:
                col: The column number. Zero-indexed.

            Returns:
                The name of the column at the index colIndex.

            Raises:
                ArrayIndexOutOfBoundsException: If the given index is
                    out of range.
            """
            if col == -1:
                raise ArrayIndexOutOfBoundsException()
            return "column_name"

        def getColumnNames(self):
            # type: () -> List[Union[str, unicode]]
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
            if col == -1:
                raise ArrayIndexOutOfBoundsException()
            return Class()

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
            if row == 0 and col == 0:
                raise IllegalArgumentException()
            if row == -1 and col == -1:
                raise UnsupportedOperationException()
            return 42.0

        def getQualityAt(self, row, col):
            # type: (int, int) -> QualityCode
            """Returns the quality of the value at the given location.

            Args:
                row: The row index. Zero-based index.
                col: The column index. Zero-based index.

            Returns:
                The quality of the value at the given location.

            Raises:
                ArrayIndexOutOfBoundsException: If the column isn't
                    found.
            """
            if row == -1 and col == -1:
                raise ArrayIndexOutOfBoundsException()
            return QualityCode().Good

        def getRowCount(self):
            # type: () -> int
            """Returns the number of rows in the dataset.

            Returns:
                The number of rows in the dataset.
            """
            pass

        def getUnderlyingDataset(self):
            # type: () -> Dataset
            """Returns the underlying dataset.

            Returns:
                The underlying dataset.
            """
            return Dataset()

        def getValueAt(self, row, col):
            # type: (int, Union[int, str, unicode]) -> Any
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
            if row == 0 and col == 0:
                raise ArrayIndexOutOfBoundsException()
            print(row, col)
            return True

        def setData(self, data):
            # type: (Dataset) -> None
            """Used for serialization only."""
            pass

        def __add__(self, other):
            # type: (PyObject) -> PyObject
            pass

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
        # type: (bool, List[Object]) -> Union[str, unicode]
        pass

    @staticmethod
    def dataSetToExcelBytes(
        headerRow,  # type: bool
        objects,  # type: List[Object]
        nullsEmpty,  # type: bool
        sheetNames,  # type: List[Union[str, unicode]]
    ):
        # type: (...) -> bytearray
        pass

    @staticmethod
    def dataSetToExcelStreaming(headerRow, objects, out, nullsEmpty):
        # type: (bool, List[Object], OutputStream, bool) -> None
        pass

    @staticmethod
    def dataSetToHTML(
        headerRow,  # type: bool
        ds,  # type: Dataset
        title,  # type: Union[str, unicode]
    ):
        # type: (...) -> Union[str, unicode]
        pass

    @staticmethod
    def dataSetToHTMLStreaming(headerRow, ds, title, fw):
        # type: (bool, Dataset, Union[str, unicode], Writer) -> None
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
        # type: (Dataset, Union[str, unicode], Locale) -> Dataset
        pass

    @staticmethod
    def fromCSV(csv):
        # type: (Union[str, unicode]) -> Dataset
        pass

    @staticmethod
    def fromCSVJava(csv):
        # type: (Union[str, unicode]) -> Dataset
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
        col,  # type: Union[int, str, unicode]
        value,  # type: Union[Object, PyObject]
    ):
        # type: (...) -> Dataset
        pass

    @staticmethod
    def sort(
        ds,  # type: Dataset
        keyColumn,  # type: Union[int, str, unicode]
        ascending=None,  # type: Optional[bool]
        naturalOrdering=None,  # type: Optional[bool]
    ):
        # type: (...) -> BasicDataset
        pass

    @staticmethod
    def toCSV(*args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> Union[str, unicode]  # noqa: W505
        pass

    @staticmethod
    def toCSVJava(ds, showHeaders, forExport, localized=False):
        # type: (Dataset, bool, bool, bool) -> Union[str, unicode]
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
        # type: (*PyObject, **Union[str, unicode]) -> bytearray
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
    def updateRow(
        ds,  # type: Dataset
        row,  # type: int
        changes,  # type: Dict[Union[str, unicode], Any]
    ):
        # type: (...) -> Dataset
        pass


class SProcCall(Object):

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
        name = None  # type: Union[str, unicode]

        def getParamIndex(self):
            # type: () -> int
            pass

        def getParamName(self):
            # type: () -> Union[str, unicode]
            pass

        def isNamedParam(self):
            # type: () -> bool
            return True

    callFinished = False  # type: bool
    datasource = ""  # type: Union[str, unicode]
    params = None  # type: Dict[SProcCall.SProcArgKey, SProcCall.SProcArg]
    procedureName = None  # type: Union[str, unicode]
    resultset = None  # type: Dataset
    returnParam = None  # type: SProcCall.SProcArg
    skipAudit = None  # type: bool
    txId = None  # type: Union[str, unicode]
    updateCount = None  # type: int

    def getDataSource(self):
        # type: () -> Union[str, unicode]
        pass

    def getOutParamValue(self, param):
        # type: (Union[int, str, unicode]) -> Any
        print(self, param)
        return 0

    def getProcedureName(self):
        # type: () -> Union[str, unicode]
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
        # type: () -> Union[str, unicode]
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
        # type: (Union[int, str, unicode], int, Any) -> None
        print(self, param, typeCode, value)

    def registerOutParam(self, param, typeCode):
        # type: (Union[int, str, unicode], int) -> None
        print(self, param, typeCode)

    def registerReturnParam(self, typeCode):
        # type: (int) -> None
        print(self, typeCode)

    def setSkipAudit(self, skipAudit):
        # type: (bool) -> None
        pass

    def setTxId(self, txId):
        # type: (Union[str, unicode]) -> None
        pass


class SystemUtilities(Object):

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

    @staticmethod
    def logger(loggerName):
        # type: (Union[str, unicode]) -> Logger
        pass

    @staticmethod
    def parseTranslateArguments(*args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> Tuple[Union[str, unicode], Union[str, unicode], bool]  # noqa: E501, W505  # pylint: disable=line-too-long
        pass
