__all__ = ["Expression", "FunctionFactory"]

from typing import Any, Iterable, Set, Union

from java.lang import Class

from com.inductiveautomation.ignition.common.binding import InteractionListener
from com.inductiveautomation.ignition.common.expressions.functions import Function
from com.inductiveautomation.ignition.common.model.values import QualifiedValue


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
        # type: () -> Union[str, unicode]
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
        # type: () -> Set[Union[str, unicode]]
        raise NotImplementedError

    def getFunction(self, name):
        # type: (Union[str, unicode]) -> Function
        raise NotImplementedError

    def getFunctionNames(self):
        # type: () -> Set[Union[str, unicode]]
        raise NotImplementedError

    def getFunctionsInCategory(self, name):
        # type: (Union[str, unicode]) -> Set[Union[str, unicode]]
        raise NotImplementedError
