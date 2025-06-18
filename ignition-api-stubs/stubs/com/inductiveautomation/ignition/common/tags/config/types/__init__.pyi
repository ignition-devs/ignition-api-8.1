from typing import Iterable

from dev.coatl.helper.types import AnyStr
from java.lang import Enum

class TagObjectType(Enum):
    @staticmethod
    def fromString(value: AnyStr) -> TagObjectType: ...
    def isComplexTag(self) -> bool: ...
    @staticmethod
    def values() -> Iterable[TagObjectType]: ...
