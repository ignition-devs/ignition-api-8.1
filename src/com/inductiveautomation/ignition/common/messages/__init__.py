__all__ = ["MessageInterface", "MessageReceiver", "UIResponse"]

from abc import ABCMeta, abstractmethod

from java.lang import Object


class MessageInterface(ABCMeta):
    @abstractmethod
    def addMessageReceiver(cls, protocol, rcv):
        pass

    @abstractmethod
    def sendCall(cls, protocol, scope, msg):
        pass

    @abstractmethod
    def sendMessage(cls, protocol, scope, msg):
        pass


class MessageReceiver(ABCMeta):
    @abstractmethod
    def receiveCall(cls, msg):
        pass


class UIResponse(Object):
    def __init__(self, locale):
        self.locale = locale

    def attempt(self, method):
        pass

    def error(self, message, args):
        pass

    def getErrors(self):
        pass

    def getInfos(self):
        pass

    def getLocale(self):
        pass

    def getWarns(self):
        pass

    def info(self, message, args):
        pass

    def warn(self, message, args):
        pass

    def wrap(self, locale, fx):
        pass
