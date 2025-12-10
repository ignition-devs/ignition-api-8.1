from typing import Any

from java.lang import Object


class ClassID(Object):
    EQUATION30 = None  # type: ClassID
    EXCEL_V3 = None  # type: ClassID
    EXCEL_V3_CHART = None  # type: ClassID
    EXCEL_V3_MACRO = None  # type: ClassID
    EXCEL2003 = None  # type: ClassID
    EXCEL2007 = None  # type: ClassID
    EXCEL2007_MACRO = None  # type: ClassID
    EXCEL2007_XLSB = None  # type: ClassID
    EXCEL2010 = None  # type: ClassID
    EXCEL2010_CHART = None  # type: ClassID
    EXCEL2010_ODS = None  # type: ClassID
    EXCEL95 = None  # type: ClassID
    EXCEL95_CHART = None  # type: ClassID
    EXCEL97 = None  # type: ClassID
    EXCEL97_CHART = None  # type: ClassID
    LENGTH = None  # type: ClassID
    OLE10_PACKAGE = None  # type: ClassID
    POWERPOINT2007 = None  # type: ClassID
    POWERPOINT2007_MACRO = None  # type: ClassID
    POWERPOINT95 = None  # type: ClassID
    POWERPOINT97 = None  # type: ClassID
    PPT_SHOW = None  # type: ClassID
    TXT_ONLY = None  # type: ClassID
    WORD2007 = None  # type: ClassID
    WORD2007_MACRO = None  # type: ClassID
    WORD95 = None  # type: ClassID
    WORD97 = None  # type: ClassID
    XLS_WORKBOOK = None  # type: ClassID

    def __init__(self, *args):
        # type: (*Any) -> None
        super(ClassID, self).__init__()
        print(args)

    def copy(self):
        # type: () -> ClassID
        pass

    def equalsInverted(self, o):
        # type: (ClassID) -> bool
        pass

    def getBytes(self):
        # type: () -> bytes
        pass

    def length(self):
        # type: () -> int
        pass

    def read(self, src, offset):
        # type: (bytes, int) -> None
        pass

    def setBytes(self, bytes_):
        # type: (bytes) -> None
        pass

    def write(self, *args):
        # type: (*Any) -> None
        pass
