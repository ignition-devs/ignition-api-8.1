__all__ = ["TypeBuilder"]

from typing import Any, Union

from java.lang import Class


class TypeBuilder(object):
    def getBase(self):
        # type: () -> Class
        raise NotImplementedError

    def getDict(self, var1):
        # type: (Any) -> Any
        raise NotImplementedError

    def getDoc(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getIsBaseType(self):
        # type: () -> bool
        raise NotImplementedError

    def getName(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getTypeClass(self):
        # type: () -> Class
        raise NotImplementedError
