__all__ = ["MessageInterface", "MessageReceiver", "UIResponse"]

from typing import Any, List

from com.inductiveautomation.ignition.common.functional import FragileRunnable
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from java.util import Locale
from java.util.function import Consumer


class MessageInterface(object):
    def addMessageReceiver(self, protocol, rcv):
        # type: (AnyStr, MessageReceiver) -> None
        raise NotImplementedError

    def sendCall(self, protocol, scope, msg):
        # type: (AnyStr, int, Any) -> Any
        raise NotImplementedError

    def sendMessage(self, protocol, scope, msg):
        # type: (AnyStr, int, Any) -> None
        raise NotImplementedError


class MessageReceiver(object):
    def receiveCall(self, msg):
        # type: (Any) -> Any
        raise NotImplementedError


class UIResponse(Object):
    errors = []  # type: List[AnyStr]
    infos = []  # type: List[AnyStr]
    locale = None  # type: Locale
    warns = []  # type: List[AnyStr]

    def __init__(self, locale):
        # type: (Locale) -> None
        super(UIResponse, self).__init__()
        self.locale = locale

    def attempt(self, method):
        # type: (FragileRunnable) -> None
        pass

    def error(self, message, *args):
        # type: (AnyStr, *Object) -> None
        pass

    def getErrors(self):
        # type: () -> List[AnyStr]
        pass

    def getInfos(self):
        # type: () -> List[AnyStr]
        pass

    def getLocale(self):
        # type: () -> Locale
        return self.locale

    def getWarns(self):
        # type: () -> List[AnyStr]
        pass

    def info(self, message, *args):
        # type: (AnyStr, *Object) -> None
        pass

    def warn(self, message, *args):
        # type: (AnyStr, *Object) -> None
        pass

    @staticmethod
    def wrap(locale, fx):
        # type: (Locale, Consumer) -> UIResponse
        pass
