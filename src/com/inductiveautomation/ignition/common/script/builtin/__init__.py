from __future__ import print_function

__all__ = ["AbstractOPCUtilities", "DatasetUtilities", "SProcCall", "SystemUtilities"]

from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common import BasicDataset, Dataset
from com.inductiveautomation.ignition.common.model.values import QualityCode
from com.inductiveautomation.ignition.common.opc import BrowseElementType
from com.inductiveautomation.ignition.common.script.abc import AbstractJythonSequence
from com.inductiveautomation.ignition.common.script.message import Request
from java.lang import Class, Object, String
from java.util import Locale
from org.python.core import PyObject


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
            # type: (str) -> PyObject
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
        keyColumn,  # type: Union[int, str]
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
        pass

    @staticmethod
    def updateRow(ds, row, changes):
        pass

    class PyDataSet(Dataset, AbstractJythonSequence):
        _ds = None

        def __init__(self, ds=None):
            # type: (Optional[BasicDataset]) -> None
            self._ds = ds

        def getColumnCount(self):
            # type: () -> int
            pass

        def getColumnIndex(self, name):
            # type: (str) -> int
            pass

        def getColumnName(self, col):
            # type: (int) -> String
            pass

        def getColumnNames(self):
            # type: () -> List[String]
            pass

        def getColumnType(self, col):
            # type: (int) -> Class
            pass

        def getColumnTypes(self):
            # type: () -> List[Class]
            pass

        def getPrimitiveValueAt(self, row, col):
            # type: (int, int) -> float
            pass

        def getQualityAt(self, row, col):
            # type: (int, int) -> QualityCode
            pass

        def getRowCount(self):
            # type: () -> int
            pass

        def getValueAt(self, row, col):
            # type: (int, Union[int, String]) -> Any
            pass


class SProcCall(Object):
    def __init__(self):
        # type: () -> None
        pass

    def getDataSource(self):
        # type: () -> str
        pass

    def getOutParamValue(self, param):
        # type: (Union[int, str]) -> Any
        print(self, param)
        return 0

    def getProcedureName(self):
        # type: () -> str
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
        # type: () -> str
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
        # type: (Union[int, str], int, Any) -> None
        print(self, param, typeCode, value)

    def registerOutParam(self, param, typeCode):
        # type: (Union[int, str], int) -> None
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
        def getParamType(self):
            # type: () -> int
            pass

        def getValue(self):
            # type: () -> Any
            pass

        def isInParam(self):
            pass

        def isOutParam(self):
            pass

        def setParamType(self, paramType):
            pass

        def setValue(self, value):
            pass

    class SProcArgKey(Object):
        def getParamIndex(self):
            pass

        def getParamName(self):
            pass

        def isNamedParam(self):
            pass


class SystemUtilities(Object):
    @staticmethod
    def logger(loggerName):
        pass

    @staticmethod
    def parseTranslateArguments(*args, **kwargs):
        pass

    class RequestImpl(Object, Request):
        timeout = None  # type: int

        def __init__(self, timeout):
            # type: (int) -> None
            self.timeout = timeout

        def checkTimeout(self):
            pass

        def dispatchFunc(self):
            pass

        def finishExceptionally(self, e):
            pass

        def finishSuccessfully(self, value):
            pass

        def getLongId(self):
            pass

        def cancel(self):
            pass

        def get(self):
            pass

        def getError(self):
            pass

        def onError(self, func):
            pass

        def onSuccess(self, func):
            pass
