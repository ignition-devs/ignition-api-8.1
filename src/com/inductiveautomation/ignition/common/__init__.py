from __future__ import print_function

__all__ = ["AbstractDataset", "BasicDataset", "Dataset", "Path", "QualifiedPath"]

from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common.model.values import QualityCode
from com.inductiveautomation.ignition.common.sqltags.model.types import DataQuality
from java.lang import Class, Object, String


class Dataset(object):
    """A dataset is a collection of values arranged in a structured
    format.

    Most datasets are two dimensional -- they can be viewed as a table
    with rows and columns being the two dimensions. Values in a dataset
    are usually accessed by specifying one index for each dimension of
    data (row and column for tables).
    """

    def binarySearch(self, column, key):
        # type: (int, Any) -> int
        pass

    def getColumnAsList(self, col):
        # type: (int) -> List[Any]
        pass

    def getColumnCount(self):
        # type: () -> int
        raise NotImplementedError

    def getColumnIndex(self, name):
        # type: (str) -> int
        raise NotImplementedError

    def getColumnName(self, col):
        # type: (int) -> String
        raise NotImplementedError

    def getColumnNames(self):
        # type: () -> List[String]
        raise NotImplementedError

    def getColumnType(self, col):
        # type: (int) -> Class
        raise NotImplementedError

    def getColumnTypes(self):
        # type: () -> List[Class]
        raise NotImplementedError

    def getPrimitiveValueAt(self, row, col):
        # type: (int, int) -> float
        raise NotImplementedError

    def getQualityAt(self, row, col):
        # type: (int, int) -> QualityCode
        raise NotImplementedError

    def getRowCount(self):
        # type: () -> int
        raise NotImplementedError

    def getValueAt(self, row, col):
        # type: (int, Union[int, String]) -> Any
        raise NotImplementedError

    def hasQualityData(self):
        # type: () -> bool
        pass


class AbstractDataset(Dataset):
    _columnNames = None  # type: List[String]
    _columnNamesLowercase = None  # type: List[String]
    _columnTypes = None  # type: List[Class]
    _qualityCodes = None  # type: Optional[List[List[QualityCode]]]

    def __init__(
        self,
        columnNames,  # type: List[String]
        columnTypes,  # type: List[Class]
        qualityCodes=None,  # type: Optional[List[List[QualityCode]]]
    ):
        # type: (...) -> None
        self._columnNames = columnNames
        self._columnTypes = columnTypes
        self._qualityCodes = qualityCodes

    @staticmethod
    def convertToQualityCodes(dataQualities):
        # type: (List[List[DataQuality]]) -> List[List[QualityCode]]
        pass

    def getBulkQualityCodes(self):
        # type: () -> List[List[QualityCode]]
        pass

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

    def setColumnNames(self, arg):
        # type: (List[str]) -> None
        pass

    def setColumnTypes(self, arg):
        # type: (List[Class]) -> None
        pass

    def setDirty(self):
        # type: () -> None
        pass


class BasicDataset(AbstractDataset):
    def __init__(self, *args):
        # type: (Any) -> None
        print(args)
        super(BasicDataset, self).__init__([""], [Class()])

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


class Path(object):
    def getLastPathComponent(self):
        # type: () -> str
        pass

    def getParentPath(self):
        # type: () -> Path
        pass

    def getPathLength(self):
        # type: () -> int
        pass

    def isAncestorOf(self, path):
        # type: (Path) -> bool
        pass


class QualifiedPath(Object):
    def extend(self, id_, value):
        pass

    def getFirstPathComponent(self):
        pass

    def getFirstPathComponentId(self):
        pass
