__all__ = ["NamedQuery", "NamedQueryManager"]

from typing import Any, Mapping, Optional, Set

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object


class NamedQueryManager(object):
    def beginTransaction(self, project, datasource, isolationLevel, timeout):
        # type: (AnyStr, AnyStr, int, long) -> AnyStr
        raise NotImplementedError

    def clearAllCaches(self, project):
        # type: (AnyStr) -> None
        raise NotImplementedError

    def clearCache(self, project, queryPaths):
        # type: (AnyStr, Set[AnyStr]) -> None
        raise NotImplementedError

    def execute(self, *args):
        # type: (*Any) -> Object
        raise NotImplementedError

    def executeSFquery(self, project, path, parameters):
        # type: (AnyStr, AnyStr, Mapping[AnyStr, Object]) -> Object
        raise NotImplementedError

    def getQueryFromPath(self, project, queryPath):
        # type: (AnyStr, AnyStr) -> NamedQuery
        raise NotImplementedError


class NamedQuery(Object):
    def __init__(self, nq=None):
        # type: (Optional[NamedQuery]) -> None
        super(NamedQuery, self).__init__()
        print(nq)
