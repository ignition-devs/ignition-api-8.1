from __future__ import print_function, unicode_literals

__all__ = ["PyJsonObjectAdapter"]

from java.lang import Object


class PyJsonObjectAdapter(Object):
    def __init__(self, obj):
        print(self, obj)

    def __delitem__(self, key):
        pass

    def __findattr_ex__(self, name):
        pass

    def __finditem__(self, key):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def __setitem__(self, key, value):
        pass

    def clear(self):
        pass

    def get(self, key, default=None):
        pass

    def has_key(self, key):
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

    def pop(self, key):
        pass

    def popitem(self):
        pass

    def setdefault(self, key, default):
        pass

    def update(self, *args, **kwargs):
        pass

    def values(self):
        pass
