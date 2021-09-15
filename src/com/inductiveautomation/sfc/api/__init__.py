__all__ = ["PyChartScope"]

from java.lang import Object


class PyChartScope(Object):
    """This class represents any "scope" in the SFC system, and is
    fundamentally just an observable dictionary.

    Despite its name, it is not limited to chart scope. This class
    notifies listeners when values are changed, and wraps any
    dictionaries assigned to it as PyChartScopes as well.
    """

    def __set__(self, instance, value):
        pass

    def __setattr__(self, key, value):
        pass

    def __setitem__(self, key, value):
        pass
