__all__ = ["PyChartScope"]

from org.python.core import PyObject


class PyChartScope(PyObject):
    """This class represents any "scope" in the SFC system, and is
    fundamentally just an observable dictionary.

    Despite its name, it is not limited to chart scope. This class
    notifies listeners when values are changed, and wraps any
    dictionaries assigned to it as PyChartScopes as well.
    """

    def __init__(self):
        # type: () -> None
        super(PyChartScope, self).__init__()
