__all__ = ["AlarmQueryResult", "AlarmQueryResultImpl"]


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


class AlarmQueryResultImpl(AlarmQueryResult):
    def __init__(self, *args):
        pass

    def getAssociatedDate(self, uuid):
        pass

    def getDataSet(self):
        pass

    def getEvent(self, uuid):
        pass
