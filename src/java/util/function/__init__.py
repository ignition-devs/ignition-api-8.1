__all__ = [
    "BiConsumer",
    "BiFunction",
    "BiPredicate",
    "BinaryOperator",
    "Consumer",
    "Function",
    "Predicate",
    "Supplier",
    "ToDoubleFunction",
    "ToIntFunction",
    "ToLongFunction",
]

from typing import Any

from java.lang import Object


class BiConsumer(object):
    def accept(self, t, u):
        # type: (Any, Any) -> None
        raise NotImplementedError

    def andThen(self, after):
        # type: (BiConsumer) -> BiConsumer
        pass


class BiFunction(object):
    def andThen(self, after):
        # type: (Function) -> BiFunction
        pass

    def apply(self, t, u):
        # type: (Any, Any) -> Any
        raise NotImplementedError


class BiPredicate(object):
    def negate(self):
        # type: () -> BiPredicate
        pass

    def test(self, t, u):
        # type: (Any, Any) -> bool
        return True


class BinaryOperator(BiFunction):
    def apply(self, t, u):
        # type: (Any, Any) -> Any
        raise NotImplementedError

    @staticmethod
    def maxBy(comparator):
        # type: (Any) -> BinaryOperator
        pass

    @staticmethod
    def minBy(comparator):
        # type: (Any) -> BinaryOperator
        pass


class Consumer(object):
    def accept(self, t):
        # type: (Any) -> None
        raise NotImplementedError

    def andThen(self, after):
        # type: (Consumer) -> Consumer
        pass


class Function(object):
    def andThen(self, after):
        # type: (Function) -> Function
        pass

    def apply(self, t):
        # type: (Any) -> Any
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
        # type: (Any) -> bool
        raise NotImplementedError


class Supplier(object):
    def get(self):
        # type: () -> Any
        raise NotImplementedError


class ToDoubleFunction(object):
    def applyAsDouble(self, value):
        # type: (Any) -> object
        raise NotImplementedError


class ToIntFunction(object):
    def applyAsInt(self, value):
        # type: (Any) -> object
        raise NotImplementedError


class ToLongFunction(object):
    def applyAsLong(self, value):
        # type: (Any) -> object
        raise NotImplementedError
