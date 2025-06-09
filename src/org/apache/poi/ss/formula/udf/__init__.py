from dev.coatl.helper.types import AnyStr
from org.apache.poi.ss.formula.functions import FreeRefFunction


class UDFFinder(object):
    def findFunction(self, name):
        # type: (AnyStr) -> FreeRefFunction
        raise NotImplementedError
