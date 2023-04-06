from __future__ import print_function

from typing import Any, List

from com.inductiveautomation.ignition.common.xmlserialization import ClassNameResolver
from com.inductiveautomation.ignition.common.xmlserialization.encoding import (
    AttributeEncoder,
)
from com.inductiveautomation.ignition.common.xmlserialization.serialization.equalitydelegates import (
    EqualityDelegate,
)
from dev.thecesrom.helper.types import AnyStr
from java.lang import Class, Object


class Element(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Element, self).__init__()
        print(args)

    def addChild(self, element):
        # type: (Element) -> None
        pass

    def getAttributes(self):
        # type: () -> List[Element.Attribute]
        pass

    def getBody(self):
        # type: () -> Any
        pass

    def getChildCount(self):
        # type: () -> int
        pass

    def getChildren(self):
        # type: () -> List[Element]
        pass

    def getName(self):
        # type: () -> AnyStr
        pass

    def getObject(self):
        # type: () -> Object
        pass

    def getSubName(self):
        # type: () -> AnyStr
        pass

    def isSkipRefTracking(self):
        # type: () -> bool
        pass

    def setAttribute(self, *args):
        # type: (*Any) -> None
        pass

    def setBody(self, body):
        # type: (Any) -> None
        pass

    def setSkipRefTrack(self, skipRefTracking):
        # type: (bool) -> None
        pass

    class Attribute(Object):
        def __init__(self, name, value):
            # type: (AnyStr, AttributeEncoder) -> None
            super(Element.Attribute, self).__init__()
            self._name = name
            self._value = value

        def getName(self):
            # type: () -> AnyStr
            return self._name

        def getValue(self):
            # type: () -> AttributeEncoder
            return self._value


class SerializationDelegate(object):
    def isSkipReferenceTracking(self):
        # type: () -> bool
        raise NotImplementedError

    def serialize(self, context, obj):
        # type: (XMLSerializationContext, Any) -> Element
        raise NotImplementedError


class XMLSerializationContext(Object):
    def __init__(self, serializer):
        # type: (XMLSerializer) -> None
        super(XMLSerializationContext, self).__init__()
        print(serializer)

    def getClassNameMap(self):
        # type: () -> ClassNameResolver
        pass

    def getCleanCopy(self, type_):
        # type: (Class) -> Object
        pass

    def getRefForElement(self, elm):
        # type: (Element) -> int
        pass

    def registerEqualityDelegate(self, clazz, delegate):
        # type: (Class, EqualityDelegate) -> None
        pass

    def safeEquals(self, foo, bar):
        # type: (Object, Object) -> bool
        pass

    def serialize(self, obj):
        # type: (Object) -> Element
        pass


class XMLSerializer(Object):
    def __init__(self):
        # type: () -> None
        super(XMLSerializer, self).__init__()

    def addObject(self, obj):
        # type: (Object) -> None
        pass

    def addRootAttribute(self, key, value):
        # type: (AnyStr, AnyStr) -> None
        pass

    def addSerializationDelegate(self, clazz, delegate):
        # type: (Class, SerializationDelegate) -> None
        pass
