__all__ = ["NamedQuery", "NamedQueryManager"]

from typing import Any, Mapping, Optional, Set, Union

from java.lang import Object


class NamedQueryManager(object):
    def beginTransaction(
        self,
        project,  # type: Union[str, unicode]
        datasource,  # type: Union[str, unicode]
        isolationLevel,  # type: int
        timeout,  # type: long
    ):
        # type: (...) -> Union[str, unicode]
        raise NotImplementedError

    def clearAllCaches(self, project):
        # type: (Union[str, unicode]) -> None
        raise NotImplementedError

    def clearCache(self, project, queryPaths):
        # type: (Union[str, unicode], Set[Union[str, unicode]]) -> None
        raise NotImplementedError

    def execute(self, *args):
        # type: (*Any) -> Object
        raise NotImplementedError

    def executeSFquery(
        self,
        project,  # type: Union[str, unicode]
        path,  # type: Union[str, unicode]
        parameters,  # type: Mapping[Union[str, unicode], Object]
    ):
        # type: (...) -> Object
        raise NotImplementedError

    def getQueryFromPath(self, project, queryPath):
        # type: (Union[str, unicode], Union[str, unicode]) -> NamedQuery
        raise NotImplementedError


class NamedQuery(Object):
    def __init__(self, nq=None):
        # type: (Optional[NamedQuery]) -> None
        super(NamedQuery, self).__init__()
        print(nq)
