from typing import Union

from dev.coatl.helper.types import AnyStr
from java.util import HashMap

class TranslationMap(HashMap):
    def __init__(self, arg: Union[AnyStr, TranslationMap]) -> None: ...
    def getKey(self) -> AnyStr: ...
