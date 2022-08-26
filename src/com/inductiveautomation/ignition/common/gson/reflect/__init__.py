from typing import Any

from java.lang import Object


class TypeToken(Object):
    @staticmethod
    def get(type):
        # type: (Any) -> TypeToken
        pass

    @staticmethod
    def getArray(componentType):
        # type: (Any) -> TypeToken
        pass

    @staticmethod
    def getParameterized(*args):
        # type: (Any) -> TypeToken
        pass
