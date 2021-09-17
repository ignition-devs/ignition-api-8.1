__all__ = ["AbstractDataset", "BasicDataset", "Dataset"]

from abc import ABCMeta, abstractmethod


class Dataset(ABCMeta):
    """A dataset is a collection of values arranged in a structured
    format.

    Most datasets are two dimensional -- they can be viewed as a table
    with rows and columns being the two dimensions. Values in a dataset
    are usually accessed by specifying one index for each dimension of
    data (row and column for tables).
    """

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def getColumnCount(cls):
        pass

    @abstractmethod
    def getColumnIndex(cls, name):
        pass

    @abstractmethod
    def getColumnName(cls, col):
        pass

    @abstractmethod
    def getColumnNames(cls):
        pass

    @abstractmethod
    def getColumnType(cls, col):
        pass

    @abstractmethod
    def getPrimitiveValueAt(cls, row, col):
        pass

    @abstractmethod
    def getQualityAt(cls, row, col):
        pass

    @abstractmethod
    def getRowCount(cls):
        pass

    @abstractmethod
    def getValueAt(cls, row, colName):
        pass


class AbstractDataset(Dataset):
    @staticmethod
    def convertToQualityCodes(dataQualities):
        pass

    def getBulkQualityCodes(self):
        pass

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

    def getValueAt(self, row, colName):
        pass

    def hasQualityData(self):
        pass

    def setColumnNames(self, arg):
        pass

    def setColumnTypes(self, arg):
        pass

    def setDirty(self):
        pass


class BasicDataset(AbstractDataset):
    def binarySearch(self, column, key):
        pass

    def columnContainsNulls(self, col):
        pass

    def datasetContainsNulls(self):
        pass

    def getColumnAsList(self, col):
        pass

    def getData(self):
        pass

    def getRowCount(self):
        pass

    def setAllDirectly(self, columnNames, columnTypes, data):
        pass

    def setDataDirectly(self, arg):
        pass

    def setFromXML(self, columnNames, columnTypes, encodedData, rowCount):
        pass

    def setValueAt(self, row, col, value):
        pass
