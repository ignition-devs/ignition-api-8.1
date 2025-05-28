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
        pass

    def getBorderDiagonal(self):
        # type: () -> BorderStyle
        pass

    def getBorderHorizontal(self):
        # type: () -> BorderStyle
        pass

    def getBorderLeft(self):
        # type: () -> BorderStyle
        pass

    def getBorderRight(self):
        # type: () -> BorderStyle
        pass

    def getBorderTop(self):
        # type: () -> BorderStyle
        pass

    def getBorderVertical(self):
        # type: () -> BorderStyle
        pass

    def getBottomBorderColor(self):
        # type: () -> int
        pass

    def getBottomBorderColorColor(self):
        # type: () -> Color
        pass

    def getDiagonalBorderColor(self):
        # type: () -> int
        pass

    def getDiagonalBorderColorColor(self):
        # type: () -> Color
        pass

    def getHorizontalBorderColor(self):
        # type: () -> int
        pass

    def getHorizontalBorderColorColor(self):
        # type: () -> Color
        pass

    def getLeftBorderColor(self):
        # type: () -> int
        pass

    def getLeftBorderColorColor(self):
        # type: () -> Color
        pass

    def getRightBorderColor(self):
        # type: () -> int
        pass

    def getRightBorderColorColor(self):
        # type: () -> Color
        pass

    def getTopBorderColor(self):
        # type: () -> int
        pass

    def getTopBorderColorColor(self):
        # type: () -> Color
        pass

    def getVerticalBorderColor(self):
        # type: () -> int
        pass

    def getVerticalBorderColorColor(self):
        # type: () -> Color
        pass

    def setBorderBottom(self, border):
        # type: (BorderStyle) -> None
        pass

    def setBorderDiagonal(self, border):
        # type: (BorderStyle) -> None
        pass

    def setBorderHorizontal(self, border):
        # type: (BorderStyle) -> None
        pass

    def setBorderLeft(self, border):
        # type: (BorderStyle) -> None
        pass

    def setBorderRight(self, border):
        # type: (BorderStyle) -> None
        pass

    def setBorderTop(self, border):
        # type: (BorderStyle) -> None
        pass

    def setBorderVertical(self, border):
        # type: (BorderStyle) -> None
        pass

    def setBottomBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        pass

    def setDiagonalBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        pass

    def setHorizontalBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        pass

    def setLeftBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        pass

    def setRightBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        pass

    def setTopBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        pass

    def setVerticalBorderColor(self, color):
        # type: (Union[int, Color]) -> None
        pass


class Cell(object):
    def getAddress(self):
        # type: () -> CellAddress
        pass

    def getArrayFormulaRange(self):
        # type: () -> CellRangeAddress
        pass

    def getBooleanCellValue(self):
        # type: () -> bool
        pass

    def getCachedFormulaResultType(self):
        # type: () -> CellType
        pass

    def getCellComment(self):
        # type: () -> Comment
        pass

    def getCellFormula(self):
        # type: () -> AnyStr
        pass

    def getCellStyle(self):
        # type: () -> CellStyle
        pass

    def getCellType(self):
        # type: () -> CellType
        pass

    def getColumnIndex(self):
        # type: () -> int
        pass

    def getDateCellValue(self):
        # type: () -> Date
        pass

    def getErrorCellValue(self):
        # type: () -> int
        pass

    def getHyperlink(self):
        # type: () -> Hyperlink
        pass

    def getLocalDateTimeCellValue(self):
        # type: () -> LocalDateTime
        pass

    def getNumericCellValue(self):
        # type: () -> float
        pass

    def getRichStringCellValue(self):
        # type: () -> RichTextString
        pass

    def getRow(self):
        # type: () -> Row
        pass

    def getRowIndex(self):
        # type: () -> int
        pass

    def getSheet(self):
        # type: () -> Sheet
        pass

    def getStringCellValue(self):
        # type: () -> AnyStr
        pass

    def isPartOfArrayFormulaGroup(self):
        # type: () -> bool
        pass

    def removeCellComment(self):
        # type: () -> None
        pass

    def removeFormula(self):
        # type: () -> None
        pass

    def removeHyperlink(self):
        # type: () -> None
        pass

    def setAsActiveCell(self):
        # type: () -> None
        pass

    def setBlank(self):
        # type: () -> None
        pass

    def setCellComment(self, comment):
        # type: (Comment) -> None
        pass

    def setCellErrorValue(self, value):
        # type: (int) -> None
        pass

    def setCellFormula(self, formula):
        # type: (AnyStr) -> None
        pass

    def setCellStyle(self, style):
        # type: (CellStyle) -> None
        pass

    def setCellValue(self, value):
        # type: (Any) -> None
        pass

    def setHyperlink(self, link):
        # type: (Hyperlink) -> None
        pass


class CellRange(object):
    def __iter__(self):
        # type: () -> Iterator[Cell]
        pass

    def getCell(self, relativeRowIndex, relativeColumnIndex):
        # type: (int, int) -> Cell
        pass

    def getCells(self):
        # type: () -> List[List[Cell]]
        pass

    def getFlattenedCells(self):
        # type: () -> List[Cell]
        pass

    def getHeight(self):
        # type: () -> int
        pass

    def getReferenceText(self):
        # type: () -> AnyStr
        pass

    def getTopLeftCell(self):
        # type: () -> Cell
        pass

    def getWidth(self):
        # type: () -> int
        pass

    def size(self):
        # type: () -> int
        pass


class CellStyle(object):
    def cloneStyleFrom(self, source):
        # type: (CellStyle) -> None
        pass

    def getAlignment(self):
        # type: () -> HorizontalAlignment
        pass

    def getBorderBottom(self):
        # type: () -> BorderStyle
        pass

    def getBorderLeft(self):
        # type: () -> BorderStyle
        pass

    def getBorderRight(self):
        # type: () -> BorderStyle
        pass

    def getBorderTop(self):
        # type: () -> BorderStyle
        pass

    def getBottomBorderColor(self):
        # type: () -> int
        pass

    def getDataFormat(self):
        # type: () -> int
        pass

    def getDataFormatString(self):
        # type: () -> AnyStr
        pass

    def getFillBackgroundColor(self):
        # type: () -> int
        pass

    def getFillBackgroundColorColor(self):
        # type: () -> Color
        pass

    def getFillForegroundColor(self):
        # type: () -> int
        pass

    def getFillForegroundColorColor(self):
        # type: () -> Color
        pass

    def getFillPattern(self):
        # type: () -> FillPatternType
        pass

    def getFontIndexAsInt(self):
        # type: () -> int
        pass

    def getHidden(self):
        # type: () -> bool
        pass

    def getIndention(self):
        # type: () -> int
        pass

    def getIndex(self):
        # type: () -> int
        pass

    def getLeftBorderColor(self):
        # type: () -> int
        pass

    def getLocked(self):
        # type: () -> bool
        pass

    def getQuotePrefixed(self):
        # type: () -> bool
        pass

    def getRightBorderColor(self):
        # type: () -> int
        pass

    def getRotation(self):
        # type: () -> int
        pass

    def getShrinkToFit(self):
        # type: () -> bool
        pass

    def getTopBorderColor(self):
        # type: () -> int
        pass

    def getVerticalAlignment(self):
        # type: () -> VerticalAlignment
        pass

    def getWrapText(self):
        # type: () -> bool
        pass

    def setAlignment(self, align):
        # type: (HorizontalAlignment) -> None
        pass

    def setDataFormat(self, formatIndex):
        # type: (int) -> None
        pass

    def setFillBackgroundColor(self, colorIndex):
        # type: (int) -> None
        pass

    def setFillForegroundColor(self, colorIndex):
        # type: (int) -> None
        raise NotImplementedError


class ChildAnchor(object):
    def getDx1(self):
        # type: () -> int
        pass

    def getDx2(self):
        # type: () -> int
        pass

    def getDy1(self):
        # type: () -> int
        pass

    def getDy2(self):
        # type: () -> int
        pass

    def getCol1(self):
        # type: () -> int
        pass

    def getCol2(self):
        # type: () -> int
        pass

    def getRow1(self):
        # type: () -> int
        pass

    def getRow2(self):
        # type: () -> int
        pass


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
        pass

    def getCol1(self):
        # type: () -> int
        pass

    def getCol2(self):
        # type: () -> int
        pass

    def getDx1(self):
        # type: () -> int
        pass

    def getDx2(self):
        # type: () -> int
        pass

    def getDy1(self):
        # type: () -> int
        pass

    def getDy2(self):
        # type: () -> int
        pass

    def getRow1(self):
        # type: () -> int
        pass

    def getRow2(self):
        # type: () -> int
        pass

    def setAnchorType(self, anchorType):
        # type: (ClientAnchor.AnchorType) -> None
        pass

    def setCol1(self, col1):
        # type: (int) -> None
        pass

    def setCol2(self, col2):
        # type: (int) -> None
        pass

    def setDx1(self, dx1):
        # type: (int) -> None
        pass

    def setDx2(self, dx2):
        # type: (int) -> None
        pass

    def setDy1(self, dy1):
        # type: (int) -> None
        pass

    def setDy2(self, dy2):
        # type: (int) -> None
        pass

    def setRow1(self, row1):
        # type: (int) -> None
        pass

    def setRow2(self, row2):
        # type: (int) -> None
        pass


class Color(object):
    pass


class ColorScaleFormatting(object):
    def createThreshold(self):
        # type: () -> ConditionalFormattingThreshold
        pass

    def getColors(self):
        # type: () -> List[Color]
        pass

    def getNumControlPoints(self):
        # type: () -> int
        pass

    def getThresholds(self):
        # type: () -> List[ConditionalFormattingThreshold]
        pass

    def setColors(self, colors):
        # type: (List[Color]) -> None
        pass

    def setNumControlPoints(self, num):
        # type: (int) -> None
        pass

    def setThresholds(self, thresholds):
        # type: (List[ConditionalFormattingThreshold]) -> None
        pass


class Comment(object):
    def getAddress(self):
        # type: () -> CellAddress
        pass

    def getAuthor(self):
        # type: () -> AnyStr
        pass

    def getClientAnchor(self):
        # type: () -> ClientAnchor
        pass

    def getColumn(self):
        # type: () -> int
        pass

    def getRow(self):
        # type: () -> int
        pass

    def getString(self):
        # type: () -> RichTextString
        pass

    def isVisible(self):
        # type: () -> bool
        pass

    def setAddress(self, *args):
        # type: (*Any) -> None
        pass

    def setAuthor(self, author):
        # type: (AnyStr) -> None
        pass

    def setColumn(self, column):
        # type: (int) -> None
        pass

    def setRow(self, row):
        # type: (int) -> None
        pass

    def setString(self, string):
        # type: (RichTextString) -> None
        pass

    def setVisible(self, visible):
        # type: (bool) -> None
        pass


class ConditionFilterData(object):
    def getAboveAverage(self):
        # type: () -> bool
        pass

    def getBottom(self):
        # type: () -> int
        pass

    def getEqualAverage(self):
        # type: () -> bool
        pass

    def getPercent(self):
        # type: () -> bool
        pass

    def getRank(self):
        # type: () -> long
        pass

    def getStdDev(self):
        # type: () -> int
        pass


class ConditionalFormatting(object):
    def addRule(self, cfRule):
        # type: (ConditionalFormattingRule) -> None
        pass

    def getFormattingRanges(self):
        # type: () -> List[CellRangeAddress]
        pass

    def getNumberOfRules(self):
        # type: () -> int
        pass

    def getRule(self, idx):
        # type: (int) -> ConditionalFormattingRule
        pass

    def setFormattingRanges(self, ranges):
        # type: (List[CellRangeAddress]) -> None
        pass

    def setRule(self, idx, cfRule):
        # type: (int, ConditionalFormattingRule) -> None
        pass


class ConditionalFormattingRule(object):
    def createBorderFormatting(self):
        # type: () -> BorderFormatting
        pass

    def createFontFormatting(self):
        # type: () -> FontFormatting
        pass

    def createPatternFormatting(self):
        # type: () -> PatternFormatting
        pass

    def getBorderFormatting(self):
        # type: () -> BorderFormatting
        pass

    def getColorScaleFormatting(self):
        # type: () -> ColorScaleFormatting
        pass

    def getComparisonOperation(self):
        # type: () -> int
        pass

    def getConditionFilterType(self):
        # type: () -> ConditionFilterType
        pass

    def getConditionType(self):
        # type: () -> ConditionType
        pass

    def getDataBarFormatting(self):
        # type: () -> DataBarFormatting
        pass

    def getFilterConfiguration(self):
        # type: () -> ConditionFilterData
        pass

    def getFontFormatting(self):
        # type: () -> FontFormatting
        pass

    def getFormula1(self):
        # type: () -> AnyStr
        pass

    def getFormula2(self):
        # type: () -> AnyStr
        pass

    def getMultiStateFormatting(self):
        # type: () -> IconMultiStateFormatting
        pass

    def getNumberFormatting(self):
        # type: () -> ExcelNumberFormat
        pass

    def getPatternFormatting(self):
        # type: () -> PatternFormatting
        pass

    def getPriority(self):
        # type: () -> int
        pass

    def getStopIfTrue(self):
        # type: () -> bool
        pass

    def getText(self):
        # type: () -> AnyStr
        pass


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
        pass

    def getRangeType(self):
        # type: () -> ConditionalFormattingThreshold.RangeType
        pass

    def getValue(self):
        # type: () -> float
        pass

    def setFormula(self, formula):
        # type: (AnyStr) -> None
        pass

    def setRangeType(self, rangeType):
        # type: (ConditionalFormattingThreshold.RangeType) -> None
        pass

    def setValue(self, value):
        # type: (float) -> None
        pass


class CreationHelper(object):
    def createAreaReference(self, *args):
        # type: (*Any) -> AreaReference
        pass

    def createClientAnchor(self):
        # type: () -> ClientAnchor
        pass

    def createDataFormat(self):
        # type: () -> DataFormat
        pass

    def createExtendedColor(self):
        # type: () -> ExtendedColor
        pass

    def createFormulaEvaluator(self):
        # type: () -> FormulaEvaluator
        pass

    def createHyperlink(self, type):
        # type: (HyperlinkType) -> Hyperlink
        pass

    def createRichTextString(self, text):
        # type: (AnyStr) -> RichTextString
        pass


class DataBarFormatting(object):
    def getColor(self):
        # type: () -> Color
        pass

    def getMaxThreshold(self):
        # type: () -> ConditionalFormattingThreshold
        pass

    def getMinThreshold(self):
        # type: () -> ConditionalFormattingThreshold
        pass

    def getWidthMax(self):
        # type: () -> int
        pass

    def getWidthMin(self):
        # type: () -> int
        pass

    def isIconOnly(self):
        # type: () -> bool
        pass

    def isLeftToRight(self):
        # type: () -> bool
        pass

    def setColor(self, color):
        # type: (Color) -> None
        pass

    def setIconOnly(self, only):
        # type: (bool) -> None
        pass

    def setLeftToRight(self, ltr):
        # type: (bool) -> None
        pass

    def setWidthMax(self, width):
        # type: (int) -> None
        pass

    def setWidthMin(self, width):
        # type: (int) -> None
        pass


class DataFormat(object):
    def getFormat(self, arg):
        # type: (Union[int, AnyStr]) -> int
        pass


class DataValidation(object):
    def createErrorBox(self, title, text):
        # type: (AnyStr, AnyStr) -> None
        pass

    def createPromptBox(self, title, text):
        # type: (AnyStr, AnyStr) -> None
        pass

    def getEmptyCellAllowed(self):
        # type: () -> bool
        pass

    def getErrorBoxText(self):
        # type: () -> AnyStr
        pass

    def getErrorBoxTitle(self):
        # type: () -> AnyStr
        pass

    def getErrorStyle(self):
        # type: () -> int
        pass

    def getPromptBoxText(self):
        # type: () -> AnyStr
        pass

    def getPromptBoxTitle(self):
        # type: () -> AnyStr
        pass

    def getRegions(self):
        # type: () -> CellRangeAddressList
        pass

    def showShowErrorBox(self):
        # type: () -> bool
        pass

    def showShowPromptBox(self):
        # type: () -> bool
        pass

    def getSuppressDropDownArrow(self):
        # type: () -> bool
        pass

    def getValidationConstraint(self):
        # type: () -> DataValidationConstraint
        pass

    def setEmptyCellAllowed(self, allowed):
        # type: (bool) -> None
        pass

    def setErrorStyle(self, error_style):
        # type: (int) -> None
        pass

    def setShowErrorBox(self, show):
        # type: (bool) -> None
        pass

    def setShowPromptBox(self, show):
        # type: (bool) -> None
        pass

    def setSuppressDropDownArrow(self, suppress):
        # type: (bool) -> None
        pass


class DataValidationConstraint(object):
    class OperatorType(Object):
        BETWEEN = None  # type: int
        EQUAL = None  # type: int
        GREATER_OR_EQUAL = None  # type: int
        GREATER_THAN = None  # type: int
        IGNORED = None  # type: int
        LESS_OR_EQUAL = None  # type: int
        LESS_THAN = None  # type: int
        NOT_BETWEEN = None  # type: int
        NOT_EQUAL = None  # type: int

        def validateSecondArg(self, comparisonOperator, paramValue):
            # type: (int, AnyStr) -> None
            pass

    class ValidationType(Object):
        ANY = None  # type: int
        DATE = None  # type: int
        DECIMAL = None  # type: int
        FORMULA = None  # type: int
        INTEGER = None  # type: int
        LIST = None  # type: int
        TEXT_LENGTH = None  # type: int
        TIME = None  # type: int

    def getExplicitListValues(self):
        # type: () -> List[AnyStr]
        pass

    def getFormula1(self):
        # type: () -> AnyStr
        pass

    def getFormula2(self):
        # type: () -> AnyStr
        pass

    def getOperator(self):
        # type: () -> int
        pass

    def getValidationType(self):
        # type: () -> int
        pass

    def setExplicitListValues(self, explicitListValues):
        # type: (List[AnyStr]) -> None
        pass

    def setFormula1(self, formula):
        # type: (AnyStr) -> None
        pass

    def setFormula2(self, formula):
        # type: (AnyStr) -> None
        pass

    def setOperator(self, operator):
        # type: (int) -> None
        pass


class DataValidationHelper(object):
    def createCustomConstraint(self, formula):
        # type: (AnyStr) -> DataValidationConstraint
        pass

    def createDateConstraint(
        self,
        operatorType,  # type: int
        formula1,  # type: AnyStr
        formula2,  # type: AnyStr
        dateFormat,  # type: AnyStr
    ):
        # type: (...) -> DataValidationConstraint
        pass

    def createDecimalConstraint(self, operatorType, formula1, formula2):
        # type: (int, AnyStr, AnyStr) -> DataValidationConstraint
        pass

    def createExplicitListConstraint(self, listOfValues):
        # type: (List[AnyStr]) -> DataValidationConstraint
        pass

    def createFormulaListConstraint(self, listFormula):
        # type: (AnyStr) -> DataValidationConstraint
        pass

    def createIntegerConstraint(self, operatorType, formula1, formula2):
        # type: (int, AnyStr, AnyStr) -> DataValidationConstraint
        pass

    def createNumericConstraint(self, validationType, operatorType, formula1, formula2):
        # type: (int, int, AnyStr, AnyStr) -> DataValidationConstraint
        pass

    def createTextLengthConstraint(self, operatorType, formula1, formula2):
        # type: (int, AnyStr, AnyStr) -> DataValidationConstraint
        pass

    def createTimeConstraint(self, operatorType, formula1, formula2):
        # type: (int, AnyStr, AnyStr) -> DataValidationConstraint
        pass

    def createValidation(
        self,
        constraint,  # type: DataValidationConstraint
        cellRangeAddressList,  # type: CellRangeAddressList
    ):
        # type: (...) -> DataValidation
        pass


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
    ANSI_CHARSET = None  # type: int
    COLOR_NORMAL = None  # type: int
    COLOR_RED = None  # type: int
    DEFAULT_CHARSET = None  # type: int
    SS_NONE = None  # type: int
    SS_SUB = None  # type: int
    SS_SUPER = None  # type: int
    SYMBOL_CHARSET = None  # type: int
    U_DOUBLE = None  # type: int
    U_DOUBLE_ACCOUNTING = None  # type: int
    U_NONE = None  # type: int
    U_SINGLE = None  # type: int
    U_SINGLE_ACCOUNTING = None  # type: int

    def getBold(self):
        # type: () -> bool
        pass

    def getCharSet(self):
        # type: () -> int
        pass

    def getColor(self):
        # type: () -> Color
        pass

    def getFontHeight(self):
        # type: () -> int
        pass

    def getFontHeightInPoints(self):
        # type: () -> int
        pass

    def getFontName(self):
        # type: () -> AnyStr
        pass

    def getIndexAsInt(self):
        # type: () -> int
        pass

    def getItalic(self):
        # type: () -> bool
        pass

    def getStrikeout(self):
        # type: () -> bool
        pass

    def getTypeOffset(self):
        # type: () -> int
        pass

    def getUnderline(self):
        # type: () -> int
        pass

    def setBold(self, bold):
        # type: (bool) -> None
        pass

    def setCharSet(self, charset):
        # type: (int) -> None
        pass

    def setColor(self, color):
        # type: (Color) -> None
        pass

    def setFontHeight(self, height):
        # type: (int) -> None
        pass

    def setFontHeightInPoints(self, height):
        # type: (int) -> None
        pass

    def setFontName(self, name):
        # type: (AnyStr) -> None
        pass

    def setItalic(self, italic):
        # type: (bool) -> None
        pass

    def setStrikeout(self, strikeout):
        # type: (bool) -> None
        pass

    def setTypeOffset(self, offset):
        # type: (int) -> None
        pass

    def setUnderline(self, underline):
        # type: (int) -> None
        pass


class FontFormatting(object):
    SS_NONE = None  # type: int
    SS_SUB = None  # type: int
    SS_SUPER = None  # type: int
    U_DOUBLE = None  # type: int
    U_DOUBLE_ACCOUNTING = None  # type: int
    U_NONE = None  # type: int
    U_SINGLE = None  # type: int
    U_SINGLE_ACCOUNTING = None  # type: int

    def getEscapementType(self):
        # type: () -> int
        pass

    def getFontColor(self):
        # type: () -> Color
        pass

    def getFontColorIndex(self):
        # type: () -> int
        pass

    def getFontHeight(self):
        # type: () -> int
        pass

    def getUnderlineType(self):
        # type: () -> int
        pass

    def isBold(self):
        # type: () -> bool
        pass

    def isItalic(self):
        # type: () -> bool
        pass

    def isStruckout(self):
        # type: () -> bool
        pass

    def resetFontStyle(self):
        # type: () -> None
        pass

    def setEscapementType(self, escapementType):
        # type: (int) -> None
        pass

    def setFontColor(self, color):
        # type: (Color) -> None
        pass

    def setFontColorIndex(self, color):
        # type: (int) -> None
        pass

    def setFontHeight(self, height):
        # type: (int) -> None
        pass

    def setFontStyle(self, italic, bold):
        # type: (bool, bool) -> None
        pass

    def setUnderlineType(self, underlineType):
        # type: (int) -> None
        pass


class HeaderFooter(object):
    def getCenter(self):
        # type: () -> AnyStr
        pass

    def getLeft(self):
        # type: () -> AnyStr
        pass

    def getRight(self):
        # type: () -> AnyStr
        pass

    def setCenter(self, newCenter):
        # type: (AnyStr) -> None
        pass

    def setLeft(self, newLeft):
        # type: (AnyStr) -> None
        pass

    def setRight(self, newRight):
        # type: (AnyStr) -> None
        pass


class Footer(HeaderFooter):
    pass


class FormulaEvaluator(object):
    def clearAllCachedResultValues(self):
        # type: () -> None
        pass

    def evaluate(self, cell):
        # type: (Cell) -> CellValue
        pass

    def evaluateAll(self):
        # type: () -> None
        pass

    def evaluateFormulaCell(self, cell):
        # type: (Cell) -> CellType
        pass

    def evaluateInCell(self, cell):
        # type: (Cell) -> Cell
        pass

    def notifyDeleteCell(self, cell):
        # type: (Cell) -> None
        pass

    def notifyUpdateCell(self, cell):
        # type: (Cell) -> None
        pass

    def notifySetFormula(self, cell):
        # type: (Cell) -> None
        pass

    def setDebugEvaluationOutputForNextEval(self, value):
        # type: (bool) -> None
        pass

    def setIgnoreMissingWorkbooks(self, ignore):
        # type: (bool) -> None
        pass

    def setupReferencedWorkbooks(self, workbooks):
        # type: (Dict[AnyStr, FormulaEvaluator]) -> None
        pass


class Header(HeaderFooter):
    pass


class Hyperlink(IHyperlink):
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

    def setFirstColumn(self, col):
        # type: (int) -> None
        pass

    def setFirstRow(self, row):
        # type: (int) -> None
        pass

    def setLastColumn(self, col):
        # type: (int) -> None
        pass

    def setLastRow(self, row):
        # type: (int) -> None
        pass


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
        pass

    def getIconSet(self):
        # type: () -> IconSet
        pass

    def getThresholds(self):
        # type: () -> List[ConditionalFormattingThreshold]
        pass

    def isIconOnly(self):
        # type: () -> bool
        pass

    def isReversed(self):
        # type: () -> bool
        pass

    def setIconOnly(self, only):
        # type: (bool) -> None
        pass

    def setIconSet(self, set):
        # type: (IconSet) -> None
        pass

    def setReversed(self, reversed):
        # type: (bool) -> None
        pass

    def setThresholds(self, thresholds):
        # type: (List[ConditionalFormattingThreshold]) -> None
        pass


class Name(object):
    def getComment(self):
        # type: () -> AnyStr
        pass

    def getNameName(self):
        # type: () -> AnyStr
        pass

    def getRefersToFormula(self):
        # type: () -> AnyStr
        pass

    def getSheetIndex(self):
        # type: () -> int
        pass

    def getSheetName(self):
        # type: () -> AnyStr
        pass

    def isDeleted(self):
        # type: () -> bool
        pass

    def isFunctionName(self):
        # type: () -> bool
        pass

    def setComment(self, comment):
        # type: (AnyStr) -> None
        pass

    def setFunction(self, value):
        # type: (bool) -> None
        pass

    def setNameName(self, name):
        # type: (AnyStr) -> None
        pass

    def setRefersToFormula(self, formulaText):
        # type: (AnyStr) -> None
        pass

    def setSheetIndex(self, sheetId):
        # type: (int) -> None
        pass


class Shape(object):
    def getAnchor(self):
        # type: () -> ChildAnchor
        pass

    def getParent(self):
        # type: () -> Shape
        pass

    def getShapeName(self):
        # type: () -> AnyStr
        pass

    def isNoFill(self):
        # type: () -> bool
        pass

    def setFillColor(self, red, green, blue):
        # type: (int, int, int) -> None
        pass

    def setLineStyleColor(self, red, green, blue):
        # type: (int, int, int) -> None
        pass

    def setNoFill(self, noFill):
        # type: (bool) -> None
        pass


class Picture(Shape):
    def getClientAnchor(self):
        # type: () -> ClientAnchor
        pass

    def getImageDimension(self):
        # type: () -> Dimension
        pass

    def getPictureData(self):
        # type: () -> PictureData
        pass

    def getPreferredSize(self, scaleX=1, scaleY=1):
        # type: (int, int) -> ClientAnchor
        pass

    def getSheet(self):
        # type: () -> Sheet
        pass

    def resize(self, *args):
        # type: (*Any) -> AnyStr
        pass


class PatternFormatting(object):
    ALT_BARS = None  # type: int
    BIG_SPOTS = None  # type: int
    BRICKS = None  # type: int
    DIAMONDS = None  # type: int
    FINE_DOTS = None  # type: int
    LEAST_DOTS = None  # type: int
    LESS_DOTS = None  # type: int
    NO_FILL = None  # type: int
    SOLID_FOREGROUND = None  # type: int
    SPARSE_DOTS = None  # type: int
    SQUARES = None  # type: int
    THICK_BACKWARD_DIAG = None  # type: int
    THICK_FORWARD_DIAG = None  # type: int
    THICK_HORZ_BANDS = None  # type: int
    THICK_VERT_BANDS = None  # type: int
    THIN_BACKWARD_DIAG = None  # type: int
    THIN_FORWARD_DIAG = None  # type: int
    THIN_HORZ_BANDS = None  # type: int
    THIN_VERT_BANDS = None  # type: int

    def getFillBackgroundColor(self):
        # type: () -> int
        pass

    def getFillBackgroundColorColor(self):
        # type: () -> Color
        pass

    def getFillForegroundColor(self):
        # type: () -> int
        pass

    def getFillForegroundColorColor(self):
        # type: () -> Color
        pass

    def getFillPattern(self):
        # type: () -> FillPatternType
        pass

    def setFillBackgroundColor(self, bg):
        # type: (Union[int, Color]) -> None
        pass

    def setFillForegroundColor(self, bg):
        # type: (Union[int, Color]) -> None
        pass

    def setFillPattern(self, fp):
        # type: (FillPatternType) -> None
        pass


class PictureData(object):
    def getData(self):
        # type: () -> bytearray
        pass

    def getMimeType(self):
        # type: () -> AnyStr
        pass

    def getPictureType(self):
        # type: () -> int
        pass

    def suggestFileExtension(self):
        # type: () -> AnyStr
        pass


class PrintSetup(object):
    def getCopies(self):
        # type: () -> int
        pass

    def getDraft(self):
        # type: () -> bool
        pass

    def getFitHeight(self):
        # type: () -> int
        pass

    def getFitWidth(self):
        # type: () -> int
        pass

    def getFooterMargin(self):
        # type: () -> float
        pass

    def getHeaderMargin(self):
        # type: () -> float
        pass

    def getHResolution(self):
        # type: () -> int
        pass

    def getLandscape(self):
        # type: () -> bool
        pass

    def getLeftToRight(self):
        # type: () -> bool
        pass

    def getNoColor(self):
        # type: () -> bool
        pass

    def getNoOrientation(self):
        # type: () -> bool
        pass

    def getNotes(self):
        # type: () -> bool
        pass

    def getPageStart(self):
        # type: () -> int
        pass

    def getPaperSize(self):
        # type: () -> int
        pass

    def getScale(self):
        # type: () -> int
        pass

    def getUsePage(self):
        # type: () -> bool
        pass

    def getValidSettings(self):
        # type: () -> bool
        pass

    def getVResolution(self):
        # type: () -> int
        pass

    def setCopies(self, copies):
        # type: (int) -> None
        pass

    def setDraft(self, d):
        # type: (bool) -> None
        pass

    def setFitHeight(self, height):
        # type: (int) -> None
        pass

    def setFitWidth(self, width):
        # type: (int) -> None
        pass

    def setFooterMargin(self, footermargin):
        # type: (float) -> None
        pass

    def setHeaderMargin(self, headermargin):
        # type: (float) -> None
        pass

    def setHResolution(self, resolution):
        # type: (int) -> None
        pass

    def setLandscape(self, ls):
        # type: (bool) -> None
        pass

    def setLeftToRight(self, ltor):
        # type: (bool) -> None
        pass

    def setNoColor(self, mono):
        # type: (bool) -> None
        pass

    def setNoOrientation(self, orientation):
        # type: (bool) -> None
        pass

    def setNotes(self, printnotes):
        # type: (bool) -> None
        pass

    def setPageStart(self, start):
        # type: (int) -> None
        pass

    def setPaperSize(self, size):
        # type: (int) -> None
        pass

    def setScale(self, scale):
        # type: (int) -> None
        pass

    def setUsePage(self, page):
        # type: (bool) -> None
        pass

    def setValidSettings(self, valid):
        # type: (bool) -> None
        pass

    def setVResolution(self, resolution):
        # type: (int) -> None
        pass


class RichTextString(object):
    def applyFont(self, *args):
        # type: (*Any) -> None
        pass

    def clearFormatting(self):
        # type: () -> None
        pass

    def getIndexOfFormattingRun(self, index):
        # type: (int) -> int
        pass

    def getString(self):
        # type: () -> AnyStr
        pass

    def length(self):
        # type: () -> int
        pass

    def numFormattingRuns(self):
        # type: () -> int
        pass


class Row(object):
    class MissingCellPolicy(Enum):
        CREATE_NULL_AS_BLANK = None  # type: Row.MissingCellPolicy
        RETURN_BLANK_AS_NULL = None  # type: Row.MissingCellPolicy
        RETURN_NULL_AND_BLANK = None  # type: Row.MissingCellPolicy

        @staticmethod
        def values():
            # type: () -> List[Row.MissingCellPolicy]
            pass

    def __iter__(self):
        # type: () -> Iterator[Cell]
        yield Cell()

    def cellIterator(self):
        # type: () -> Iterator[Cell]
        pass

    def createCell(self, column, type_=None):
        # type: (int, Optional[CellType]) -> Cell
        pass

    def getCell(self, cellnum, policy=None):
        # type: (int, Optional[Row.MissingCellPolicy]) -> Cell
        pass

    def getFirstCellNum(self):
        # type: () -> int
        pass

    def getHeight(self):
        # type: () -> int
        pass

    def getHeightInPoints(self):
        # type: () -> float
        pass

    def getLastCellNum(self):
        # type: () -> int
        pass

    def getOutlineLevel(self):
        # type: () -> int
        pass

    def getPhysicalNumberOfCells(self):
        # type: () -> int
        pass

    def getRowNum(self):
        # type: () -> int
        pass

    def getRowStyle(self):
        # type: () -> CellStyle
        pass

    def getSheet(self):
        # type: () -> Sheet
        pass

    def getZeroHeight(self):
        # type: () -> bool
        pass

    def isFormatted(self):
        # type: () -> bool
        pass

    def removeCell(self, cell):
        # type: (Cell) -> None
        pass

    def setHeight(self, height):
        # type: (int) -> None
        pass

    def setHeightInPoints(self, height):
        # type: (float) -> None
        pass

    def setRowNum(self, rowNum):
        # type: (int) -> None
        pass

    def setRowStyle(self, style):
        # type: (CellStyle) -> None
        pass

    def setZeroHeight(self, zHeight):
        # type: (bool) -> None
        pass

    def shiftCellsLeft(self, firstShiftColumnIndex, lastShiftColumnIndex, step):
        # type: (int, int, int) -> None
        pass

    def shiftCellsRight(self, firstShiftColumnIndex, lastShiftColumnIndex, step):
        # type: (int, int, int) -> None
        pass


class ShapeContainer(object):
    pass


class SimpleShape(Shape):
    def getShapeId(self):
        # type: () -> int
        pass


class ObjectData(SimpleShape):
    def getContentType(self):
        # type: () -> AnyStr
        pass

    def getDirectory(self):
        # type: () -> DirectoryEntry
        pass

    def getFileName(self):
        # type: () -> AnyStr
        pass

    def getObjectData(self):
        # type: () -> bytearray
        pass

    def getOLE2ClassName(self):
        # type: () -> AnyStr
        pass

    def getPictureData(self):
        # type: () -> PictureData
        pass

    def hasDirectoryEntry(self):
        # type: () -> bool
        pass


class Drawing(ShapeContainer):
    def createAnchor(self, dx1, dy1, dx2, dy2, col1, row1, col2, row2):
        # type: (int, int, int, int, int, int, int, int) -> ClientAnchor
        pass

    def createCellComment(self, anchor):
        # type: (ClientAnchor) -> Comment
        pass

    def createObjectData(self, anchor, storageId, pictureIndex):
        # type: (ClientAnchor, int, int) -> ObjectData
        pass

    def createPicture(self, anchor, pictureIndex):
        # type: (ClientAnchor, int) -> Picture
        pass


class Sheet(object):
    PANE_LOWER_LEFT = None  # type: int
    PANE_LOWER_RIGHT = None  # type: int
    PANE_UPPER_LEFT = None  # type: int
    PANE_UPPER_RIGHT = None  # type: int
    BottomMargin = None  # type: int
    FooterMargin = None  # type: int
    HeaderMargin = None  # type: int
    LeftMargin = None  # type: int
    RightMargin = None  # type: int
    TopMargin = None  # type: int

    def __iter__(self):
        # type: () -> Iterator[Row]
        yield Row()

    def addMergedRegion(self, region):
        # type: (CellRangeAddress) -> None
        pass

    def addMergedRegionUnsafe(self, region):
        # type: (CellRangeAddress) -> None
        pass

    def addValidationData(self, data):
        # type: (DataValidation) -> None
        pass

    def autoSizeColumn(self, column, useMergedCells=False):
        # type: (int, bool) -> None
        pass

    def createDrawingPatriarch(self):
        # type: () -> Drawing
        pass

    def createFreezePane(self, colSplit, rowSplit, leftmostColumn=0, topRow=0):
        # type: (int, int, int, int) -> None
        pass

    def createRow(self, rownum):
        # type: (int) -> Row
        pass

    def createSplitPane(self, xSplitPos, ySplitPos, leftmostColumn, topRow, activePane):
        # type: (int, int, int, int, int) -> None
        pass

    def getActiveCell(self):
        # type: () -> CellAddress
        pass

    def getAutobreaks(self):
        # type: () -> bool
        pass

    def getCellComment(self, ref):
        # type: (CellAddress) -> Comment
        pass

    def getCellComments(self):
        # type: () -> Dict[CellAddress, Comment]
        pass

    def getColumnBreaks(self):
        # type: () -> List[int]
        pass

    def getColumnOutlineLevel(self, column):
        # type: (int) -> int
        pass

    def getColumnStyle(self, column):
        # type: (int) -> CellStyle
        pass

    def getColumnWidth(self, column):
        # type: (int) -> int
        pass

    def getColumnWidthInPixels(self, column):
        # type: (int) -> float
        pass

    def getDataValidationHelper(self):
        # type: () -> DataValidationHelper
        pass

    def getDataValidations(self):
        # type: () -> List[DataValidation]
        pass

    def getDefaultColumnWidth(self):
        # type: () -> int
        pass

    def getDefaultRowHeight(self):
        # type: () -> int
        pass

    def getDefaultRowHeightInPoints(self):
        # type: () -> float
        pass

    def getDisplayGuts(self):
        # type: () -> bool
        pass

    def getDrawingPatriarch(self):
        # type: () -> Drawing
        pass

    def getFirstRowNum(self):
        # type: () -> int
        pass

    def getFitToPage(self):
        # type: () -> bool
        pass

    def getFooter(self):
        # type: () -> Footer
        pass

    def getForceFormulaRecalculation(self):
        # type: () -> bool
        pass

    def getHeader(self):
        # type: () -> Header
        pass

    def getHorizontallyCenter(self):
        # type: () -> bool
        pass

    def getHyperlink(self, *args):
        # type: (*Any) -> Hyperlink
        pass

    def getHyperlinks(self):
        # type: () -> List[Hyperlink]
        pass

    def getLastRowNum(self):
        # type: () -> int
        pass

    def getLeftCol(self):
        # type: () -> int
        pass

    def getMargin(self, margin):
        # type: (int) -> float
        pass

    def getMergedRegions(self):
        # type: () -> List[CellRangeAddress]
        pass

    def getNumMergedRegions(self):
        # type: () -> int
        pass

    def getPaneInformation(self):
        # type: () -> PaneInformation
        pass

    def getPhysicalNumberOfRows(self):
        # type: () -> int
        pass

    def getPrintSetup(self):
        # type: () -> PrintSetup
        pass

    def getProtect(self):
        # type: () -> bool
        pass

    def getRepeatingColumns(self):
        # type: () -> CellRangeAddress
        pass

    def getRepeatingRows(self):
        # type: () -> CellRangeAddress
        pass

    def getRow(self, rownum):
        # type: (int) -> Row
        pass

    def getRowBreaks(self):
        # type: () -> List[int]
        pass

    def getRowSumsBelow(self):
        # type: () -> bool
        pass

    def getRowSumsRight(self):
        # type: () -> bool
        pass

    def getScenarioProtect(self):
        # type: () -> bool
        pass

    def getSheetConditionalFormatting(self):
        # type: () -> SheetConditionalFormatting
        pass

    def getSheetName(self):
        # type: () -> AnyStr
        pass

    def getTopRow(self):
        # type: () -> int
        pass

    def getVerticallyCenter(self):
        # type: () -> bool
        pass

    def getWorkbook(self):
        # type: () -> Workbook
        pass

    def groupColumn(self, fromColumn, toColumn):
        # type: (int, int) -> None
        pass

    def groupRow(self, fromRow, toRow):
        # type: (int, int) -> None
        pass

    def isColumnBroken(self, column):
        # type: (int) -> bool
        pass

    def isColumnHidden(self, column):
        # type: (int) -> bool
        pass

    def isDisplayFormulas(self):
        # type: () -> bool
        pass

    def isDisplayGridlines(self):
        # type: () -> bool
        pass

    def isDisplayRowColHeadings(self):
        # type: () -> bool
        pass

    def isDisplayZeros(self):
        # type: () -> bool
        pass

    def isPrintGridlines(self):
        # type: () -> bool
        pass

    def isPrintRowAndColumnHeadings(self):
        # type: () -> bool
        pass

    def isRightToLeft(self):
        # type: () -> bool
        pass

    def isRowBroken(self, row):
        # type: (int) -> bool
        pass

    def isSelected(self):
        # type: () -> bool
        pass

    def protectSheet(self, password):
        # type: (AnyStr) -> None
        pass

    def removeArrayFormula(self, cell):
        # type: (Cell) -> CellRange
        pass

    def removeColumnBreak(self, column):
        # type: (int) -> None
        pass

    def removeMergedRegion(self, index):
        # type: (int) -> None
        pass

    def removeMergedRegions(self, indices):
        # type: (List[int]) -> None
        pass

    def removeRow(self, row):
        # type: (Row) -> None
        pass

    def removeRowBreak(self, row):
        # type: (int) -> None
        pass

    def rowIterator(self):
        # type: () -> Iterator[Row]
        pass

    def setActiveCell(self, address):
        # type: (CellAddress) -> None
        pass

    def setArrayFormula(self, formula, range):
        # type: (AnyStr, CellRangeAddress) -> CellRange
        pass

    def setAutobreaks(self, value):
        # type: (bool) -> None
        pass

    def setAutoFilter(self, range):
        # type: (CellRangeAddress) -> AutoFilter
        pass

    def setColumnBreak(self, column):
        # type: (int) -> None
        pass

    def setColumnGroupCollapsed(self, columnNumber, collapsed):
        # type: (int, bool) -> None
        pass

    def setColumnHidden(self, columnIndex, hidden):
        # type: (int, bool) -> None
        pass

    def setColumnWidth(self, columnIndex, width):
        # type: (int, int) -> None
        pass

    def setDefaultColumnStyle(self, column, style):
        # type: (int, CellStyle) -> None
        pass

    def setDefaultColumnWidth(self, width):
        # type: (int) -> None
        pass

    def setDefaultRowHeight(self, height):
        # type: (int) -> None
        pass

    def setDefaultRowHeightInPoints(self, height):
        # type: (float) -> None
        pass

    def setDisplayFormulas(self, show):
        # type: (bool) -> None
        pass

    def setDisplayGridlines(self, show):
        # type: (bool) -> None
        pass

    def setDisplayGuts(self, value):
        # type: (bool) -> None
        pass

    def setDisplayRowColHeadings(self, show):
        # type: (bool) -> None
        pass

    def setDisplayZeros(self, value):
        # type: (bool) -> None
        pass

    def setFitToPage(self, value):
        # type: (bool) -> None
        pass

    def setForceFormulaRecalculation(self, value):
        # type: (bool) -> None
        pass

    def setHorizontallyCenter(self, value):
        # type: (bool) -> None
        pass

    def setMargin(self, margin, size):
        # type: (int, float) -> None
        pass

    def setPrintGridlines(self, show):
        # type: (bool) -> None
        pass

    def setPrintRowAndColumnHeadings(self, show):
        # type: (bool) -> None
        pass

    def setRepeatingColumns(self, columnRangeRef):
        # type: (CellRangeAddress) -> None
        pass

    def setRepeatingRows(self, rowRangeRef):
        # type: (CellRangeAddress) -> None
        pass

    def setRightToLeft(self, value):
        # type: (bool) -> None
        pass

    def setRowBreak(self, row):
        # type: (int) -> None
        pass

    def setRowGroupCollapsed(self, row, collapse):
        # type: (int, bool) -> None
        pass

    def setRowSumsBelow(self, value):
        # type: (bool) -> None
        pass

    def setRowSumsRight(self, value):
        # type: (bool) -> None
        pass

    def setSelected(self, value):
        # type: (bool) -> None
        pass

    def setVerticallyCenter(self, value):
        # type: (bool) -> None
        pass

    def setZoom(self, scale):
        # type: (int) -> None
        pass

    def shiftColumns(self, startColumn, endColumn, n):
        # type: (int, int, int) -> None
        pass

    def shiftRows(
        self, startRow, endRow, n, copyRowHeight=True, resetOriginalRowHeight=True
    ):
        # type: (int, int, int, bool, bool) -> None
        pass

    def showInPane(self, topRow, leftCol):
        # type: (int, int) -> None
        pass

    def ungroupColumn(self, fromColumn, toColumn):
        # type: (int, int) -> None
        pass

    def ungroupRow(self, fromRow, toRow):
        # type: (int, int) -> None
        pass

    def valudateMergedRegions(self):
        # type: () -> None
        pass


class SheetConditionalFormatting(object):
    def addConditionalFormatting(self, *args):
        # type: (*Any) -> int
        pass

    def createConditionalFormattingColorScaleRule(self):
        # type: () -> ConditionalFormattingRule
        pass

    def createConditionalFormattingRule(self, *args):
        # type: (*Any) -> ConditionalFormattingRule
        pass

    def getConditionalFormattingAt(self, index):
        # type: (int) -> ConditionalFormatting
        pass

    def getNumConditionalFormattings(self):
        # type: () -> int
        pass

    def removeConditionalFormatting(self, index):
        # type: (int) -> None
        pass


class Workbook(Closeable):
    PICTURE_TYPE_DIB = None  # type: int
    PICTURE_TYPE_EMF = None  # type: int
    PICTURE_TYPE_JPEG = None  # type: int
    PICTURE_TYPE_PICT = None  # type: int
    PICTURE_TYPE_PNG = None  # type: int
    PICTURE_TYPE_WMF = None  # type: int

    def __iter__(self):
        # type: () -> Iterator[Sheet]
        yield Sheet()

    def addOlePackage(self, oleData, label, fileName, command):
        # type: (bytearray, AnyStr, AnyStr, AnyStr) -> int
        pass

    def addPicture(self, pictureData, format_):
        # type: (bytearray, int) -> int
        pass

    def addToolPack(self, toolpack):
        # type: (UDFFinder) -> None
        pass

    def cloneSheet(self, sheetNum):
        # type: (int) -> Sheet
        pass

    def close(self):
        # type: () -> None
        pass

    def createCellStyle(self):
        # type: () -> CellStyle
        pass

    def createDataFormat(self):
        # type: () -> DataFormat
        pass

    def createFont(self):
        # type: () -> Font
        pass

    def createName(self):
        # type: () -> Name
        pass

    def createSheet(self, name=None):
        # type: (Optional[AnyStr]) -> Sheet
        pass

    def findFont(self, bold, color, fontHeight, name, italic, strikeout, underline):
        # type: (bool, int, float, AnyStr, bool, bool, int) -> Font
        pass

    def getActiveSheetIndex(self):
        # type: () -> int
        pass

    def getAllNames(self):
        # type: () -> List[Name]
        pass

    def getAllPictures(self):
        # type: () -> List[PictureData]
        pass

    def getCellStyleAt(self, idx):
        # type: (int) -> CellStyle
        pass

    def getCreationHelper(self):
        # type: () -> CreationHelper
        pass

    def getFirstVisibleTab(self):
        # type: () -> int
        pass

    def getFontAt(self, idx):
        # type: (int) -> Font
        pass

    def getForceFormulaRecalculation(self):
        # type: () -> bool
        pass

    def getMissingCellPolicy(self):
        # type: () -> Row.MissingCellPolicy
        pass

    def getName(self, name):
        # type: (AnyStr) -> Name
        pass

    def getNames(self):
        # type: () -> List[Name]
        pass

    def getNumberOfFontsAsInt(self):
        # type: () -> int
        pass

    def getNumberOfNames(self):
        # type: () -> int
        pass

    def getNumberOfSheets(self):
        # type: () -> int
        pass

    def getNumCellStyles(self):
        # type: () -> int
        pass

    def getPrintArea(self):
        # type: () -> AnyStr
        pass

    def getSheet(self, name):
        # type: (AnyStr) -> Sheet
        pass

    def getSheetAt(self, index):
        # type: (int) -> Sheet
        pass

    def getSheetIndex(self, arg):
        # type: (Union[AnyStr, Sheet]) -> int
        pass

    def getSheetName(self, sheet):
        # type: (int) -> AnyStr
        pass

    def getSheetVisibility(self, sheetIx):
        # type: (int) -> SheetVisibility
        pass

    def getSpreadsheetVersion(self):
        # type: () -> SpreadsheetVersion
        pass

    def isHidden(self):
        # type: () -> bool
        pass

    def isSheetHidden(self, sheetIx):
        # type: (int) -> bool
        pass

    def isSheetVeryHidden(self, sheetIx):
        # type: (int) -> bool
        pass

    def linkExternalWorkbook(self, name, workbook):
        # type: (AnyStr, Workbook) -> None
        pass

    def removeName(self, name):
        # type: (Name) -> None
        pass

    def removePrintArea(self, sheetIndex):
        # type: (int) -> None
        pass

    def removeSheetAt(self, sheetIndex):
        # type: (int) -> None
        pass

    def setActiveSheet(self, sheetIndex):
        # type: (int) -> None
        pass

    def setFirstVisibleTab(self, sheetIndex):
        # type: (int) -> None
        pass

    def setForceFormulaRecalculation(self, value):
        # type: (bool) -> None
        pass

    def setHidden(self, hiddenFlag):
        # type: (bool) -> None
        pass

    def setMissingCellPolicy(self, missingCellPolicy):
        # type: (Row.MissingCellPolicy) -> None
        pass

    def setPrintArea(self, sheetIndex, *args):
        # type: (int, *AnyStr) -> None
        pass

    def setSelectedTab(self, index):
        # type: (int) -> None
        pass

    def setSheetHidden(self, sheetIx, hidden):
        # type: (int, bool) -> None
        pass

    def setSheetName(self, sheet, name):
        # type: (int, AnyStr) -> None
        pass

    def setSheetOrder(self, sheetName, pos):
        # type: (AnyStr, int) -> None
        pass

    def setSheetVisibility(self, sheetIx, visibility):
        # type: (int, SheetVisibility) -> None
        pass

    def sheetIterator(self):
        # type: () -> Iterator[Sheet]
        pass

    def write(self, stream):
        # type: (OutputStream) -> None
        pass


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
