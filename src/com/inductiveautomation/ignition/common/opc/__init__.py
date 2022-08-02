__all__ = [
    "BasicOPCBrowseElement",
    "BasicServerNodeId",
    "BrowseElementType",
    "OPCBrowseElement",
    "ServerBrowseElement",
    "ServerNodeId",
]

from typing import Any, List

from java.lang import Class, Enum, Object, String


class OPCBrowseElement(object):
    def getDataType(self):
        # type: () -> Class
        raise NotImplementedError

    def getDescription(self):
        # type: () -> String
        raise NotImplementedError

    def getDisplayName(self):
        # type: () -> String
        raise NotImplementedError

    def getElementType(self):
        # type: () -> BrowseElementType
        raise NotImplementedError

    def getServerNodeId(self):
        # type: () -> ServerNodeId
        raise NotImplementedError


class ServerNodeId(object):
    def getNodeId(self):
        # type: () -> String
        raise NotImplementedError

    def getServerName(self):
        # type: () -> String
        raise NotImplementedError


class BasicOPCBrowseElement(Object, OPCBrowseElement):
    def __init__(self, *args):
        # type: (Any) -> None
        pass

    def getDataType(self):
        # type: () -> Class
        pass

    def getDescription(self):
        # type: () -> String
        pass

    def getDisplayName(self):
        # type: () -> String
        pass

    def getElementType(self):
        # type: () -> BrowseElementType
        pass

    def getServerNodeId(self):
        # type: () -> ServerNodeId
        pass


class BasicServerNodeId(Object, ServerNodeId):
    nodeId = None  # type: String
    serverName = None  # type: String

    def __init__(self, serverName, nodeId):
        # type: (String, String) -> None
        self.serverName = serverName
        self.nodeId = nodeId

    def getNodeId(self):
        # type: () -> String
        return self.nodeId

    def getServerName(self):
        # type: () -> String
        return self.serverName


class BrowseElementType(Enum):
    DATAVARIABLE = None  # type: BrowseElementType
    DEVICE = None  # type: BrowseElementType
    FOLDER = None  # type: BrowseElementType
    METHOD = None  # type: BrowseElementType
    OBJECT = None  # type: BrowseElementType
    PROPERTY = None  # type: BrowseElementType
    SERVER = None  # type: BrowseElementType
    VIEW = None  # type: BrowseElementType

    def isSubscribable(self):
        # type: () -> bool
        pass

    @staticmethod
    def values():
        # type: () -> List[BrowseElementType]
        pass


class ServerBrowseElement(Object, OPCBrowseElement):
    nodeId = None  # type: ServerNodeId

    def __init__(self, serverName):
        # type: (String) -> None
        self.nodeId = BasicServerNodeId(serverName, "")

    def getDataType(self):
        # type: () -> Class
        pass

    def getDescription(self):
        # type: () -> String
        return ""

    def getDisplayName(self):
        # type: () -> String
        pass

    def getElementType(self):
        # type: () -> BrowseElementType
        return BrowseElementType.SERVER

    def getServerNodeId(self):
        # type: () -> ServerNodeId
        return self.nodeId
