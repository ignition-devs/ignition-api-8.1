from typing import Any, List, Optional, Union

from java.lang import CharSequence, Object, String, StringBuffer, StringBuilder
from java.util.function import Function, Predicate


class MatchResult(object):
    def end(self, group=None):
        # type: (Optional[int]) -> int
        raise NotImplementedError

    def group(self, group=None):
        # type: (Optional[int]) -> String
        raise NotImplementedError

    def groupCount(self):
        # type: () -> int
        raise NotImplementedError

    def start(self, group=None):
        # type: (Optional[int]) -> int
        raise NotImplementedError


class Matcher(Object, MatchResult):
    def appendReplacement(self, sb, replacement):
        # type: (Union[StringBuffer, StringBuilder], String) -> Matcher
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
        pass

    def group(self, group=None):
        # type: (Optional[Union[int, String]]) -> String
        pass

    def groupCount(self):
        # type: () -> int
        pass

    def hasAnchoringBounds(self):
        # type: () -> bool
        pass

    def hasTransparentBounds(self):
        # type: () -> bool
        pass

    def hitEnd(self):
        # type: () -> bool
        pass

    def lookingAt(self):
        # type: () -> bool
        pass

    def matches(self):
        # type: () -> bool
        pass

    def pattern(self):
        # type: () -> Pattern
        pass

    @staticmethod
    def quoteReplacement(s):
        # type: (String) -> String
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
        # type: (Union[Function, String]) -> String
        pass

    def replaceFirst(self, arg):
        # type: (Union[Function, String]) -> String
        pass

    def requireEnd(self):
        # type: () -> bool
        pass

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
        # type: (String, Optional[int]) -> Pattern
        pass

    def flags(self):
        # type: () -> int
        pass

    def matcher(self, input):
        # type: (CharSequence) -> Matcher
        pass

    @staticmethod
    def matches(regex, input):
        # type: (String, CharSequence) -> bool
        pass

    def pattern(self):
        # type: () -> String
        pass

    @staticmethod
    def quote(s):
        # type: (String) -> String
        pass

    def split(self, input, limit=None):
        # type: (CharSequence, Optional[int]) -> List[String]
        pass

    def splitAsStream(self, input):
        # type: (CharSequence) -> Any
        pass
