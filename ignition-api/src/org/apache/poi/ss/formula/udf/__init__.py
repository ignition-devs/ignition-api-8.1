from typing import Union

from org.apache.poi.ss.formula.functions import FreeRefFunction


class UDFFinder(object):
    def findFunction(self, name):
        # type: (Union[str, unicode]) -> FreeRefFunction
        raise NotImplementedError
