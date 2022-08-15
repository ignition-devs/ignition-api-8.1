from __future__ import print_function

__all__ = ["PyJsonObjectAdapter"]

from typing import List, Optional

from com.inductiveautomation.ignition.common.gson import JsonObject
from java.lang import Object, String
from org.python.core import PyObject


class PyJsonObjectAdapter(Object):
    def __init__(self, obj):
        # type: (JsonObject) -> None
        print(self, obj)

    def __delitem__(self, key):
        # type: (PyObject) -> None
        pass

    def __findattr_ex__(self, name):
        # type: (String) -> PyObject
        pass

    def __finditem__(self, key):
        # type: (PyObject) -> PyObject
        pass

    def __iter__(self):
        # type: () -> PyObject
        pass

    def __len__(self):
        # type: () -> int
        pass

    def __setitem__(self, key, value):
        # type: (PyObject, PyObject) -> None
        pass

    def clear(self):
        # type: () -> None
        pass

    def get(self, key, default=None):
        # type: (PyObject, Optional[PyObject]) -> PyObject
        pass

    def has_key(self, key):
        # type: (PyObject) -> bool
        pass

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
        # type: (PyObject, String) -> None
        pass

    def values(self):
        # type: () -> List[PyObject]
        pass
