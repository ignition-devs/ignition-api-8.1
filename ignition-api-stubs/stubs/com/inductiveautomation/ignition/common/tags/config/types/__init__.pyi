from typing import Iterable, Union

from java.lang import Enum

class TagObjectType(Enum):
    @staticmethod
    def fromString(value: Union[str, unicode]) -> TagObjectType: ...
    def isComplexTag(self) -> bool: ...
    @staticmethod
    def values() -> Iterable[TagObjectType]: ...
