__all__ = ["AlarmQueryResult"]

from abc import ABCMeta, abstractmethod


class AlarmQueryResult(ABCMeta):
    """This is the result of a query against the alarming system, for
    both status and history.

    It provides the results as a list, but also provides additional
    helper functions for getting the event and associated data as a
    dataset.
    """

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def getAssociatedDate(cls, uuid):
        pass

    @abstractmethod
    def getDataSet(cls):
        pass

    @abstractmethod
    def getEvent(cls, uuid):
        pass
