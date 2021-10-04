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


class JythonMap(object):
    def __contains__(self, item):
        raise NotImplementedError

    def __finditem__(self, key):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def get(self, *args):
        raise NotImplementedError

    def has_key(self, pyKey):
        raise NotImplementedError

    def items(self):
        pass

    def iteritems(self):
        raise NotImplementedError

    def iterkeys(self):
        raise NotImplementedError

    def itervalues(self):
        raise NotImplementedError

    def keys(self):
        raise NotImplementedError

    def values(self):
        raise NotImplementedError


class JythonSequence(object):
    def __contains__(self, item):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __mul__(self, other):
        pass

    def __repr__(self):
        pass

    def __rmul__(self, other):
        raise NotImplementedError

    def count(self, element):
        raise NotImplementedError

    def index(self, element):
        raise NotImplementedError


class MutableJythonMap(object):
    def __delitem__(self, key):
        raise NotImplementedError

    def __setitem__(self, key, value):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError

    def pop(self, *args):
        raise NotImplementedError

    def popitem(self):
        raise NotImplementedError

    def setdefault(self, *args):
        raise NotImplementedError

    def update(self, *args, **kwargs):
        raise NotImplementedError


class MutableJythonSequence(object):
    def __add__(self, other):
        raise NotImplementedError

    def __imul__(self, other):
        raise NotImplementedError

    def append(self, element):
        raise NotImplementedError

    def extend(self, sequence):
        raise NotImplementedError

    def insert(self, index, element):
        raise NotImplementedError

    def pop(self, *args):
        raise NotImplementedError

    def remove(self, element):
        raise NotImplementedError

    def sort(self, *args, **kwargs):
        raise NotImplementedError


class AbstractJythonMap(JythonMap):
    def __contains__(self, item):
        pass

    def __finditem__(self, key):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def get(self, *args):
        pass

    def has_key(self, pyKey):
        pass

    def items(self):
        pass

    def iteritems(self):
        pass

    def iterkeys(self):
        pass

    def itervalues(self):
        pass

    def keys(self):
        pass

    def values(self):
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
    def __delitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def clear(self):
        pass

    def pop(self, *args):
        pass

    def popitem(self):
        pass

    def setdefault(self, *args):
        pass

    def update(self, *args, **kwargs):
        pass


class AbstractMutableJythonSequence(MutableJythonSequence):
    def __add__(self, other):
        pass

    def __imul__(self, other):
        pass

    def append(self, element):
        pass

    def extend(self, sequence):
        pass

    def insert(self, index, element):
        pass

    def pop(self, *args):
        pass

    def remove(self, element):
        pass

    def sort(self, *args, **kwargs):
        pass
