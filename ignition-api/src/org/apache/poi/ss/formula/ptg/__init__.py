from __future__ import print_function

from typing import Any, List, Union

from dev.coatl.helper.types import AnyStr
from java.lang import Object
from org.apache.poi.common import Duplicatable
from org.apache.poi.ss.formula import (
    ExternSheetReferenceToken,
    WorkbookDependentFormula,
)
from org.apache.poi.util import LittleEndianInput, LittleEndianOutput


class AreaI(object):
    class OffsetArea(object):
        def __init__(
            self,
            baseRow,  # type: int
            baseColumn,  # type: int
            relFirstRow,  # type: int
            relLastRowIx,  # type: int
            relFirstColIx,  # type: int
            relLastColIx,  # type: int
        ):
            # type: (...) -> None
            super(AreaI.OffsetArea, self).__init__()
            print(
                baseRow,
                baseColumn,
                relFirstRow,
                relLastRowIx,
                relFirstColIx,
                relLastColIx,
            )

        def getFirstRow(self):
            # type: () -> int
            pass

        def getFirstColumn(self):
            # type: () -> int
            pass

        def getLastRow(self):
            # type: () -> int
            pass

        def getLastColumn(self):
            # type: () -> int
            pass

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


class Pxg(object):
    def getExternalWorkbookNumber(self):
        # type: () -> int
        raise NotImplementedError

    def getSheetName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def setSheetName(self, name):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def toFormulaString(self):
        # type: () -> AnyStr
        raise NotImplementedError


class Pxg3D(Pxg):
    def getExternalWorkbookNumber(self):
        # type: () -> int
        raise NotImplementedError

    def getLastSheetName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getSheetName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def setLastSheetName(self, name):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def setSheetName(self, name):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def toFormulaString(self):
        # type: () -> AnyStr
        raise NotImplementedError


class Ptg(Object, Duplicatable):
    CLASS_ARRAY = None  # type: int
    CLASS_REF = None  # type: int
    CLASS_VALUE = None  # type: int
    EMPTY_PTG_ARRAY = None  # type: List[Ptg]

    def copy(self):
        # type: () -> Duplicatable
        pass

    @staticmethod
    def createPtg(in_):
        # type: (LittleEndianInput) -> Ptg
        pass

    @staticmethod
    def doesFormulaReferToDeletedCell(ptgs):
        # type: (List[Ptg]) -> bool
        pass

    def getDefaultOperandClass(self):
        # type: () -> int
        pass

    @staticmethod
    def getEncodedSize(ptgs):
        # type: (List[Ptg]) -> int
        pass

    @staticmethod
    def getEncodedSizeWithoutArrayData(ptgs):
        # type: (List[Ptg]) -> int
        pass

    def getPtgClass(self):
        # type: () -> int
        pass

    def getRVAType(self):
        # type: () -> AnyStr
        pass

    def getSize(self):
        # type: () -> int
        pass

    def isBaseToken(self):
        # type: () -> bool
        return True

    @staticmethod
    def readTokens(size, in_):
        # type: (int, LittleEndianInput) -> List[Ptg]
        pass

    @staticmethod
    def serializePtgs(ptgs, array, offset):
        # type: (List[Ptg], bytearray, int) -> int
        pass

    def setClass(self, thePtgClass):
        # type: (int) -> None
        pass

    def toFormulaString(self):
        # type: () -> AnyStr
        pass

    def write(self, out):
        # type: (LittleEndianOutput) -> None
        pass


class OperandPtg(Ptg):
    pass


class NamePtg(OperandPtg):
    sid = None  # type: int

    def __init__(self, arg):
        # type: (Union[int, LittleEndianInput,NamePtg]) -> None
        super(NamePtg, self).__init__()
        print(arg)

    def getIndex(self):
        # type: () -> int
        pass


class AreaPtgBase(OperandPtg, AreaI):
    sid = None  # type: int

    def __init__(self, *args):
        # type: (*Any) -> None
        super(AreaPtgBase, self).__init__()
        print(args)

    def getFirstColumn(self):
        # type: () -> int
        pass

    def getFirstColumnRaw(self):
        # type: () -> int
        pass

    def getFirstRow(self):
        # type: () -> int
        pass

    def getLastColumn(self):
        # type: () -> int
        pass

    def getLastColumnRaw(self):
        # type: () -> int
        pass

    def getLastRow(self):
        # type: () -> int
        pass

    def isFirstColRelative(self):
        # type: () -> bool
        pass

    def isFirstRowRelative(self):
        # type: () -> bool
        pass

    def isLastColRelative(self):
        # type: () -> bool
        pass

    def isLastRowRelative(self):
        # type: () -> bool
        pass

    def setFirstColRelative(self, rel):
        # type: (bool) -> None
        pass

    def setFirstColumnRaw(self, colIx):
        # type: (int) -> None
        pass

    def setFirstRowRelative(self, rel):
        # type: (bool) -> None
        pass

    def setLastColRelative(self, rel):
        # type: (bool) -> None
        pass

    def setLastColumn(self, colIx):
        # type: (int) -> None
        pass

    def setLastColumnRaw(self, column):
        # type: (int) -> None
        pass

    def setLastRow(self, rowIx):
        # type: (int) -> None
        pass

    def setLastRowRelative(self, rel):
        # type: (bool) -> None
        pass

    def sortTopLeftToBottomRight(self):
        # type: () -> None
        pass


class Area3DPtg(AreaPtgBase, WorkbookDependentFormula, ExternSheetReferenceToken):

    def __init__(self, *args):
        # type: (*Any) -> None
        super(Area3DPtg, self).__init__()
        print(args)

    def format2DRefAsString(self):
        # type: () -> AnyStr
        pass

    def getExternSheetIndex(self):
        # type: () -> int
        pass

    def setExternSheetIndex(self, index):
        # type: (int) -> None
        pass


class Area3DPxg(AreaPtgBase, Pxg3D):

    def __init__(self, *args):
        # type: (*Any) -> None
        super(Area3DPxg, self).__init__()
        print(args)

    def format2DRefAsString(self):
        # type: () -> AnyStr
        pass

    def getExternalWorkbookNumber(self):
        # type: () -> int
        pass

    def getLastSheetName(self):
        # type: () -> AnyStr
        pass

    def getSheetName(self):
        # type: () -> AnyStr
        pass

    def setLastSheetName(self, name):
        # type: (AnyStr) -> None
        pass

    def setSheetName(self, name):
        # type: (AnyStr) -> None
        pass


class NameXPtg(OperandPtg):
    sid = None  # type: int

    def __init__(self, *args):
        # type: (*Any) -> None
        super(NameXPtg, self).__init__()
        print(args)

    def getNameIndex(self):
        # type: () -> int
        pass

    def getSheetRefIndex(self):
        # type: () -> int
        pass


class NameXPxg(OperandPtg):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(NameXPxg, self).__init__()
        print(args)

    def getExternalWorkbookNumber(self):
        # type: () -> int
        pass

    def getNameName(self):
        # type: () -> AnyStr
        pass

    def getSheetName(self):
        # type: () -> AnyStr
        pass

    def setSheetName(self, sheetName):
        # type: (AnyStr) -> None
        pass


class RefPtgBase(OperandPtg):
    def getColumn(self):
        # type: () -> int
        pass

    def getRow(self):
        # type: () -> int
        pass

    def isColRelative(self):
        # type: () -> bool
        pass

    def isRowRelative(self):
        # type: () -> bool
        pass

    def setColRelative(self, rel):
        # type: (bool) -> None
        pass

    def setColumn(self, colIx):
        # type: (int) -> None
        pass

    def setRow(self, rowIx):
        # type: (int) -> None
        pass

    def setRowRelative(self, rel):
        # type: (bool) -> None
        pass


class Ref3DPtg(RefPtgBase, WorkbookDependentFormula, ExternSheetReferenceToken):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Ref3DPtg, self).__init__()
        print(args)

    def format2DRefAsString(self):
        # type: () -> AnyStr
        pass

    def getExternSheetIndex(self):
        # type: () -> int
        pass

    def setExternSheetIndex(self, index):
        # type: (int) -> None
        pass


class Ref3DPxg(RefPtgBase, Pxg3D):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Ref3DPxg, self).__init__()
        print(args)

    def format2DRefAsString(self):
        # type: () -> AnyStr
        pass

    def getExternalWorkbookNumber(self):
        # type: () -> int
        pass

    def getLastSheetName(self):
        # type: () -> AnyStr
        pass

    def getSheetName(self):
        # type: () -> AnyStr
        pass

    def setLastSheetName(self, name):
        # type: (AnyStr) -> None
        pass

    def setSheetName(self, name):
        # type: (AnyStr) -> None
        pass
