from __future__ import print_function

__all__ = [
    "AbstractJythonMap",
    "AbstractJythonSequence",
    "AbstractMutableJythonMap",
    "AbstractMutableJythonSequence",
    "JythonMap",
    "JythonSequence",
    "MutableJythonMap",
    "MutableJythonSequence",
]

from typing import Any, Iterator, Optional, Union

from dev.coatl.helper.types import AnyStr
from java.lang import Class
from org.python.core import PyInteger, PyList, PyObject, PySequence


class JythonMap(object):

    def __finditem__(self, key):
        # type: (Union[int, PyObject, AnyStr]) -> PyObject
        raise NotImplementedError

    def get(self, pyKey, def_=None):
        # type: (PyObject, Optional[PyObject]) -> PyObject
        raise NotImplementedError

    def has_key(self, pyKey):
        # type: (PyObject) -> bool
        raise NotImplementedError

    def items(self):
        # type: () -> PyList
        pass

    def iteritems(self):
        # type: () -> PyObject
        raise NotImplementedError

    def iterkeys(self):
        # type: () -> PyObject
        raise NotImplementedError

    def itervalues(self):
        # type: () -> PyObject
        raise NotImplementedError

    def keys(self):
        # type: () -> PyList
        raise NotImplementedError

    def values(self):
        # type: () -> PyList
        raise NotImplementedError

    def __iter__(self):
        # type: () -> Iterator[Any]
        raise NotImplementedError

    def __contains__(self, pyKey):
        # type: (PyObject) -> bool
        raise NotImplementedError

    def __len__(self):
        # type: () -> int
        raise NotImplementedError


class JythonSequence(object):

    def count(self, element):
        # type: (PyObject) -> PyInteger
        raise NotImplementedError

    def index(self, element):
        # type: (PyObject) -> int
        raise NotImplementedError

    def __iter__(self):
        # type: () -> Iterator[Any]
        raise NotImplementedError

    def __contains__(self, o):
        # type: (PyObject) -> bool
        raise NotImplementedError

    def __len__(self):
        # type: () -> int
        raise NotImplementedError

    def __mul__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rmul__(self, other):
        # type: (PyObject) -> PyObject
        raise NotImplementedError


class MutableJythonMap(object):

    def clear(self):
        # type: () -> None
        raise NotImplementedError

    def pop(self, pyKey, def_=None):
        # type: (PyObject, Optional[PyObject]) -> PyObject
        raise NotImplementedError

    def popitem(self):
        # type: () -> PyObject
        raise NotImplementedError

    def setdefault(self, pyKey, def_=None):
        # type: (PyObject, Optional[PyObject]) -> PyObject
        raise NotImplementedError

    def update(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> None
        raise NotImplementedError

    def __setitem__(self, pyKey, pyValue):
        # type: (PyObject, PyObject) -> None
        raise NotImplementedError

    def __delitem__(self, pyKey):
        # type: (PyObject) -> None
        raise NotImplementedError


class MutableJythonSequence(JythonSequence):

    def append(self, element):
        # type: (PyObject) -> None
        raise NotImplementedError

    def count(self, element):
        # type: (PyObject) -> PyInteger
        raise NotImplementedError

    def extend(self, sequence):
        # type: (PyObject) -> None
        raise NotImplementedError

    def index(self, element):
        # type: (PyObject) -> int
        raise NotImplementedError

    def insert(self, index, element):
        # type: (int, PyObject) -> None
        raise NotImplementedError

    def pop(self, index=None):
        # type: (Optional[int]) -> PyObject
        raise NotImplementedError

    def remove(self, element):
        # type: (PyObject) -> None
        raise NotImplementedError

    def sort(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> None
        raise NotImplementedError

    def __iter__(self):
        # type: () -> Iterator[Any]
        raise NotImplementedError

    def __contains__(self, o):
        # type: (PyObject) -> bool
        raise NotImplementedError

    def __len__(self):
        # type: () -> int
        raise NotImplementedError

    def __add__(self, other):
        # type: (PyObject) -> PyObject
        raise NotImplementedError

    def __mul__(self, other):
        # type: (PyObject) -> PyObject
        pass

    def __rmul__(self, other):
        # type: (PyObject) -> PyObject
        raise NotImplementedError

    def __imul__(self, other):
        # type: (PyObject) -> PyObject
        raise NotImplementedError


class AbstractJythonMap(JythonMap):

    def __finditem__(self, key):
        # type: (Union[int, PyObject, AnyStr]) -> PyObject
        pass

    def get(self, pyKey, def_=None):
        # type: (PyObject, Optional[PyObject]) -> PyObject
        pass

    def has_key(self, pyKey):
        # type: (PyObject) -> bool
        return True

    def items(self):
        # type: () -> PyList
        raise NotImplementedError

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
        # type: () -> PyList
        raise NotImplementedError

    def values(self):
        # type: () -> PyList
        raise NotImplementedError

    def __iter__(self):
        # type: () -> Iterator[Any]
        pass

    def __contains__(self, pyKey):
        # type: (PyObject) -> bool
        return True

    def __len__(self):
        # type: () -> int
        pass


class AbstractJythonSequence(PySequence, JythonSequence):
    def __init__(self, clazz):
        # type: (Class) -> None
        print(clazz)
        super(AbstractJythonSequence, self).__init__()

    def count(self, element):
        # type: (PyObject) -> PyInteger
        pass

    def index(self, element):
        # type: (PyObject) -> int
        pass

    def __len__(self):
        # type: () -> int
        pass

    def __add__(self, other):
        # type: (PyObject) -> PyObject
        raise NotImplementedError

    def __mul__(self, other):
        # type: (PyObject) -> PyObject
        pass


class AbstractMutableJythonMap(MutableJythonMap):

    def clear(self):
        # type: () -> None
        raise NotImplementedError

    def pop(self, pyKey, def_=None):
        # type: (PyObject, Optional[PyObject]) -> PyObject
        pass

    def popitem(self):
        # type: () -> PyObject
        raise NotImplementedError

    def setdefault(self, pyKey, def_=None):
        # type: (PyObject, Optional[PyObject]) -> PyObject
        pass

    def update(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> None
        raise NotImplementedError

    def __setitem__(self, pyKey, value):
        # type: (PyObject, PyObject) -> None
        raise NotImplementedError

    def __delitem__(self, pyKey):
        # type: (PyObject) -> None
        raise NotImplementedError


class AbstractMutableJythonSequence(AbstractJythonSequence, MutableJythonSequence):

    def append(self, element):
        # type: (PyObject) -> None
        raise NotImplementedError

    def extend(self, sequence):
        # type: (PyObject) -> None
        raise NotImplementedError

    def insert(self, index, element):
        # type: (int, PyObject) -> None
        raise NotImplementedError

    def pop(self, index=None):
        # type: (Optional[int]) -> PyObject
        raise NotImplementedError

    def remove(self, element):
        # type: (PyObject) -> None
        raise NotImplementedError

    def sort(self, *args, **kwargs):
        # type: (*PyObject, **AnyStr) -> None
        pass

    def __add__(self, other):
        # type: (PyObject) -> PyObject
        pass
