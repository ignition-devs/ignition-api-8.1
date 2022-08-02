__all__ = ["MessageInterface", "MessageReceiver", "UIResponse"]

from typing import List

from com.inductiveautomation.ignition.common.functional import FragileRunnable
from java.lang import Object, String
from java.util import Locale
from java.util.function import Consumer


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
    errors = []  # type: List[String]
    infos = []  # type: List[String]
    locale = None  # type: Locale
    warns = []  # type: List[String]

    def __init__(self, locale):
        # type: (Locale) -> None
        self.locale = locale

    def attempt(self, method):
        # type: (FragileRunnable) -> None
        pass

    def error(self, message, *args):
        # type: (String, Object) -> None
        pass

    def getErrors(self):
        # type: () -> List[String]
        pass

    def getInfos(self):
        # type: () -> List[String]
        pass

    def getLocale(self):
        # type: () -> Locale
        return self.locale

    def getWarns(self):
        # type: () -> List[String]
        pass

    def info(self, message, *args):
        # type: (String, Object) -> None
        pass

    def warn(self, message, *args):
        # type: (String, Object) -> None
        pass

    @staticmethod
    def wrap(locale, fx):
        # type: (Locale, Consumer) -> UIResponse
        pass
