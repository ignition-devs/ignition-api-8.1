__all__ = ["ToStringStyle"]

from typing import Any

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object, StringBuffer


class ToStringStyle(Object):
    DEFAULT_STYLE = None  # type: ToStringStyle
    JSON_STYLE = None  # type: ToStringStyle
    MULTI_LINE_STYLE = None  # type: ToStringStyle
    NO_CLASS_NAME_STYLE = None  # type: ToStringStyle
    NO_FIELD_NAMES_STYLE = None  # type: ToStringStyle
    SHORT_PREFIX_STYLE = None  # type: ToStringStyle
    SIMPLE_STYLE = None  # type: ToStringStyle

    def append(self, buffer, fieldName, *args):
        # type: (StringBuffer, AnyStr, Any) -> None
        pass

    def appendEnd(self, buffer, obj):
        # type: (StringBuffer, Any) -> None
        pass

    def appendStart(self, buffer, obj):
        # type: (StringBuffer, Any) -> None
        pass

    def appendSuper(self, buffer, superToString):
        # type: (StringBuffer, AnyStr) -> None
        pass

    def appendToString(self, buffer, toString):
        # type: (StringBuffer, AnyStr) -> None
        pass
