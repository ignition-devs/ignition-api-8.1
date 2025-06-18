__all__ = ["DateTimeFormatter", "ResolverStyle", "TextStyle"]

from typing import TYPE_CHECKING, List

from dev.coatl.helper.types import AnyStr
from java.lang import Appendable, Enum, Object

if TYPE_CHECKING:
    from java.time.chrono import Chronology
    from java.time.temporal import TemporalAccessor


class DateTimeFormatter(Object):
    BASIC_ISO_DATE = None  # type: DateTimeFormatter
    ISO_DATE = None  # type: DateTimeFormatter
    ISO_DATE_TIME = None  # type: DateTimeFormatter
    ISO_INSTANT = None  # type: DateTimeFormatter
    ISO_LOCAL_DATE = None  # type: DateTimeFormatter
    ISO_LOCAL_DATE_TIME = None  # type: DateTimeFormatter
    ISO_LOCAL_TIME = None  # type: DateTimeFormatter
    ISO_OFFSET_DATE = None  # type: DateTimeFormatter
    ISO_OFFSET_DATE_TIME = None  # type: DateTimeFormatter
    ISO_OFFSET_TIME = None  # type: DateTimeFormatter
    ISO_ORDINAL_DATE = None  # type: DateTimeFormatter
    ISO_TIME = None  # type: DateTimeFormatter
    ISO_WEEK_DATE = None  # type: DateTimeFormatter
    ISO_ZONED_DATE_TIME = None  # type: DateTimeFormatter
    RFC_1123_DATE_TIME = None  # type: DateTimeFormatter

    def format(self, temporal):
        # type: (TemporalAccessor) -> AnyStr
        pass

    def formatTo(self, temporal, appendable):
        # type: (TemporalAccessor, Appendable) -> None
        pass

    def getChronology(self):
        # type: () -> Chronology
        pass


class ResolverStyle(Enum):
    LENIENT = None  # type: ResolverStyle
    SMART = None  # type: ResolverStyle
    STRICT = None  # type: ResolverStyle

    @staticmethod
    def values():
        # type: () -> List[ResolverStyle]
        pass


class TextStyle(Enum):
    FULL = None  # type: TextStyle
    FULL_STANDALONE = None  # type: TextStyle
    NARROW = None  # type: TextStyle
    NARROW_STANDALONE = None  # type: TextStyle
    SHORT = None  # type: TextStyle
    SHORT_STANDALONE = None  # type: TextStyle

    def asNormal(self):
        # type: () -> TextStyle
        pass

    def asStandalone(self):
        # type: () -> TextStyle
        pass

    @staticmethod
    def values():
        # type: () -> List[TextStyle]
        pass
