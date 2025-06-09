from typing import Any, List, Optional, Union

from dev.coatl.helper.types import AnyStr
from java.lang import Comparable, Enum, Object
from org.apache.poi.common import Duplicatable
from org.apache.poi.ss import SpreadsheetVersion
from org.apache.poi.util import LittleEndianOutput


class AreaReference(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(AreaReference, self).__init__()
        print(args)

    def formatAsString(self):
        # type: () -> AnyStr
        pass

    @staticmethod
    def generateContiguous(version, reference):
        # type: (SpreadsheetVersion, AnyStr) -> List[AreaReference]
        pass

    def getAllReferencedCells(self):
        # type: () -> List[CellReference]
        pass

    def getFirstCell(self):
        # type: () -> CellReference
        pass

    def getLastCell(self):
        # type: () -> CellReference
        pass

    @staticmethod
    def getWholeColumn(version, start, end):
        # type: (SpreadsheetVersion, AnyStr, AnyStr) -> AreaReference
        pass

    @staticmethod
    def getWholeRow(version, start, end):
        # type: (SpreadsheetVersion, AnyStr, AnyStr) -> AreaReference
        pass

    def isSingleCell(self):
        # type: () -> bool
        pass

    @staticmethod
    def isWholeColumnReference(
        version=None,  # type: Optional[SpreadsheetVersion]
        topLeft=None,  # type: Optional[CellReference]
        botRight=None,  # type: Optional[CellReference]
    ):
        # type: (...) -> bool
        pass


class CellAddress(Object, Comparable):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(CellAddress, self).__init__()
        print(args)

    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def formatAsString(self):
        # type: () -> AnyStr
        pass

    def getColumn(self):
        # type: () -> int
        pass

    def getRow(self):
        # type: () -> int
        pass


class CellRangeAddressBase(Object, Duplicatable):

    class CellPosition(Enum):
        BOTTOM = None  # type: CellRangeAddressBase.CellPosition
        LEFT = None  # type: CellRangeAddressBase.CellPosition
        RIGHT = None  # type: CellRangeAddressBase.CellPosition
        TOP = None  # type: CellRangeAddressBase.CellPosition

        @staticmethod
        def values():
            # type: () -> List[CellRangeAddressBase.CellPosition]
            pass

    def containsColumn(self, colInd):
        # type: (int) -> bool
        pass

    def containsRow(self, rowInd):
        # type: (int) -> bool
        pass

    def copy(self):
        # type: () -> Duplicatable
        pass

    def getFirstColumn(self):
        # type: () -> int
        pass

    def getFirstRow(self):
        # type: () -> int
        pass

    def getLastColumn(self):
        # type: () -> int
        pass

    def getLastRow(self):
        # type: () -> int
        pass

    def getNumberOfCells(self):
        # type: () -> int
        pass

    def getPosition(self, rowInd, colInd):
        # type: (int, int) -> Any
        pass

    def intersects(self, other):
        # type: (CellRangeAddressBase) -> bool
        pass

    def isFullColumnRange(self):
        # type: () -> bool
        pass

    def isFullRowRange(self):
        # type: () -> bool
        pass

    def isInRange(self, *args):
        # type: (*Any) -> bool
        pass

    def iterator(self):
        # type: () -> Any
        pass

    def setFirstColumn(self, firstCol):
        # type: (int) -> None
        pass

    def setFirstRow(self, firstRow):
        # type: (int) -> None
        pass

    def setLastColumn(self, lastCol):
        # type: (int) -> None
        pass

    def setLastRow(self, lastRow):
        # type: (int) -> None
        pass

    def validate(self, ssVesion):
        # type: (SpreadsheetVersion) -> None
        pass


class CellRangeAddress(CellRangeAddressBase):
    ENCODED_SIZE = 0  # type: int

    def __init__(self, *args):
        # type: (*Any) -> None
        super(CellRangeAddress, self).__init__()
        print(args)

    def formatAsString(self, sheetName=None, useAbsoluteAddress=False):
        # type: (Optional[AnyStr], bool) -> AnyStr
        pass

    @staticmethod
    def getEncodedSize():
        # type: () -> int
        pass

    def serialize(self, out):
        # type: (LittleEndianOutput) -> None
        pass

    @staticmethod
    def valueOf(ref):
        # type: (AnyStr) -> CellRangeAddress
        pass


class CellRangeAddressList(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(CellRangeAddressList, self).__init__()
        print(args)

    def addCellRangeAddress(self, *args):
        # type: (*Any) -> None
        pass

    def copy(self):
        # type: () -> CellRangeAddressList
        pass

    def countRanges(self):
        # type: () -> int
        pass

    def getCellRangeAddress(self, index):
        # type: (int) -> CellRangeAddress
        pass

    def getCellRangeAddresses(self):
        # type: () -> List[CellRangeAddress]
        pass

    @staticmethod
    def getEncodedSize(numberOfRanges):
        # type: (int) -> int
        pass

    def getSize(self):
        # type: () -> int
        pass

    def remove(self, rangeIdex):
        # type: (int) -> CellRangeAddress
        pass

    def serialize(self, *args):
        # type: (*Any) -> None
        pass


class CellReference(Object):

    class NameType(Enum):
        BAD_CELL_OR_NAMED_RANGE = None  # type: CellReference.NameType
        CELL = None  # type: CellReference.NameType
        COLUMN = None  # type: CellReference.NameType
        NAMED_RANGE = None  # type: CellReference.NameType
        ROW = None  # type: CellReference.NameType

        @staticmethod
        def values():
            # type: () -> List[CellReference.NameType]
            pass

    def __init__(self, *args):
        # type: (*Any) -> None
        super(CellReference, self).__init__()
        print(args)

    @staticmethod
    def cellReferenceIsWithinRange(colStr, rowStr, ssVersion):
        # type: (AnyStr, AnyStr, SpreadsheetVersion) -> bool
        pass

    @staticmethod
    def classifyCellReference(str_, ssVersion):
        # type: (AnyStr, SpreadsheetVersion) -> CellReference.NameType
        pass

    @staticmethod
    def convertColStringToIndex(ref):
        # type: (AnyStr) -> int
        pass

    @staticmethod
    def converNumToColString(col):
        # type: (int) -> AnyStr
        pass

    def formatAsString(self, includeSheetName=False):
        # type: (bool) -> AnyStr
        pass

    def getCellRefParts(self):
        # type: () -> List[AnyStr]
        pass

    def getCol(self):
        # type: () -> int
        pass

    def getRow(self):
        # type: () -> int
        pass

    def getSheetName(self):
        # type: () -> AnyStr
        pass

    def isColAbsolute(self):
        # type: () -> bool
        pass

    @staticmethod
    def isColumnWithinRange(colStr, ssVersion):
        # type: (AnyStr, SpreadsheetVersion) -> bool
        pass

    @staticmethod
    def isPartAbsolute(part):
        # type: (AnyStr) -> bool
        pass

    def isRowAbsolute(self):
        # type: () -> bool
        pass

    @staticmethod
    def isRowWithinRange(rowNumOrStr, ssVersion):
        # type: (Union[int, AnyStr], SpreadsheetVersion) -> bool
        pass


class PaneInformation(Object):
    PANE_LOWER_LEFT = None  # type: int
    PANE_LOWER_RIGHT = None  # type: int
    PANE_UPPER_LEFT = None  # type: int
    PANE_UPPER_RIGHT = None  # type: int

    def __init__(self, x, y, top, left, active, frozen):
        # type: (int, int, int, int, int, bool) -> None
        super(PaneInformation, self).__init__()
        print(x, y, top, left, active, frozen)

    def getActivePane(self):
        # type: () -> int
        pass

    def getHorizontalSplitPosition(self):
        # type: () -> int
        pass

    def getHorizontalSplitTopRow(self):
        # type: () -> int
        pass

    def getVerticalSplitLeftColumn(self):
        # type: () -> int
        pass

    def getVerticalSplitPosition(self):
        # type: () -> int
        pass

    def isFreezePane(self):
        # type: () -> bool
        return True
