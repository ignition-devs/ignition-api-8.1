from __future__ import print_function

from typing import Any, Iterator, List, Optional

from java.io import Writer
from java.lang import Number, Object, String


class JSONArray(Object):
    def __init__(self, arg=None):
        # type: (Any) -> None
        print(arg)

    def get(self, index):
        # type: (int) -> Object
        pass

    def getBoolean(self, index):
        # type: (int) -> bool
        pass

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
        # type: (int) -> String
        pass

    def isNull(self, index):
        # type: (int) -> bool
        pass

    def join(self, separator):
        # type: (String) -> String
        pass

    def length(self):
        # type: () -> int
        pass

    def opt(self, index):
        # type: (int) -> Object
        pass

    def optBoolean(self, index, defaultValue=None):
        # type: (int, Optional[bool]) -> bool
        pass

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
        # type: (int, Optional[String]) -> String
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
        # type: (Optional[int]) -> String
        pass

    def write(self, writer):
        # type: (Writer) -> Writer
        pass


class JSONObject(Object):
    NULL = None  # type: Object

    def __init__(self, *args):
        # type: (Any) -> None
        pass

    def accumulate(self, key, value):
        # type: (String, Object) -> JSONObject
        pass

    def append(self, key, value):
        # type: (String, Object) -> JSONObject
        pass

    @staticmethod
    def doubleToString(d):
        # type: (float) -> String
        pass

    def get(self, key):
        # type: (String) -> Object
        pass

    def getBoolean(self, key):
        # type: (String) -> bool
        pass

    def getDouble(self, key):
        # type: (String) -> float
        pass

    def getInt(self, key):
        # type: (String) -> int
        pass

    def getJSONArray(self, key):
        # type: (String) -> JSONArray
        pass

    def getJSONObject(self, key):
        # type: (String) -> JSONObject
        pass

    def getLong(self, key):
        # type: (String) -> long
        pass

    @staticmethod
    def getNames(arg):
        # type: (JSONObject) -> List[String]
        pass

    def getString(self, key):
        # type: (String) -> String
        pass

    def has(self, key):
        # type: (String) -> bool
        pass

    def increment(self, key):
        # type: (String) -> JSONObject
        pass

    def isNull(self, key):
        # type: (String) -> bool
        pass

    def keys(self):
        # type: () -> Iterator[String]
        pass

    def length(self):
        # type: () -> int
        pass

    def names(self):
        # type: () -> JSONArray
        pass

    @staticmethod
    def numberToString(n):
        # type: (Number) -> String
        pass

    def opt(self, key):
        # type: (String) -> Object
        pass

    def optBoolean(self, key, defaultValue=None):
        # type: (String, Optional[bool]) -> bool
        pass

    def optDouble(self, key, defaultValue=None):
        # type: (String, Optional[float]) -> float
        pass

    def optInt(self, key, defaultValue=None):
        # type: (String, Optional[int]) -> int
        pass

    def optJSONArray(self, key):
        # type: (String) -> JSONArray
        pass

    def optJSONObject(self, key):
        # type: (String) -> JSONObject
        pass

    def optLong(self, key, defaultValue=None):
        # type: (String, Optional[long]) -> long
        pass

    def optString(self, key, defaultValue=None):
        # type: (String, Optional[String]) -> String
        pass

    def put(self, key, value):
        # type: (String, Any) -> JSONObject
        pass

    def putOnce(self, key, value):
        # type: (String, Object) -> JSONObject
        pass

    def putOpt(self, key, value):
        # type: (String, Object) -> JSONObject
        pass

    @staticmethod
    def quote(string):
        # type: (String) -> String
        pass

    def remove(self, key):
        # type: (String) -> Object
        pass

    def sortedKeys(self):
        # type: () -> Iterator[String]
        pass

    @staticmethod
    def stringToValue(s):
        # type: (String) -> Object
        pass

    def toJSONArray(self, names):
        # type: (JSONArray) -> JSONArray
        pass

    def toString(self, indentFactor=None):
        # type: (Optional[int]) -> String
        pass

    @staticmethod
    def valueToString(value):
        # type: (Object) -> String
        pass

    @staticmethod
    def wrap(obj):
        # type: (Object) -> Object
        pass

    def write(self, writer):
        # type: (Writer) -> Writer
        pass
