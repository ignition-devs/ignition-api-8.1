from __future__ import print_function

__all__ = ["BrowseTag", "OPCBrowseTag"]

from typing import Optional

from com.inductiveautomation.ignition.common.opc import BrowseElementType
from com.inductiveautomation.ignition.common.sqltags.model.types import DataType
from com.inductiveautomation.ignition.common.tags.config.types import TagObjectType
from java.lang import Class, Object


class BrowseTag(Object):
    dataType = None  # type: DataType
    name = None  # type: str
    fullPath = None  # type: str
    path = None  # type: str
    type = None  # type: TagObjectType
    valueSource = None  # type: str

    def __init__(
        self,
        name,  # type: str
        path,  # type: str
        fullPath,  # type: str
        type_,  # type: TagObjectType
        valueSource,  # type: str
        dataType,  # type: DataType
    ):
        self.name = name
        self.path = path
        self.fullPath = fullPath
        self.type = type_
        self.valueSource = valueSource
        self.dataType = dataType

    def getDataType(self):
        return self.dataType

    def getFullPath(self):
        return self.fullPath

    def getPath(self):
        return self.path

    def getTagType(self):
        return self.type

    def getValueSource(self):
        return self.valueSource

    def isDB(self):
        print(self)
        return True

    def isExpression(self):
        print(self)
        return True

    def isFolder(self):
        print(self)
        return True

    def isMemory(self):
        print(self)
        return True

    def isOPC(self):
        print(self)
        return True

    def isQuery(self):
        print(self)
        return True

    def isUDT(self):
        print(self)
        return True


class OPCBrowseTag(Object):
    def __init__(
        self,
        opcServer=None,  # type: Optional[str]
        type_=None,  # type: Optional[BrowseElementType]
        displayName=None,  # type: Optional[str]
        displayPath=None,  # type: Optional[str]
        dataType=None,  # type: Optional[Class]
        opcItemPath=None,  # type: Optional[str]
    ):
        # type: (...) -> None
        self._opcServer = opcServer
        self._type = type_
        self._displayName = displayName
        self._displayPath = displayPath
        self._dataType = dataType
        self._opcItemPath = opcItemPath

    def getDataType(self):
        return self._dataType

    def getDisplayName(self):
        return self._displayName

    def getDisplayPath(self):
        return self._displayPath

    def getOpcItemPath(self):
        return self._opcItemPath

    def getOpcServer(self):
        return self._opcServer

    def getType(self):
        return self._type
