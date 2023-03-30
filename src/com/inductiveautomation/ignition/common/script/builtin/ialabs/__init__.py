from __future__ import print_function

__all__ = ["BrowseTag", "OPCBrowseTag"]

from typing import Optional

from com.inductiveautomation.ignition.common.opc import BrowseElementType
from com.inductiveautomation.ignition.common.sqltags.model.types import DataType
from com.inductiveautomation.ignition.common.tags.config.types import TagObjectType
from dev.thecesrom.helper.types import AnyStr
from java.lang import Class, Object


class BrowseTag(Object):
    dataType = None  # type: DataType
    name = None  # type: AnyStr
    fullPath = None  # type: AnyStr
    path = None  # type: AnyStr
    type = None  # type: TagObjectType
    valueSource = None  # type: AnyStr

    def __init__(
        self,
        name,  # type: str
        path,  # type: str
        fullPath,  # type: str
        type_,  # type: TagObjectType
        valueSource,  # type: str
        dataType,  # type: DataType
    ):
        super(BrowseTag, self).__init__()
        self.name = name
        self.path = path
        self.fullPath = fullPath
        self.type = type_
        self.valueSource = valueSource
        self.dataType = dataType

    def getDataType(self):
        # type: () -> DataType
        return self.dataType

    def getFullPath(self):
        # type: () -> AnyStr
        return self.fullPath

    def getPath(self):
        # type: () -> AnyStr
        return self.path

    def getTagType(self):
        # type: () -> TagObjectType
        return self.type

    def getValueSource(self):
        # type: () -> AnyStr
        return self.valueSource

    def isDB(self):
        # type: () -> bool
        print(self)
        return True

    def isExpression(self):
        # type: () -> bool
        print(self)
        return True

    def isFolder(self):
        # type: () -> bool
        print(self)
        return True

    def isMemory(self):
        # type: () -> bool
        print(self)
        return True

    def isOPC(self):
        # type: () -> bool
        print(self)
        return True

    def isQuery(self):
        # type: () -> bool
        print(self)
        return True

    def isUDT(self):
        # type: () -> bool
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
        super(OPCBrowseTag, self).__init__()
        self._opcServer = opcServer
        self._type = type_
        self._displayName = displayName
        self._displayPath = displayPath
        self._dataType = dataType
        self._opcItemPath = opcItemPath

    def getDataType(self):
        # type: () -> Optional[Class]
        return self._dataType

    def getDisplayName(self):
        # type: () -> Optional[str]
        return self._displayName

    def getDisplayPath(self):
        # type: () -> Optional[str]
        return self._displayPath

    def getOpcItemPath(self):
        # type: () -> Optional[str]
        return self._opcItemPath

    def getOpcServer(self):
        # type: () -> Optional[str]
        return self._opcServer

    def getType(self):
        # type: () -> Optional[BrowseElementType]
        return self._type
