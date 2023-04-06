from __future__ import print_function

__all__ = ["ClassNameResolver", "SerializationException"]

from typing import Any

from dev.thecesrom.helper.types import AnyStr
from java.lang import Class, Exception, Object


class ClassNameResolver(Object):
    def __init__(self):
        # type: () -> None
        super(ClassNameResolver, self).__init__()

    def addAlias(self, clazz, alias):
        # type: (Class, AnyStr) -> None
        pass

    def addDefaults(self):
        # type: () -> None
        pass

    def addSearchPath(self, path):
        # type: (AnyStr) -> None
        pass

    def classForName(self, name):
        # type: (AnyStr) -> Class
        pass

    def createBasic(self):
        # type: () -> ClassNameResolver
        pass

    def getName(self, clazz):
        # type: (Class) -> AnyStr
        pass


class SerializationException(Exception):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(SerializationException, self).__init__()
        print(args)
