__all__ = ["Principal"]

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from javax.security.auth import Subject


class Principal(object):
    def equals(self, another):
        # type: (Object) -> bool
        raise NotImplementedError

    def getName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def hashCode(self):
        # type: () -> int
        raise NotImplementedError

    def implies(self, subject):
        # type: (Subject) -> bool
        return True

    def toString(self):
        # type: () -> AnyStr
        raise NotImplementedError
