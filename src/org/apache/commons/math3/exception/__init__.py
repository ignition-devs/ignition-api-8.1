from __future__ import print_function

__all__ = [
    "DimensionMismatchException",
    "MathIllegalArgumentException",
    "MathIllegalNumberException",
]

from typing import Any

from java.lang import IllegalArgumentException, Number
from org.apache.commons.math3.exception.util import ExceptionContext


class MathIllegalArgumentException(IllegalArgumentException):
    """Base class for all preconditions violation exceptions. In most
    cases, this class should not be instantiated directly: it should
    serve as a base class to create all the exceptions that have the
    semantics of the standard IllegalArgumentException.
    """

    def __init__(self, *args):
        # type: (*Any) -> None
        print(args)
        super(MathIllegalArgumentException, self).__init__()

    def getContext(self):
        # type: () -> ExceptionContext
        pass


class MathIllegalNumberException(MathIllegalArgumentException):
    """Base class for exceptions raised by a wrong number.

    This class is not intended to be instantiated directly: it should
    serve as a base class to create all the exceptions that are raised
    because some precondition is violated by a number argument.
    """

    INTEGER_ZERO = 0

    def getArgument(self):
        # type: () -> Number
        pass


class DimensionMismatchException(MathIllegalNumberException):
    """Exception to be thrown when two dimensions differ."""

    def __init__(self, *args):
        # type: (*Any) -> None
        super(DimensionMismatchException, self).__init__(*args)

    def getDimension(self):
        # type: () -> int
        pass
