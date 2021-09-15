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

from abc import ABCMeta, abstractmethod


class JythonMap(ABCMeta):
    @abstractmethod
    def __contains__(cls, item):
        pass

    @abstractmethod
    def __finditem__(cls, key):
        pass

    @abstractmethod
    def __iter__(cls):
        pass

    @abstractmethod
    def __len__(cls):
        pass

    @abstractmethod
    def get(cls, *args):
        pass

    @abstractmethod
    def has_key(cls, pyKey):
        pass

    @abstractmethod
    def items(cls):
        pass

    @abstractmethod
    def iteritems(cls):
        pass

    @abstractmethod
    def iterkeys(cls):
        pass

    @abstractmethod
    def itervalues(cls):
        pass

    @abstractmethod
    def keys(cls):
        pass

    @abstractmethod
    def values(cls):
        pass


class JythonSequence(ABCMeta):
    @abstractmethod
    def __contains__(cls, item):
        pass

    @abstractmethod
    def __iter__(cls):
        pass

    @abstractmethod
    def __len__(cls):
        pass

    @abstractmethod
    def __mul__(cls, other):
        pass

    @abstractmethod
    def __repr__(cls):
        pass

    @abstractmethod
    def __rmul__(cls, other):
        pass

    @abstractmethod
    def count(cls, element):
        pass

    @abstractmethod
    def index(cls, element):
        pass


class MutableJythonMap(ABCMeta):
    @abstractmethod
    def __delitem__(cls, key):
        pass

    @abstractmethod
    def __setitem__(cls, key, value):
        pass

    @abstractmethod
    def clear(cls):
        pass

    @abstractmethod
    def pop(cls, *args):
        pass

    @abstractmethod
    def popitem(cls):
        pass

    @abstractmethod
    def setdefault(cls, *args):
        pass

    @abstractmethod
    def update(cls, *args, **kwargs):
        pass


class MutableJythonSequence(ABCMeta):
    @abstractmethod
    def __add__(cls, other):
        pass

    @abstractmethod
    def __imul__(cls, other):
        pass

    @abstractmethod
    def append(cls, element):
        pass

    @abstractmethod
    def extend(cls, sequence):
        pass

    @abstractmethod
    def insert(cls, index, element):
        pass

    @abstractmethod
    def pop(cls, *args):
        pass

    @abstractmethod
    def remove(cls, element):
        pass

    @abstractmethod
    def sort(cls, *args, **kwargs):
        pass


class AbstractJythonMap(JythonMap):
    def __contains__(cls, item):
        pass

    def __finditem__(cls, key):
        pass

    def __iter__(cls):
        pass

    def __len__(cls):
        pass

    def get(cls, *args):
        pass

    def has_key(cls, pyKey):
        pass

    def items(cls):
        pass

    def iteritems(cls):
        pass

    def iterkeys(cls):
        pass

    def itervalues(cls):
        pass

    def keys(cls):
        pass

    def values(cls):
        pass


class AbstractJythonSequence(JythonSequence):
    def __contains__(self, item):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __mul__(self, other):
        pass

    def __repr__(self):
        pass

    def __rmul__(self, other):
        pass

    def count(self, element):
        pass

    def index(self, element):
        pass


class AbstractMutableJythonMap(MutableJythonMap):
    def __delitem__(cls, key):
        pass

    def __setitem__(cls, key, value):
        pass

    def clear(cls):
        pass

    def pop(cls, *args):
        pass

    def popitem(cls):
        pass

    def setdefault(cls, *args):
        pass

    def update(cls, *args, **kwargs):
        pass


class AbstractMutableJythonSequence(MutableJythonSequence):
    def __add__(cls, other):
        pass

    def __imul__(cls, other):
        pass

    def append(cls, element):
        pass

    def extend(cls, sequence):
        pass

    def insert(cls, index, element):
        pass

    def pop(cls, *args):
        pass

    def remove(cls, element):
        pass

    def sort(cls, *args, **kwargs):
        pass
