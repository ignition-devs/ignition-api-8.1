from typing import Any

from java.lang import Object

class TypeToken(Object):
    @staticmethod
    def get(type: Any) -> TypeToken: ...
    @staticmethod
    def getArray(componentType: Any) -> TypeToken: ...
    @staticmethod
    def getParameterized(*args: Any) -> TypeToken: ...
