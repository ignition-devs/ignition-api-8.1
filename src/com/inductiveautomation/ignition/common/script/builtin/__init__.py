from __future__ import print_function, unicode_literals

__all__ = ["AbstractOPCUtilities", "DatasetUtilities", "SProcCall", "SystemUtilities"]

from com.inductiveautomation.ignition.common import BasicDataset, Dataset
from com.inductiveautomation.ignition.common.script.abc import AbstractJythonSequence
from com.inductiveautomation.ignition.common.script.message import Request
from java.lang import Object
from java.util import Locale
from org.python.core import PyObject


class AbstractOPCUtilities(Object):
    def browseServer(self, opcServer, nodeId):
        return [AbstractOPCUtilities.PyOPCTag(opcServer, nodeId, None, self.__class__)]

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
        _displayName = None
        _elementType = None
        _nodeId = None
        _serverName = None

        def __init__(self, serverName, nodeId, displayName, elementType):
            self._serverName = serverName
            self._nodeId = nodeId
            self._displayName = displayName
            self._elementType = elementType
            super(AbstractOPCUtilities.PyOPCTag, self).__init__()

        def __findattr_ex__(self, name):
            pass

        def getDisplayName(self):
            return self._displayName

        def getElementType(self):
            return self._elementType

        def getNodeId(self):
            return self._nodeId

        def getServerName(self):
            return self._serverName


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
    def sort(ds, keyColumn, ascending=None, naturalOrdering=None):
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
            self._ds = ds

        def getColumnCount(self):
            pass

        def getColumnIndex(self, name):
            pass

        def getColumnName(self, col):
            pass

        def getColumnNames(self):
            pass

        def getColumnType(self, col):
            pass

        def getColumnTypes(self):
            pass

        def getPrimitiveValueAt(self, row, col):
            pass

        def getQualityAt(self, row, col):
            pass

        def getRowCount(self):
            pass

        def getValueAt(self, row, col):
            pass


class SProcCall(Object):
    def __init__(self):
        pass

    def getResultSet(self):
        print(self)
        return BasicDataset()

    def getUpdateCount(self):
        print(self)
        return 1

    def getReturnValue(self):
        print(self)
        return 0

    def getOutParamValue(self, param):
        print(self, param)
        return 0

    def registerInParam(self, param, typeCode, value):
        print(self, param, typeCode, value)

    def registerOutParam(self, param, typeCode):
        print(self, param, typeCode)

    def registerReturnParam(self, typeCode):
        print(self, typeCode)

    class SProcArg(Object):
        def getParamType(self):
            pass

        def getValue(self):
            pass

        def isInParam(self):
            pass

        def isOutParam(self):
            pass

        def setParamType(self, paramType):
            pass

        def setValue(self, value):
            pass

        def toString(self):
            pass

    class SProcArgKey(Object):
        def getParamIndex(self):
            pass

        def getParamName(self):
            pass

        def hashCode(self):
            pass

        def isNamedParam(self):
            pass

        def toString(self):
            pass


class SystemUtilities(Object):
    @staticmethod
    def logger(loggerName):
        pass

    @staticmethod
    def parseTranslateArguments(*args, **kwargs):
        pass

    class RequestImpl(Object, Request):
        def __init__(self, timeout):
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
