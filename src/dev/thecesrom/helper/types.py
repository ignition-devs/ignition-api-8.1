"""Types module."""

__all__ = ["AnyNum", "AnyStr"]

from typing import Union

AnyStr = Union[str, unicode]
AnyNum = Union[float, int, long]
