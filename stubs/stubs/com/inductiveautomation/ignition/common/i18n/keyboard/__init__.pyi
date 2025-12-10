from typing import Any, List, Optional, Union

from java.lang import Object

class KeyboardLayout(Object):
    alias: Union[str, unicode]
    id: Any
    labels: Optional[Any]
    name: Union[str, unicode]
    rows: Optional[List[Any]]
    title: Union[str, unicode]
    supportedLanguages: Optional[List[Union[str, unicode]]]
    def __init__(
        self,
        id: Any,
        name: Union[str, unicode],
        title: Union[str, unicode],
        alias: Union[str, unicode],
        rows: Optional[List[Any]] = ...,
        supportedLanguages: Optional[List[Union[str, unicode]]] = ...,
        labels: Optional[Any] = ...,
    ) -> None: ...
    def getAlias(self) -> Union[str, unicode]: ...
    def getId(self) -> Any: ...
    def getLabels(self) -> Optional[Any]: ...
    def getName(self) -> Union[str, unicode]: ...
    def getRows(self) -> Optional[List[Any]]: ...
    def getSupportedLanguages(self) -> Optional[List[Union[str, unicode]]]: ...
