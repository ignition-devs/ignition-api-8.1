from typing import List

from dev.coatl.helper.types import AnyStr
from java.lang import Enum


class SpreadsheetVersion(Enum):
    def getLastColumnIndex(self):
        # type: () -> int
        pass

    def getLastColumnName(self):
        # type: () -> AnyStr
        pass

    def getLastRowIndex(self):
        # type: () -> int
        pass

    def getMaxCellStyles(self):
        # type: () -> int
        pass

    def getMaxColumns(self):
        # type: () -> int
        pass

    def getMaxConditionalFormats(self):
        # type: () -> int
        pass

    def getMaxFunctionArgs(self):
        # type: () -> int
        pass

    def getMaxRows(self):
        # type: () -> int
        pass

    def getMaxTextLength(self):
        # type: () -> int
        pass

    @staticmethod
    def getValueOf(name):
        # type: (AnyStr) -> SpreadsheetVersion
        pass

    @staticmethod
    def values():
        # type: () -> List[SpreadsheetVersion]
        pass
