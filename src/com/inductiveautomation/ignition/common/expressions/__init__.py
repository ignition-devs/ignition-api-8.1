__all__ = ["Expression", "FunctionFactory"]

from typing import Any, Iterable, Set

from com.inductiveautomation.ignition.common.binding import InteractionListener
from com.inductiveautomation.ignition.common.expressions.functions import Function
from com.inductiveautomation.ignition.common.model.values import QualifiedValue
from dev.thecesrom.helper.types import AnyStr
from java.lang import Class


class Expression(object):
    def connect(self, context, updateListener):
        # type: (Any, InteractionListener) -> None
        raise NotImplementedError

    def disconnect(self):
        # type: () -> None
        raise NotImplementedError

    def execute(self, args):
        # type: (Iterable[Expression]) -> QualifiedValue
        raise NotImplementedError

    def getChildren(self):
        # type: () -> Iterable[Expression]
        raise NotImplementedError

    def getOpName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getType(self):
        # type: () -> Class
        pass

    def shutdown(self):
        # type: () -> None
        raise NotImplementedError

    def startup(self):
        # type: () -> None
        raise NotImplementedError


class FunctionFactory(object):
    def getCategories(self):
        # type: () -> Set[AnyStr]
        raise NotImplementedError

    def getFunction(self, name):
        # type: (AnyStr) -> Function
        raise NotImplementedError

    def getFunctionNames(self):
        # type: () -> Set[AnyStr]
        raise NotImplementedError

    def getFunctionsInCategory(self, name):
        # type: (AnyStr) -> Set[AnyStr]
        raise NotImplementedError
