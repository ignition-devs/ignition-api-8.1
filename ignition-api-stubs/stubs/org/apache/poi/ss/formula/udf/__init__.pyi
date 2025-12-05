from typing import Union

from org.apache.poi.ss.formula.functions import FreeRefFunction

class UDFFinder:
    def findFunction(self, name: Union[str, unicode]) -> FreeRefFunction: ...
