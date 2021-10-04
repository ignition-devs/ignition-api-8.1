__all__ = ["AbstractDataset", "BasicDataset", "Dataset"]


class Dataset(object):
    """A dataset is a collection of values arranged in a structured
    format.

    Most datasets are two dimensional -- they can be viewed as a table
    with rows and columns being the two dimensions. Values in a dataset
    are usually accessed by specifying one index for each dimension of
    data (row and column for tables).
    """

    def binarySearch(self, column, key):
        pass

    def getColumnAsList(self, col):
        pass

    def getColumnCount(self):
        raise NotImplementedError

    def getColumnIndex(self, name):
        raise NotImplementedError

    def getColumnName(self, col):
        raise NotImplementedError

    def getColumnNames(self):
        raise NotImplementedError

    def getColumnType(self, col):
        raise NotImplementedError

    def getColumnTypes(self):
        raise NotImplementedError

    def getPrimitiveValueAt(self, row, col):
        raise NotImplementedError

    def getQualityAt(self, row, col):
        raise NotImplementedError

    def getRowCount(self):
        raise NotImplementedError

    def getValueAt(self, row, col):
        raise NotImplementedError

    def hasQualityData(self):
        pass


class AbstractDataset(Dataset):
    _columnNames = None
    _columnNamesLowercase = None
    _columnTypes = None
    _qualityCodes = None

    def __init__(self, columnNames, columnTypes, qualityCodes=None):
        self._columnNames = columnNames
        self._columnTypes = columnTypes
        self._qualityCodes = qualityCodes

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

    def getValueAt(self, row, col):
        pass

    def setColumnNames(self, arg):
        pass

    def setColumnTypes(self, arg):
        pass

    def setDirty(self):
        pass


class BasicDataset(AbstractDataset):
    def __init__(self, columnNames=None, columnTypes=None):
        super(BasicDataset, self).__init__(columnNames, columnTypes)

    def columnContainsNulls(self, col):
        pass

    def datasetContainsNulls(self):
        pass

    def getData(self):
        pass

    def setAllDirectly(self, columnNames, columnTypes, data):
        pass

    def setDataDirectly(self, arg):
        pass

    def setFromXML(self, columnNames, columnTypes, encodedData, rowCount):
        pass

    def setValueAt(self, row, col, value):
        pass
