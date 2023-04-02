from __future__ import print_function

__all__ = ["TranslationMap"]

from typing import Union

from dev.thecesrom.helper.types import AnyStr
from java.util import HashMap


class TranslationMap(HashMap):
    def __init__(self, arg):
        # type: (Union[AnyStr, TranslationMap]) -> None
        super(TranslationMap, self).__init__()
        print(arg)

    def getKey(self):
        # type: () -> AnyStr
        pass
