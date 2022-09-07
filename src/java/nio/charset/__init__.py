__all__ = ["Charset", "CharsetDecoder", "CharsetEncoder", "CoderResult"]

from typing import Dict, Optional, Set, Union

from java.lang import Object, String
from java.nio import ByteBuffer, CharBuffer
from java.util import Locale


class Charset(Object):
    def aliases(self):
        # type: () -> Set[String]
        pass

    @staticmethod
    def availableCharsets():
        # type: () -> Dict[String, Charset]
        pass

    def canEncode(self):
        # type: () -> bool
        pass

    def compareTo(self, that):
        # type: (Charset) -> int
        pass

    def contains(self, cs):
        # type: (Charset) -> bool
        pass

    def decode(self, bb):
        # type: (ByteBuffer) -> CharBuffer
        pass

    @staticmethod
    def defaultCharset():
        # type: () -> Charset
        pass

    def displayName(self, locale):
        # type: (Optional[Locale]) -> String
        pass

    def encode(self, arg):
        # type: (Union[Charset, String]) -> ByteBuffer
        pass

    @staticmethod
    def forName(charsetName):
        # type: (String) -> Charset
        pass

    def isRegistered(self):
        # type: () -> bool
        pass

    @staticmethod
    def isSupported(charsetName):
        # type: (String) -> bool
        pass

    def name(self):
        # type: () -> String
        pass

    def newDecoder(self):
        # type: () -> CharsetDecoder
        pass

    def newEncoder(self):
        # type: () -> CharsetEncoder
        pass


class CharsetDecoder(Object):
    def charset(self):
        # type: () -> Charset
        pass

    def decode(
        self,
        in_,  # type: ByteBuffer
        out=None,  # type: Optional[CharBuffer]
        endOfInput=None,  # type: Optional[bool]
    ):
        # type: (...) -> CharBuffer
        pass


class CharsetEncoder(Object):
    def charset(self):
        # type: () -> Charset
        pass

    def encode(
        self,
        in_,  # type: ByteBuffer
        out=None,  # type: Optional[ByteBuffer]
        endOfInput=None,  # type: Optional[bool]
    ):
        # type: (...) -> Union[ByteBuffer, CoderResult]
        pass


class CoderResult(Object):
    OVERFLOW = None  # type: CoderResult
    UNDERFLOW = None  # type: CoderResult

    def isError(self):
        # type: () -> bool
        pass

    def isMalformed(self):
        # type: () -> bool
        pass

    def isOverflow(self):
        # type: () -> bool
        pass

    def isUnderFlow(self):
        # type: () -> bool
        pass

    def isUnmappable(self):
        # type: () -> bool
        pass

    def length(self):
        # type: () -> int
        pass

    @staticmethod
    def malformedForLength(length):
        # type: (int) -> CoderResult
        pass

    def throwException(self):
        # type: () -> None
        pass

    @staticmethod
    def unmappableForLength(length):
        # type: (int) -> CoderResult
        pass
