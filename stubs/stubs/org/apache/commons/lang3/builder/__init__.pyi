from typing import Any, Union

from java.lang import Object, StringBuffer

class ToStringStyle(Object):
    DEFAULT_STYLE: ToStringStyle
    JSON_STYLE: ToStringStyle
    MULTI_LINE_STYLE: ToStringStyle
    NO_CLASS_NAME_STYLE: ToStringStyle
    NO_FIELD_NAMES_STYLE: ToStringStyle
    SHORT_PREFIX_STYLE: ToStringStyle
    SIMPLE_STYLE: ToStringStyle
    def append(
        self, buffer: StringBuffer, fieldName: Union[str, unicode], *args: Any
    ) -> None: ...
    def appendEnd(self, buffer: StringBuffer, obj: Any) -> None: ...
    def appendStart(self, buffer: StringBuffer, obj: Any) -> None: ...
    def appendSuper(
        self, buffer: StringBuffer, superToString: Union[str, unicode]
    ) -> None: ...
    def appendToString(
        self, buffer: StringBuffer, toString: Union[str, unicode]
    ) -> None: ...
