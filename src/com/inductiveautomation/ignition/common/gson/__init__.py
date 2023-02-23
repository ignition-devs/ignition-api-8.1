from __future__ import print_function

__all__ = [
    "ExclusionStrategy",
    "FieldAttributes",
    "FieldNamingPolicy",
    "FieldNamingStrategy",
    "Gson",
    "GsonBuilder",
    "JsonArray",
    "JsonElement",
    "JsonPrimitive",
    "LongSerializationPolicy",
    "TypeAdapter",
    "TypeAdapterFactory",
]

from typing import Any, Iterable, Optional, TypeVar, Union

from com.inductiveautomation.ignition.common.gson.reflect import TypeToken
from com.inductiveautomation.ignition.common.gson.stream import JsonReader, JsonWriter
from dev.thecesrom.helper.types import AnyStr
from java.io import Reader, Writer
from java.lang import Class, Enum, Object

Number = Union[float, int, long]
T = TypeVar("T")


class ExclusionStrategy(object):
    def shouldSkipClass(self, clazz):
        # type: (Class) -> bool
        raise NotImplementedError

    def shouldSkipField(self, attributes):
        # type: (FieldAttributes) -> bool
        raise NotImplementedError


class FieldNamingStrategy(object):
    def translateName(self, arg):
        # type: (Any) -> AnyStr
        raise NotImplementedError


class TypeAdapterFactory(object):
    def create(self, gson, token):
        # type: (Gson, TypeToken) -> TypeAdapter
        raise NotImplementedError


class FieldAttributes(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(FieldAttributes, self).__init__()
        print(args)

    def getAnnotation(self, annotation):
        # type: (Class) -> T
        pass

    def getAnnotations(self):
        # type: () -> Iterable[Any]
        pass

    def getDeclaredClass(self):
        # type: () -> Class
        pass

    def getDeclaredType(self):
        # type: () -> Any
        pass

    def getDeclaringClass(self):
        # type: () -> Class
        pass

    def getName(self):
        # type: () -> AnyStr
        pass

    def hasModifier(self, modifier):
        # type: (int) -> bool
        return True

    def isSynthetic(self):
        # type: () -> bool
        return True


class FieldNamingPolicy(Enum, FieldNamingStrategy):
    IDENTITY = None  # type: AnyStr
    UPPER_CAMEL_CASE = None  # type: AnyStr
    UPPER_CAMEL_CASE_WITH_SPACES = None  # type: AnyStr
    LOWER_CASE_WITH_UNDERSCORES = None  # type: AnyStr
    LOWER_CASE_WITH_DASHES = None  # type: AnyStr
    LOWER_CASE_WITH_DOTS = None  # type: AnyStr

    def translateName(self, arg):
        # type: (Any) -> AnyStr
        pass


class Gson(Object):
    def excluder(self):
        # type: () -> Any
        pass

    def fieldNamingStrategy(self):
        # type: () -> FieldNamingStrategy
        pass

    def fromJson(self, *args):
        # type: (*Any) -> T
        pass

    def getAdapter(self, type=None):
        # type: (TypeToken) -> TypeAdapter
        pass

    def getDelegateAdapter(self, skipPast, type):
        # type: (TypeAdapterFactory, TypeToken) -> TypeAdapter
        pass

    def htmlSafe(self):
        # type: () -> bool
        return True

    def newBuilder(self):
        # type: () -> GsonBuilder
        pass

    def newJsonReader(self, reader):
        # type: (Reader) -> JsonReader
        pass

    def newJsonWriter(self, writer):
        # type: (Writer) -> JsonWriter
        pass

    def serializeNulls(self):
        # type: () -> bool
        return True

    def toJson(self, *args):
        # type: (*Any) -> Optional[AnyStr]
        pass

    def toJsonTree(self, src, typeOfSrc=None):
        # type: (Object, Any) -> JsonElement
        pass


class GsonBuilder(object):
    def __init__(self, *args):
        # type: (*Any) -> None
        pass

    def addDeserializationExclusionStrategy(self, strategy):
        # type: (ExclusionStrategy) -> GsonBuilder
        pass

    def addSerializationExclusionStrategy(self, strategy):
        # type: (ExclusionStrategy) -> GsonBuilder
        pass

    def create(self):
        # type: () -> Gson
        pass

    def disableHtmlEscaping(self):
        # type: () -> GsonBuilder
        pass

    def disableInnerClassSerialization(self):
        # type: () -> GsonBuilder
        pass

    def enableComplexMapKeySerialization(self):
        # type: () -> GsonBuilder
        pass

    def excludeFieldsWithoutExposeAnnotation(self):
        # type: () -> GsonBuilder
        pass

    def excludeFieldsWithModifiers(self, *args):
        # type: (*int) -> GsonBuilder
        pass

    def generateNonExecutableJson(self):
        # type: () -> GsonBuilder
        pass

    def setLenient(self):
        # type: () -> GsonBuilder
        pass

    def registerTypeAdapter(self, type, typeAdapter):
        # type: (Any, Object) -> GsonBuilder
        pass

    def registerTypeAdapterFactory(self, factory):
        # type: (TypeAdapterFactory) -> GsonBuilder
        pass

    def registerTypeHierarchyAdapter(self, baseType, typeAdapter):
        # type: (Class, Object) -> GsonBuilder
        pass

    def serializeNulls(self):
        # type: () -> GsonBuilder
        pass

    def serializeSpecialFloatingPointValues(self):
        # type: () -> GsonBuilder
        pass

    def setDateFormat(self, *args):
        # type: (*Any) -> GsonBuilder
        pass

    def setExclusionStrategies(self, *args):
        # type: (*ExclusionStrategy) -> GsonBuilder
        pass

    def setFieldNamingPolicy(self, namingConvention):
        # type: (FieldNamingPolicy) -> GsonBuilder
        pass

    def setFieldNamingStrategy(self, fieldNamingStrategy):
        # type: (FieldNamingStrategy) -> GsonBuilder
        pass

    def setLongSerializationPolicy(self, policy):
        # type: (LongSerializationPolicy) -> GsonBuilder
        pass

    def setPrettyPrinting(self):
        # type: () -> GsonBuilder
        pass

    def setVersion(self, ignoreVersionsAfter):
        # type: (float) -> GsonBuilder
        pass


class JsonElement(object):
    def deepCopy(self):
        # type: () -> JsonElement
        pass

    def getAsBigDecimal(self):
        # type: () -> float
        raise NotImplementedError

    def getAsBigInteger(self):
        # type: () -> int
        raise NotImplementedError

    def getAsBoolean(self):
        # type: () -> bool
        raise NotImplementedError

    def getAsByte(self):
        # type: () -> Any
        raise NotImplementedError

    def getAsCharacter(self):
        # type: () -> str
        raise NotImplementedError

    def getAsDouble(self):
        # type: () -> float
        raise NotImplementedError

    def getAsFloat(self):
        # type: () -> float
        raise NotImplementedError

    def getAsInt(self):
        # type: () -> int
        raise NotImplementedError

    def getAsJsonArray(self):
        # type: () -> JsonArray
        pass

    def getAsJsonObject(self):
        # type: () -> JsonObject
        pass

    def getAsJsonPrimitive(self):
        # type: () -> JsonPrimitive
        pass

    def getAsJsonNull(self):
        # type: () -> JsonNull
        pass

    def getAsLong(self):
        # type: () -> long
        raise NotImplementedError

    def getAsNumber(self):
        # type: () -> Number
        raise NotImplementedError

    def getAsShort(self):
        # type: () -> int
        raise NotImplementedError

    def isJsonArray(self):
        # type: () -> bool
        return True

    def isJsonObject(self):
        # type: () -> bool
        return True

    def isJsonPrimitive(self):
        # type: () -> bool
        return True

    def isJsonNull(self):
        # type: () -> bool
        return True


class JsonArray(JsonElement):
    def __init__(self, capacity=None):
        # type: (Optional[int]) -> None
        print(capacity)

    def add(self, arg):
        # type: (Any) -> None
        pass

    def addAll(self, array):
        # type: (JsonArray) -> None
        pass

    def contains(self, element):
        # type: (JsonElement) -> bool
        return True

    def get(self, i):
        # type: (int) -> JsonElement
        pass

    def getAsBigDecimal(self):
        # type: () -> float
        pass

    def getAsBigInteger(self):
        # type: () -> int
        pass

    def getAsBoolean(self):
        # type: () -> bool
        return True

    def getAsByte(self):
        # type: () -> Any
        pass

    def getAsCharacter(self):
        # type: () -> str
        pass

    def getAsDouble(self):
        # type: () -> float
        pass

    def getAsFloat(self):
        # type: () -> float
        pass

    def getAsInt(self):
        # type: () -> int
        pass

    def getAsLong(self):
        # type: () -> long
        pass

    def getAsNumber(self):
        # type: () -> Number
        pass

    def getAsShort(self):
        # type: () -> int
        pass

    def iterator(self):
        # type: () -> Iterable[JsonElement]
        pass

    def remove(self, index):
        # type: (int) -> JsonElement
        pass

    def size(self):
        # type: () -> int
        pass


class JsonNull(JsonElement):
    def equals(self, other):
        # type: (Object) -> bool
        return True

    def getAsBigDecimal(self):
        # type: () -> float
        pass

    def getAsBigInteger(self):
        # type: () -> int
        pass

    def getAsBoolean(self):
        # type: () -> bool
        return True

    def getAsByte(self):
        # type: () -> Any
        pass

    def getAsCharacter(self):
        # type: () -> str
        pass

    def getAsDouble(self):
        # type: () -> float
        pass

    def getAsFloat(self):
        # type: () -> float
        pass

    def getAsInt(self):
        # type: () -> int
        pass

    def getAsLong(self):
        # type: () -> long
        pass

    def getAsNumber(self):
        # type: () -> Number
        pass

    def getAsShort(self):
        # type: () -> int
        pass

    def hashCode(self):
        # type: () -> int
        pass


class JsonObject(JsonElement):
    def add(self, property, value):
        # type: (AnyStr, JsonElement) -> None
        pass

    def addProperty(self, property, value):
        # type: (AnyStr, Any) -> None
        pass

    def createJsonElement(self, value):
        # type: (Object) -> JsonElement
        pass

    def get(self, memberName):
        # type: (AnyStr) -> JsonElement
        pass

    def getAsBigDecimal(self):
        # type: () -> float
        pass

    def getAsBigInteger(self):
        # type: () -> int
        pass

    def getAsBoolean(self):
        # type: () -> bool
        return True

    def getAsByte(self):
        # type: () -> Any
        pass

    def getAsCharacter(self):
        # type: () -> str
        pass

    def getAsDouble(self):
        # type: () -> float
        pass

    def getAsFloat(self):
        # type: () -> float
        pass

    def getAsInt(self):
        # type: () -> int
        pass

    def getAsLong(self):
        # type: () -> long
        pass

    def getAsNumber(self):
        # type: () -> Number
        pass

    def getAsShort(self):
        # type: () -> int
        pass

    def has(self, memberName):
        # type: (AnyStr) -> bool
        return True

    def remove(self, property):
        # type: (AnyStr) -> JsonElement
        pass

    def size(self):
        # type: () -> int
        pass


class JsonPrimitive(JsonElement):
    def __init__(self, arg):
        # type: (Any) -> None
        print(arg)

    def equals(self, other):
        # type: (Object) -> bool
        return True

    def getAsBigDecimal(self):
        # type: () -> float
        pass

    def getAsBigInteger(self):
        # type: () -> int
        pass

    def getAsBoolean(self):
        # type: () -> bool
        return True

    def getAsByte(self):
        # type: () -> Any
        pass

    def getAsCharacter(self):
        # type: () -> str
        pass

    def getAsDouble(self):
        # type: () -> float
        pass

    def getAsFloat(self):
        # type: () -> float
        pass

    def getAsInt(self):
        # type: () -> int
        pass

    def getAsLong(self):
        # type: () -> long
        pass

    def getAsNumber(self):
        # type: () -> Number
        pass

    def getAsShort(self):
        # type: () -> int
        pass

    def hashCode(self):
        # type: () -> int
        pass

    def isBoolean(self):
        # type: () -> bool
        return True

    @staticmethod
    def isPrimitiveOrString(target):
        # type: (Object) -> bool
        return True

    @staticmethod
    def isIntegral(primitive):
        # type: (JsonPrimitive) -> bool
        return True

    def isString(self):
        # type: () -> bool
        return True


class LongSerializationPolicy(object):
    DEFAULT = None  # type: JsonElement
    STRING = None  # type: JsonElement

    def serialize(self, arg):
        # type: (long) -> JsonElement
        raise NotImplementedError


class TypeAdapter(object):
    def fromJson(self, arg):
        # type: (Union[Reader, AnyStr]) -> T
        pass

    def fromJsonTree(self, jsonTree):
        # type: (JsonElement) -> T
        pass

    def nullSafe(self):
        # type: () -> TypeAdapter
        pass

    def read(self, reader):
        # type: (JsonReader) -> T
        raise NotImplementedError

    def toJson(self, out, value):
        # type: (Writer, T) -> Optional[AnyStr]
        pass

    def toJsonTree(self, value):
        # type: (T) -> JsonElement
        pass

    def write(self, *args):
        raise NotImplementedError
