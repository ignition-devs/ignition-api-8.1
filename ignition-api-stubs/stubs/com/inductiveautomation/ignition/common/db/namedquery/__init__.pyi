from typing import Any, Mapping, Optional, Set, Union

from java.lang import Object

class NamedQueryManager:
    def beginTransaction(
        self,
        project: Union[str, unicode],
        datasource: Union[str, unicode],
        isolationLevel: int,
        timeout: long,
    ) -> Union[str, unicode]: ...
    def clearAllCaches(self, project: Union[str, unicode]) -> None: ...
    def clearCache(
        self, project: Union[str, unicode], queryPaths: Set[Union[str, unicode]]
    ) -> None: ...
    def execute(self, *args: Any) -> Object: ...
    def executeSFquery(
        self,
        project: Union[str, unicode],
        path: Union[str, unicode],
        parameters: Mapping[Union[str, unicode], Object],
    ) -> Object: ...
    def getQueryFromPath(
        self, project: Union[str, unicode], queryPath: Union[str, unicode]
    ) -> NamedQuery: ...

class NamedQuery(Object):
    def __init__(self, nq: Optional[NamedQuery] = ...) -> None: ...
