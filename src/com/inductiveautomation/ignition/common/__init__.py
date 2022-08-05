from __future__ import print_function

__all__ = ["AbstractDataset", "BasicDataset", "Dataset", "Path", "QualifiedPath"]

from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common.model.values import QualityCode
from com.inductiveautomation.ignition.common.sqltags.model.types import DataQuality
from java.lang import Class, Object, String


class Dataset(object):
    """A dataset is a collection of values arranged in a structured
    format.

    Most datasets are two-dimensional -- they can be viewed as a table
    with rows and columns being the two dimensions. Values in a dataset
    are usually accessed by specifying one index for each dimension of
    data (row and column for tables).
    """

    def binarySearch(self, column, key):
        # type: (int, Any) -> int
        pass

    def getColumnAsList(self, col):
        # type: (int) -> List[Any]
        """Returns the column at the specified index as a list.

        Args:
            col: The column index. Zero-indexed.

        Returns:
            The column at the specified index as a list.
        """
        pass

    def getColumnCount(self):
        # type: () -> int
        """Returns the number of columns in the dataset.

        Returns:
            The number of columns in the dataset.
        """
        raise NotImplementedError

    def getColumnIndex(self, colName):
        # type: (String) -> int
        """Returns the index of the column with the name colName.

        Args:
            colName: The name of the column.

        Returns:
            The index of the column with the name colName.
        """
        raise NotImplementedError

    def getColumnName(self, col):
        # type: (int) -> String
        """Returns the name of the column at the index colIndex.

        Args:
            col: The column number. Zero-indexed.

        Returns:
            The name of the column at the index colIndex.
        """
        raise NotImplementedError

    def getColumnNames(self):
        # type: () -> List[String]
        """Returns a list with the names of all the columns.

        Returns:
            A list with the names of all the columns.
        """
        raise NotImplementedError

    def getColumnType(self, col):
        # type: (int) -> Class
        """Returns the type of the column at the index.

        Args:
            col: The column number. Zero-indexed.

        Returns:
            The type of the column at the index.
        """
        raise NotImplementedError

    def getColumnTypes(self):
        # type: () -> List[Class]
        """Returns a list with the types of all the columns.

        Returns:
            A list with the types of all the columns.
        """
        raise NotImplementedError

    def getPrimitiveValueAt(self, row, col):
        # type: (int, int) -> float
        """If the given column is a numeric type or a Date, then the
        value will be returned as a double.

        Args:
            row: The row index. Zero-based index.
            col: The column index. Zero-based index.

        Raises:
            IllegalArgumentException: if the value at row, col is not a
                number or Date.
            UnsupportedOperationException: If the Dataset implementation
                declines to implement this operation.
        """
        raise NotImplementedError

    def getQualityAt(self, row, col):
        # type: (int, int) -> QualityCode
        """Returns the quality of the value at the given location.

        Args:
            row: The row index. Zero-based index.
            col: The column index. Zero-based index.

        Raises:
            ArrayIndexOutOfBoundsException: If the given row, col is out
                of range and hasQualityData() returns true.
        """
        raise NotImplementedError

    def getRowCount(self):
        # type: () -> int
        """Returns the number of rows in the dataset.

        Returns:
            The number of rows in the dataset.
        """
        raise NotImplementedError

    def getValueAt(self, row, col):
        # type: (int, Union[int, String]) -> Any
        """Returns the value at the specified row index and column name
        or index.

        Args:
            row: The row number. Zero-indexed.
            col: The column number (zero-indexed) or name.

        Returns:
            The value found at the row and column.
        """
        raise NotImplementedError

    def hasQualityData(self):
        # type: () -> bool
        """Whether this dataset has any quality data to report.

        Returns:
            Whether this dataset has any quality data to report.
        """
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
            IllegalArgumentException: if the value at row, col is not a
                number or Date.
            UnsupportedOperationException: If the Dataset implementation
                declines to implement this operation.
        """
        pass

    def getQualityAt(self, row, col):
        # type: (int, int) -> QualityCode
        """Returns the quality of the value at the given location.

        Args:
            row: The row index. Zero-based index.
            col: The column index. Zero-based index.

        Raises:
            ArrayIndexOutOfBoundsException: If the given row, col is out
                of range and hasQualityData() returns true.
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
        """Returns the value at the specified row index and column name
        or index.

        Args:
            row: The row number. Zero-indexed.
            col: The column number (zero-indexed) or name.

        Returns:
            The value found at the row and column.
        """
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
