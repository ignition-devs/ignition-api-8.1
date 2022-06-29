__all__ = ["MessageInterface", "MessageReceiver", "UIResponse"]

from java.lang import Object
from java.util import Locale


class MessageInterface(object):
    def addMessageReceiver(self, protocol, rcv):
        raise NotImplementedError

    def sendCall(self, protocol, scope, msg):
        raise NotImplementedError

    def sendMessage(self, protocol, scope, msg):
        raise NotImplementedError


class MessageReceiver(object):
    def receiveCall(self, msg):
        raise NotImplementedError


class UIResponse(Object):
    def __init__(self, locale):
        # type: (Locale) -> None
        self._locale = locale

    def attempt(self, method):
        pass

    def error(self, message, args):
        pass

    def getErrors(self):
        pass

    def getInfos(self):
        pass

    def getLocale(self):
        # type: () -> Locale
        return self._locale

    def getWarns(self):
        pass

    def info(self, message, args):
        pass

    def warn(self, message, args):
        pass

    def wrap(self, locale, fx):
        pass
