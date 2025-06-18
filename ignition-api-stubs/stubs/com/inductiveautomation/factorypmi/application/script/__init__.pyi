from dev.coatl.helper.types import AnyStr
from java.lang import Object
from org.python.core import PyObject

class PyComponentWrapper(PyObject):
    def __init__(self, component: Object) -> None: ...
    def wrapMethod(self, name: AnyStr) -> PyObject: ...
