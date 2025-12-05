from __future__ import print_function

__all__ = ["JSONArray", "JSONObject"]

from typing import Any, Iterator, List, Optional, Union

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
        # type: (int) -> Union[str, unicode]
        pass

    def isNull(self, index):
        # type: (int) -> bool
        return True

    def join(self, separator):
        # type: (Union[str, unicode]) -> Union[str, unicode]
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
        # type: (int, Union[str, unicode, None]) -> Union[str, unicode]
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
        # type: (Optional[int]) -> Union[str, unicode]
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
        # type: (Union[str, unicode], Object) -> JSONObject
        pass

    def append(self, key, value):
        # type: (Union[str, unicode], Object) -> JSONObject
        pass

    @staticmethod
    def doubleToString(d):
        # type: (float) -> Union[str, unicode]
        pass

    def get(self, key):
        # type: (Union[str, unicode]) -> Object
        pass

    def getBoolean(self, key):
        # type: (Union[str, unicode]) -> bool
        return True

    def getDouble(self, key):
        # type: (Union[str, unicode]) -> float
        pass

    def getInt(self, key):
        # type: (Union[str, unicode]) -> int
        pass

    def getJSONArray(self, key):
        # type: (Union[str, unicode]) -> JSONArray
        pass

    def getJSONObject(self, key):
        # type: (Union[str, unicode]) -> JSONObject
        pass

    def getLong(self, key):
        # type: (Union[str, unicode]) -> long
        pass

    @staticmethod
    def getNames(arg):
        # type: (JSONObject) -> List[Union[str, unicode]]
        pass

    def getString(self, key):
        # type: (Union[str, unicode]) -> Union[str, unicode]
        pass

    def has(self, key):
        # type: (Union[str, unicode]) -> bool
        return True

    def increment(self, key):
        # type: (Union[str, unicode]) -> JSONObject
        pass

    def isNull(self, key):
        # type: (Union[str, unicode]) -> bool
        return True

    def keys(self):
        # type: () -> Iterator[Union[str, unicode]]
        pass

    def length(self):
        # type: () -> int
        pass

    def names(self):
        # type: () -> JSONArray
        pass

    @staticmethod
    def numberToString(n):
        # type: (Number) -> Union[str, unicode]
        pass

    def opt(self, key):
        # type: (Union[str, unicode]) -> Object
        pass

    def optBoolean(self, key, defaultValue=None):
        # type: (Union[str, unicode], Optional[bool]) -> bool
        return True

    def optDouble(self, key, defaultValue=None):
        # type: (Union[str, unicode], Optional[float]) -> float
        pass

    def optInt(self, key, defaultValue=None):
        # type: (Union[str, unicode], Optional[int]) -> int
        pass

    def optJSONArray(self, key):
        # type: (Union[str, unicode]) -> JSONArray
        pass

    def optJSONObject(self, key):
        # type: (Union[str, unicode]) -> JSONObject
        pass

    def optLong(self, key, defaultValue=None):
        # type: (Union[str, unicode], Optional[long]) -> long
        pass

    def optString(
        self,
        key,  # type: Union[str, unicode]
        defaultValue=None,  # type: Union[str, unicode, None]
    ):
        # type: (...) -> Union[str, unicode]
        pass

    def put(self, key, value):
        # type: (Union[str, unicode], Any) -> JSONObject
        pass

    def putOnce(self, key, value):
        # type: (Union[str, unicode], Object) -> JSONObject
        pass

    def putOpt(self, key, value):
        # type: (Union[str, unicode], Object) -> JSONObject
        pass

    @staticmethod
    def quote(string):
        # type: (Union[str, unicode]) -> Union[str, unicode]
        pass

    def remove(self, key):
        # type: (Union[str, unicode]) -> Object
        pass

    def sortedKeys(self):
        # type: () -> Iterator[Union[str, unicode]]
        pass

    @staticmethod
    def stringToValue(s):
        # type: (Union[str, unicode]) -> Object
        pass

    def toJSONArray(self, names):
        # type: (JSONArray) -> JSONArray
        pass

    def toString(self, indentFactor=None):
        # type: (Optional[int]) -> Union[str, unicode]
        pass

    @staticmethod
    def valueToString(value):
        # type: (Object) -> Union[str, unicode]
        pass

    @staticmethod
    def wrap(obj):
        # type: (Object) -> Object
        pass

    def write(self, writer):
        # type: (Writer) -> Writer
        pass
