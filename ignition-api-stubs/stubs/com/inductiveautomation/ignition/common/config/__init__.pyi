from typing import Any, Iterable, List, Union

from dev.coatl.helper.types import AnyStr
from java.beans import PropertyChangeListener
from java.lang import Class, Object
from java.util import Collection

class Property:
    def getDefaultValue(self) -> Any: ...
    def getName(self) -> AnyStr: ...
    def getType(self) -> Class: ...

class PropertySet:
    @staticmethod
    def builder() -> BasicPropertySet.Builder: ...
    def extend(self, parent: PropertySet) -> PropertySet: ...
    def isExtended(self, prop: Property) -> bool: ...
    def newDefaultInstance(self) -> PropertySet: ...
    def newExtension(self) -> PropertySet: ...

class PropertyValueSource:
    def contains(self, prop: Property) -> bool: ...
    def get(self, prop: Property) -> Any: ...
    def getNonNull(self, *args: Any) -> Any: ...
    def getOrDefault(self, prop: Property) -> Any: ...
    def getOrElse(self, prop: Property) -> Any: ...
    def getProperties(self) -> Collection: ...
    def getValues(self) -> List[PropertyValue]: ...

class BasicProperty(Property, Object):
    def __init__(self, *args: Any) -> None: ...
    def getClazz(self) -> Class: ...
    def getDefaultValue(self) -> Any: ...
    def getName(self) -> AnyStr: ...
    def getType(self) -> Class: ...
    def setClazz(self, clazz: Class) -> None: ...
    def setClazz_(self, clazz: Class) -> BasicProperty: ...
    def setDefaultValue(self, defaultValue: Any) -> None: ...
    def setDefaultValue_(self, defaultValue: Any) -> BasicProperty: ...
    def setName(self, name: AnyStr) -> None: ...
    def setName_(self, name: AnyStr) -> BasicProperty: ...

class BasicPropertySet(Object):
    class Builder(Object):
        def build(self) -> BasicPropertySet: ...
        def set(self, prop: Property, value: Any) -> BasicPropertySet.Builder: ...

    def __init__(self, *args: Any) -> None: ...
    def addPropertySet(self, *args: Any) -> None: ...
    def contains(self, prop: Property) -> bool: ...
    def get(self, prop: Property) -> Any: ...
    def getCount(self) -> int: ...
    def getExtension(self) -> PropertySet: ...
    def getOrDefault(self, prop: Property) -> Any: ...
    def getOrElse(self, prop: Property, value: Any) -> Any: ...
    def getProperties(self) -> List[Property]: ...
    def getRawValueMap(self) -> Any: ...
    def getValues(self) -> List[PropertyValue]: ...
    def isExtended(self, prop: Property) -> bool: ...
    def isInherited(self, prop: Property) -> bool: ...
    def iterator(self) -> Iterable[PropertyValue]: ...
    @staticmethod
    def of(*args: PropertyValue) -> PropertySet: ...
    def remove(self, prop: Property) -> None: ...
    def removePropertyChangeListener(
        self, listener: PropertyChangeListener
    ) -> None: ...
    def set(self, prop: Union[Property, PropertyValue], value: Any) -> None: ...
    def setDirect(self, prop: Property, value: Object) -> None: ...
    def setRawValueMap(self, copy: Any) -> None: ...

class PropertyValue(Object):
    def __init__(self, *args: Any) -> None: ...
    def getProperty(self) -> Property: ...
    def getValue(self) -> Object: ...
    @staticmethod
    def of(prop: Property, value: Object) -> PropertyValue: ...
