__all__ = ["Type"]

from typing import Union


class Type(object):
    def getTypeName(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError
