__all__ = ["Aggregate"]

from abc import ABCMeta, abstractmethod


class Aggregate(ABCMeta):
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

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def getDesc(cls):
        pass

    @abstractmethod
    def getId(cls):
        pass

    @abstractmethod
    def getName(cls):
        pass
