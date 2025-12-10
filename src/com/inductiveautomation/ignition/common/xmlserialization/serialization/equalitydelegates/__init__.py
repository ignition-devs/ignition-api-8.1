__all__ = ["EqualityDelegate"]

from typing import Any


class EqualityDelegate(object):
    def eq(self, foo, bar):
        # type: (Any, Any) -> bool
        raise NotImplementedError

    def hash(self, foo):
        # type: (Any) -> int
        raise NotImplementedError
