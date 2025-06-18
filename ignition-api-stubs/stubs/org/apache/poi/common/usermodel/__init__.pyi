from typing import List

from dev.coatl.helper.types import AnyStr as AnyStr
from java.lang import Enum

class Hyperlink:
    def getAddress(self) -> AnyStr: ...
    def getLabel(self) -> AnyStr: ...
    def getType(self) -> HyperlinkType: ...
    def setAddress(self, address: AnyStr) -> None: ...
    def setLabel(self, label: AnyStr) -> None: ...

class HyperlinkType(Enum):
    DOCUMENT: int
    EMAIL: int
    FILE: int
    NONE: int
    URL: int
    @staticmethod
    def values() -> List[HyperlinkType]: ...
