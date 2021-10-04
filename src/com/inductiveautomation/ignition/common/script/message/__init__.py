__all__ = ["Request", "RequestWatcher"]


class Request(object):
    def cancel(self):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    def getError(self):
        raise NotImplementedError

    def onError(self, func):
        raise NotImplementedError

    def onSuccess(self, func):
        raise NotImplementedError


class RequestWatcher(object):
    def block(self):
        raise NotImplementedError

    def compose(self, requestWatchers):
        raise NotImplementedError
