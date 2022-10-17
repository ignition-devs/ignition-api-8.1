from __future__ import print_function

__all__ = ["PyComponentWrapper"]

from java.lang import String
from org.python.core import PyObject


class PyComponentWrapper(PyObject):
    def __init__(self, component):
        print(component)
        super(PyComponentWrapper, self).__init__()

    def wrapMethod(self, name):
        # type: (String) -> PyObject
        pass
