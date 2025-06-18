from __future__ import print_function

from typing import TYPE_CHECKING, Any, List, Optional, Union

from dev.coatl.helper.types import AnyStr
from java.lang import Comparable, Enum, Object
from org.apache.poi.ss import SpreadsheetVersion
from org.apache.poi.ss.formula.eval import ValueEval
from org.apache.poi.ss.formula.udf import UDFFinder
from org.apache.poi.ss.usermodel import (
    Cell,
    CellType,
    ConditionalFormatting,
    ConditionalFormattingRule,
    ConditionType,
    ExcelNumberFormat,
    Sheet,
    Workbook,
)
from org.apache.poi.ss.util import CellRangeAddress, CellRangeAddressBase, CellReference

if TYPE_CHECKING:
    from org.apache.poi.ss.formula.functions import FreeRefFunction, Function
    from org.apache.poi.ss.formula.ptg import (
        Area3DPtg,
        Area3DPxg,
        NamePtg,
        NameXPtg,
        NameXPxg,
        Ptg,
        Ref3DPtg,
        Ref3DPxg,
    )


class EvaluationCell(object):
    def getArrayFormulaRange(self):
        # type: () -> CellRangeAddress
        raise NotImplementedError

    def getBooleanCellValue(self):
        # type: () -> bool
        raise NotImplementedError

    def getCacheFormulaResultType(self):
        # type: () -> CellType
        raise NotImplementedError

    def getCellType(self):
        # type: () -> CellType
        raise NotImplementedError

    def getColumnIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getErrorCellValue(self):
        # type: () -> int
        raise NotImplementedError

    def getIdentityKey(self):
        # type: () -> Object
        raise NotImplementedError

    def getNumericCellValue(self):
        # type: () -> float
        raise NotImplementedError

    def getRowIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getSheet(self):
        # type: () -> EvaluationSheet
        raise NotImplementedError

    def getStringCellValue(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def isPartOfArrayFormulaGroup(self):
        # type: () -> bool
        raise NotImplementedError


class EvaluationSheet(object):
    def clearAllCachedResultValues(self):
        # type: () -> None
        raise NotImplementedError

    def getCell(self, rowIndex, columnIndex):
        # type: (int, int) -> EvaluationCell
        raise NotImplementedError

    def getLastRowNum(self):
        # type: () -> int
        raise NotImplementedError

    def isRowHidden(self, rowIndex):
        # type: (int) -> bool
        raise NotImplementedError


class EvaluationWorkbook(object):
    class ExternalName(Object):
        _nameName = None  # type: AnyStr
        _nameNumber = None  # type: int
        _ix = None  # type: int

        def __init__(self, nameName, nameNumber, ix):
            # type: (AnyStr, int, int) -> None
            super(EvaluationWorkbook.ExternalName, self).__init__()
            self._nameName = nameName
            self._nameNumber = nameNumber
            self._ix = ix

        def getIx(self):
            # type: () -> int
            return self._ix

        def getNameName(self):
            # type: () -> AnyStr
            return self._nameName

        def getNameNumber(self):
            # type: () -> int
            return self._nameNumber

    class ExternalSheet(Object):
        _workbookName = None  # type: AnyStr
        _sheetName = None  # type: AnyStr

        def __init__(self, workbookName, sheetName):
            # type: (AnyStr, AnyStr) -> None
            super(EvaluationWorkbook.ExternalSheet, self).__init__()
            self._workbookName = workbookName
            self._sheetName = sheetName

        def getSheetName(self):
            # type: () -> AnyStr
            return self._sheetName

        def getWorkbookName(self):
            # type: () -> AnyStr
            return self._workbookName

    class ExternalSheetRange(Object):
        _workbookName = None  # type: AnyStr
        _firstSheetName = None  # type: AnyStr
        _lastSheetName = None  # type: AnyStr

        def __init__(self, workbookName, firstSheetName, lastSheetName):
            # type: (AnyStr, AnyStr, AnyStr) -> None
            super(EvaluationWorkbook.ExternalSheetRange, self).__init__()
            self._workbookName = workbookName
            self._firstSheetName = firstSheetName
            self._lastSheetName = lastSheetName

        def getFirstSheetName(self):
            # type: () -> AnyStr
            return self._firstSheetName

        def getLastSheetName(self):
            # type: () -> AnyStr
            return self._lastSheetName

    def clearAllCachedResultValues(self):
        # type: () -> None
        raise NotImplementedError

    def convertFromExternSheetIndex(self, externSheetIndex):
        # type: (int) -> int
        raise NotImplementedError

    def getExternalName(self, externSheetIndex, sheetName, externalWorkbookNumber=None):
        # type: (int, int, Optional[int]) -> ExternalName
        raise NotImplementedError

    def getExternalSheet(self, *args):
        # type: (*Any) -> ExternalSheet
        raise NotImplementedError

    def getFormulaTokens(self, cell):
        # type: (EvaluationCell) -> List[Ptg]
        raise NotImplementedError

    def getName(self, name, sheetIndex=None):
        # type: (Union[AnyStr, NamePtg], Optional[int]) -> ExternalName
        raise NotImplementedError

    def getSheet(self, sheetIndex):
        # type: (int) -> EvaluationSheet
        raise NotImplementedError

    def getSheetIndex(self, arg):
        # type: (Union[AnyStr, EvaluationSheet]) -> int
        raise NotImplementedError

    def getSheetName(self, sheetIndex):
        # type: (int) -> AnyStr
        raise NotImplementedError

    def getSpreadsheetVersion(self):
        # type: () -> SpreadsheetVersion
        raise NotImplementedError

    def getUDFFinder(self):
        # type: () -> UDFFinder
        raise NotImplementedError

    def resolveNameXText(self, ptg):
        # type: (NameXPtg) -> AnyStr
        raise NotImplementedError


class EvaluationCache(Object):
    def clear(self):
        # type: () -> None
        pass

    def getOrCreateFormulaCellEntry(self, cell):
        # type: (EvaluationCell) -> FormulaCellCacheEntry
        pass

    def getPlainValueEntry(
        self,
        bookIndex,  # type: int
        sheetIndex,  # type: int
        rowIndex,  # type: int
        columnIndex,  # type: int
        value,  # type: ValueEval
    ):
        # type: (...) -> PlainValueCellCacheEntry
        pass

    def notifyDeleteCell(self, bookIndex, sheetIndex, cell):
        # type: (int, int, EvaluationCell) -> None
        pass

    def notifyUpdateCell(self, bookIndex, sheetIndex, cell):
        # type: (int, int, EvaluationCell) -> None
        pass


class EvaluationTracker(Object):
    def __init__(self, cache):
        # type: (EvaluationCache) -> None
        super(EvaluationTracker, self).__init__()

    def acceptFormulaDependency(self, cce):
        # type: (CellCacheEntry) -> None
        pass

    def acceptPlainValueDependency(
        self,
        bookIndex,  # type: int
        sheetIndex,  # type: int
        rowIndex,  # type: int
        columnIndex,  # type: int
        value,  # type: ValueEval
    ):
        # type: (...) -> None
        pass

    def endEvaluate(self, cce):
        # type: (CellCacheEntry) -> None
        pass

    def startEvaluate(self, cce):
        # type: (FormulaCellCacheEntry) -> bool
        return True

    def updateCacheResult(self, result):
        # type: (ValueEval) -> int
        pass


class IEvaluationListener(object):
    class ICacheEntry(object):
        def getValue(self):
            # type: () -> ValueEval
            raise NotImplementedError

    def onCacheHit(self, var1, var2, var3, var4):
        # type: (int, int, int, ValueEval) -> None
        raise NotImplementedError

    def onReadPlainValue(self, var1, var2, var3, var4):
        # type: (int, int, int, ICacheEntry) -> None
        raise NotImplementedError

    def onStartEvaluate(self, var1, var2):
        # type: (EvaluationCell, ICacheEntry) -> None
        raise NotImplementedError

    def onClearWholeCache(self):
        # type: () -> None
        raise NotImplementedError

    def onClearCachedValue(self, var1):
        # type: (ICacheEntry) -> None
        raise NotImplementedError

    def sortDependentCachedValues(self, var1):
        # type: (List[ICacheEntry]) -> None
        raise NotImplementedError

    def onClearDependentCachedValues(self, var1, var2):
        # type: (ICacheEntry, int) -> None
        raise NotImplementedError

    def onChangeFromBlankValue(self, var1, var2, var3, var4, var5):
        # type: (int, int, int, ValueEval, ICacheEntry) -> None
        pass


class CellCacheEntry(Object, IEvaluationListener.ICacheEntry):
    def addConsumingCell(self, cellLoc):
        # type: (FormulaCellCacheEntry) -> None
        raise NotImplementedError

    def clearConsumingCell(self, cce):
        # type: (FormulaCellCacheEntry) -> None
        raise NotImplementedError

    def getConsumingCells(self):
        # type: () -> List[FormulaCellCacheEntry]
        raise NotImplementedError

    def getValue(self):
        # type: () -> ValueEval
        raise NotImplementedError

    def recurseClearCachedFormulaResults(self, listener):
        # type: (IEvaluationListener) -> None
        raise NotImplementedError

    def updateValue(self, value):
        # type: (ValueEval) -> None
        raise NotImplementedError


class ExternSheetReferenceToken(object):
    def format2DRefAsString(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getExternSheetIndex(self):
        # type: () -> int
        raise NotImplementedError


class FormulaCellCacheEntry(CellCacheEntry):
    def __init__(self):
        # type: () -> None
        super(FormulaCellCacheEntry, self).__init__()

    def addConsumingCell(self, cellLoc):
        # type: (FormulaCellCacheEntry) -> None
        raise NotImplementedError

    def changeConsumingCells(self, usedCells):
        # type: (List[CellCacheEntry]) -> None
        pass

    def clearFormulaEntry(self):
        # type: () -> None
        pass

    def getConsumingCells(self):
        # type: () -> List[FormulaCellCacheEntry]
        raise NotImplementedError

    def getValue(self):
        # type: () -> ValueEval
        raise NotImplementedError

    def isInputSensitive(self):
        # type: () -> bool
        return False

    def notifyUpdatedBlankCell(self, bsj, rowIndex, columnIndex, evaluationListener):
        # type: (int, int, int, IEvaluationListener) -> None
        pass

    def recurseClearCachedFormulaResults(self, listener):
        # type: (IEvaluationListener) -> None
        raise NotImplementedError

    def setSensitiveInputCells(self, sensitiveInputCells):
        # type: (List[CellCacheEntry]) -> None
        pass

    def updateFormulaResult(
        self,
        result,  # type: ValueEval
        sensitiveInputCells,  # type: List[CellCacheEntry]
        usedBlankAreas,  # type: FormulaUsedBlankCellSet
    ):
        # type: (...) -> None
        pass

    def updateValue(self, value):
        # type: (ValueEval) -> None
        raise NotImplementedError


class FormulaUsedBlankCellSet(Object):
    class BlankCellRectangleGroup(Object):
        _firstRowIndex = None  # type: int
        _firstColumnIndex = None  # type: int
        _lastColumnIndex = None  # type: int
        _lastRowIndex = None  # type: int

        def __init__(self, firstRowIndex, firstColumnIndex, lastColumnIndex):
            # type: (int, int, int) -> None
            super(FormulaUsedBlankCellSet.BlankCellRectangleGroup, self).__init__()
            self._firstRowIndex = firstRowIndex
            self._firstColumnIndex = firstColumnIndex
            self._lastColumnIndex = lastColumnIndex

        def containsCell(self, rowIndex, columnIndex):
            # type: (int, int) -> bool
            pass

        def acceptRow(self, rowIndex, firstColumnIndex, lastColumnIndex):
            # type: (int, int, int) -> bool
            pass

    class BlankCellSheetGroup(Object):
        _rectangleGroups = (
            None
        )  # type: List[FormulaUsedBlankCellSet.BlankCellRectangleGroup]
        _currentRowIndex = -1  # type: int
        _firstColumnIndex = None  # type: int
        _lastColumnIndex = None  # type: int
        _currentRectangleGroup = (
            None
        )  # type: FormulaUsedBlankCellSet.BlankCellRectangleGroup
        _lastDefinedRow = None  # type: int

        def __init__(self, lastDefinedRow):
            # type: (int) -> None
            super(FormulaUsedBlankCellSet.BlankCellSheetGroup, self).__init__()
            self._lastDefinedRow = lastDefinedRow

        def addCell(self, rowIndex, columnIndex):
            # type: (int, int) -> None
            pass

        def containsCell(self, rowIndex, columnIndex):
            # type: (int, int) -> bool
            pass

    class BookSheetKey(Object):
        _bookIndex = None  # type: int
        _sheetIndex = None  # type: int

        def __init__(self, bookIndex, sheetIndex):
            # type: (int, int) -> None
            super(FormulaUsedBlankCellSet.BookSheetKey, self).__init__()
            self._bookIndex = bookIndex
            self._sheetIndex = sheetIndex

    def addCell(self, evalWorkbook, bookIndex, sheetIndex, rowIndex, columnIndex):
        # type: (EvaluationWorkbook, int, int, int, int) -> None
        pass

    def getSheetGroup(self, evalWorkbook, bookIndex, sheetIndex):
        # type: (EvaluationWorkbook, int, int) -> BlankCellSheetGroup
        pass

    def containsCell(self, key, rowIndex, columnIndex):
        # type: (BookSheetKey, int, int) -> bool
        pass

    def isEmpty(self):
        # type: () -> bool
        pass


class PlainValueCellCacheEntry(CellCacheEntry):
    def __init__(self, value):
        # type: (ValueEval) -> None
        super(PlainValueCellCacheEntry, self).__init__()
        print(value)

    def addConsumingCell(self, cellLoc):
        # type: (FormulaCellCacheEntry) -> None
        raise NotImplementedError

    def clearConsumingCell(self, cce):
        # type: (FormulaCellCacheEntry) -> None
        raise NotImplementedError

    def getConsumingCells(self):
        # type: () -> List[FormulaCellCacheEntry]
        raise NotImplementedError

    def getValue(self):
        # type: () -> ValueEval
        raise NotImplementedError

    def recurseClearCachedFormulaResults(self, listener):
        # type: (IEvaluationListener) -> None
        raise NotImplementedError

    def updateValue(self, value):
        # type: (ValueEval) -> None
        raise NotImplementedError


class SheetRange(object):
    def getFirstSheetIndex(self):
        # type: () -> int
        raise NotImplementedError

    def getLastSheetIndex(self):
        # type: () -> int
        raise NotImplementedError


class SheetRefEvaluator(Object):
    _bookEvaluator = None  # type: WorkbookEvaluator
    _tracker = None  # type: EvaluationTracker
    _sheetIndex = None  # type: int
    _sheet = None  # type: EvaluationSheet

    def __init__(self, bookEvaluator, tracker, sheetIndex):
        # type: (WorkbookEvaluator, EvaluationTracker, int) -> None
        super(SheetRefEvaluator, self).__init__()
        self._bookEvaluator = bookEvaluator
        self._tracker = tracker
        self._sheetIndex = sheetIndex

    def getEvalForCell(self, rowIndex, columnIndex):
        # type: (int, int) -> ValueEval
        pass

    def getSheet(self):
        # type: () -> EvaluationSheet
        pass

    def getSheetName(self):
        # type: () -> AnyStr
        pass

    def isSubTotal(self, rowIndex, columnIndex):
        # type: (int, int) -> bool
        pass

    def isRowHidden(self, rowIndex):
        # type: (int) -> bool
        pass


class SheetRangeEvaluator(Object, SheetRange):
    _firstSheetIndex = None  # type: int
    _lastSheetIndex = None  # type: int
    _sheetEvaluators = None  # type: List[SheetRefEvaluator]

    def __init__(self, firstSheetIndex, lastSheetIndex, sheetEvaluators):
        # type: (int, int, List[SheetRefEvaluator]) -> None
        super(SheetRangeEvaluator, self).__init__()
        self._firstSheetIndex = firstSheetIndex
        self._lastSheetIndex = lastSheetIndex
        self._sheetEvaluators = sheetEvaluators

    def getEvalForCell(self, sheetIndex, rowIndex, columnIndex):
        # type: (int, int, int) -> ValueEval
        pass

    def getFirstSheetIndex(self):
        # type: () -> int
        pass

    def getLastSheetIndex(self):
        # type: () -> int
        pass

    def getSheetEvaluator(self, sheetIndex):
        # type: (int) -> SheetRefEvaluator
        pass

    def getSheetName(self, sheetIndex):
        # type: (int) -> AnyStr
        pass

    def getSheetNameRange(self):
        # type: () -> AnyStr
        pass


class OperationEvaluationContext(Object):
    UDF = None  # type: FreeRefFunction

    def __init__(
        self,
        bookEvaluator,  # type: WorkbookEvaluator
        workbook,  # type: EvaluationWorkbook
        sheetIndex,  # type: int
        srcRowNum,  # type: int
        srcColNum,  # type: int
        tracker,  # type: EvaluationTracker
        isSingleValue=True,  # type: bool
    ):
        # type: (...) -> None
        super(OperationEvaluationContext, self).__init__()
        print(
            bookEvaluator,
            workbook,
            sheetIndex,
            srcRowNum,
            srcColNum,
            tracker,
            isSingleValue,
        )

    def findUserDefinedFunction(self, name):
        # type: (AnyStr) -> FreeRefFunction
        pass

    def getArea3DEval(self, aptg):
        # type: (Union[Area3DPtg, Area3DPxg]) -> ValueEval
        pass

    def getAreaEval(
        self,
        firstRowIndex,  # type: int
        firstColumnIndex,  # type: int
        lastRowIndex,  # type: int
        lastColumnIndex,  # type: int
    ):
        # type: (...) -> ValueEval
        pass

    def getAreaValueEval(
        self,
        firstRowIndex,  # type: int
        firstColumnIndex,  # type: int
        lastRowIndex,  # type: int
        lastColumnIndex,  # type: int
        tokens,  # type: List[Object]
    ):
        # type: (...) -> ValueEval
        pass

    def getColumnIndex(self):
        # type: () -> int
        pass

    def getDynamicReference(
        self,
        workbookName,  # type: AnyStr
        sheetName,  # type: AnyStr
        refStrPart1,  # type: AnyStr
        refStrPart2,  # type: AnyStr
        isA1Style,  # type: bool
    ):
        # type: (...) -> ValueEval
        pass

    def getNameXEval(self, arg):
        # type: (Union[NameXPtg, NameXPxg]) -> ValueEval
        pass

    def getRef3DEval(self, arg):
        # type: (Union[Ref3DPtg, Ref3DPxg]) -> ValueEval
        pass

    def getRefEval(self, rowIndex, colIndex):
        # type: (int, int) -> ValueEval
        pass

    def getRefEvaluatorForCurrentSheet(self):
        # type: () -> SheetRangeEvaluator
        pass

    def getRowIndex(self):
        # type: () -> int
        pass

    def getSheetIndex(self):
        # type: () -> int
        pass

    def getWorkbook(self):
        # type: () -> EvaluationWorkbook
        pass

    def isArrayMode(self):
        # type: () -> bool
        pass

    def isSingleValue(self):
        # type: () -> bool
        pass

    def setArrayMode(self, value):
        # type: (bool) -> None
        pass


class IStabilityClassifier(object):
    TOTALLY_IMMUTABLE = None  # type: IStabilityClassifier

    def isCellFinal(self, sheetIndex, rowIndex, columnIndex):
        # type: (int, int, int) -> bool
        raise NotImplementedError


class WorkbookDependentFormula(object):
    def toFormulaString(self):
        # type: () -> AnyStr
        raise NotImplementedError


class WorkbookEvaluator(Object):
    def __init__(
        self,
        workbook,  # type: EvaluationWorkbook
        stabilityClassifier,  # type: IStabilityClassifier
        udfFinder,  # type: UDFFinder
    ):
        # type: (...) -> None
        super(WorkbookEvaluator, self).__init__()
        print(workbook, stabilityClassifier, udfFinder)

    def clearAllCachedResultValues(self):
        # type: () -> None
        pass

    @staticmethod
    def dereferenceResult(evaluationResult, srcRowNum, srcColNum):
        # type: (ValueEval, int, int) -> ValueEval
        pass

    def evaluate(self, *args):
        # type: (*Any) -> ValueEval
        pass

    def evaluateList(
        self,
        formula,  # type: AnyStr
        target,  # type: CellReference
        region,  # type: CellRangeAddressBase
    ):
        # type: (...) -> ValueEval
        pass

    def findUserDefinedFunction(self, name):
        # type: (AnyStr) -> FreeRefFunction
        pass

    @staticmethod
    def getNotSupportedFunctionNames():
        # type: () -> List[AnyStr]
        pass

    @staticmethod
    def getSupportedFunctionNames():
        # type: () -> List[AnyStr]
        pass

    def isDebugEvaluationOutpotForNextEval(self):
        # type: () -> bool
        pass

    def isIgnoreMissingWorkbooks(self):
        # type: () -> bool
        pass

    def notifyDeleteCell(self, cell):
        # type: (EvaluationCell) -> None
        pass

    def notifyUpdateCell(self, cell):
        # type: (EvaluationCell) -> None
        pass

    @staticmethod
    def registerFunction(name, func):
        # type: (AnyStr, Union[FreeRefFunction, Function]) -> None
        pass

    def setDebugEvaluationOutputForNextEval(self, value):
        # type: (bool) -> None
        pass

    def setIgnoreMissingWorkbooks(self, ignore):
        # type: (bool) -> None
        pass


class WorkbookEvaluatorProvider(object):
    def _getWorkbookEvaluator(self):
        # type: () -> WorkbookEvaluator
        raise NotImplementedError


class EvaluationConditionalFormatRule(Object, Comparable):
    class OperatorEnum(Enum):
        BETWEEN = None  # type: EvaluationConditionalFormatRule.OperatorEnum
        EQUAL = None  # type: EvaluationConditionalFormatRule.OperatorEnum
        GREATER_OR_EQUAL = None  # type: EvaluationConditionalFormatRule.OperatorEnum
        GREATER_THAN = None  # type: EvaluationConditionalFormatRule.OperatorEnum
        LESS_OR_EQUAL = None  # type: EvaluationConditionalFormatRule.OperatorEnum
        LESS_THAN = None  # type: EvaluationConditionalFormatRule.OperatorEnum
        NO_COMPARISON = None  # type: EvaluationConditionalFormatRule.OperatorEnum
        NOT_BETWEEN = None  # type: EvaluationConditionalFormatRule.OperatorEnum
        NOT_EQUAL = None  # type: EvaluationConditionalFormatRule.OperatorEnum

        def isValid(self, *args):
            # type: (*Comparable) -> bool
            pass

        def isValidForCompatibleTypes(self):
            # type: () -> bool
            pass

        @staticmethod
        def values():
            # type: () -> List[EvaluationConditionalFormatRule.OperatorEnum]  # noqa: W505
            pass

    def __init__(
        self,
        workbookEvaluator,  # type: WorkbookEvaluator
        sheet,  # type: Sheet
        formatting,  # type: ConditionalFormatting
        formattingIndex,  # type: int
        rule,  # type: ConditionalFormattingRule
        ruleIndex,  # type: int
        regions,  # type: List[CellRangeAddress]
    ):
        # type: (...) -> None
        super(EvaluationConditionalFormatRule, self).__init__()
        print(
            workbookEvaluator,
            sheet,
            formatting,
            formattingIndex,
            rule,
            ruleIndex,
            regions,
        )

    def compareTo(self, o):
        # type: (Any) -> int
        pass

    def getFormatting(self):
        # type: () -> ConditionalFormatting
        pass

    def getFormattingIndex(self):
        # type: () -> int
        pass

    def getFormula1(self):
        # type: () -> AnyStr
        pass

    def getFormula2(self):
        # type: () -> AnyStr
        pass

    def getNumberFormat(self):
        # type: () -> ExcelNumberFormat
        pass

    def getOperator(self):
        # type: () -> EvaluationConditionalFormatRule.OperatorEnum
        pass

    def getPriority(self):
        # type: () -> int
        pass

    def getRegions(self):
        # type: () -> List[CellRangeAddress]
        pass

    def getRule(self):
        # type: () -> ConditionalFormattingRule
        pass

    def getRuleIndex(self):
        # type: () -> int
        pass

    def getSheet(self):
        # type: () -> Sheet
        pass

    def getText(self):
        # type: () -> AnyStr
        pass

    def getType(self):
        # type: () -> ConditionType
        pass


class ConditionalFormattingEvaluator(Object):
    def __init__(self, wb, provider):
        # type: (Workbook, WorkbookEvaluatorProvider) -> None
        super(ConditionalFormattingEvaluator, self).__init__()
        print(wb, provider)

    def clearAllCachedFormats(self):
        # type: () -> None
        pass

    def clearAllCachedValues(self):
        # type: () -> None
        pass

    def getConditionalFormattingForCell(
        self,
        cell,  # type: Union[Cell, CellReference]
    ):
        # type: (...) -> List[EvaluationConditionalFormatRule]
        pass

    def getFormatRulesForSheet(
        self,
        sheet,  # type: Union[AnyStr, Sheet]
    ):
        # type: (...) -> List[EvaluationConditionalFormatRule]
        pass

    def getMatchingCells(self, *args):
        # type: (*Any) -> List[Cell]
        pass

    @staticmethod
    def getRef(cell):
        # type: (Cell) -> CellReference
        pass
