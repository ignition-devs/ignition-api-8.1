from typing import Any, List, Sequence, TypeVar, Union

from java.beans import PropertyChangeListener
from java.lang import Class, Object, String

T = TypeVar("T")


class BasicPropertySet(Object):
    def __init__(self, *args):
        # type: (Any) -> None
        pass

    def addPropertySet(self, *args):
        # type: (Any) -> None
        pass

    def contains(self, prop):
        # type: (Property) -> bool
        pass

    def get(self, prop):
        # type: (Property) -> T
        pass

    def getCount(self):
        # type: () -> int
        pass

    def getExtension(self):
        # type: () -> PropertySet
        pass

    def getOrDefault(self, prop):
        # type: (Property) -> T
        pass

    def getOrElse(self, prop, value):
        # type: (Property, T) -> T
        pass

    def getProperties(self):
        # type: () -> List[Property]
        pass

    def getRawValueMap(self):
        # type: () -> Any
        pass

    def getValues(self):
        # type: () -> List[PropertyValue]
        pass

    def isExtended(self, prop):
        # type: (Property) -> bool
        pass

    def isInherited(self, prop):
        # type: (Property) -> bool
        pass

    def iterator(self):
        # type: () -> Sequence[PropertyValue]
        pass

    @staticmethod
    def of(*args):
        # type: (PropertyValue) -> PropertySet
        pass

    def remove(self, prop):
        # type: (Property) -> None
        pass

    def removePropertyChangeListener(self, listener):
        # type: (PropertyChangeListener) -> None
        pass

    def set(self, prop, value):
        # type: (Union[Property, PropertyValue], T) -> None
        pass

    def setDirect(self, prop, value):
        # type: (Property, Object) -> None
        pass

    def setRawValueMap(self, copy):
        # type: (Any) -> None
        pass

    class Builder(Object):
        def build(self):
            # type: () -> BasicPropertySet
            pass

        def set(self, prop, value):
            # type: (Property, T) -> BasicPropertySet.Builder
            pass


class Property(object):
    def getDefaultValue(self):
        # type: () -> T
        pass

    def getName(self):
        # type: () -> String
        pass

    def getType(self):
        # type: () -> Class
        pass


class PropertySet(object):
    @staticmethod
    def builder():
        # type: () -> BasicPropertySet.Builder
        pass

    def extend(self, parent):
        # type: (PropertySet) -> PropertySet
        pass

    def isExtended(self, prop):
        # type: (Property) -> bool
        pass

    def newDefaultInstance(self):
        # type: () -> PropertySet
        pass

    def newExtension(self):
        # type: () -> PropertySet
        pass


class PropertyValue(Object):
    def __init__(self, *args):
        # type: (Any) -> None
        pass

    def getProperty(self):
        # type: () -> Property
        pass

    def getValue(self):
        # type: () -> Object
        pass

    @staticmethod
    def of(prop, value):
        # type: (Property, Object) -> PropertyValue
        pass
