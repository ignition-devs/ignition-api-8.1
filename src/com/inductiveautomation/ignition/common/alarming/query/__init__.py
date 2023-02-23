__all__ = ["AlarmQueryResult", "AlarmQueryResultImpl"]

from typing import Any, Iterator, List

from com.inductiveautomation.ignition.common import Dataset
from com.inductiveautomation.ignition.common.alarming import AlarmEvent, PyAlarmEvent
from dev.thecesrom.helper.types import AnyStr


class AlarmQueryResult(object):
    """This is the result of a query against the alarming system, for
    both status and history.

    It provides the results as a list, but also provides additional
    helper functions for getting the event and associated data as a
    dataset.
    """

    def getAssociatedDate(self, uuid):
        # type: (AnyStr) -> Dataset
        raise NotImplementedError

    def getDataSet(self):
        # type: () -> Dataset
        raise NotImplementedError

    def getEvent(self, uuid):
        # type: (AnyStr) -> AlarmEvent
        raise NotImplementedError


class AlarmQueryResultImpl(AlarmQueryResult):
    def __init__(self, *args):
        # type: (*Any) -> None
        pass

    def __iter__(self):
        # type: () -> Iterator[PyAlarmEvent]
        yield PyAlarmEvent()

    @staticmethod
    def buildFrom(results):
        # type: (List[AlarmQueryResult]) -> AlarmQueryResult
        pass

    def getAssociatedDate(self, uuid):
        # type: (AnyStr) -> Dataset
        pass

    def getDataSet(self):
        # type: () -> Dataset
        pass

    def getEvent(self, uuid):
        # type: (AnyStr) -> AlarmEvent
        pass
