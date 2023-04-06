from __future__ import print_function

__all__ = [
    "AbstractDataset",
    "BasicDataset",
    "Dataset",
    "JsonPath",
    "Path",
    "QualifiedPath",
    "StringPath",
    "TypeUtilities",
]

from typing import Any, Iterable, List, Optional, Set, Union

from com.inductiveautomation.ignition.common.document import DocumentElement
from com.inductiveautomation.ignition.common.gson import Gson, JsonElement
from dev.thecesrom.helper.types import AnyStr
from java.awt import Color
from java.lang import Class, Comparable, Number, Object
from java.util import UUID, Comparator, Date, Locale
from org.json import JSONObject
from org.python.core import PyObject


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
        # type: (AnyStr) -> int
        """Returns the index of the column with the name colName.

        Args:
            colName: The name of the column.

        Returns:
            The index of the column with the name colName.
        """
        raise NotImplementedError

    def getColumnName(self, col):
        # type: (int) -> AnyStr
        """Returns the name of the column at the index colIndex.

        Args:
            col: The column number. Zero-indexed.

        Returns:
            The name of the column at the index colIndex.
        """
        raise NotImplementedError

    def getColumnNames(self):
        # type: () -> List[AnyStr]
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
        # type: (int, int) -> Any
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
        # type: (int, Union[int, AnyStr]) -> Any
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
        return True


class AbstractDataset(Dataset):
    _columnNames = None  # type: List[AnyStr]
    _columnNamesLowercase = None  # type: List[AnyStr]
    _columnTypes = None  # type: List[Class]
    _qualityCodes = None  # type: Optional[List[List[Any]]]

    def __init__(
        self,
        columnNames,  # type: List[AnyStr]
        columnTypes,  # type: List[Class]
        qualityCodes=None,  # type: Optional[List[List[Any]]]
    ):
        # type: (...) -> None
        self._columnNames = columnNames
        self._columnTypes = columnTypes
        self._qualityCodes = qualityCodes

    @staticmethod
    def convertToQualityCodes(dataQualities):
        # type: (List[List[Any]]) -> List[List[Any]]
        pass

    def getBulkQualityCodes(self):
        # type: () -> List[List[Any]]
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
        """
        pass

    def getColumnName(self, col):
        # type: (int) -> AnyStr
        """Returns the name of the column at the index colIndex.

        Args:
            col: The column number. Zero-indexed.

        Returns:
            The name of the column at the index colIndex.
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
        # type: (int, int) -> Any
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
        # type: (int, Union[int, AnyStr]) -> Any
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
        # type: (*Any) -> None
        print(args)
        super(BasicDataset, self).__init__([""], [Class()])

    def columnContainsNulls(self, col):
        # type: (int) -> bool
        return True

    def datasetContainsNulls(self):
        # type: () -> bool
        return True

    def getData(self):
        # type: () -> List[Object]
        pass

    def setAllDirectly(self, columnNames, columnTypes, data):
        # type: (List[AnyStr], List[Class], Any) -> None
        pass

    def setDataDirectly(self, arg):
        # type: (Any) -> None
        pass

    def setFromXML(self, columnNames, columnTypes, encodedData, rowCount):
        # type: (List[AnyStr], List[Class], AnyStr, int) -> None
        pass

    def setValueAt(self, row, col, value):
        # type: (int, int, Any) -> None
        pass


class JsonPath(Object):
    ROOT = None  # type: JsonPath

    def createChildPath(self, arg):
        # type: (Union[JsonPath, int, AnyStr]) -> JsonPath
        pass

    def getAsLinkedList(self):
        # type: () -> Any
        pass

    def getDepth(self):
        # type: () -> int
        pass

    def getKey(self):
        # type: () -> Object
        pass

    def getParent(self):
        # type: () -> JsonPath
        pass

    def getPathElements(self):
        # type: () -> List[JsonPath]
        pass

    def getSubPath(self, startingDepth):
        # type: (int) -> JsonPath
        pass

    def isAncestorOf(self, element):
        # type: (JsonPath) -> bool
        return True

    def isRelatedTo(self, other):
        # type: (JsonPath) -> bool
        return True

    def isRoot(self):
        # type: () -> bool
        return True

    @staticmethod
    def isValidIdentifier(test):
        # type: (AnyStr) -> bool
        return True

    @staticmethod
    def parse(path):
        # type: (AnyStr) -> AnyStr
        pass


class Path(object):
    SERIALIZATION_WHITELIST = None  # type: Set[Class]

    def getLastPathComponent(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getParentPath(self):
        # type: () -> Path
        raise NotImplementedError

    def getPathComponent(self, i):
        # type: (int) -> AnyStr
        raise NotImplementedError

    def getPathLength(self):
        # type: () -> int
        raise NotImplementedError

    def isAncestorOf(self, path):
        # type: (Path) -> bool
        raise NotImplementedError


class QualifiedPath(Object):
    def __init__(self):
        # type: () -> None
        super(QualifiedPath, self).__init__()


class StringPath(Object, Path, Comparable):
    PATH_RELATIVE = None  # type: AnyStr
    PATH_RELATIVE_UP = None  # type: AnyStr
    PATH_SEPARATOR = None  # type: AnyStr
    ROOT = None  # type: StringPath

    def __init__(self, *parts):
        # type: (*AnyStr) -> None
        super(StringPath, self).__init__()
        print(parts)

    def caseSensitive(self):
        # type: () -> StringPath.CaseSensitiveStringPath
        pass

    def compareTo(self, o):
        # type: (Any) -> int
        pass

    @staticmethod
    def extend(parent, *args):
        # type: (StringPath, *Any) -> StringPath
        pass

    def getChildPath(self, *pathParts):
        # type: (*AnyStr) -> StringPath
        pass

    def getLastPathComponent(self):
        # type: () -> AnyStr
        pass

    def getParentPath(self):
        # type: () -> StringPath
        pass

    def getParts(self):
        # type: () -> Iterable[AnyStr]
        pass

    def getPathComponent(self, i):
        # type: (int) -> AnyStr
        pass

    def getPathLength(self):
        # type: () -> int
        pass

    def isAncestorOf(self, path):
        # type: (Path) -> bool
        pass

    @staticmethod
    def isRelative(path):
        # type: (StringPath) -> bool
        pass

    def isRoot(self):
        # type: () -> bool
        pass

    @staticmethod
    def makeRelative(toRelative, root):
        # type: (StringPath, StringPath) -> StringPath
        pass

    @staticmethod
    def of(*parts):
        # type: (*AnyStr) -> StringPath
        pass

    @staticmethod
    def removeRelative(relative, root):
        # type: (StringPath, StringPath) -> StringPath
        pass

    def subPath(self, start=None, length=None):
        # type: (Optional[int], Optional[int]) -> StringPath
        pass

    class CaseSensitiveStringPath(Object, Comparable):
        def compareTo(self, o):
            # type: (Any) -> int
            pass

        def isAncestorOf(self, child):
            # type: (Path) -> bool
            pass


class TypeUtilities(Object):
    DATE_FORMAT_STRING = "yyyyMMdd.HHmmssSSSZ"  # type: AnyStr
    NULL_SAFE_CASE_INSENSITIVE_ORDER = None  # type: Comparator

    def __init__(self):
        # type: () -> None
        super(TypeUtilities, self).__init__()

    @staticmethod
    def anyEqual(value, *args):
        # type: (Any, Any) -> bool
        return True

    @staticmethod
    def coerce(value, destType):
        # type: (Object, Class) -> Object
        pass

    @staticmethod
    def coerceForLocale(value, target, valueLocale):
        # type: (Object, Class, Locale) -> Object
        pass

    @staticmethod
    def coerceGeneric(value, destType):
        # type: (Object, Class) -> Any
        pass

    @staticmethod
    def coerceLocaleSafe(str, type):
        # type: (AnyStr, Class) -> Object
        pass

    @staticmethod
    def coerceNullSafe(value, destType):
        # type: (Object, Class) -> Object
        pass

    @staticmethod
    def coerceNumberForLocale(value, destType, locale):
        # type: (Object, Class, Locale) -> Object
        pass

    @staticmethod
    def coerceNumberNullSafe(value, destType, locale):
        # type: (Object, Class, Locale) -> Object
        pass

    @staticmethod
    def colorToHex(c):
        # type: (Color) -> AnyStr
        pass

    @staticmethod
    def compareInts(foo, bar):
        # type: (int, int) -> int
        pass

    @staticmethod
    def compareNullHigh(c1, c2):
        # type: (Any, Any) -> Any
        pass

    @staticmethod
    def compareNullLow(c1, c2):
        # type: (Any, Any) -> Any
        pass

    @staticmethod
    def datasetFromJSON(json):
        # type: (JSONObject) -> Dataset
        pass

    @staticmethod
    def datasetFromJsonString(jsonStr):
        # type: (AnyStr) -> Dataset
        pass

    @staticmethod
    def datasetToGson(data, gson=None):
        # type: (Dataset, Optional[Gson]) -> JsonElement
        pass

    @staticmethod
    def datasetToJSON(data):
        # type: (Dataset) -> JSONObject
        pass

    @staticmethod
    def deepEquals(o1, o2, checkArrayTypes):
        # type: (Object, Object, bool) -> bool
        return True

    @staticmethod
    def equalsIgnoreCase(o1, o2):
        # type: (Object, Object) -> bool
        return True

    @staticmethod
    def fromString(value, dest, locale):
        # type: (AnyStr, Class, Locale) -> Object
        pass

    @staticmethod
    def getColorFromString(color):
        # type: (AnyStr) -> Color
        pass

    @staticmethod
    def getFirstOrNull(list_):
        # type: (List[Any]) -> Any
        pass

    @staticmethod
    def getInitValueForClass(c):
        # type: (Class) -> Object
        pass

    @staticmethod
    def getLastNameComponent(name):
        # type: (AnyStr) -> AnyStr
        pass

    @staticmethod
    def getPrimitiveType(c):
        # type: (Class) -> Object
        pass

    @staticmethod
    def getWrapperType(c):
        # type: (Class) -> Class
        pass

    @staticmethod
    def gsonToPy(element):
        # type: (JsonElement) -> PyObject
        pass

    @staticmethod
    def hasPrimitiveType(c):
        # type: (Class) -> bool
        return True

    @staticmethod
    def hasValueChanged(
        currentValue,  # type: Any
        previousValue,  # type: Any
        expectedType,  # type: Any
        deadband,  # type: float
    ):
        # type: (...) -> bool
        return True

    @staticmethod
    def isAssignable(dest, source):
        # type: (Class, Class) -> bool
        return True

    @staticmethod
    def isBoolean(clazz):
        # type: (Class) -> bool
        return True

    @staticmethod
    def isDirectlyAssignable(dest, source):
        # type: (Class, Class) -> bool
        return True

    @staticmethod
    def isFractional(clazz):
        # type: (Class) -> bool
        return True

    @staticmethod
    def isNullOrEmpty(s):
        # type: (AnyStr) -> bool
        return not s

    @staticmethod
    def isNumber(clazz):
        # type: (Class) -> bool
        return True

    @staticmethod
    def isPrimitive(clazz):
        # type: (Class) -> bool
        return True

    @staticmethod
    def isProperNumber(clazz):
        # type: (Class) -> bool
        return True

    @staticmethod
    def neq(o1, o2):
        # type: (Object, Object) -> bool
        return True

    @staticmethod
    def pyToGson(pyObject, customGson=None):
        # type: (PyObject, Optional[Gson]) -> JsonElement
        pass

    @staticmethod
    def pyToJava(pyObject):
        # type: (PyObject) -> Object
        pass

    @staticmethod
    def setArrayValue(arrayValue, newVal, pos):
        # type: (Object, Object, int) -> Any
        pass

    @staticmethod
    def setClassInitializer(init):
        # type: (TypeUtilities.ClassInitializer) -> None
        pass

    @staticmethod
    def toBool(value):
        # type: (Object) -> bool
        return True

    @staticmethod
    def toByteArray(uuid):
        # type: (UUID) -> bytearray
        pass

    @staticmethod
    def toColor(color):
        # type: (Object) -> Color
        pass

    @staticmethod
    def toDataset(value):
        # type: (Object) -> Dataset
        pass

    @staticmethod
    def toDate(value):
        # type: (Object) -> Date
        pass

    @staticmethod
    def toDocument(value):
        # type: (Object) -> DocumentElement
        pass

    @staticmethod
    def toDouble(value):
        # type: (Object) -> float
        pass

    @staticmethod
    def toEnum(enumType, value):
        # type: (Class, AnyStr) -> Any
        pass

    @staticmethod
    def toFloat(value):
        # type: (Object) -> float
        pass

    @staticmethod
    def toInteger(value):
        # type: (Object) -> int
        pass

    @staticmethod
    def toLong(value):
        # type: (Object) -> long
        pass

    @staticmethod
    def toNumber(value, locale=None):
        # type: (Object, Optional[Locale]) -> Number
        pass

    @staticmethod
    def toShort(value):
        # type: (Object) -> int
        pass

    @staticmethod
    def toStr(value):
        # type: (Object) -> AnyStr
        pass

    @staticmethod
    def toStringLocalized(value, locale=None):
        # type: (Object, Optional[Locale]) -> AnyStr
        pass

    @staticmethod
    def toStringOnlyNumberLocalized(value, locale):
        # type: (Object, Locale) -> AnyStr
        pass

    @staticmethod
    def toUUID(barr):
        # type: (bytearray) -> UUID
        pass

    class ClassInitializer(object):
        def createNew(self, claz):
            # type: (Class) -> Object
            pass
