__all__ = ["TypeBuilder"]

from typing import Any

from dev.thecesrom.helper.types import AnyStr
from java.lang import Class


class TypeBuilder(object):
    def getBase(self):
        # type: () -> Class
        raise NotImplementedError

    def getDict(self, var1):
        # type: (Any) -> Any
        raise NotImplementedError

    def getDoc(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getIsBaseType(self):
        # type: () -> bool
        raise NotImplementedError

    def getName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getTypeClass(self):
        # type: () -> Class
        raise NotImplementedError
