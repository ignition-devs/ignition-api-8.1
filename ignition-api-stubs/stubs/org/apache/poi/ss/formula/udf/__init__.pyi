from dev.coatl.helper.types import AnyStr as AnyStr
from org.apache.poi.ss.formula.functions import FreeRefFunction

class UDFFinder:
    def findFunction(self, name: AnyStr) -> FreeRefFunction: ...
