from __future__ import print_function

__all__ = ["ClassNameResolver", "SerializationException"]

from typing import Any

import java.lang
from dev.thecesrom.helper.types import AnyStr


class ClassNameResolver(java.lang.Object):
    def __init__(self):
        # type: () -> None
        super(ClassNameResolver, self).__init__()

    def addAlias(self, clazz, alias):
        # type: (java.lang.Class, AnyStr) -> None
        pass

    def addDefaults(self):
        # type: () -> None
        pass

    def addSearchPath(self, path):
        # type: (AnyStr) -> None
        pass

    def classForName(self, name):
        # type: (AnyStr) -> java.lang.Class
        pass

    def createBasic(self):
        # type: () -> ClassNameResolver
        pass

    def getName(self, clazz):
        # type: (java.lang.Class) -> AnyStr
        pass


class SerializationException(java.lang.Exception):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(SerializationException, self).__init__()
        print(args)
