from typing import Any, List, Optional

from dev.coatl.helper.types import AnyStr as AnyStr
from java.lang import Object

class KeyboardLayout(Object):
    alias: AnyStr
    id: Any
    labels: Optional[Any]
    name: AnyStr
    rows: Optional[List[Any]]
    title: AnyStr
    supportedLanguages: Optional[List[AnyStr]]
    def __init__(
        self,
        id: Any,
        name: AnyStr,
        title: AnyStr,
        alias: AnyStr,
        rows: Optional[List[Any]] = ...,
        supportedLanguages: Optional[List[AnyStr]] = ...,
        labels: Optional[Any] = ...,
    ) -> None: ...
    def getAlias(self) -> AnyStr: ...
    def getId(self) -> Any: ...
    def getLabels(self) -> Optional[Any]: ...
    def getName(self) -> AnyStr: ...
    def getRows(self) -> Optional[List[Any]]: ...
    def getSupportedLanguages(self) -> Optional[List[AnyStr]]: ...
