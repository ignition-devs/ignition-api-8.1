"""Contains the base BSON classes."""

from __future__ import print_function

__all__ = ["BSONObject", "BsonDocument", "BsonValue", "Document"]

from typing import TYPE_CHECKING, Any, Set, Union

from java.lang import Class, Object
from java.util import Collection, Date, Map

from org.bson.codecs.configuration import CodecRegistry

if TYPE_CHECKING:
    from org.bson.types import ObjectId


class BSONObject(object):
    def containsField(self, s):
        # type: (Union[str, unicode]) -> bool
        raise NotImplementedError

    def get(self, key):
        # type: (Union[str, unicode]) -> Object
        raise NotImplementedError

    def keySet(self):
        # type: () -> Set[Union[str, unicode]]
        raise NotImplementedError

    def put(self, k, v):
        # type: (Union[str, unicode], Object) -> Object
        raise NotImplementedError

    def putAll(self, arg):
        # type: (Union[BSONObject, Map]) -> None
        raise NotImplementedError

    def removeField(self, key):
        # type: (Union[str, unicode]) -> Object
        raise NotImplementedError

    def toMap(self):
        # type: () -> Map
        raise NotImplementedError


class BsonValue(Object):
    def __init__(self):
        # type: () -> None
        super(BsonValue, self).__init__()


class BsonDocument(BsonValue):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(BsonDocument, self).__init__()
        print(args)


class Document(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Document, self).__init__()
        print(args)

    def append(self, key, value):
        # type: (Union[str, unicode], Object) -> Document
        pass

    def clear(self):
        # type: () -> None
        pass

    def containsKey(self, key):
        # type: (Object) -> bool
        return True

    def containsValue(self, value):
        # type: (Object) -> bool
        return True

    def entrySet(self):
        # type: () -> Set[Any]
        pass

    def get(self, *args):
        # type: (*Any) -> Any
        pass

    def getBoolean(self, *args):
        # type: (*Any) -> bool
        return True

    def getDate(self, key):
        # type: (Object) -> Date
        pass

    def getDouble(self, key):
        # type: (Object) -> float
        pass

    def getInteger(self, key):
        # type: (Object) -> int
        pass

    def getLong(self, key):
        # type: (Object) -> long
        pass

    def getObjectId(self, key):
        # type: (Object) -> ObjectId
        pass

    def getString(self, key):
        # type: (Object) -> Union[str, unicode]
        pass

    def isEmpty(self):
        # type: () -> bool
        return True

    def keySet(self):
        # type: () -> Set[Union[str, unicode]]
        pass

    @staticmethod
    def parse(*args):
        # type: (*Any) -> Document
        pass

    def put(self, key, value):
        # type: (Union[str, unicode], Object) -> Object
        pass

    def putAll(self, map):
        # type: (Map) -> None
        pass

    def remove(self, key):
        # type: (Object) -> Object
        pass

    def size(self):
        # type: () -> int
        pass

    def toBsonDocument(self, documentClass, codecRegistry):
        # type: (Class, CodecRegistry) -> BsonDocument
        pass

    def toJson(self, *args):
        # type: (*Any) -> Union[str, unicode]
        pass

    def values(self):
        # type: () -> Collection
        pass
