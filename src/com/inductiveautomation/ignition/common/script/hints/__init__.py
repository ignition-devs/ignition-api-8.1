__all__ = ["ScriptFunctionHint"]

from typing import Mapping, Union


class ScriptFunctionHint(object):
    def getAutocompleteText(self):
        # type: () -> Union[str, unicode]
        pass

    def getMethodDescription(self):
        # type: () -> Union[str, unicode]
        pass

    def getMethodSignature(self):
        # type: () -> Union[str, unicode]
        pass

    def getParameterDescriptions(self):
        # type: () -> Mapping[Union[str, unicode], Union[str, unicode]]
        pass

    def getReturnValueDescription(self):
        # type: () -> Union[str, unicode]
        pass
