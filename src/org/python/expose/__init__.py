from typing import Any

from java.lang import Class, String


class TypeBuilder(object):
    def getBase(self):
        # type: () -> Class
        raise NotImplementedError

    def getDict(self, var1):
        # type: (Any) -> Any
        raise NotImplementedError

    def getDoc(self):
        # type: () -> String
        raise NotImplementedError

    def getIsBaseType(self):
        # type: () -> bool
        raise NotImplementedError

    def getName(self):
        # type: () -> String
        raise NotImplementedError

    def getTypeClass(self):
        # type: () -> Class
        raise NotImplementedError
