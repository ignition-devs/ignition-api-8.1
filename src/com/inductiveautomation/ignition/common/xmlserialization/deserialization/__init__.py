from __future__ import print_function

__all__ = [
    "AttributesMap",
    "DeserializationContext",
    "DeserializationHandler",
    "XMLDeserializer",
]

from typing import Any, Iterable, List, Mapping, Optional

from com.inductiveautomation.ignition.common.xmlserialization import (
    ClassNameResolver,
    SerializationException,
)
from com.inductiveautomation.ignition.common.xmlserialization.serialization import (
    XMLSerializer,
)
from dev.thecesrom.helper.types import AnyStr
from java.io import InputStream, Reader
from java.lang import Class, Object


class AttributesMap(object):
    def getClass(self, name):
        # type: (AnyStr) -> Class
        raise NotImplementedError

    def getDecoder(self, name):
        # type: (AnyStr) -> Any
        raise NotImplementedError

    def getInt(self, name):
        # type: (AnyStr) -> int
        raise NotImplementedError

    def getLength(self):
        # type: () -> int
        raise NotImplementedError

    def getName(self, index):
        # type: (int) -> AnyStr
        raise NotImplementedError

    def getSignature(self, name):
        # type: (AnyStr) -> Iterable[Class]
        raise NotImplementedError

    def getAnyStr(self, name):
        # type: (AnyStr) -> AnyStr
        raise NotImplementedError

    def getValue(self, name, decoder):
        # type: (AnyStr, Any) -> Any
        raise NotImplementedError


class DeserializationContext(object):
    def getClassNameMap(self):
        # type: () -> ClassNameResolver
        raise NotImplementedError

    def getRootAttributes(self):
        # type: () -> Mapping[AnyStr, AnyStr]
        raise NotImplementedError

    def getRootObjects(self):
        # type: () -> List[Object]
        raise NotImplementedError

    def getWarnings(self):
        # type: () -> List[SerializationException]
        raise NotImplementedError


class DeserializationHandler(object):
    def clone(self):
        # type: () -> DeserializationHandler
        raise NotImplementedError

    def endElement(self, context):
        # type: (DeserializationContext) -> None
        raise NotImplementedError

    def endObject(self, obj):
        # type: (Object) -> None
        raise NotImplementedError

    def endSubElement(self, name, context):
        # type: (AnyStr, DeserializationContext) -> None
        raise NotImplementedError

    def getBodyDecoder(self):
        # type: () -> Any
        raise NotImplementedError

    def getElementName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getObject(self):
        # type: () -> Object
        raise NotImplementedError

    def getRefId(self):
        # type: () -> int
        raise NotImplementedError

    def onBody(self, body):
        # type: (Object) -> None
        raise NotImplementedError

    def setRefId(self, id_):
        # type: (int) -> None
        raise NotImplementedError

    def startElement(self, name, attributes, context):
        # type: (AnyStr, AttributesMap, DeserializationContext) -> None
        raise NotImplementedError

    def startSubElement(self, name, attributes, context):
        # type: (AnyStr, AttributesMap, DeserializationContext) -> None
        raise NotImplementedError

    def supportsNestedElements(self):
        # type: () -> bool
        raise NotImplementedError


class XMLDeserializer(Object):
    def __init__(self, resolver=None):
        # type: (Optional[ClassNameResolver]) -> None
        super(XMLDeserializer, self).__init__()
        self.__classNameMap = resolver if resolver is not None else ClassNameResolver()

    def addHandler(self, handler):
        # type: (DeserializationHandler) -> None
        pass

    def deserialize(self, *args):
        # type: (*Any) -> DeserializationContext
        pass

    def deserializeBinary(self, *args):
        # type: (*Any) -> DeserializationContext
        pass

    def deserializeMultiple(self, bytes_, count):
        # type: (bytearray, int) -> List[DeserializationContext]
        pass

    def deserializeXML(self, streamReader, topAttributesOnly):
        # type: (Reader, bool) -> DeserializationContext
        pass

    def getClassNameMap(self):
        # type: () -> ClassNameResolver
        return self.__classNameMap

    def initDefaults(self):
        # type: () -> XMLDeserializer
        pass

    def readRootAttributes(self, arg):
        # type: (Any) -> Mapping[AnyStr, AnyStr]
        pass

    def transcodeToXML(self, binary, serializer):
        # type: (InputStream, XMLSerializer) -> AnyStr
        pass
