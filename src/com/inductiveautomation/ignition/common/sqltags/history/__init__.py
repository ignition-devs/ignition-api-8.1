__all__ = ["Aggregate", "AggregateInfo"]

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
        raise NotImplementedError

    def getId(self):
        raise NotImplementedError

    def getName(self):
        raise NotImplementedError


class AggregateInfo(Object, Aggregate):
    def getDesc(self):
        pass

    def getId(self):
        pass

    def getName(self):
        pass
