__all__ = [
    "BiPredicate",
    "Consumer",
    "Function",
    "Predicate",
    "ToDoubleFunction",
    "ToIntFunction",
    "ToLongFunction",
]

from typing import TypeVar

from java.lang import Object

R = TypeVar("R")
T = TypeVar("T")
U = TypeVar("U")


class BiPredicate(object):
    def negate(self):
        # type: () -> BiPredicate
        pass

    def test(self, t, u):
        # type: (T, U) -> bool
        pass


class Consumer(object):
    def accept(self, t):
        # type: (T) -> None
        raise NotImplementedError

    def andThen(self, after):
        # type: (Consumer) -> Consumer
        pass


class Function(object):
    def andThen(self, after):
        # type: (Function) -> Function
        pass

    def apply(self, t):
        # type: (T) -> R
        raise NotImplementedError

    def compose(self, before):
        # type: (Function) -> Function
        pass

    @staticmethod
    def identity():
        # type: () -> Function
        pass


class Predicate(object):
    @staticmethod
    def isEqual(targetRef):
        # type: (Object) -> Predicate
        pass

    def negate(self):
        # type: () -> Predicate
        pass

    def test(self, t):
        # type: (T) -> bool
        raise NotImplementedError


class ToDoubleFunction(object):
    def applyAsDouble(self, value):
        # type: (T) -> object
        raise NotImplementedError


class ToIntFunction(object):
    def applyAsInt(self, value):
        # type: (T) -> object
        raise NotImplementedError


class ToLongFunction(object):
    def applyAsLong(self, value):
        # type: (T) -> object
        raise NotImplementedError
