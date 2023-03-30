from __future__ import print_function

__all__ = ["PyComponentWrapper"]

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from org.python.core import PyObject


class PyComponentWrapper(PyObject):
    def __init__(self, component):
        # type: (Object) -> None
        print(component)
        super(PyComponentWrapper, self).__init__()

    def wrapMethod(self, name):
        # type: (AnyStr) -> PyObject
        pass
