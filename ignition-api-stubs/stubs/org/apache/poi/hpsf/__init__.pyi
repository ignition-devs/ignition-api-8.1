from typing import Any

from java.lang import Object

class ClassID(Object):
    EQUATION30: ClassID
    EXCEL_V3: ClassID
    EXCEL_V3_CHART: ClassID
    EXCEL_V3_MACRO: ClassID
    EXCEL2003: ClassID
    EXCEL2007: ClassID
    EXCEL2007_MACRO: ClassID
    EXCEL2007_XLSB: ClassID
    EXCEL2010: ClassID
    EXCEL2010_CHART: ClassID
    EXCEL2010_ODS: ClassID
    EXCEL95: ClassID
    EXCEL95_CHART: ClassID
    EXCEL97: ClassID
    EXCEL97_CHART: ClassID
    LENGTH: ClassID
    OLE10_PACKAGE: ClassID
    POWERPOINT2007: ClassID
    POWERPOINT2007_MACRO: ClassID
    POWERPOINT95: ClassID
    POWERPOINT97: ClassID
    PPT_SHOW: ClassID
    TXT_ONLY: ClassID
    WORD2007: ClassID
    WORD2007_MACRO: ClassID
    WORD95: ClassID
    WORD97: ClassID
    XLS_WORKBOOK: ClassID
    def __init__(self, *args: Any) -> None: ...
    def copy(self) -> ClassID: ...
    def equalsInverted(self, o: ClassID) -> bool: ...
    def getBytes(self) -> bytes: ...
    def length(self) -> int: ...
    def read(self, src: bytes, offset: int) -> None: ...
    def setBytes(self, bytes_: bytes) -> None: ...
    def write(self, *args: Any) -> None: ...
