__all__ = ["Type"]

from dev.thecesrom.helper.types import AnyStr


class Type(object):
    def getTypeName(self):
        # type: () -> AnyStr
        raise NotImplementedError
