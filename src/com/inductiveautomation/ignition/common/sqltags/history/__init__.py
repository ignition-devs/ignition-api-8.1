from __future__ import print_function

__all__ = ["Aggregate", "AggregateInfo"]

from typing import Any

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object


class Aggregate(object):
    """This interface defines an aggregation function used by the
    history query system.

    Different types of history providers may support different Aggregate
    functions, and may define new types of aggregates. The name and
    description are for informational purposes, aggregates are only
    identified by their id (name and description should not be taken
    into account).

    The general implementation class is AggregateInfo. Common or "well
    known" aggregates are defined in the AggregationMode enum. The
    system works like this for historical reasons, previous to 7.7 only
    the AggregationMode aggregates were used. After, with the
    introduction of history providers as an extension point, new
    providers could define any aggregation function.
    """

    def getDesc(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getId(self):
        # type: () -> int
        raise NotImplementedError

    def getName(self):
        # type: () -> AnyStr
        raise NotImplementedError


class AggregateInfo(Object, Aggregate):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(AggregateInfo, self).__init__()
        print(args)

    def getDesc(self):
        # type: () -> AnyStr
        pass

    def getId(self):
        # type: () -> int
        pass

    def getName(self):
        # type: () -> AnyStr
        pass
