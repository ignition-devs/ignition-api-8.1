__all__ = ["Request", "RequestWatcher"]

from abc import ABCMeta, abstractmethod


class Request(ABCMeta):
    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def cancel(cls):
        pass

    @abstractmethod
    def get(cls):
        pass

    @abstractmethod
    def getError(cls):
        pass

    @abstractmethod
    def onError(cls, func):
        pass

    @abstractmethod
    def onSuccess(cls, func):
        pass


class RequestWatcher(ABCMeta):
    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def block(cls):
        pass

    @abstractmethod
    def compose(cls, requestWatchers):
        pass
