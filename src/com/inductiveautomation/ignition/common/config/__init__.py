from __future__ import print_function

__all__ = [
    "BasicProperty",
    "BasicPropertySet",
    "Property",
    "PropertySet",
    "PropertyValue",
    "PropertyValueSource",
]

from typing import Any, Iterable, List, Union

from dev.thecesrom.helper.types import AnyStr
from java.beans import PropertyChangeListener
from java.lang import Class, Object
from java.util import Collection


class Property(object):
    def getDefaultValue(self):
        # type: () -> Any
        raise NotImplementedError

    def getName(self):
        # type: () -> AnyStr
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


class PropertyValueSource(object):
    def contains(self, prop):
        # type: (Property) -> bool
        raise NotImplementedError

    def get(self, prop):
        # type: (Property) -> Any
        raise NotImplementedError

    def getNonNull(self, *args):
        # type: (*Any) -> Any
        pass

    def getOrDefault(self, prop):
        # type: (Property) -> Any
        raise NotImplementedError

    def getOrElse(self, prop):
        # type: (Property) -> Any
        raise NotImplementedError

    def getProperties(self):
        # type: () -> Collection
        raise NotImplementedError

    def getValues(self):
        # type: () -> List[PropertyValue]
        pass


class BasicProperty(Property, Object):
    _name = None  # type: AnyStr
    _clazz = None  # type: Any
    _defaultValue = None  # type: Any
    _hcode = None  # type: int

    def __init__(self, *args):
        # type: (*Any) -> None
        super(BasicProperty, self).__init__()
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
        # type: () -> AnyStr
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
        # type: (AnyStr) -> None
        pass

    def setName_(self, name):
        # type: (AnyStr) -> BasicProperty
        pass


class BasicPropertySet(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(BasicPropertySet, self).__init__()

    def addPropertySet(self, *args):
        # type: (*Any) -> None
        pass

    def contains(self, prop):
        # type: (Property) -> bool
        return True

    def get(self, prop):
        # type: (Property) -> Any
        pass

    def getCount(self):
        # type: () -> int
        pass

    def getExtension(self):
        # type: () -> PropertySet
        pass

    def getOrDefault(self, prop):
        # type: (Property) -> Any
        pass

    def getOrElse(self, prop, value):
        # type: (Property, Any) -> Any
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
        return True

    def isInherited(self, prop):
        # type: (Property) -> bool
        return True

    def iterator(self):
        # type: () -> Iterable[PropertyValue]
        pass

    @staticmethod
    def of(*args):
        # type: (*PropertyValue) -> PropertySet
        pass

    def remove(self, prop):
        # type: (Property) -> None
        pass

    def removePropertyChangeListener(self, listener):
        # type: (PropertyChangeListener) -> None
        pass

    def set(self, prop, value):
        # type: (Union[Property, PropertyValue], Any) -> None
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
            # type: (Property, Any) -> BasicPropertySet.Builder
            pass


class PropertyValue(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(PropertyValue, self).__init__()
        print(args)

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
