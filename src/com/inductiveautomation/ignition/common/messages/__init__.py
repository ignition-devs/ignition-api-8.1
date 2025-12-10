__all__ = ["MessageInterface", "MessageReceiver", "UIResponse"]

from typing import Any, List, Union

from java.lang import Object
from java.util import Locale
from java.util.function import Consumer

from com.inductiveautomation.ignition.common.functional import FragileRunnable


class MessageInterface(object):
    def addMessageReceiver(self, protocol, rcv):
        # type: (Union[str, unicode], MessageReceiver) -> None
        raise NotImplementedError

    def sendCall(self, protocol, scope, msg):
        # type: (Union[str, unicode], int, Any) -> Any
        raise NotImplementedError

    def sendMessage(self, protocol, scope, msg):
        # type: (Union[str, unicode], int, Any) -> None
        raise NotImplementedError


class MessageReceiver(object):
    def receiveCall(self, msg):
        # type: (Any) -> Any
        raise NotImplementedError


class UIResponse(Object):
    errors = []  # type: List[Union[str, unicode]]
    infos = []  # type: List[Union[str, unicode]]
    locale = None  # type: Locale
    warns = []  # type: List[Union[str, unicode]]

    def __init__(self, locale):
        # type: (Locale) -> None
        super(UIResponse, self).__init__()
        self.locale = locale

    def attempt(self, method):
        # type: (FragileRunnable) -> None
        pass

    def error(self, message, *args):
        # type: (Union[str, unicode], *Object) -> None
        pass

    def getErrors(self):
        # type: () -> List[Union[str, unicode]]
        pass

    def getInfos(self):
        # type: () -> List[Union[str, unicode]]
        pass

    def getLocale(self):
        # type: () -> Locale
        return self.locale

    def getWarns(self):
        # type: () -> List[Union[str, unicode]]
        pass

    def info(self, message, *args):
        # type: (Union[str, unicode], *Object) -> None
        pass

    def warn(self, message, *args):
        # type: (Union[str, unicode], *Object) -> None
        pass

    @staticmethod
    def wrap(locale, fx):
        # type: (Locale, Consumer) -> UIResponse
        pass
