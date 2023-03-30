from __future__ import print_function

__all__ = ["BrowseFilter", "Result", "Results"]

from typing import Any, Iterable, List, Mapping, Optional, Sequence

from com.inductiveautomation.ignition.common import Path, QualifiedPath
from com.inductiveautomation.ignition.common.config import Property, PropertyValueSource
from com.inductiveautomation.ignition.common.model.values import QualityCode
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object


class Result(object):
    def getDisplayPath(self):
        # type: () -> Path
        raise NotImplementedError

    def getPath(self):
        # type: () -> QualifiedPath
        raise NotImplementedError

    def getType(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def hasChildren(self):
        # type: () -> bool
        raise NotImplementedError


class BrowseFilter(Object):
    def addExcludeProperty(self, property, value):
        # type: (Property, Object) -> None
        pass

    def addNameFilter(self, typeId, *filters):
        # type: (AnyStr, *AnyStr) -> BrowseFilter
        pass

    def addProperty(self, property, value):
        # type: (Property, Object) -> None
        pass

    def checkNameFilters(self, path):
        # type: (Any) -> bool
        pass

    def checkProperties(self, toCheck):
        # type: (PropertyValueSource) -> bool
        pass

    def getAllowedTypes(self):
        # type: () -> Iterable[AnyStr]
        pass

    def getContinuationPoint(self):
        # type: () -> AnyStr
        pass

    def getFilterExcludeProperty(self, property):
        # type: (Property) -> BrowseFilter.FilterPropertyValue
        pass

    def getFilterProperty(self, property):
        # type: (Property) -> BrowseFilter.FilterPropertyValue
        pass

    def getMaxResults(self):
        # type: () -> int
        pass

    def getMeta(self):
        # type: () -> BrowseFilter.Meta
        pass

    def getNameFilters(self):
        # type: () -> Iterable[BrowseFilter.NameFilter]
        pass

    def getNameFiltersAsMap(self):
        # type: () -> Mapping[AnyStr, BrowseFilter.NameFilter]
        pass

    def getOffset(self):
        # type: () -> int
        pass

    def isEmptyFilter(self):
        # type: () -> bool
        pass

    def isRecursive(self):
        # type: () -> bool
        pass

    def setAllowedTypes(self, allowedTypes):
        # type: (Iterable[AnyStr]) -> BrowseFilter
        pass

    def setContinuationPoint(self, continuationPoint):
        # type: (AnyStr) -> BrowseFilter
        pass

    def setMaxResults(self, maxResults):
        # type: (int) -> BrowseFilter
        pass

    def setMeta(self, meta):
        # type: (BrowseFilter.Meta) -> None
        pass

    def setNameFilters(self, filters):
        # type: (Iterable[BrowseFilter.NameFilter]) -> BrowseFilter
        pass

    def setOffset(self, offset):
        # type: (int) -> BrowseFilter
        pass

    def setRecursive(self, recursive):
        # type: (bool) -> BrowseFilter
        pass

    class FilterPropertyValue(Object):
        property = None  # type: Property
        value = None  # type: Object

        def __init__(self, property, value):
            # type: (Property, Object) -> None
            super(BrowseFilter.FilterPropertyValue, self).__init__()
            self.property = property
            self.value = value

    class Meta(Object):
        addFolderOverrides = None  # type: bool

        def __init__(self, addFolderOverrides):
            # type: (bool) -> None
            super(BrowseFilter.Meta, self).__init__()
            self.addFolderOverrides = addFolderOverrides

    class NameFilter(Object):
        def __init__(self, typeId, *filters):
            # type: (AnyStr, *AnyStr) -> None
            super(BrowseFilter.NameFilter, self).__init__()
            self._typeId = typeId
            self._filters = filters

        def getFilters(self):
            # type: () -> Iterable[AnyStr]
            return self._filters

        def getTypeId(self):
            # type: () -> AnyStr
            return self._typeId

        def passes(self, value):
            # type: (AnyStr) -> bool
            pass


class Results(Object):
    """The results of a browse operation.

    May only represent a partial result set, which can be determined by
    comparing the Total Available Size to the Returned Size. If there is
    a mismatch, the continuation point should be non-null and can be
    used in constructing the subsequent BrowseFilter to continue the
    browse.
    """

    continuationPoint = None  # type: Optional[AnyStr]
    resultQuality = None  # type: QualityCode
    results = None  # type: Sequence[Any]
    totalAvailableResults = None  # type: int

    def __init__(self, *args):
        # type: (*Any) -> None
        super(Results, self).__init__()
        print(args)
        self.continuationPoint = None
        self.resultQuality = QualityCode.Good
        self.results = []
        self.totalAvailableResults = 0

    @staticmethod
    def error(result):
        # type: (Results) -> Results
        return Results(result)

    def getContinuationPoint(self):
        # type: () -> Optional[AnyStr]
        return self.continuationPoint

    def getResultQuality(self):
        # type: () -> QualityCode
        return self.resultQuality

    def getResults(self):
        # type: () -> Sequence[Any]
        return self.results

    def getReturnedSize(self):
        # type: () -> int
        return 0 if self.results is None else len(self.results)

    def getTotalAvailableSize(self):
        # type: () -> int
        return self.totalAvailableResults

    @staticmethod
    def of(results):
        # type: (List[Any]) -> Results
        return Results(results)

    def setContinuationPoint(self, continuationPoint=None):
        # type: (Optional[AnyStr]) -> None
        self.continuationPoint = continuationPoint

    def setResultQuality(self, value):
        # type: (QualityCode) -> None
        self.resultQuality = value

    def setResults(self, results):
        # type: (List[Any]) -> None
        self.results = results

    def setTotalAvailableResults(self, totalAvailableResults):
        # type: (int) -> None
        self.totalAvailableResults = totalAvailableResults
