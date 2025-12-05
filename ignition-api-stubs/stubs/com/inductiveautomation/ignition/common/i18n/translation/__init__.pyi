from typing import Union

from java.util import HashMap

class TranslationMap(HashMap):
    def __init__(self, arg: Union[str, unicode, TranslationMap]) -> None: ...
    def getKey(self) -> Union[str, unicode]: ...
