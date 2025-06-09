from typing import TYPE_CHECKING, Any, Dict, Iterator, List, Optional, Union

from dev.coatl.helper.types import AnyStr
from java.awt import Dimension
from java.io import Closeable, OutputStream
from java.lang import Enum, Object
from java.time import LocalDate, LocalDateTime
from java.util import Calendar, Date, TimeZone
from org.apache.poi.common.usermodel import Hyperlink as IHyperlink
from org.apache.poi.common.usermodel import HyperlinkType
from org.apache.poi.poifs.filesystem import DirectoryEntry
from org.apache.poi.ss import SpreadsheetVersion
from org.apache.poi.ss.formula.udf import UDFFinder
from org.apache.poi.ss.util import (
    AreaReference,
    CellAddress,
    CellRangeAddress,
    CellRangeAddressList,
    PaneInformation,
)

if TYPE_CHECKING:
    from org.apache.poi.ss.formula import ConditionalFormattingEvaluator


class AutoFilter(object):
    pass


class BorderFormatting(object):
    def getBorderBottom(self):
        # type: () -> BorderStyle
        raise NotImplementedError

    def getBorderDiagonal(self):
        # type: () -> BorderStyle
        raise NotImplementedError

    def getBorderHorizontal(self):
        # type: () -> BorderStyle
        raise NotImplementedError

    def getBorderLeft(self):
        # type: () -> BorderStyle
        raise NotImplementedError

    def getBorderRight(self):
        # type: () -> BorderStyle
        raise NotImplementedError

    def getBorderTop(self):
        # type: () -> BorderStyle
        raise NotImplementedError

    def getBorderVertical(self):
        # type: () -> BorderStyle
        raise NotImplementedError

    def getBottomBorderColor(self):
        # type: () -> int
        raise NotImplementedError

    def getBottomBorderColorColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getDiagonalBorderColor(self):
        # type: () -> int
        raise NotImplementedError

    def getDiagonalBorderColorColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getHorizontalBorderColor(self):
        # type: () -> int
        raise NotImplementedError

    def getHorizontalBorderColorColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getLeftBorderColor(self):
        # type: () -> int
        raise NotImplementedError

    def getLeftBorderColorColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getRightBorderColor(self):
        # type: () -> int
        raise NotImplementedError

    def getRightBorderColorColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getTopBorderColor(self):
        # type: () -> int
        raise NotImplementedError

    def getTopBorderColorColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getVerticalBorderColor(self):
        # type: () -> int
        raise NotImplementedError

    def getVerticalBorderColorColor(self):
        # type: () -> Color
        raise NotImplementedError

    def setBorderBottom(self, border):
        # type: (BorderStyle) -> None
        raise NotImplementedError

    def setBorderDiagonal(self, border):
        # type: (BorderStyle) -> None
        raise NotImplementedError

    def setBorderHorizontal(self, border):
        # type: (BorderStyle) -> None
        raise NotImplementedError

    def setBorderLeft(self, border):
        # type: (BorderStyle) -> None
        raise NotImplementedError

    def setBorderRight(self, border):
        # type: (BorderStyle) -> None
        raise NotImplementedError

    def setBorderTop(self, border):
        # type: (BorderStyle) -> None
        raise NotImplementedError

    def setBorderVertical(self, border):
        # type: (BorderStyle) -> None
        raise NotImplementedError

    def setBottomBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        raise NotImplementedError

    def setDiagonalBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        raise NotImplementedError

    def setHorizontalBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        raise NotImplementedError

    def setLeftBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        raise NotImplementedError

    def setRightBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        raise NotImplementedError

    def setTopBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        raise NotImplementedError

    def setVerticalBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        raise NotImplementedError


class Cell(object):
    def getAddress(self):
        # type: () -> CellAddress
        raise NotImplementedError

    def getArrayFormulaRange(self):
        # type: () -> CellRangeAddress
        raise NotImplementedError

    def getBooleanCellValue(self):
        # type: () -> bool
        raise NotImplementedError

    def getCachedFormulaResultType(self):
        # type: () -> CellType
        raise NotImplementedError

    def getCellComment(self):
        # type: () -> Comment
        raise NotImplementedError

    def getCellFormula(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getCellStyle(self):
        # type: () -> CellStyle
        raise NotImplementedError

    def getCellType(self):
        # type: () -> CellType
        raise NotImplementedError

    def getColumnIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getDateCellValue(self):
        # type: () -> Date
        raise NotImplementedError

    def getErrorCellValue(self):
        # type: () -> int
        raise NotImplementedError

    def getHyperlink(self):
        # type: () -> Hyperlink
        raise NotImplementedError

    def getLocalDateTimeCellValue(self):
        # type: () -> LocalDateTime
        raise NotImplementedError

    def getNumericCellValue(self):
        # type: () -> float
        raise NotImplementedError

    def getRichStringCellValue(self):
        # type: () -> RichTextString
        raise NotImplementedError

    def getRow(self):
        # type: () -> Row
        raise NotImplementedError

    def getRowIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getSheet(self):
        # type: () -> Sheet
        raise NotImplementedError

    def getStringCellValue(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def isPartOfArrayFormulaGroup(self):
        # type: () -> bool
        raise NotImplementedError

    def removeCellComment(self):
        # type: () -> None
        raise NotImplementedError

    def removeFormula(self):
        # type: () -> None
        raise NotImplementedError

    def removeHyperlink(self):
        # type: () -> None
        raise NotImplementedError

    def setAsActiveCell(self):
        # type: () -> None
        raise NotImplementedError

    def setBlank(self):
        # type: () -> None
        raise NotImplementedError

    def setCellComment(self, comment):
        # type: (Comment) -> None
        raise NotImplementedError

    def setCellErrorValue(self, value):
        # type: (int) -> None
        raise NotImplementedError

    def setCellFormula(self, formula):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setCellStyle(self, style):
        # type: (CellStyle) -> None
        raise NotImplementedError

    def setCellValue(self, value):
        # type: (Any) -> None
        raise NotImplementedError

    def setHyperlink(self, link):
        # type: (Hyperlink) -> None
        raise NotImplementedError


class CellRange(object):

    def getCell(self, relativeRowIndex, relativeColumnIndex):
        # type: (int, int) -> Cell
        raise NotImplementedError

    def getCells(self):
        # type: () -> List[List[Cell]]
        raise NotImplementedError

    def getFlattenedCells(self):
        # type: () -> List[Cell]
        raise NotImplementedError

    def getHeight(self):
        # type: () -> int
        raise NotImplementedError

    def getReferenceText(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getTopLeftCell(self):
        # type: () -> Cell
        raise NotImplementedError

    def getWidth(self):
        # type: () -> int
        raise NotImplementedError

    def size(self):
        # type: () -> int
        raise NotImplementedError

    def __iter__(self):
        # type: () -> Iterator[Cell]
        pass


class CellStyle(object):
    def cloneStyleFrom(self, source):
        # type: (CellStyle) -> None
        raise NotImplementedError

    def getAlignment(self):
        # type: () -> HorizontalAlignment
        raise NotImplementedError

    def getBorderBottom(self):
        # type: () -> BorderStyle
        raise NotImplementedError

    def getBorderLeft(self):
        # type: () -> BorderStyle
        raise NotImplementedError

    def getBorderRight(self):
        # type: () -> BorderStyle
        raise NotImplementedError

    def getBorderTop(self):
        # type: () -> BorderStyle
        raise NotImplementedError

    def getBottomBorderColor(self):
        # type: () -> int
        raise NotImplementedError

    def getDataFormat(self):
        # type: () -> int
        raise NotImplementedError

    def getDataFormatString(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getFillBackgroundColor(self):
        # type: () -> int
        raise NotImplementedError

    def getFillBackgroundColorColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getFillForegroundColor(self):
        # type: () -> int
        raise NotImplementedError

    def getFillForegroundColorColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getFillPattern(self):
        # type: () -> FillPatternType
        raise NotImplementedError

    def getFontIndexAsInt(self):
        # type: () -> int
        raise NotImplementedError

    def getHidden(self):
        # type: () -> bool
        raise NotImplementedError

    def getIndention(self):
        # type: () -> int
        raise NotImplementedError

    def getIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getLeftBorderColor(self):
        # type: () -> int
        raise NotImplementedError

    def getLocked(self):
        # type: () -> bool
        raise NotImplementedError

    def getQuotePrefixed(self):
        # type: () -> bool
        raise NotImplementedError

    def getRightBorderColor(self):
        # type: () -> int
        raise NotImplementedError

    def getRotation(self):
        # type: () -> int
        raise NotImplementedError

    def getShrinkToFit(self):
        # type: () -> bool
        raise NotImplementedError

    def getTopBorderColor(self):
        # type: () -> int
        raise NotImplementedError

    def getVerticalAlignment(self):
        # type: () -> VerticalAlignment
        raise NotImplementedError

    def getWrapText(self):
        # type: () -> bool
        raise NotImplementedError

    def setAlignment(self, align):
        # type: (HorizontalAlignment) -> None
        raise NotImplementedError

    def setDataFormat(self, formatIndex):
        # type: (int) -> None
        raise NotImplementedError

    def setFillBackgroundColor(self, colorIndex):
        # type: (int) -> None
        raise NotImplementedError

    def setFillForegroundColor(self, colorIndex):
        # type: (int) -> None
        raise NotImplementedError


class ChildAnchor(object):
    def getDx1(self):
        # type: () -> int
        raise NotImplementedError

    def getDx2(self):
        # type: () -> int
        raise NotImplementedError

    def getDy1(self):
        # type: () -> int
        raise NotImplementedError

    def getDy2(self):
        # type: () -> int
        raise NotImplementedError

    def getCol1(self):
        # type: () -> int
        raise NotImplementedError

    def getCol2(self):
        # type: () -> int
        raise NotImplementedError

    def getRow1(self):
        # type: () -> int
        raise NotImplementedError

    def getRow2(self):
        # type: () -> int
        raise NotImplementedError


class ClientAnchor(object):
    class AnchorType(Enum):
        DONT_MOVE_AND_RESIZE = 0  # type: int
        DONT_MOVE_DO_RESIZE = 1  # type: int
        MOVE_AND_RESIZE = 2  # type: int
        MOVE_DONT_RESIZE = 3  # type: int

        value = None  # type: int

        @staticmethod
        def byId(value):
            # type: (int) -> ClientAnchor.AnchorType
            pass

        @staticmethod
        def values():
            # type: () -> List[ClientAnchor.AnchorType]
            pass

    def getAnchorType(self):
        # type: () -> ClientAnchor.AnchorType
        raise NotImplementedError

    def getCol1(self):
        # type: () -> int
        raise NotImplementedError

    def getCol2(self):
        # type: () -> int
        raise NotImplementedError

    def getDx1(self):
        # type: () -> int
        raise NotImplementedError

    def getDx2(self):
        # type: () -> int
        raise NotImplementedError

    def getDy1(self):
        # type: () -> int
        raise NotImplementedError

    def getDy2(self):
        # type: () -> int
        raise NotImplementedError

    def getRow1(self):
        # type: () -> int
        raise NotImplementedError

    def getRow2(self):
        # type: () -> int
        raise NotImplementedError

    def setAnchorType(self, anchorType):
        # type: (ClientAnchor.AnchorType) -> None
        raise NotImplementedError

    def setCol1(self, col1):
        # type: (int) -> None
        raise NotImplementedError

    def setCol2(self, col2):
        # type: (int) -> None
        raise NotImplementedError

    def setDx1(self, dx1):
        # type: (int) -> None
        raise NotImplementedError

    def setDx2(self, dx2):
        # type: (int) -> None
        raise NotImplementedError

    def setDy1(self, dy1):
        # type: (int) -> None
        raise NotImplementedError

    def setDy2(self, dy2):
        # type: (int) -> None
        raise NotImplementedError

    def setRow1(self, row1):
        # type: (int) -> None
        raise NotImplementedError

    def setRow2(self, row2):
        # type: (int) -> None
        raise NotImplementedError


class Color(object):
    pass


class ColorScaleFormatting(object):
    def createThreshold(self):
        # type: () -> ConditionalFormattingThreshold
        raise NotImplementedError

    def getColors(self):
        # type: () -> List[Color]
        raise NotImplementedError

    def getNumControlPoints(self):
        # type: () -> int
        raise NotImplementedError

    def getThresholds(self):
        # type: () -> List[ConditionalFormattingThreshold]
        raise NotImplementedError

    def setColors(self, colors):
        # type: (List[Color]) -> None
        raise NotImplementedError

    def setNumControlPoints(self, num):
        # type: (int) -> None
        raise NotImplementedError

    def setThresholds(self, thresholds):
        # type: (List[ConditionalFormattingThreshold]) -> None
        raise NotImplementedError


class Comment(object):
    def getAddress(self):
        # type: () -> CellAddress
        raise NotImplementedError

    def getAuthor(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getClientAnchor(self):
        # type: () -> ClientAnchor
        raise NotImplementedError

    def getColumn(self):
        # type: () -> int
        raise NotImplementedError

    def getRow(self):
        # type: () -> int
        raise NotImplementedError

    def getString(self):
        # type: () -> RichTextString
        raise NotImplementedError

    def isVisible(self):
        # type: () -> bool
        raise NotImplementedError

    def setAddress(self, *args):
        # type: (*Any) -> None
        raise NotImplementedError

    def setAuthor(self, author):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setColumn(self, column):
        # type: (int) -> None
        raise NotImplementedError

    def setRow(self, row):
        # type: (int) -> None
        raise NotImplementedError

    def setString(self, string):
        # type: (RichTextString) -> None
        raise NotImplementedError

    def setVisible(self, visible):
        # type: (bool) -> None
        raise NotImplementedError


class ConditionFilterData(object):
    def getAboveAverage(self):
        # type: () -> bool
        raise NotImplementedError

    def getBottom(self):
        # type: () -> int
        raise NotImplementedError

    def getEqualAverage(self):
        # type: () -> bool
        raise NotImplementedError

    def getPercent(self):
        # type: () -> bool
        raise NotImplementedError

    def getRank(self):
        # type: () -> long
        raise NotImplementedError

    def getStdDev(self):
        # type: () -> int
        raise NotImplementedError


class ConditionalFormatting(object):
    def addRule(self, cfRule):
        # type: (ConditionalFormattingRule) -> None
        raise NotImplementedError

    def getFormattingRanges(self):
        # type: () -> List[CellRangeAddress]
        raise NotImplementedError

    def getNumberOfRules(self):
        # type: () -> int
        raise NotImplementedError

    def getRule(self, idx):
        # type: (int) -> ConditionalFormattingRule
        raise NotImplementedError

    def setFormattingRanges(self, ranges):
        # type: (List[CellRangeAddress]) -> None
        raise NotImplementedError

    def setRule(self, idx, cfRule):
        # type: (int, ConditionalFormattingRule) -> None
        raise NotImplementedError


class ConditionalFormattingRule(object):
    def createBorderFormatting(self):
        # type: () -> BorderFormatting
        raise NotImplementedError

    def createFontFormatting(self):
        # type: () -> FontFormatting
        raise NotImplementedError

    def createPatternFormatting(self):
        # type: () -> PatternFormatting
        raise NotImplementedError

    def getBorderFormatting(self):
        # type: () -> BorderFormatting
        raise NotImplementedError

    def getColorScaleFormatting(self):
        # type: () -> ColorScaleFormatting
        raise NotImplementedError

    def getComparisonOperation(self):
        # type: () -> int
        raise NotImplementedError

    def getConditionFilterType(self):
        # type: () -> ConditionFilterType
        raise NotImplementedError

    def getConditionType(self):
        # type: () -> ConditionType
        raise NotImplementedError

    def getDataBarFormatting(self):
        # type: () -> DataBarFormatting
        raise NotImplementedError

    def getFilterConfiguration(self):
        # type: () -> ConditionFilterData
        raise NotImplementedError

    def getFontFormatting(self):
        # type: () -> FontFormatting
        raise NotImplementedError

    def getFormula1(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getFormula2(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getMultiStateFormatting(self):
        # type: () -> IconMultiStateFormatting
        raise NotImplementedError

    def getNumberFormatting(self):
        # type: () -> ExcelNumberFormat
        raise NotImplementedError

    def getPatternFormatting(self):
        # type: () -> PatternFormatting
        raise NotImplementedError

    def getPriority(self):
        # type: () -> int
        raise NotImplementedError

    def getStopIfTrue(self):
        # type: () -> bool
        raise NotImplementedError

    def getText(self):
        # type: () -> AnyStr
        raise NotImplementedError


class ConditionalFormattingThreshold(object):
    class RangeType(Enum):
        FORMULA = None  # type: ConditionalFormattingThreshold.RangeType
        MAX = None  # type: ConditionalFormattingThreshold.RangeType
        MIN = None  # type: ConditionalFormattingThreshold.RangeType
        NUMBER = None  # type: ConditionalFormattingThreshold.RangeType
        PERCENT = None  # type: ConditionalFormattingThreshold.RangeType
        PERCENTILE = None  # type: ConditionalFormattingThreshold.RangeType
        UNALLOCATED = None  # type: ConditionalFormattingThreshold.RangeType

        @staticmethod
        def byId(id_):
            # type: (int) -> ConditionalFormattingThreshold.RangeType
            pass

        @staticmethod
        def byName(name):
            # type: (AnyStr) -> ConditionalFormattingThreshold.RangeType
            pass

        @staticmethod
        def values():
            # type: () -> List[ConditionalFormattingThreshold.RangeType]
            pass

    def getFormula(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getRangeType(self):
        # type: () -> ConditionalFormattingThreshold.RangeType
        raise NotImplementedError

    def getValue(self):
        # type: () -> float
        raise NotImplementedError

    def setFormula(self, formula):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setRangeType(self, rangeType):
        # type: (ConditionalFormattingThreshold.RangeType) -> None
        raise NotImplementedError

    def setValue(self, value):
        # type: (float) -> None
        raise NotImplementedError


class CreationHelper(object):
    def createAreaReference(self, *args):
        # type: (*Any) -> AreaReference
        raise NotImplementedError

    def createClientAnchor(self):
        # type: () -> ClientAnchor
        raise NotImplementedError

    def createDataFormat(self):
        # type: () -> DataFormat
        raise NotImplementedError

    def createExtendedColor(self):
        # type: () -> ExtendedColor
        raise NotImplementedError

    def createFormulaEvaluator(self):
        # type: () -> FormulaEvaluator
        raise NotImplementedError

    def createHyperlink(self, type):
        # type: (HyperlinkType) -> Hyperlink
        raise NotImplementedError

    def createRichTextString(self, text):
        # type: (AnyStr) -> RichTextString
        raise NotImplementedError


class DataBarFormatting(object):
    def getColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getMaxThreshold(self):
        # type: () -> ConditionalFormattingThreshold
        raise NotImplementedError

    def getMinThreshold(self):
        # type: () -> ConditionalFormattingThreshold
        raise NotImplementedError

    def getWidthMax(self):
        # type: () -> int
        raise NotImplementedError

    def getWidthMin(self):
        # type: () -> int
        raise NotImplementedError

    def isIconOnly(self):
        # type: () -> bool
        raise NotImplementedError

    def isLeftToRight(self):
        # type: () -> bool
        raise NotImplementedError

    def setColor(self, color):
        # type: (Color) -> None
        raise NotImplementedError

    def setIconOnly(self, only):
        # type: (bool) -> None
        raise NotImplementedError

    def setLeftToRight(self, ltr):
        # type: (bool) -> None
        raise NotImplementedError

    def setWidthMax(self, width):
        # type: (int) -> None
        raise NotImplementedError

    def setWidthMin(self, width):
        # type: (int) -> None
        raise NotImplementedError


class DataFormat(object):
    def getFormat(self, arg):
        # type: (Union[int, AnyStr]) -> int
        raise NotImplementedError


class DataValidation(object):
    class ErrorStyle(object):
        STOP = 0  # type: int
        WARNING = 1  # type: int
        INFO = 2  # type: int

    def createErrorBox(self, title, text):
        # type: (AnyStr, AnyStr) -> None
        raise NotImplementedError

    def createPromptBox(self, title, text):
        # type: (AnyStr, AnyStr) -> None
        raise NotImplementedError

    def getEmptyCellAllowed(self):
        # type: () -> bool
        raise NotImplementedError

    def getErrorBoxText(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getErrorBoxTitle(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getErrorStyle(self):
        # type: () -> int
        raise NotImplementedError

    def getPromptBoxText(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getPromptBoxTitle(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getRegions(self):
        # type: () -> CellRangeAddressList
        raise NotImplementedError

    def showShowErrorBox(self):
        # type: () -> bool
        raise NotImplementedError

    def showShowPromptBox(self):
        # type: () -> bool
        raise NotImplementedError

    def getSuppressDropDownArrow(self):
        # type: () -> bool
        raise NotImplementedError

    def getValidationConstraint(self):
        # type: () -> DataValidationConstraint
        raise NotImplementedError

    def setEmptyCellAllowed(self, allowed):
        # type: (bool) -> None
        raise NotImplementedError

    def setErrorStyle(self, error_style):
        # type: (int) -> None
        raise NotImplementedError

    def setShowErrorBox(self, show):
        # type: (bool) -> None
        raise NotImplementedError

    def setShowPromptBox(self, show):
        # type: (bool) -> None
        raise NotImplementedError

    def setSuppressDropDownArrow(self, suppress):
        # type: (bool) -> None
        raise NotImplementedError


class DataValidationConstraint(object):
    class OperatorType(Object):
        BETWEEN = 0  # type: int
        NOT_BETWEEN = 1  # type: int
        EQUAL = 2  # type: int
        NOT_EQUAL = 3  # type: int
        GREATER_THAN = 4  # type: int
        LESS_THAN = 5  # type: int
        GREATER_OR_EQUAL = 6  # type: int
        LESS_OR_EQUAL = 7  # type: int
        IGNORED = 0  # type: int

        def validateSecondArg(self, comparisonOperator, paramValue):
            # type: (int, AnyStr) -> None
            pass

    class ValidationType(Object):
        ANY = 0  # type: int
        INTEGER = 1  # type: int
        DECIMAL = 2  # type: int
        LIST = 3  # type: int
        DATE = 4  # type: int
        TIME = 5  # type: int
        TEXT_LENGTH = 6  # type: int
        FORMULA = 7  # type: int

    def getExplicitListValues(self):
        # type: () -> List[AnyStr]
        raise NotImplementedError

    def getFormula1(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getFormula2(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getOperator(self):
        # type: () -> int
        raise NotImplementedError

    def getValidationType(self):
        # type: () -> int
        raise NotImplementedError

    def setExplicitListValues(self, explicitListValues):
        # type: (List[AnyStr]) -> None
        raise NotImplementedError

    def setFormula1(self, formula):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setFormula2(self, formula):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setOperator(self, operator):
        # type: (int) -> None
        raise NotImplementedError


class DataValidationHelper(object):
    def createCustomConstraint(self, formula):
        # type: (AnyStr) -> DataValidationConstraint
        raise NotImplementedError

    def createDateConstraint(
        self,
        operatorType,  # type: int
        formula1,  # type: AnyStr
        formula2,  # type: AnyStr
        dateFormat,  # type: AnyStr
    ):
        # type: (...) -> DataValidationConstraint
        raise NotImplementedError

    def createDecimalConstraint(self, operatorType, formula1, formula2):
        # type: (int, AnyStr, AnyStr) -> DataValidationConstraint
        raise NotImplementedError

    def createExplicitListConstraint(self, listOfValues):
        # type: (List[AnyStr]) -> DataValidationConstraint
        raise NotImplementedError

    def createFormulaListConstraint(self, listFormula):
        # type: (AnyStr) -> DataValidationConstraint
        raise NotImplementedError

    def createIntegerConstraint(self, operatorType, formula1, formula2):
        # type: (int, AnyStr, AnyStr) -> DataValidationConstraint
        raise NotImplementedError

    def createNumericConstraint(self, validationType, operatorType, formula1, formula2):
        # type: (int, int, AnyStr, AnyStr) -> DataValidationConstraint
        raise NotImplementedError

    def createTextLengthConstraint(self, operatorType, formula1, formula2):
        # type: (int, AnyStr, AnyStr) -> DataValidationConstraint
        raise NotImplementedError

    def createTimeConstraint(self, operatorType, formula1, formula2):
        # type: (int, AnyStr, AnyStr) -> DataValidationConstraint
        raise NotImplementedError

    def createValidation(
        self,
        constraint,  # type: DataValidationConstraint
        cellRangeAddressList,  # type: CellRangeAddressList
    ):
        # type: (...) -> DataValidation
        raise NotImplementedError


class DateUtil(Object):
    DAY_MILLISECONDS = None  # type: long
    HOURS_PER_DAY = None  # type: int
    MINUTES_PER_HOUR = None  # type: int
    SECONDS_PER_DAY = None  # type: int
    SECONDS_PER_SECOND = None  # type: int

    @staticmethod
    def convertTime(timeStr):
        # type: (AnyStr) -> float
        pass

    @staticmethod
    def getExcelDate(
        date,  # type: Union[Calendar, Date, LocalDate, LocalDateTime]
        use1904windowing=False,  # type: bool
    ):
        # type: (...) -> float
        pass

    @staticmethod
    def getJavaCalendar(
        date,  # type: float
        use1904windowing=False,  # type: bool
        timezone=None,  # type: Optional[TimeZone]
        roundSeconds=False,  # type: bool
    ):
        # type: (...) -> Calendar
        pass

    @staticmethod
    def getJavCalendarUTC(date, use1904windowing=False):
        # type: (float, bool) -> Calendar
        pass

    @staticmethod
    def getJavaDate(
        date,  # type: float
        use1904windowing=False,  # type: bool
        timezone=None,  # type: Optional[TimeZone]
        roundSeconds=False,  # type: bool
    ):
        # type: (...) -> Date
        pass

    @staticmethod
    def getLocalDateTime(
        date,  # type: float
        use1904windowing=False,  # type: bool
        roundSeconds=False,  # type: bool
    ):
        # type: (...) -> LocalDateTime
        pass

    @staticmethod
    def isADateFormat(numFmt):
        # type: (ExcelNumberFormat) -> bool
        return True

    @staticmethod
    def isCellDateFormatted(cell, cfEvaluator=None):
        # type: (Cell, Optional[ConditionalFormattingEvaluator]) -> bool
        return True

    @staticmethod
    def isCellInternalDateFormatted(cell):
        # type: (Cell) -> bool
        pass

    @staticmethod
    def isInternalDateFormat(format):
        # type: (int) -> bool
        pass

    @staticmethod
    def isValidExcelDate(date):
        # type: (float) -> bool
        pass

    @staticmethod
    def parseDateTime(str_):
        # type: (AnyStr) -> float
        pass

    @staticmethod
    def parseYYYYMMDDDate(dateStr):
        # type: (AnyStr) -> float
        pass

    @staticmethod
    def setCalendar(
        calendar, wholeDays, millisecondsInDay, use1904windowing, roundSeconds
    ):
        # type: (Calendar, int, int, bool, bool) -> None
        pass

    @staticmethod
    def toLocalDateTime(date):
        # type: (Union[Calendar, Date]) -> LocalDateTime
        pass


class Font(object):
    COLOR_NORMAL = 32767  # type: int
    COLOR_RED = 10  # type: int
    SS_NONE = 0  # type: int
    SS_SUPER = 1  # type: int
    SS_SUB = 2  # type: int
    U_NONE = 0  # type: int
    U_SINGLE = 1  # type: int
    U_DOUBLE = 2  # type: int
    U_SINGLE_ACCOUNTING = 33  # type: int
    U_DOUBLE_ACCOUNTING = 34  # type: int
    ANSI_CHARSET = 0  # type: int
    DEFAULT_CHARSET = 1  # type: int
    SYMBOL_CHARSET = 2  # type: int

    def getBold(self):
        # type: () -> bool
        raise NotImplementedError

    def getCharSet(self):
        # type: () -> int
        raise NotImplementedError

    def getColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getFontHeight(self):
        # type: () -> int
        raise NotImplementedError

    def getFontHeightInPoints(self):
        # type: () -> int
        raise NotImplementedError

    def getFontName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getIndexAsInt(self):
        # type: () -> int
        raise NotImplementedError

    def getItalic(self):
        # type: () -> bool
        raise NotImplementedError

    def getStrikeout(self):
        # type: () -> bool
        raise NotImplementedError

    def getTypeOffset(self):
        # type: () -> int
        raise NotImplementedError

    def getUnderline(self):
        # type: () -> int
        raise NotImplementedError

    def setBold(self, bold):
        # type: (bool) -> None
        raise NotImplementedError

    def setCharSet(self, charset):
        # type: (int) -> None
        raise NotImplementedError

    def setColor(self, color):
        # type: (Color) -> None
        raise NotImplementedError

    def setFontHeight(self, height):
        # type: (int) -> None
        raise NotImplementedError

    def setFontHeightInPoints(self, height):
        # type: (int) -> None
        raise NotImplementedError

    def setFontName(self, name):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setItalic(self, italic):
        # type: (bool) -> None
        raise NotImplementedError

    def setStrikeout(self, strikeout):
        # type: (bool) -> None
        raise NotImplementedError

    def setTypeOffset(self, offset):
        # type: (int) -> None
        raise NotImplementedError

    def setUnderline(self, underline):
        # type: (int) -> None
        raise NotImplementedError


class FontFormatting(object):
    SS_NONE = 0  # type: int
    SS_SUPER = 1  # type: int
    SS_SUB = 2  # type: int
    U_NONE = 0  # type: int
    U_SINGLE = 1  # type: int
    U_DOUBLE = 2  # type: int
    U_SINGLE_ACCOUNTING = 33  # type: int
    U_DOUBLE_ACCOUNTING = 34  # type: int

    def getEscapementType(self):
        # type: () -> int
        raise NotImplementedError

    def getFontColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getFontColorIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getFontHeight(self):
        # type: () -> int
        raise NotImplementedError

    def getUnderlineType(self):
        # type: () -> int
        raise NotImplementedError

    def isBold(self):
        # type: () -> bool
        raise NotImplementedError

    def isItalic(self):
        # type: () -> bool
        raise NotImplementedError

    def isStruckout(self):
        # type: () -> bool
        raise NotImplementedError

    def resetFontStyle(self):
        # type: () -> None
        raise NotImplementedError

    def setEscapementType(self, escapementType):
        # type: (int) -> None
        raise NotImplementedError

    def setFontColor(self, color):
        # type: (Color) -> None
        raise NotImplementedError

    def setFontColorIndex(self, color):
        # type: (int) -> None
        raise NotImplementedError

    def setFontHeight(self, height):
        # type: (int) -> None
        raise NotImplementedError

    def setFontStyle(self, italic, bold):
        # type: (bool, bool) -> None
        raise NotImplementedError

    def setUnderlineType(self, underlineType):
        # type: (int) -> None
        raise NotImplementedError


class HeaderFooter(object):
    def getCenter(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getLeft(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getRight(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def setCenter(self, newCenter):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setLeft(self, newLeft):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setRight(self, newRight):
        # type: (AnyStr) -> None
        raise NotImplementedError


class Footer(HeaderFooter):
    def getCenter(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getLeft(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getRight(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def setCenter(self, newCenter):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setLeft(self, newLeft):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setRight(self, newRight):
        # type: (AnyStr) -> None
        raise NotImplementedError


class FormulaEvaluator(object):
    def clearAllCachedResultValues(self):
        # type: () -> None
        raise NotImplementedError

    def evaluate(self, cell):
        # type: (Cell) -> CellValue
        raise NotImplementedError

    def evaluateAll(self):
        # type: () -> None
        raise NotImplementedError

    def evaluateFormulaCell(self, cell):
        # type: (Cell) -> CellType
        raise NotImplementedError

    def evaluateInCell(self, cell):
        # type: (Cell) -> Cell
        raise NotImplementedError

    def notifyDeleteCell(self, cell):
        # type: (Cell) -> None
        raise NotImplementedError

    def notifyUpdateCell(self, cell):
        # type: (Cell) -> None
        raise NotImplementedError

    def notifySetFormula(self, cell):
        # type: (Cell) -> None
        raise NotImplementedError

    def setDebugEvaluationOutputForNextEval(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setIgnoreMissingWorkbooks(self, ignore):
        # type: (bool) -> None
        raise NotImplementedError

    def setupReferencedWorkbooks(self, workbooks):
        # type: (Dict[AnyStr, FormulaEvaluator]) -> None
        raise NotImplementedError


class Header(HeaderFooter):
    def getCenter(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getLeft(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getRight(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def setCenter(self, newCenter):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setLeft(self, newLeft):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setRight(self, newRight):
        # type: (AnyStr) -> None
        raise NotImplementedError


class Hyperlink(IHyperlink):
    def getFirstColumn(self):
        # type: () -> int
        raise NotImplementedError

    def getFirstRow(self):
        # type: () -> int
        raise NotImplementedError

    def getLastColumn(self):
        # type: () -> int
        raise NotImplementedError

    def getLastRow(self):
        # type: () -> int
        raise NotImplementedError

    def setFirstColumn(self, col):
        # type: (int) -> None
        raise NotImplementedError

    def setFirstRow(self, row):
        # type: (int) -> None
        raise NotImplementedError

    def setLastColumn(self, col):
        # type: (int) -> None
        raise NotImplementedError

    def setLastRow(self, row):
        # type: (int) -> None
        raise NotImplementedError


class IconMultiStateFormatting(object):
    class IconSet(Enum):
        GREY_3_ARROWS = None  # type: IconMultiStateFormatting.IconSet
        GREY_4_ARROWS = None  # type: IconMultiStateFormatting.IconSet
        GREY_5_ARROWS = None  # type: IconMultiStateFormatting.IconSet
        GYR_3_ARROW = None  # type: IconMultiStateFormatting.IconSet
        GYR_3_FLAGS = None  # type: IconMultiStateFormatting.IconSet
        GYR_3_SHAPES = None  # type: IconMultiStateFormatting.IconSet
        GYR_3_SYMBOLS = None  # type: IconMultiStateFormatting.IconSet
        GYR_3_SYMBOLS_CIRCLE = None  # type: IconMultiStateFormatting.IconSet
        GYR_3_TRAFFIC_LIGHTS = None  # type: IconMultiStateFormatting.IconSet
        GYR_3_TRAFFIC_LIGHTS_BOX = None  # type: IconMultiStateFormatting.IconSet
        GYR_4_ARROWS = None  # type: IconMultiStateFormatting.IconSet
        GYRB_4_TRAFFIC_LIGHTS = None  # type: IconMultiStateFormatting.IconSet
        GYYYR_5_ARROWS = None  # type: IconMultiStateFormatting.IconSet
        QUARTERS_5 = None  # type: IconMultiStateFormatting.IconSet
        RATINGS_4 = None  # type: IconMultiStateFormatting.IconSet
        RATINGS_5 = None  # type: IconMultiStateFormatting.IconSet
        RB_4_TRAFFIC_LIGHTS = None  # type: IconMultiStateFormatting.IconSet

        @staticmethod
        def byId(id):
            # type: (int) -> IconMultiStateFormatting.IconSet
            pass

        @staticmethod
        def byName(name):
            # type: (AnyStr) -> IconMultiStateFormatting.IconSet
            pass

        @staticmethod
        def values():
            # type: () -> List[IconMultiStateFormatting.IconSet]
            pass

    def createThreshold(self):
        # type: () -> ConditionalFormattingThreshold
        raise NotImplementedError

    def getIconSet(self):
        # type: () -> IconSet
        raise NotImplementedError

    def getThresholds(self):
        # type: () -> List[ConditionalFormattingThreshold]
        raise NotImplementedError

    def isIconOnly(self):
        # type: () -> bool
        raise NotImplementedError

    def isReversed(self):
        # type: () -> bool
        raise NotImplementedError

    def setIconOnly(self, only):
        # type: (bool) -> None
        raise NotImplementedError

    def setIconSet(self, set):
        # type: (IconSet) -> None
        raise NotImplementedError

    def setReversed(self, reversed):
        # type: (bool) -> None
        raise NotImplementedError

    def setThresholds(self, thresholds):
        # type: (List[ConditionalFormattingThreshold]) -> None
        raise NotImplementedError


class Name(object):
    def getComment(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getNameName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getRefersToFormula(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getSheetIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getSheetName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def isDeleted(self):
        # type: () -> bool
        raise NotImplementedError

    def isFunctionName(self):
        # type: () -> bool
        raise NotImplementedError

    def setComment(self, comment):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setFunction(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setNameName(self, name):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setRefersToFormula(self, formulaText):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setSheetIndex(self, sheetId):
        # type: (int) -> None
        raise NotImplementedError


class Shape(object):
    def getAnchor(self):
        # type: () -> ChildAnchor
        raise NotImplementedError

    def getParent(self):
        # type: () -> Shape
        raise NotImplementedError

    def getShapeName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def isNoFill(self):
        # type: () -> bool
        raise NotImplementedError

    def setFillColor(self, red, green, blue):
        # type: (int, int, int) -> None
        raise NotImplementedError

    def setLineStyleColor(self, red, green, blue):
        # type: (int, int, int) -> None
        raise NotImplementedError

    def setNoFill(self, noFill):
        # type: (bool) -> None
        raise NotImplementedError


class Picture(Shape):
    def getClientAnchor(self):
        # type: () -> ClientAnchor
        raise NotImplementedError

    def getImageDimension(self):
        # type: () -> Dimension
        raise NotImplementedError

    def getPictureData(self):
        # type: () -> PictureData
        raise NotImplementedError

    def getPreferredSize(self, scaleX=1, scaleY=1):
        # type: (int, int) -> ClientAnchor
        raise NotImplementedError

    def getSheet(self):
        # type: () -> Sheet
        raise NotImplementedError

    def resize(self, *args):
        # type: (*Any) -> AnyStr
        raise NotImplementedError


class PatternFormatting(object):
    NO_FILL = 0  # type: int
    SOLID_FOREGROUND = 1  # type: int
    FINE_DOTS = 2  # type: int
    ALT_BARS = 3  # type: int
    SPARSE_DOTS = 4  # type: int
    THICK_HORZ_BANDS = 5  # type: int
    THICK_VERT_BANDS = 6  # type: int
    THICK_BACKWARD_DIAG = 7  # type: int
    THICK_FORWARD_DIAG = 8  # type: int
    BIG_SPOTS = 9  # type: int
    BRICKS = 10  # type: int
    THIN_BACKWARD_DIAG = 11  # type: int
    THIN_VERT_BANDS = 12  # type: int
    THIN_HORZ_BANDS = 13  # type: int
    THIN_FORWARD_DIAG = 14  # type: int
    SQUARES = 15  # type: int
    DIAMONDS = 16  # type: int
    LESS_DOTS = 17  # type: int
    LEAST_DOTS = 18  # type: int

    def getFillBackgroundColor(self):
        # type: () -> int
        raise NotImplementedError

    def getFillBackgroundColorColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getFillForegroundColor(self):
        # type: () -> int
        raise NotImplementedError

    def getFillForegroundColorColor(self):
        # type: () -> Color
        raise NotImplementedError

    def getFillPattern(self):
        # type: () -> FillPatternType
        raise NotImplementedError

    def setFillBackgroundColor(self, bg):
        # type: (Union[int, Color]) -> None
        raise NotImplementedError

    def setFillForegroundColor(self, bg):
        # type: (Union[int, Color]) -> None
        raise NotImplementedError

    def setFillPattern(self, fp):
        # type: (FillPatternType) -> None
        raise NotImplementedError


class PictureData(object):
    def getData(self):
        # type: () -> bytearray
        raise NotImplementedError

    def getMimeType(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getPictureType(self):
        # type: () -> int
        raise NotImplementedError

    def suggestFileExtension(self):
        # type: () -> AnyStr
        raise NotImplementedError


class PrintSetup(object):
    PRINTER_DEFAULT_PAPERSIZE = 0
    LETTER_PAPERSIZE = 1
    LETTER_SMALL_PAGESIZE = 2
    TABLOID_PAPERSIZE = 3
    LEDGER_PAPERSIZE = 4
    LEGAL_PAPERSIZE = 5
    STATEMENT_PAPERSIZE = 6
    EXECUTIVE_PAPERSIZE = 7
    A3_PAPERSIZE = 8
    A4_PAPERSIZE = 9
    A4_SMALL_PAPERSIZE = 10
    A5_PAPERSIZE = 11
    B4_PAPERSIZE = 12
    B5_PAPERSIZE = 13
    FOLIO8_PAPERSIZE = 14
    QUARTO_PAPERSIZE = 15
    TEN_BY_FOURTEEN_PAPERSIZE = 16
    ELEVEN_BY_SEVENTEEN_PAPERSIZE = 17
    NOTE8_PAPERSIZE = 18
    ENVELOPE_9_PAPERSIZE = 19
    ENVELOPE_10_PAPERSIZE = 20
    ENVELOPE_DL_PAPERSIZE = 27
    ENVELOPE_CS_PAPERSIZE = 28
    ENVELOPE_C5_PAPERSIZE = 28
    ENVELOPE_C3_PAPERSIZE = 29
    ENVELOPE_C4_PAPERSIZE = 30
    ENVELOPE_C6_PAPERSIZE = 31
    ENVELOPE_MONARCH_PAPERSIZE = 37
    A4_EXTRA_PAPERSIZE = 53
    A4_TRANSVERSE_PAPERSIZE = 55
    A4_PLUS_PAPERSIZE = 60
    LETTER_ROTATED_PAPERSIZE = 75
    A4_ROTATED_PAPERSIZE = 77

    def getCopies(self):
        # type: () -> int
        raise NotImplementedError

    def getDraft(self):
        # type: () -> bool
        raise NotImplementedError

    def getFitHeight(self):
        # type: () -> int
        raise NotImplementedError

    def getFitWidth(self):
        # type: () -> int
        raise NotImplementedError

    def getFooterMargin(self):
        # type: () -> float
        raise NotImplementedError

    def getHeaderMargin(self):
        # type: () -> float
        raise NotImplementedError

    def getHResolution(self):
        # type: () -> int
        raise NotImplementedError

    def getLandscape(self):
        # type: () -> bool
        raise NotImplementedError

    def getLeftToRight(self):
        # type: () -> bool
        raise NotImplementedError

    def getNoColor(self):
        # type: () -> bool
        raise NotImplementedError

    def getNoOrientation(self):
        # type: () -> bool
        raise NotImplementedError

    def getNotes(self):
        # type: () -> bool
        raise NotImplementedError

    def getPageStart(self):
        # type: () -> int
        raise NotImplementedError

    def getPaperSize(self):
        # type: () -> int
        raise NotImplementedError

    def getScale(self):
        # type: () -> int
        raise NotImplementedError

    def getUsePage(self):
        # type: () -> bool
        raise NotImplementedError

    def getValidSettings(self):
        # type: () -> bool
        raise NotImplementedError

    def getVResolution(self):
        # type: () -> int
        raise NotImplementedError

    def setCopies(self, copies):
        # type: (int) -> None
        raise NotImplementedError

    def setDraft(self, d):
        # type: (bool) -> None
        raise NotImplementedError

    def setFitHeight(self, height):
        # type: (int) -> None
        raise NotImplementedError

    def setFitWidth(self, width):
        # type: (int) -> None
        raise NotImplementedError

    def setFooterMargin(self, footermargin):
        # type: (float) -> None
        raise NotImplementedError

    def setHeaderMargin(self, headermargin):
        # type: (float) -> None
        raise NotImplementedError

    def setHResolution(self, resolution):
        # type: (int) -> None
        raise NotImplementedError

    def setLandscape(self, ls):
        # type: (bool) -> None
        raise NotImplementedError

    def setLeftToRight(self, ltor):
        # type: (bool) -> None
        raise NotImplementedError

    def setNoColor(self, mono):
        # type: (bool) -> None
        raise NotImplementedError

    def setNoOrientation(self, orientation):
        # type: (bool) -> None
        raise NotImplementedError

    def setNotes(self, printnotes):
        # type: (bool) -> None
        raise NotImplementedError

    def setPageStart(self, start):
        # type: (int) -> None
        raise NotImplementedError

    def setPaperSize(self, size):
        # type: (int) -> None
        raise NotImplementedError

    def setScale(self, scale):
        # type: (int) -> None
        raise NotImplementedError

    def setUsePage(self, page):
        # type: (bool) -> None
        raise NotImplementedError

    def setValidSettings(self, valid):
        # type: (bool) -> None
        raise NotImplementedError

    def setVResolution(self, resolution):
        # type: (int) -> None
        raise NotImplementedError


class RichTextString(object):
    def applyFont(self, *args):
        # type: (*Any) -> None
        raise NotImplementedError

    def clearFormatting(self):
        # type: () -> None
        raise NotImplementedError

    def getIndexOfFormattingRun(self, index):
        # type: (int) -> int
        raise NotImplementedError

    def getString(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def length(self):
        # type: () -> int
        raise NotImplementedError

    def numFormattingRuns(self):
        # type: () -> int
        raise NotImplementedError


class Row(object):
    class MissingCellPolicy(Enum):
        CREATE_NULL_AS_BLANK = None  # type: Row.MissingCellPolicy
        RETURN_BLANK_AS_NULL = None  # type: Row.MissingCellPolicy
        RETURN_NULL_AND_BLANK = None  # type: Row.MissingCellPolicy

        @staticmethod
        def values():
            # type: () -> List[Row.MissingCellPolicy]
            pass

    def cellIterator(self):
        # type: () -> Iterator[Cell]
        raise NotImplementedError

    def createCell(self, column, type_=None):
        # type: (int, Optional[CellType]) -> Cell
        raise NotImplementedError

    def getCell(self, cellnum, policy=None):
        # type: (int, Optional[Row.MissingCellPolicy]) -> Cell
        raise NotImplementedError

    def getFirstCellNum(self):
        # type: () -> int
        raise NotImplementedError

    def getHeight(self):
        # type: () -> int
        raise NotImplementedError

    def getHeightInPoints(self):
        # type: () -> float
        raise NotImplementedError

    def getLastCellNum(self):
        # type: () -> int
        raise NotImplementedError

    def getOutlineLevel(self):
        # type: () -> int
        raise NotImplementedError

    def getPhysicalNumberOfCells(self):
        # type: () -> int
        raise NotImplementedError

    def getRowNum(self):
        # type: () -> int
        raise NotImplementedError

    def getRowStyle(self):
        # type: () -> CellStyle
        raise NotImplementedError

    def getSheet(self):
        # type: () -> Sheet
        raise NotImplementedError

    def getZeroHeight(self):
        # type: () -> bool
        raise NotImplementedError

    def isFormatted(self):
        # type: () -> bool
        raise NotImplementedError

    def removeCell(self, cell):
        # type: (Cell) -> None
        raise NotImplementedError

    def setHeight(self, height):
        # type: (int) -> None
        raise NotImplementedError

    def setHeightInPoints(self, height):
        # type: (float) -> None
        raise NotImplementedError

    def setRowNum(self, rowNum):
        # type: (int) -> None
        raise NotImplementedError

    def setRowStyle(self, style):
        # type: (CellStyle) -> None
        raise NotImplementedError

    def setZeroHeight(self, zHeight):
        # type: (bool) -> None
        raise NotImplementedError

    def shiftCellsLeft(self, firstShiftColumnIndex, lastShiftColumnIndex, step):
        # type: (int, int, int) -> None
        raise NotImplementedError

    def shiftCellsRight(self, firstShiftColumnIndex, lastShiftColumnIndex, step):
        # type: (int, int, int) -> None
        raise NotImplementedError

    def __iter__(self):
        # type: () -> Iterator[Cell]
        yield Cell()


class ShapeContainer(object):
    pass


class SimpleShape(Shape):
    def getShapeId(self):
        # type: () -> int
        raise NotImplementedError


class ObjectData(SimpleShape):
    def getContentType(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getDirectory(self):
        # type: () -> DirectoryEntry
        raise NotImplementedError

    def getFileName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getObjectData(self):
        # type: () -> bytearray
        raise NotImplementedError

    def getOLE2ClassName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getPictureData(self):
        # type: () -> PictureData
        raise NotImplementedError

    def hasDirectoryEntry(self):
        # type: () -> bool
        raise NotImplementedError


class Drawing(ShapeContainer):
    def createAnchor(self, dx1, dy1, dx2, dy2, col1, row1, col2, row2):
        # type: (int, int, int, int, int, int, int, int) -> ClientAnchor
        raise NotImplementedError

    def createCellComment(self, anchor):
        # type: (ClientAnchor) -> Comment
        raise NotImplementedError

    def createObjectData(self, anchor, storageId, pictureIndex):
        # type: (ClientAnchor, int, int) -> ObjectData
        raise NotImplementedError

    def createPicture(self, anchor, pictureIndex):
        # type: (ClientAnchor, int) -> Picture
        raise NotImplementedError


class Sheet(object):
    LeftMargin = 0  # type: int
    RightMargin = 1  # type: int
    TopMargin = 2  # type: int
    BottomMargin = 3  # type: int
    FooterMargin = 5  # type: int
    HeaderMargin = 4  # type: int
    PANE_LOWER_RIGHT = 0  # type: int
    PANE_UPPER_RIGHT = 1  # type: int
    PANE_LOWER_LEFT = 2  # type: int
    PANE_UPPER_LEFT = 3  # type: int

    def addMergedRegion(self, region):
        # type: (CellRangeAddress) -> None
        raise NotImplementedError

    def addMergedRegionUnsafe(self, region):
        # type: (CellRangeAddress) -> None
        raise NotImplementedError

    def addValidationData(self, data):
        # type: (DataValidation) -> None
        raise NotImplementedError

    def autoSizeColumn(self, column, useMergedCells=False):
        # type: (int, bool) -> None
        raise NotImplementedError

    def createDrawingPatriarch(self):
        # type: () -> Drawing
        raise NotImplementedError

    def createFreezePane(self, colSplit, rowSplit, leftmostColumn=0, topRow=0):
        # type: (int, int, int, int) -> None
        raise NotImplementedError

    def createRow(self, rownum):
        # type: (int) -> Row
        raise NotImplementedError

    def createSplitPane(self, xSplitPos, ySplitPos, leftmostColumn, topRow, activePane):
        # type: (int, int, int, int, int) -> None
        raise NotImplementedError

    def getActiveCell(self):
        # type: () -> CellAddress
        raise NotImplementedError

    def getAutobreaks(self):
        # type: () -> bool
        raise NotImplementedError

    def getCellComment(self, ref):
        # type: (CellAddress) -> Comment
        raise NotImplementedError

    def getCellComments(self):
        # type: () -> Dict[CellAddress, Comment]
        raise NotImplementedError

    def getColumnBreaks(self):
        # type: () -> List[int]
        raise NotImplementedError

    def getColumnOutlineLevel(self, column):
        # type: (int) -> int
        raise NotImplementedError

    def getColumnStyle(self, column):
        # type: (int) -> CellStyle
        raise NotImplementedError

    def getColumnWidth(self, column):
        # type: (int) -> int
        raise NotImplementedError

    def getColumnWidthInPixels(self, column):
        # type: (int) -> float
        raise NotImplementedError

    def getDataValidationHelper(self):
        # type: () -> DataValidationHelper
        raise NotImplementedError

    def getDataValidations(self):
        # type: () -> List[DataValidation]
        raise NotImplementedError

    def getDefaultColumnWidth(self):
        # type: () -> int
        raise NotImplementedError

    def getDefaultRowHeight(self):
        # type: () -> int
        raise NotImplementedError

    def getDefaultRowHeightInPoints(self):
        # type: () -> float
        raise NotImplementedError

    def getDisplayGuts(self):
        # type: () -> bool
        raise NotImplementedError

    def getDrawingPatriarch(self):
        # type: () -> Drawing
        raise NotImplementedError

    def getFirstRowNum(self):
        # type: () -> int
        raise NotImplementedError

    def getFitToPage(self):
        # type: () -> bool
        raise NotImplementedError

    def getFooter(self):
        # type: () -> Footer
        raise NotImplementedError

    def getForceFormulaRecalculation(self):
        # type: () -> bool
        raise NotImplementedError

    def getHeader(self):
        # type: () -> Header
        raise NotImplementedError

    def getHorizontallyCenter(self):
        # type: () -> bool
        raise NotImplementedError

    def getHyperlink(self, *args):
        # type: (*Any) -> Hyperlink
        raise NotImplementedError

    def getHyperlinks(self):
        # type: () -> List[Hyperlink]
        raise NotImplementedError

    def getLastRowNum(self):
        # type: () -> int
        raise NotImplementedError

    def getLeftCol(self):
        # type: () -> int
        raise NotImplementedError

    def getMargin(self, margin):
        # type: (int) -> float
        raise NotImplementedError

    def getMergedRegions(self):
        # type: () -> List[CellRangeAddress]
        raise NotImplementedError

    def getNumMergedRegions(self):
        # type: () -> int
        raise NotImplementedError

    def getPaneInformation(self):
        # type: () -> PaneInformation
        raise NotImplementedError

    def getPhysicalNumberOfRows(self):
        # type: () -> int
        raise NotImplementedError

    def getPrintSetup(self):
        # type: () -> PrintSetup
        raise NotImplementedError

    def getProtect(self):
        # type: () -> bool
        raise NotImplementedError

    def getRepeatingColumns(self):
        # type: () -> CellRangeAddress
        raise NotImplementedError

    def getRepeatingRows(self):
        # type: () -> CellRangeAddress
        raise NotImplementedError

    def getRow(self, rownum):
        # type: (int) -> Row
        raise NotImplementedError

    def getRowBreaks(self):
        # type: () -> List[int]
        raise NotImplementedError

    def getRowSumsBelow(self):
        # type: () -> bool
        raise NotImplementedError

    def getRowSumsRight(self):
        # type: () -> bool
        raise NotImplementedError

    def getScenarioProtect(self):
        # type: () -> bool
        raise NotImplementedError

    def getSheetConditionalFormatting(self):
        # type: () -> SheetConditionalFormatting
        raise NotImplementedError

    def getSheetName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getTopRow(self):
        # type: () -> int
        raise NotImplementedError

    def getVerticallyCenter(self):
        # type: () -> bool
        raise NotImplementedError

    def getWorkbook(self):
        # type: () -> Workbook
        raise NotImplementedError

    def groupColumn(self, fromColumn, toColumn):
        # type: (int, int) -> None
        raise NotImplementedError

    def groupRow(self, fromRow, toRow):
        # type: (int, int) -> None
        raise NotImplementedError

    def isColumnBroken(self, column):
        # type: (int) -> bool
        raise NotImplementedError

    def isColumnHidden(self, column):
        # type: (int) -> bool
        raise NotImplementedError

    def isDisplayFormulas(self):
        # type: () -> bool
        raise NotImplementedError

    def isDisplayGridlines(self):
        # type: () -> bool
        raise NotImplementedError

    def isDisplayRowColHeadings(self):
        # type: () -> bool
        raise NotImplementedError

    def isDisplayZeros(self):
        # type: () -> bool
        raise NotImplementedError

    def isPrintGridlines(self):
        # type: () -> bool
        raise NotImplementedError

    def isPrintRowAndColumnHeadings(self):
        # type: () -> bool
        raise NotImplementedError

    def isRightToLeft(self):
        # type: () -> bool
        raise NotImplementedError

    def isRowBroken(self, row):
        # type: (int) -> bool
        raise NotImplementedError

    def isSelected(self):
        # type: () -> bool
        raise NotImplementedError

    def protectSheet(self, password):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def removeArrayFormula(self, cell):
        # type: (Cell) -> CellRange
        raise NotImplementedError

    def removeColumnBreak(self, column):
        # type: (int) -> None
        raise NotImplementedError

    def removeMergedRegion(self, index):
        # type: (int) -> None
        raise NotImplementedError

    def removeMergedRegions(self, indices):
        # type: (List[int]) -> None
        raise NotImplementedError

    def removeRow(self, row):
        # type: (Row) -> None
        raise NotImplementedError

    def removeRowBreak(self, row):
        # type: (int) -> None
        raise NotImplementedError

    def rowIterator(self):
        # type: () -> Iterator[Row]
        raise NotImplementedError

    def setActiveCell(self, address):
        # type: (CellAddress) -> None
        raise NotImplementedError

    def setArrayFormula(self, formula, range):
        # type: (AnyStr, CellRangeAddress) -> CellRange
        raise NotImplementedError

    def setAutobreaks(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setAutoFilter(self, range):
        # type: (CellRangeAddress) -> AutoFilter
        raise NotImplementedError

    def setColumnBreak(self, column):
        # type: (int) -> None
        raise NotImplementedError

    def setColumnGroupCollapsed(self, columnNumber, collapsed):
        # type: (int, bool) -> None
        raise NotImplementedError

    def setColumnHidden(self, columnIndex, hidden):
        # type: (int, bool) -> None
        raise NotImplementedError

    def setColumnWidth(self, columnIndex, width):
        # type: (int, int) -> None
        raise NotImplementedError

    def setDefaultColumnStyle(self, column, style):
        # type: (int, CellStyle) -> None
        raise NotImplementedError

    def setDefaultColumnWidth(self, width):
        # type: (int) -> None
        raise NotImplementedError

    def setDefaultRowHeight(self, height):
        # type: (int) -> None
        raise NotImplementedError

    def setDefaultRowHeightInPoints(self, height):
        # type: (float) -> None
        raise NotImplementedError

    def setDisplayFormulas(self, show):
        # type: (bool) -> None
        raise NotImplementedError

    def setDisplayGridlines(self, show):
        # type: (bool) -> None
        raise NotImplementedError

    def setDisplayGuts(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setDisplayRowColHeadings(self, show):
        # type: (bool) -> None
        raise NotImplementedError

    def setDisplayZeros(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setFitToPage(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setForceFormulaRecalculation(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setHorizontallyCenter(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setMargin(self, margin, size):
        # type: (int, float) -> None
        raise NotImplementedError

    def setPrintGridlines(self, show):
        # type: (bool) -> None
        raise NotImplementedError

    def setPrintRowAndColumnHeadings(self, show):
        # type: (bool) -> None
        raise NotImplementedError

    def setRepeatingColumns(self, columnRangeRef):
        # type: (CellRangeAddress) -> None
        raise NotImplementedError

    def setRepeatingRows(self, rowRangeRef):
        # type: (CellRangeAddress) -> None
        raise NotImplementedError

    def setRightToLeft(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setRowBreak(self, row):
        # type: (int) -> None
        raise NotImplementedError

    def setRowGroupCollapsed(self, row, collapse):
        # type: (int, bool) -> None
        raise NotImplementedError

    def setRowSumsBelow(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setRowSumsRight(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setSelected(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setVerticallyCenter(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setZoom(self, scale):
        # type: (int) -> None
        raise NotImplementedError

    def shiftColumns(self, startColumn, endColumn, n):
        # type: (int, int, int) -> None
        raise NotImplementedError

    def shiftRows(
        self, startRow, endRow, n, copyRowHeight=True, resetOriginalRowHeight=True
    ):
        # type: (int, int, int, bool, bool) -> None
        raise NotImplementedError

    def showInPane(self, topRow, leftCol):
        # type: (int, int) -> None
        raise NotImplementedError

    def ungroupColumn(self, fromColumn, toColumn):
        # type: (int, int) -> None
        raise NotImplementedError

    def ungroupRow(self, fromRow, toRow):
        # type: (int, int) -> None
        raise NotImplementedError

    def valudateMergedRegions(self):
        # type: () -> None
        raise NotImplementedError

    def __iter__(self):
        # type: () -> Iterator[Row]
        yield Row()


class SheetConditionalFormatting(object):
    def addConditionalFormatting(self, *args):
        # type: (*Any) -> int
        raise NotImplementedError

    def createConditionalFormattingColorScaleRule(self):
        # type: () -> ConditionalFormattingRule
        raise NotImplementedError

    def createConditionalFormattingRule(self, *args):
        # type: (*Any) -> ConditionalFormattingRule
        raise NotImplementedError

    def getConditionalFormattingAt(self, index):
        # type: (int) -> ConditionalFormatting
        raise NotImplementedError

    def getNumConditionalFormattings(self):
        # type: () -> int
        raise NotImplementedError

    def removeConditionalFormatting(self, index):
        # type: (int) -> None
        raise NotImplementedError


class Workbook(Closeable):
    PICTURE_TYPE_EMF = 2  # type: int
    PICTURE_TYPE_WMF = 3  # type: int
    PICTURE_TYPE_PICT = 4  # type: int
    PICTURE_TYPE_JPEG = 5  # type: int
    PICTURE_TYPE_PNG = 6  # type: int
    PICTURE_TYPE_DIB = 7  # type: int

    def addOlePackage(self, oleData, label, fileName, command):
        # type: (bytearray, AnyStr, AnyStr, AnyStr) -> int
        raise NotImplementedError

    def addPicture(self, pictureData, format_):
        # type: (bytearray, int) -> int
        raise NotImplementedError

    def addToolPack(self, toolpack):
        # type: (UDFFinder) -> None
        raise NotImplementedError

    def cloneSheet(self, sheetNum):
        # type: (int) -> Sheet
        raise NotImplementedError

    def close(self):
        # type: () -> None
        raise NotImplementedError

    def createCellStyle(self):
        # type: () -> CellStyle
        raise NotImplementedError

    def createDataFormat(self):
        # type: () -> DataFormat
        raise NotImplementedError

    def createFont(self):
        # type: () -> Font
        raise NotImplementedError

    def createName(self):
        # type: () -> Name
        raise NotImplementedError

    def createSheet(self, name=None):
        # type: (Optional[AnyStr]) -> Sheet
        raise NotImplementedError

    def findFont(self, bold, color, fontHeight, name, italic, strikeout, underline):
        # type: (bool, int, float, AnyStr, bool, bool, int) -> Font
        raise NotImplementedError

    def getActiveSheetIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getAllNames(self):
        # type: () -> List[Name]
        raise NotImplementedError

    def getAllPictures(self):
        # type: () -> List[PictureData]
        raise NotImplementedError

    def getCellStyleAt(self, idx):
        # type: (int) -> CellStyle
        raise NotImplementedError

    def getCreationHelper(self):
        # type: () -> CreationHelper
        raise NotImplementedError

    def getFirstVisibleTab(self):
        # type: () -> int
        raise NotImplementedError

    def getFontAt(self, idx):
        # type: (int) -> Font
        raise NotImplementedError

    def getForceFormulaRecalculation(self):
        # type: () -> bool
        raise NotImplementedError

    def getMissingCellPolicy(self):
        # type: () -> Row.MissingCellPolicy
        raise NotImplementedError

    def getName(self, name):
        # type: (AnyStr) -> Name
        raise NotImplementedError

    def getNames(self):
        # type: () -> List[Name]
        raise NotImplementedError

    def getNumberOfFontsAsInt(self):
        # type: () -> int
        raise NotImplementedError

    def getNumberOfNames(self):
        # type: () -> int
        raise NotImplementedError

    def getNumberOfSheets(self):
        # type: () -> int
        raise NotImplementedError

    def getNumCellStyles(self):
        # type: () -> int
        raise NotImplementedError

    def getPrintArea(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getSheet(self, name):
        # type: (AnyStr) -> Sheet
        raise NotImplementedError

    def getSheetAt(self, index):
        # type: (int) -> Sheet
        raise NotImplementedError

    def getSheetIndex(self, arg):
        # type: (Union[AnyStr, Sheet]) -> int
        raise NotImplementedError

    def getSheetName(self, sheet):
        # type: (int) -> AnyStr
        raise NotImplementedError

    def getSheetVisibility(self, sheetIx):
        # type: (int) -> SheetVisibility
        raise NotImplementedError

    def getSpreadsheetVersion(self):
        # type: () -> SpreadsheetVersion
        raise NotImplementedError

    def isHidden(self):
        # type: () -> bool
        raise NotImplementedError

    def isSheetHidden(self, sheetIx):
        # type: (int) -> bool
        raise NotImplementedError

    def isSheetVeryHidden(self, sheetIx):
        # type: (int) -> bool
        raise NotImplementedError

    def linkExternalWorkbook(self, name, workbook):
        # type: (AnyStr, Workbook) -> None
        raise NotImplementedError

    def removeName(self, name):
        # type: (Name) -> None
        raise NotImplementedError

    def removePrintArea(self, sheetIndex):
        # type: (int) -> None
        raise NotImplementedError

    def removeSheetAt(self, sheetIndex):
        # type: (int) -> None
        raise NotImplementedError

    def setActiveSheet(self, sheetIndex):
        # type: (int) -> None
        raise NotImplementedError

    def setFirstVisibleTab(self, sheetIndex):
        # type: (int) -> None
        raise NotImplementedError

    def setForceFormulaRecalculation(self, value):
        # type: (bool) -> None
        raise NotImplementedError

    def setHidden(self, hiddenFlag):
        # type: (bool) -> None
        raise NotImplementedError

    def setMissingCellPolicy(self, missingCellPolicy):
        # type: (Row.MissingCellPolicy) -> None
        raise NotImplementedError

    def setPrintArea(self, sheetIndex, *args):
        # type: (int, *AnyStr) -> None
        raise NotImplementedError

    def setSelectedTab(self, index):
        # type: (int) -> None
        raise NotImplementedError

    def setSheetHidden(self, sheetIx, hidden):
        # type: (int, bool) -> None
        raise NotImplementedError

    def setSheetName(self, sheet, name):
        # type: (int, AnyStr) -> None
        raise NotImplementedError

    def setSheetOrder(self, sheetName, pos):
        # type: (AnyStr, int) -> None
        raise NotImplementedError

    def setSheetVisibility(self, sheetIx, visibility):
        # type: (int, SheetVisibility) -> None
        raise NotImplementedError

    def sheetIterator(self):
        # type: () -> Iterator[Sheet]
        raise NotImplementedError

    def write(self, stream):
        # type: (OutputStream) -> None
        raise NotImplementedError

    def __iter__(self):
        # type: () -> Iterator[Sheet]
        yield Sheet()


class BorderStyle(Enum):
    NONE = None  # type: BorderStyle
    THIN = None  # type: BorderStyle
    MEDIUM = None  # type: BorderStyle
    DASHED = None  # type: BorderStyle
    DOTTED = None  # type: BorderStyle
    THICK = None  # type: BorderStyle
    DOUBLE = None  # type: BorderStyle
    HAIR = None  # type: BorderStyle
    MEDIUM_DASHED = None  # type: BorderStyle
    DASH_DOTTED = None  # type: BorderStyle
    MEDIUM_DASH_DOTTED = None  # type: BorderStyle
    SLANTED_DASH_DOTTED = None  # type: BorderStyle

    @staticmethod
    def forInt(code):
        # type: (int) -> BorderStyle
        pass

    @staticmethod
    def values():
        # type: () -> List[BorderStyle]
        pass


class CellType(Enum):
    BLANK = None  # type: CellType
    BOOLEAN = None  # type: CellType
    ERROR = None  # type: CellType
    FORMULA = None  # type: CellType
    NUMERIC = None  # type: CellType
    STRING = None  # type: CellType
    _NONE = None  # type: CellType
    _MISSING = None  # type: CellType

    @staticmethod
    def forInt(code):
        # type: (int) -> CellType
        pass

    @staticmethod
    def values():
        # type: () -> List[CellType]
        pass


class ConditionFilterType(Enum):
    ABOVE_AVERAGE = None  # type: ConditionFilterType
    BEGINS_WITH = None  # type: ConditionFilterType
    CONTAINS_BLANKS = None  # type: ConditionFilterType
    CONTAINS_ERRORS = None  # type: ConditionFilterType
    CONTAINS_TEXT = None  # type: ConditionFilterType
    DUPLICATE_VALUES = None  # type: ConditionFilterType
    ENDS_WITH = None  # type: ConditionFilterType
    FILTER = None  # type: ConditionFilterType
    NOT_CONTAINS_BLANKS = None  # type: ConditionFilterType
    NOT_CONTAINS_ERRORS = None  # type: ConditionFilterType
    NOT_CONTAINS_TEXT = None  # type: ConditionFilterType
    TIME_PERIOD = None  # type: ConditionFilterType
    TOP_10 = None  # type: ConditionFilterType
    UNIQUE_VALUES = None  # type: ConditionFilterType

    @staticmethod
    def values():
        # type: () -> List[ConditionFilterType]
        pass


class ConditionType(Object):
    CELL_VALUE_IS = None  # type: ConditionType
    COLOR_SCALE = None  # type: ConditionType
    DATA_BAR = None  # type: ConditionType
    FILTER = None  # type: ConditionType
    FORMULA = None  # type: ConditionType
    ICON_SET = None  # type: ConditionType
    id = None  # type: int
    type = None  # type: AnyStr

    @staticmethod
    def forId(id):
        # type: (int) -> ConditionType
        pass


class ExcelNumberFormat(Object):
    id = None  # type: int
    format = None  # type: AnyStr

    def __init__(self, idx, format_):
        # type: (int, AnyStr) -> None
        super(ExcelNumberFormat, self).__init__()
        self.id = idx  # type: int
        self.format = format_  # type: AnyStr

    def getIdx(self):
        # type: () -> int
        return self.id

    def getFormat(self):
        # type: () -> AnyStr
        return self.format


class ExtendedColor(Object, Color):
    def __init__(self):
        # type: () -> None
        super(ExtendedColor, self).__init__()

    def getARGB(self):
        # type: () -> bytearray
        pass

    def getARGBHex(self):
        # type: () -> AnyStr
        pass

    def getIndex(self):
        # type: () -> int
        pass

    def getRGB(self):
        # type: () -> bytearray
        pass

    def getRGBWithTint(self):
        # type: () -> bytearray
        pass

    def getTheme(self):
        # type: () -> int
        pass

    def getTint(self):
        # type: () -> float
        pass

    def isAuto(self):
        # type: () -> bool
        pass

    def isIndexed(self):
        # type: () -> bool
        pass

    def isRGB(self):
        # type: () -> bool
        pass

    def isThemed(self):
        # type: () -> bool
        pass

    def setARGBHex(self, argb):
        # type: (AnyStr) -> None
        pass

    def setRGB(self, rgb):
        # type: (bytearray) -> None
        pass

    def setTint(self, tint):
        # type: (float) -> None
        pass


class CellValue(Object):
    FALSE = None  # type: CellValue
    TRUE = None  # type: CellValue

    def formatAsString(self):
        # type: () -> AnyStr
        pass

    def getBooleanValue(self):
        # type: () -> bool
        pass

    def getCellType(self):
        # type: () -> CellType
        pass

    @staticmethod
    def getError(errorCode):
        # type: (int) -> int
        pass

    def getErrorValue(self):
        # type: () -> int
        pass

    def getNumberValue(self):
        # type: () -> float
        pass

    def getStringValue(self):
        # type: () -> AnyStr
        pass

    @staticmethod
    def valueOf(booleanValue):
        # type: (bool) -> CellValue
        pass


class FillPatternType(Enum):
    NO_FILL = None  # type: FillPatternType
    SOLID_FOREGROUND = None  # type: FillPatternType
    FINE_DOTS = None  # type: FillPatternType
    ALT_BARS = None  # type: FillPatternType
    SPARSE_DOTS = None  # type: FillPatternType
    THICK_HORZ_BANDS = None  # type: FillPatternType
    THICK_VERT_BANDS = None  # type: FillPatternType
    THICK_BACKWARD_DIAG = None  # type: FillPatternType
    THICK_FORWARD_DIAG = None  # type: FillPatternType
    BIG_SPOTS = None  # type: FillPatternType
    BRICKS = None  # type: FillPatternType
    THIN_BACKWARD_DIAG = None  # type: FillPatternType
    THIN_FORWARD_DIAG = None  # type: FillPatternType
    THIN_HORZ_BANDS = None  # type: FillPatternType
    THIN_VERT_BANDS = None  # type: FillPatternType

    @staticmethod
    def forInt(code):
        # type: (int) -> FillPatternType
        pass

    @staticmethod
    def values():
        # type: () -> List[FillPatternType]
        pass


class HorizontalAlignment(Enum):
    CENTER = None  # type: HorizontalAlignment
    CENTER_SELECTION = None  # type: HorizontalAlignment
    DISTRIBUTED = None  # type: HorizontalAlignment
    GENERAL = None  # type: HorizontalAlignment
    JUSTIFY = None  # type: HorizontalAlignment
    LEFT = None  # type: HorizontalAlignment
    RIGHT = None  # type: HorizontalAlignment

    @staticmethod
    def forInt(code):
        # type: (int) -> HorizontalAlignment
        pass

    @staticmethod
    def values():
        # type: () -> List[HorizontalAlignment]
        pass


class SheetVisibility(Enum):
    HIDDEN = None  # type: SheetVisibility
    VISIBLE = None  # type: SheetVisibility
    VERY_HIDDEN = None  # type: SheetVisibility

    @staticmethod
    def values():
        # type: () -> List[SheetVisibility]
        pass


class VerticalAlignment(Enum):
    BOTTOM = None  # type: VerticalAlignment
    CENTER = None  # type: VerticalAlignment
    DISTRIBUTED = None  # type: VerticalAlignment
    JUSTIFY = None  # type: VerticalAlignment
    TOP = None  # type: VerticalAlignment

    @staticmethod
    def forInt(code):
        # type: (int) -> VerticalAlignment
        pass

    @staticmethod
    def values():
        # type: () -> List[VerticalAlignment]
        pass


class WorkbookFactory(Object):
    def __init__(self):
        # type: () -> None
        super(WorkbookFactory, self).__init__()

    @staticmethod
    def create(*args):
        # type: (*Any) -> Workbook
        pass
