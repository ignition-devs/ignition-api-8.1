__all__ = ["ScriptFunctionHint"]

from typing import Mapping

from dev.thecesrom.helper.types import AnyStr


class ScriptFunctionHint(object):
    def getAutocompleteText(self):
        # type: () -> AnyStr
        pass

    def getMethodDescription(self):
        # type: () -> AnyStr
        pass

    def getMethodSignature(self):
        # type: () -> AnyStr
        pass

    def getParameterDescriptions(self):
        # type: () -> Mapping[AnyStr, AnyStr]
        pass

    def getReturnValueDescription(self):
        # type: () -> AnyStr
        pass
