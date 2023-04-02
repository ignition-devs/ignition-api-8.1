from __future__ import print_function

__all__ = ["JSONArray", "JSONObject"]

from typing import Any, Iterator, List, Optional

from dev.thecesrom.helper.types import AnyStr
from java.io import Writer
from java.lang import Number, Object


class JSONArray(Object):
    def __init__(self, arg=None):
        # type: (Any) -> None
        super(JSONArray, self).__init__()
        print(arg)

    def get(self, index):
        # type: (int) -> Object
        pass

    def getBoolean(self, index):
        # type: (int) -> bool
        return True

    def getDouble(self, index):
        # type: (int) -> float
        pass

    def getInt(self, index):
        # type: (int) -> int
        pass

    def getJSONArray(self, index):
        # type: (int) -> JSONArray
        pass

    def getJSONObject(self, index):
        # type: (int) -> JSONObject
        pass

    def getLong(self, index):
        # type: (int) -> long
        pass

    def getString(self, index):
        # type: (int) -> AnyStr
        pass

    def isNull(self, index):
        # type: (int) -> bool
        return True

    def join(self, separator):
        # type: (AnyStr) -> AnyStr
        pass

    def length(self):
        # type: () -> int
        pass

    def opt(self, index):
        # type: (int) -> Object
        pass

    def optBoolean(self, index, defaultValue=None):
        # type: (int, Optional[bool]) -> bool
        return True

    def optDouble(self, index, defaultValue=None):
        # type: (int, Optional[float]) -> float
        pass

    def optInt(self, index, defaultValue=None):
        # type: (int, Optional[int]) -> int
        pass

    def optJSONArray(self, index):
        # type: (int) -> JSONArray
        pass

    def optJSONObject(self, index):
        # type: (int) -> JSONObject
        pass

    def optLong(self, index, defaultValue=None):
        # type: (int, Optional[long]) -> long
        pass

    def optString(self, index, defaultValue=None):
        # type: (int, Optional[AnyStr]) -> AnyStr
        pass

    def put(self, index, value):
        # type: (int, Any) -> JSONArray
        pass

    def remove(self, index):
        # type: (int) -> Object
        pass

    def toJSONObject(self, names):
        # type: (JSONArray) -> JSONObject
        pass

    def toString(self, indentFactor=None):
        # type: (Optional[int]) -> AnyStr
        pass

    def write(self, writer):
        # type: (Writer) -> Writer
        pass


class JSONObject(Object):
    NULL = None  # type: Object

    def __init__(self, *args):
        # type: (Any) -> None
        super(JSONObject, self).__init__()
        print(args)

    def accumulate(self, key, value):
        # type: (AnyStr, Object) -> JSONObject
        pass

    def append(self, key, value):
        # type: (AnyStr, Object) -> JSONObject
        pass

    @staticmethod
    def doubleToString(d):
        # type: (float) -> AnyStr
        pass

    def get(self, key):
        # type: (AnyStr) -> Object
        pass

    def getBoolean(self, key):
        # type: (AnyStr) -> bool
        return True

    def getDouble(self, key):
        # type: (AnyStr) -> float
        pass

    def getInt(self, key):
        # type: (AnyStr) -> int
        pass

    def getJSONArray(self, key):
        # type: (AnyStr) -> JSONArray
        pass

    def getJSONObject(self, key):
        # type: (AnyStr) -> JSONObject
        pass

    def getLong(self, key):
        # type: (AnyStr) -> long
        pass

    @staticmethod
    def getNames(arg):
        # type: (JSONObject) -> List[AnyStr]
        pass

    def getString(self, key):
        # type: (AnyStr) -> AnyStr
        pass

    def has(self, key):
        # type: (AnyStr) -> bool
        return True

    def increment(self, key):
        # type: (AnyStr) -> JSONObject
        pass

    def isNull(self, key):
        # type: (AnyStr) -> bool
        return True

    def keys(self):
        # type: () -> Iterator[AnyStr]
        pass

    def length(self):
        # type: () -> int
        pass

    def names(self):
        # type: () -> JSONArray
        pass

    @staticmethod
    def numberToString(n):
        # type: (Number) -> AnyStr
        pass

    def opt(self, key):
        # type: (AnyStr) -> Object
        pass

    def optBoolean(self, key, defaultValue=None):
        # type: (AnyStr, Optional[bool]) -> bool
        return True

    def optDouble(self, key, defaultValue=None):
        # type: (AnyStr, Optional[float]) -> float
        pass

    def optInt(self, key, defaultValue=None):
        # type: (AnyStr, Optional[int]) -> int
        pass

    def optJSONArray(self, key):
        # type: (AnyStr) -> JSONArray
        pass

    def optJSONObject(self, key):
        # type: (AnyStr) -> JSONObject
        pass

    def optLong(self, key, defaultValue=None):
        # type: (AnyStr, Optional[long]) -> long
        pass

    def optString(self, key, defaultValue=None):
        # type: (AnyStr, Optional[AnyStr]) -> AnyStr
        pass

    def put(self, key, value):
        # type: (AnyStr, Any) -> JSONObject
        pass

    def putOnce(self, key, value):
        # type: (AnyStr, Object) -> JSONObject
        pass

    def putOpt(self, key, value):
        # type: (AnyStr, Object) -> JSONObject
        pass

    @staticmethod
    def quote(string):
        # type: (AnyStr) -> AnyStr
        pass

    def remove(self, key):
        # type: (AnyStr) -> Object
        pass

    def sortedKeys(self):
        # type: () -> Iterator[AnyStr]
        pass

    @staticmethod
    def stringToValue(s):
        # type: (AnyStr) -> Object
        pass

    def toJSONArray(self, names):
        # type: (JSONArray) -> JSONArray
        pass

    def toString(self, indentFactor=None):
        # type: (Optional[int]) -> AnyStr
        pass

    @staticmethod
    def valueToString(value):
        # type: (Object) -> AnyStr
        pass

    @staticmethod
    def wrap(obj):
        # type: (Object) -> Object
        pass

    def write(self, writer):
        # type: (Writer) -> Writer
        pass
