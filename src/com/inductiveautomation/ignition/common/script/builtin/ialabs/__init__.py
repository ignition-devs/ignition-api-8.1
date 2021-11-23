from __future__ import print_function, unicode_literals

__all__ = ["BrowseTag", "OPCBrowseTag"]

from java.lang import Object


class BrowseTag(Object):
    def __init__(
        self,
        name=None,
        path=None,
        fullPath=None,
        type=None,
        valueSource=None,
        dataType=None,
    ):
        self.name = name
        self.path = path
        self.fullPath = fullPath
        self.type = type
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
        opcServer=None,
        type=None,
        displayName=None,
        displayPath=None,
        dataType=None,
        opcItemPath=None,
    ):
        self.opcServer = opcServer
        self.type = type
        self.displayName = displayName
        self.displayPath = displayPath
        self.dataType = dataType
        self.opcItemPath = opcItemPath

    def getDataType(self):
        return self.dataType

    def getDisplayName(self):
        return self.displayName

    def getDisplayPath(self):
        return self.displayPath

    def getOpcItemPath(self):
        return self.opcItemPath

    def getOpcServer(self):
        return self.opcServer

    def getType(self):
        return self.type
