from __future__ import print_function

__all__ = ["Result", "Results"]

from typing import Optional

from com.inductiveautomation.ignition.common.model.values import QualityCode
from java.lang import Object


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

    def __init__(self, *args):
        print(args)
        self._continuationPoint = ""
        self._resultQuality = QualityCode.Good
        self._results = []
        self._totalAvailableResults = 0

    @staticmethod
    def error(result):
        return Results(result)

    def getContinuationPoint(self):
        return self._continuationPoint

    def getResultQuality(self):
        return self._resultQuality

    def getResults(self):
        return self._results

    def getReturnedSize(self):
        return 0 if self._results is None else len(self._results)

    def getTotalAvailableSize(self):
        return self._totalAvailableResults

    @staticmethod
    def of(results):
        return Results(results)

    def setContinuationPoint(self, continuationPoint=None):
        # type: (Optional[str]) -> None
        self._continuationPoint = continuationPoint

    def setResultQuality(self, value):
        self._resultQuality = value

    def setResults(self, results):
        self._results = results

    def setTotalAvailableResults(self, totalAvailableResults):
        self._totalAvailableResults = totalAvailableResults
