from __future__ import print_function

from typing import Any, Iterable, Optional, Union

from java.lang import Object, String


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
        # type: () -> Union[float, int, long]
        raise NotImplementedError

    def getAsShort(self):
        # type: () -> int
        raise NotImplementedError

    def isJsonArray(self):
        # type: () -> bool
        pass

    def isJsonObject(self):
        # type: () -> bool
        pass

    def isJsonPrimitive(self):
        # type: () -> bool
        pass

    def isJsonNull(self):
        # type: () -> bool
        pass


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
        pass

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
        pass

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
        # type: () -> Union[float, int, long]
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
        pass

    def getAsBigDecimal(self):
        # type: () -> float
        pass

    def getAsBigInteger(self):
        # type: () -> int
        pass

    def getAsBoolean(self):
        # type: () -> bool
        pass

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
        # type: () -> Union[float, int, long]
        pass

    def getAsShort(self):
        # type: () -> int
        pass

    def hashCode(self):
        # type: () -> int
        pass


class JsonObject(JsonElement):
    def add(self, property, value):
        # type: (String, JsonElement) -> None
        pass

    def addProperty(self, property, value):
        # type: (String, Any) -> None
        pass

    def createJsonElement(self, value):
        # type: (Object) -> JsonElement
        pass

    def get(self, memberName):
        # type: (String) -> JsonElement
        pass

    def getAsBigDecimal(self):
        # type: () -> float
        pass

    def getAsBigInteger(self):
        # type: () -> int
        pass

    def getAsBoolean(self):
        # type: () -> bool
        pass

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
        # type: () -> Union[float, int, long]
        pass

    def getAsShort(self):
        # type: () -> int
        pass

    def has(self, memberName):
        # type: (String) -> bool
        pass

    def remove(self, property):
        # type: (String) -> JsonElement
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
        pass

    def getAsBigDecimal(self):
        # type: () -> float
        pass

    def getAsBigInteger(self):
        # type: () -> int
        pass

    def getAsBoolean(self):
        # type: () -> bool
        pass

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
        # type: () -> Union[float, int, long]
        pass

    def getAsShort(self):
        # type: () -> int
        pass

    def hashCode(self):
        # type: () -> int
        pass

    def isBoolean(self):
        # type: () -> bool
        pass

    @staticmethod
    def isPrimitiveOrString(target):
        # type: (Object) -> bool
        pass

    @staticmethod
    def isIntegral(primitive):
        # type: (JsonPrimitive) -> bool
        pass

    def isString(self):
        # type: () -> bool
        pass
