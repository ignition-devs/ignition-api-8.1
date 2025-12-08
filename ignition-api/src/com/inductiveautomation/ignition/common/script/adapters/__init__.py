from __future__ import print_function

__all__ = ["PyJsonObjectAdapter"]

from typing import Any, Iterator, List, Optional, Union

from java.lang import Object

from com.inductiveautomation.ignition.common.gson import JsonObject
from org.python.core import PyObject


class PyJsonObjectAdapter(Object):
    def __init__(self, obj):
        # type: (JsonObject) -> None
        super(PyJsonObjectAdapter, self).__init__()
        print(self, obj)

    def __findattr_ex__(self, name):
        # type: (Union[str, unicode]) -> PyObject
        pass

    def __finditem__(self, key):
        # type: (PyObject) -> PyObject
        pass

    def clear(self):
        # type: () -> None
        pass

    def get(self, key, default=None):
        # type: (PyObject, Optional[PyObject]) -> PyObject
        pass

    def has_key(self, key):
        # type: (PyObject) -> bool
        return True

    def items(self):
        # type: () -> List[PyObject]
        pass

    def iteritems(self):
        # type: () -> PyObject
        pass

    def iterkeys(self):
        # type: () -> PyObject
        pass

    def itervalues(self):
        # type: () -> PyObject
        pass

    def keys(self):
        # type: () -> List[PyObject]
        pass

    def pop(self, key):
        # type: (PyObject) -> PyObject
        pass

    def popitem(self):
        # type: () -> PyObject
        pass

    def setdefault(self, key, default):
        # type: (PyObject, PyObject) -> PyObject
        pass

    def update(self, *args, **kwargs):
        # type: (*PyObject, **Union[str, unicode]) -> None
        pass

    def values(self):
        # type: () -> List[PyObject]
        pass

    def __setitem__(self, key, value):
        # type: (PyObject, PyObject) -> None
        pass

    def __delitem__(self, key):
        # type: (PyObject) -> None
        pass

    def __iter__(self):
        # type: () -> Iterator[Any]
        pass

    def __len__(self):
        # type: () -> int
        pass
