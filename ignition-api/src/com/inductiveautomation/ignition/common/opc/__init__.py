from __future__ import print_function

__all__ = [
    "BasicOPCBrowseElement",
    "BasicServerNodeId",
    "BrowseElement",
    "BrowseElementType",
    "OPCBrowseElement",
    "ServerBrowseElement",
    "ServerNodeId",
]

from typing import Any, Dict, List, Optional, Union

from java.lang import Class, Enum, Object, StringBuilder


class OPCBrowseElement(object):
    def getDataType(self):
        # type: () -> Class
        raise NotImplementedError

    def getDescription(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getDisplayName(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getElementType(self):
        # type: () -> BrowseElementType
        raise NotImplementedError

    def getNodeId(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getServerNodeId(self):
        # type: () -> ServerNodeId
        raise NotImplementedError


class ServerNodeId(object):
    def getNodeId(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getServerName(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError


class BasicOPCBrowseElement(Object, OPCBrowseElement):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(BasicOPCBrowseElement, self).__init__()
        print(args)

    def getDataType(self):
        # type: () -> Class
        pass

    def getDescription(self):
        # type: () -> Union[str, unicode]
        pass

    def getDisplayName(self):
        # type: () -> Union[str, unicode]
        pass

    def getElementType(self):
        # type: () -> BrowseElementType
        pass

    def getNodeId(self):
        # type: () -> Union[str, unicode]
        pass

    def getServerNodeId(self):
        # type: () -> ServerNodeId
        pass


class BasicServerNodeId(Object, ServerNodeId):
    nodeId = None  # type: Union[str, unicode]
    serverName = None  # type: Union[str, unicode]

    def __init__(self, serverName, nodeId):
        # type: (Union[str, unicode], Union[str, unicode]) -> None
        super(BasicServerNodeId, self).__init__()
        self.serverName = serverName
        self.nodeId = nodeId

    def getNodeId(self):
        # type: () -> Union[str, unicode]
        return self.nodeId

    def getServerName(self):
        # type: () -> Union[str, unicode]
        return self.serverName


class BrowseElement(Object):

    class PropertyElement(Object):
        id = None  # type: int
        name = None  # type: Union[str, unicode]
        value = None  # type: Union[str, unicode]

        def __init__(
            self,
            id_,  # type: int
            name,  # type: Union[str, unicode]
            value,  # type: Union[str, unicode]
        ):
            # type: (...) -> None
            super(BrowseElement.PropertyElement, self).__init__()
            self.id = id_
            self.name = name
            self.value = value

        def getId(self):
            # type: () -> int
            return self.id

        def getName(self):
            # type: () -> Union[str, unicode]
            return self.name

        def getValue(self):
            # type: () -> Union[str, unicode]
            return self.value

    PROP_PROVIDER = 500  # type: int
    PROP_DRIVER = 501  # type: int
    _server = None  # type: Union[str, unicode]
    _browsePath = None  # type: Union[str, unicode]
    _itemName = None  # type: Union[str, unicode]
    _itemId = None  # type: Union[str, unicode]
    _itemType = None  # type: Optional[int]
    _properties = None  # type: Dict[int, BrowseElement.PropertyElement]
    _complete = False  # type: bool

    def __init__(self, itemType=None):
        # type: (Optional[int]) -> None
        super(BrowseElement, self).__init__()
        self._itemType = itemType
        self._properties = {0: BrowseElement.PropertyElement(0, "", "")}

    def addProperty(self, id_, name, value):
        # type: (int, Union[str, unicode], Union[str, unicode]) -> None
        pass

    def asServerNodeId(self):
        # type: () -> ServerNodeId
        pass

    def createRequestElement(self, type_):
        # type: (int) -> BrowseElement
        pass

    def fillInDetails(self, elm):
        # type: (BrowseElement) -> None
        pass

    def getBrowsePath(self):
        # type: () -> Union[str, unicode]
        return self._browsePath

    def getItemId(self):
        # type: () -> Union[str, unicode]
        return self._itemId

    def getItemName(self):
        # type: () -> Union[str, unicode]
        return self._itemName

    def getItemType(self):
        # type: () -> Optional[int]
        return self._itemType

    def getProperties(self):
        # type: () -> List[BrowseElement.PropertyElement]
        return self._properties.values()

    def getProperty(self, id_):
        # type: (int) -> BrowseElement.PropertyElement
        return self._properties[id_]

    def getServer(self):
        # type: () -> Union[str, unicode]
        return self._server

    def isComplete(self):
        # type: () -> bool
        return self._complete

    def setBrowsePath(self, browsePath):
        # type: (Union[str, unicode]) -> None
        self._browsePath = browsePath

    def setComplete(self, value):
        # type: (bool) -> None
        self._complete = value

    def setItemId(self, itemId):
        # type: (Union[str, unicode]) -> None
        self._itemId = itemId

    def setItemName(self, itemName):
        # type: (Union[str, unicode]) -> None
        self._itemName = itemName

    def setItemType(self, itemType):
        # type: (int) -> None
        self._itemType = itemType

    def setServer(self, server):
        # type: (Union[str, unicode]) -> None
        self._server = server

    @staticmethod
    def toBrowseElement(opcElem):
        # type: (OPCBrowseElement) -> BrowseElement
        pass

    @staticmethod
    def toBrowseElements(opcElements):
        # type: (List[OPCBrowseElement]) -> List[BrowseElement]
        pass

    @staticmethod
    def toServerNodeId(elem):
        # type: (BrowseElement) -> ServerNodeId
        pass

    def toXML(self, out, type_=None, includeProperties=None):
        # type: (StringBuilder, Optional[int], Optional[bool]) -> None
        pass


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
        return True

    @staticmethod
    def values():
        # type: () -> List[BrowseElementType]
        pass


class ServerBrowseElement(Object, OPCBrowseElement):
    nodeId = None  # type: ServerNodeId

    def __init__(self, serverName):
        # type: (Union[str, unicode]) -> None
        super(ServerBrowseElement, self).__init__()
        self.nodeId = BasicServerNodeId(serverName, "")

    def getDataType(self):
        # type: () -> Class
        pass

    def getDescription(self):
        # type: () -> Union[str, unicode]
        return ""

    def getDisplayName(self):
        # type: () -> Union[str, unicode]
        pass

    def getElementType(self):
        # type: () -> BrowseElementType
        return BrowseElementType.SERVER

    def getNodeId(self):
        # type: () -> Union[str, unicode]
        return self.getServerNodeId().getNodeId()

    def getServerNodeId(self):
        # type: () -> ServerNodeId
        return self.nodeId
