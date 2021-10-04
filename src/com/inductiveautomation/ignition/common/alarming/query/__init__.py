__all__ = ["AlarmQueryResult"]


class AlarmQueryResult(object):
    """This is the result of a query against the alarming system, for
    both status and history.

    It provides the results as a list, but also provides additional
    helper functions for getting the event and associated data as a
    dataset.
    """

    def getAssociatedDate(self, uuid):
        raise NotImplementedError

    def getDataSet(self):
        raise NotImplementedError

    def getEvent(self, uuid):
        raise NotImplementedError
