from __future__ import print_function

__all__ = ["AlarmQueryResult", "AlarmQueryResultImpl"]

from typing import Any, Iterator, List, Union

from java.util import ArrayList

from com.inductiveautomation.ignition.common import Dataset
from com.inductiveautomation.ignition.common.alarming import AlarmEvent, PyAlarmEvent


class AlarmQueryResult(object):
    """This is the result of a query against the alarming system, for
    both status and history.

    It provides the results as a list, but also provides additional
    helper functions for getting the event and associated data as a
    dataset.
    """

    def getAssociatedData(self, uuid):
        # type: (Union[str, unicode]) -> Dataset
        raise NotImplementedError

    def getDataset(self):
        # type: () -> Dataset
        raise NotImplementedError

    def getEvent(self, uuid):
        # type: (Union[str, unicode]) -> AlarmEvent
        raise NotImplementedError


class AlarmQueryResultImpl(AlarmQueryResult, ArrayList):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(AlarmQueryResultImpl, self).__init__()
        print(args)

    @staticmethod
    def buildFrom(results):
        # type: (List[AlarmQueryResult]) -> AlarmQueryResult
        pass

    def getAssociatedData(self, uuid):
        # type: (Union[str, unicode]) -> Dataset
        pass

    def getDataset(self):
        # type: () -> Dataset
        pass

    def getEvent(self, uuid):
        # type: (Union[str, unicode]) -> AlarmEvent
        pass

    def __iter__(self):
        # type: () -> Iterator[PyAlarmEvent]
        yield PyAlarmEvent()
