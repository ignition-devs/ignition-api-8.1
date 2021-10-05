__all__ = ["Request", "RequestWatcher"]


class RequestWatcher(object):
    def block(self):
        raise NotImplementedError

    def compose(self, requestWatchers):
        raise NotImplementedError


class Request(RequestWatcher):
    def block(self):
        pass

    def cancel(self):
        raise NotImplementedError

    def compose(self, requestWatchers):
        pass

    def get(self):
        raise NotImplementedError

    def getError(self):
        raise NotImplementedError

    def onError(self, func):
        raise NotImplementedError

    def onSuccess(self, func):
        raise NotImplementedError
