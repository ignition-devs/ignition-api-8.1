__all__ = ["Consumer", "Function", "Predicate"]

from typing import TypeVar

from java.lang import Object

R = TypeVar("R")
T = TypeVar("T")


class Consumer(object):
    def accept(self, t):
        # type: (T) -> None
        raise NotImplementedError

    def andThen(self, after):
        # type: (Consumer) -> Consumer
        raise NotImplementedError


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
