from __future__ import print_function

__all__ = ["Result", "Results"]

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
        self.continuationPoint = ""
        self.resultQuality = QualityCode.Good
        self.results = []
        self.totalAvailableResults = 0

    @staticmethod
    def error(result):
        return Results(result)

    def getContinuationPoint(self):
        return self.continuationPoint

    def getResultQuality(self):
        return self.resultQuality

    def getResults(self):
        return self.results

    def getReturnedSize(self):
        return 0 if self.results is None else len(self.results)

    def getTotalAvailableSize(self):
        return self.totalAvailableResults

    @staticmethod
    def of(results):
        return Results(results)

    def setContinuationPoint(self, continuationPoint=None):
        self.continuationPoint = continuationPoint

    def setResultQuality(self, value):
        self.resultQuality = value

    def setResults(self, results):
        self.results = results

    def setTotalAvailableResults(self, totalAvailableResults):
        self.totalAvailableResults = totalAvailableResults
