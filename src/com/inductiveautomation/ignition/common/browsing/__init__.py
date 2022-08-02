from __future__ import print_function

__all__ = ["Result", "Results"]

from typing import Any, List, Optional, Sequence

from com.inductiveautomation.ignition.common.model.values import QualityCode
from java.lang import Object, String


class Result(object):
    def getDisplayPath(self):
        raise NotImplementedError

    def getPath(self):
        raise NotImplementedError

    def getType(self):
        raise NotImplementedError

    def hasChildren(self):
        raise NotImplementedError


class Results(Object):
    """The results of a browse operation.

    May only represent a partial result set, which can be determined by
    comparing the Total Available Size to the Returned Size. If there is
    a mismatch, the continuation point should be non-null and can be
    used in constructing the subsequent BrowseFilter to continue the
    browse.
    """

    continuationPoint = None  # type: Optional[String]
    resultQuality = None  # type: QualityCode
    results = None  # type: Sequence[Any]
    totalAvailableResults = None  # type: int

    def __init__(self, *args):
        # type: (Any) -> None
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
        # type: () -> Optional[String]
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
        # type: (Optional[String]) -> None
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
