from java.lang import Object, String
from javax.security.auth import Subject


class Principal(object):
    def equals(self, another):
        # type: (Object) -> bool
        raise NotImplementedError

    def getName(self):
        # type: () -> String
        raise NotImplementedError

    def hashCode(self):
        # type: () -> int
        raise NotImplementedError

    def implies(self, subject):
        # type: (Subject) -> bool
        pass

    def toString(self):
        # type: () -> String
        raise NotImplementedError
