from typing import Union

from java.lang import Object
from org.python.core import PyObject

class PyComponentWrapper(PyObject):
    def __init__(self, component: Object) -> None: ...
    def wrapMethod(self, name: Union[str, unicode]) -> PyObject: ...
