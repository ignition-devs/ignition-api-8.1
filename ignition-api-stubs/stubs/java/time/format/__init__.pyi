from typing import List

from dev.coatl.helper.types import AnyStr
from java.lang import Appendable, Enum, Object
from java.time.chrono import Chronology
from java.time.temporal import TemporalAccessor

class DateTimeFormatter(Object):
    BASIC_ISO_DATE: DateTimeFormatter
    ISO_DATE: DateTimeFormatter
    ISO_DATE_TIME: DateTimeFormatter
    ISO_INSTANT: DateTimeFormatter
    ISO_LOCAL_DATE: DateTimeFormatter
    ISO_LOCAL_DATE_TIME: DateTimeFormatter
    ISO_LOCAL_TIME: DateTimeFormatter
    ISO_OFFSET_DATE: DateTimeFormatter
    ISO_OFFSET_DATE_TIME: DateTimeFormatter
    ISO_OFFSET_TIME: DateTimeFormatter
    ISO_ORDINAL_DATE: DateTimeFormatter
    ISO_TIME: DateTimeFormatter
    ISO_WEEK_DATE: DateTimeFormatter
    ISO_ZONED_DATE_TIME: DateTimeFormatter
    RFC_1123_DATE_TIME: DateTimeFormatter
    def format(self, temporal: TemporalAccessor) -> AnyStr: ...
    def formatTo(self, temporal: TemporalAccessor, appendable: Appendable) -> None: ...
    def getChronology(self) -> Chronology: ...

class ResolverStyle(Enum):
    LENIENT: ResolverStyle
    SMART: ResolverStyle
    STRICT: ResolverStyle
    @staticmethod
    def values() -> List[ResolverStyle]: ...

class TextStyle(Enum):
    FULL: TextStyle
    FULL_STANDALONE: TextStyle
    NARROW: TextStyle
    NARROW_STANDALONE: TextStyle
    SHORT: TextStyle
    SHORT_STANDALONE: TextStyle
    def asNormal(self) -> TextStyle: ...
    def asStandalone(self) -> TextStyle: ...
    @staticmethod
    def values() -> List[TextStyle]: ...
