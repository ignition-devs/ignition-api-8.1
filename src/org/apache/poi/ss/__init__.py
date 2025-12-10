from typing import List, Union

from java.lang import Enum


class SpreadsheetVersion(Enum):
    def getLastColumnIndex(self):
        # type: () -> int
        pass

    def getLastColumnName(self):
        # type: () -> Union[str, unicode]
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
        # type: (Union[str, unicode]) -> SpreadsheetVersion
        pass

    @staticmethod
    def values():
        # type: () -> List[SpreadsheetVersion]
        pass
