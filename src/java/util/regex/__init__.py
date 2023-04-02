__all__ = ["MatchResult", "Matcher", "Pattern"]

from typing import Any, List, Optional, Union

from dev.thecesrom.helper.types import AnyStr
from java.lang import CharSequence, Object, StringBuffer, StringBuilder
from java.util.function import Function, Predicate


class MatchResult(object):
    def end(self, group=None):
        # type: (Optional[int]) -> int
        raise NotImplementedError

    def group(self, group=None):
        # type: (Optional[int]) -> AnyStr
        raise NotImplementedError

    def groupCount(self):
        # type: () -> int
        raise NotImplementedError

    def start(self, group=None):
        # type: (Optional[int]) -> int
        raise NotImplementedError


class Matcher(Object, MatchResult):
    def appendReplacement(self, sb, replacement):
        # type: (Union[StringBuffer, StringBuilder], AnyStr) -> Matcher
        pass

    def appendTail(
        self,
        sb,  # type: Union[StringBuffer, StringBuilder]
    ):
        # type: (...) -> Union[StringBuffer, StringBuilder]
        pass

    def end(self, group=None):
        # type: (Optional[int]) -> int
        pass

    def find(self, start=None):
        # type: (Optional[int]) -> bool
        return True

    def group(self, group=None):
        # type: (Optional[Union[int, AnyStr]]) -> AnyStr
        pass

    def groupCount(self):
        # type: () -> int
        pass

    def hasAnchoringBounds(self):
        # type: () -> bool
        return True

    def hasTransparentBounds(self):
        # type: () -> bool
        return True

    def hitEnd(self):
        # type: () -> bool
        return True

    def lookingAt(self):
        # type: () -> bool
        return True

    def matches(self):
        # type: () -> bool
        return True

    def pattern(self):
        # type: () -> Pattern
        pass

    @staticmethod
    def quoteReplacement(s):
        # type: (AnyStr) -> AnyStr
        pass

    def region(self, start, end):
        # type: (int, int) -> Matcher
        pass

    def regionEnd(self):
        # type: () -> int
        pass

    def regionStart(self):
        # type: () -> int
        pass

    def replaceAll(self, arg):
        # type: (Union[Function, AnyStr]) -> AnyStr
        pass

    def replaceFirst(self, arg):
        # type: (Union[Function, AnyStr]) -> AnyStr
        pass

    def requireEnd(self):
        # type: () -> bool
        return True

    def reset(self, input=None):
        # type: (Optional[CharSequence]) -> Matcher
        pass

    def results(self):
        # type: () -> Any
        pass

    def start(self, group=None):
        # type: (Optional[int]) -> int
        pass

    def toMatchResult(self):
        # type: () -> MatchResult
        pass

    def useAnchoringBounds(self, b):
        # type: (bool) -> Matcher
        pass

    def usePattern(self, newPattern):
        # type: (Pattern) -> Matcher
        pass

    def useTransparentBounds(self, b):
        # type: (bool) -> Matcher
        pass


class Pattern(Object):
    CANON_EQ = None  # type: int
    CASE_INSENSITIVE = None  # type: int
    COMMENTS = None  # type: int
    DOTALL = None  # type: int
    LITERAL = None  # type: int
    MULTILINE = None  # type: int
    UNICODE_CASE = None  # type: int
    UNICODE_CHARACTER_CLASS = None  # type: int
    UNIX_LINES = None  # type: int

    def asMatchPredicate(self):
        # type: () -> Predicate
        pass

    def asPredicate(self):
        # type: () -> Predicate
        pass

    @staticmethod
    def compile(regex, flags=None):
        # type: (AnyStr, Optional[int]) -> Pattern
        pass

    def flags(self):
        # type: () -> int
        pass

    def matcher(self, input):
        # type: (CharSequence) -> Matcher
        pass

    @staticmethod
    def matches(regex, input):
        # type: (AnyStr, CharSequence) -> bool
        return True

    def pattern(self):
        # type: () -> AnyStr
        pass

    @staticmethod
    def quote(s):
        # type: (AnyStr) -> AnyStr
        pass

    def split(self, input, limit=None):
        # type: (CharSequence, Optional[int]) -> List[AnyStr]
        pass

    def splitAsStream(self, input):
        # type: (CharSequence) -> Any
        pass
