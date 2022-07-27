from __future__ import print_function

__all__ = [
    "DimensionMismatchException",
    "MathIllegalArgumentException",
    "MathIllegalNumberException",
]

from typing import Any

from java.lang import IllegalArgumentException, String


class MathIllegalArgumentException(IllegalArgumentException):
    """Base class for all preconditions violation exceptions. In most
    cases, this class should not be instantiated directly: it should
    serve as a base class to create all the exceptions that have the
    semantics of the standard IllegalArgumentException.
    """

    def __init__(self, pattern, *args):
        # type: (String, Any) -> None
        print(pattern, args)
        super(MathIllegalArgumentException, self).__init__()

    def getContext(self):
        pass


class MathIllegalNumberException(MathIllegalArgumentException):
    """Base class for exceptions raised by a wrong number.

    This class is not intended to be instantiated directly: it should
    serve as a base class to create all the exceptions that are raised
    because some precondition is violated by a number argument.
    """

    INTEGER_ZERO = 0

    def getArgument(self):
        pass


class DimensionMismatchException(MathIllegalNumberException):
    """Exception to be thrown when two dimensions differ."""

    def __init__(self, *args):
        # type: (Any) -> None
        super(DimensionMismatchException, self).__init__("", *args)

    def getDimension(self):
        pass
