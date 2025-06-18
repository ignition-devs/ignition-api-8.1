__all__ = ["Function"]

from typing import Any, Iterable

from com.inductiveautomation.ignition.common.binding import InteractionListener
from com.inductiveautomation.ignition.common.model.values import QualifiedValue
from java.lang import Class


class Function(object):
    def connect(self, context, updateListener):
        # type: (Any, InteractionListener) -> None
        raise NotImplementedError

    def copy(self):
        # type: () -> Function
        raise NotImplementedError

    def disconnect(self):
        # type: () -> None
        raise NotImplementedError

    def execute(self, args):
        # type: (Iterable[Any]) -> QualifiedValue
        raise NotImplementedError

    def getArgDocString(self):
        # type: () -> None
        raise NotImplementedError

    def getType(self):
        # type: () -> Class
        pass

    def initArgs(self, args):
        # type: (Iterable[Any]) -> None
        raise NotImplementedError

    def shutdown(self):
        # type: () -> None
        raise NotImplementedError

    def startup(self):
        # type: () -> None
        raise NotImplementedError
