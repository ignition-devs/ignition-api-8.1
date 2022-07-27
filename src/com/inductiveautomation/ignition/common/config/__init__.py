__all__ = [
    "BasicProperty",
    "BasicPropertySet",
    "Property",
    "PropertySet",
    "PropertyValue",
]

from typing import Any, Iterable, List, TypeVar, Union

from java.beans import PropertyChangeListener
from java.lang import Class, Object, String

T = TypeVar("T")


class Property(object):
    def getDefaultValue(self):
        # type: () -> Any
        raise NotImplementedError

    def getName(self):
        # type: () -> String
        raise NotImplementedError

    def getType(self):
        # type: () -> Class
        raise NotImplementedError


class PropertySet(object):
    @staticmethod
    def builder():
        # type: () -> BasicPropertySet.Builder
        raise NotImplementedError

    def extend(self, parent):
        # type: (PropertySet) -> PropertySet
        raise NotImplementedError

    def isExtended(self, prop):
        # type: (Property) -> bool
        raise NotImplementedError

    def newDefaultInstance(self):
        # type: () -> PropertySet
        raise NotImplementedError

    def newExtension(self):
        # type: () -> PropertySet
        raise NotImplementedError


class BasicProperty(Property, Object):
    _name = None  # type: String
    _clazz = None  # type: Any
    _defaultValue = None  # type: Any
    _hcode = None  # type: int

    def __init__(self, *args):
        # type: (Any) -> None
        if not args:
            self._hcode = 0
        elif len(args) == 2:
            self._name = args[0]
            self._clazz = args[1]
        elif len(args) == 3:
            self._name = args[0]
            self._clazz = args[1]
            self._defaultValue = args[2]
        else:
            raise NotImplementedError

    def getClazz(self):
        # type: () -> Class
        pass

    def getDefaultValue(self):
        # type: () -> Any
        return self._defaultValue

    def getName(self):
        # type: () -> String
        return self._name

    def getType(self):
        # type: () -> Class
        pass

    def setClazz(self, clazz):
        # type: (Class) -> None
        pass

    def setClazz_(self, clazz):
        # type: (Class) -> BasicProperty
        pass

    def setDefaultValue(self, defaultValue):
        # type: (Any) -> None
        pass

    def setDefaultValue_(self, defaultValue):
        # type: (Any) -> BasicProperty
        pass

    def setName(self, name):
        # type: (String) -> None
        pass

    def setName_(self, name):
        # type: (String) -> BasicProperty
        pass


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
        # type: () -> Iterable[PropertyValue]
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
