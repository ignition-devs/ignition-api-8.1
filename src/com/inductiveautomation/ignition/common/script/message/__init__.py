__all__ = ["Request", "RequestWatcher"]

from abc import ABCMeta, abstractmethod


class Request(ABCMeta):
    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def cancel(self):
        pass

    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def getError(self):
        pass

    @abstractmethod
    def onError(self, func):
        pass

    @abstractmethod
    def onSuccess(self, func):
        pass


class RequestWatcher(ABCMeta):
    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def block(self):
        pass

    @abstractmethod
    def compose(self, requestWatchers):
        pass
