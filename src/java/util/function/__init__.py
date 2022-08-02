__all__ = ["Consumer"]

from typing import TypeVar

T = TypeVar("T")


class Consumer(object):
    def accept(self, t):
        # type: (T) -> None
        raise NotImplementedError

    def andThen(self, after):
        # type: (Consumer) -> Consumer
        raise NotImplementedError
