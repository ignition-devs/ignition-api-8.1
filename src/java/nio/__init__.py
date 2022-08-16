from typing import Any, Optional, Union

from java.lang import Appendable, CharSequence, Object

__all__ = [
    "Buffer",
    "ByteBuffer",
    "ByteOrder",
    "CharBuffer",
    "DoubleBuffer",
    "FloatBuffer",
    "IntBuffer",
    "LongBuffer",
    "MappedByteBuffer",
    "ShortBuffer",
]


class Buffer(Object):
    def array(self):
        # type: () -> Object
        raise NotImplementedError

    def arrayOffset(self):
        # type: () -> int
        raise NotImplementedError

    def capacity(self):
        # type: () -> int
        pass

    def clear(self):
        # type: () -> Buffer
        pass

    def duplicate(self):
        # type: () -> Buffer
        raise NotImplementedError

    def flip(self):
        # type: () -> Buffer
        pass

    def hasArray(self):
        # type: () -> bool
        raise NotImplementedError

    def hasRemaining(self):
        # type: () -> bool
        pass

    def isDirect(self):
        # type: () -> bool
        raise NotImplementedError

    def isReadOnly(self):
        # type: () -> bool
        raise NotImplementedError

    def limit(self, nrewLimit=None):
        # type: (Optional[int]) -> Union[Buffer, int]
        pass

    def mark(self):
        # type: () -> Buffer
        pass

    def position(self, newPosition=None):
        # type: (Optional[int]) -> Union[Buffer, int]
        pass

    def remaining(self):
        # type: () -> int
        pass

    def reset(self):
        # type: () -> Buffer
        pass

    def rewind(self):
        # type: () -> Buffer
        pass

    def slice(self):
        # type: () -> Buffer
        raise NotImplementedError


class ByteBuffer(Buffer):
    def alignedSlice(self, unitSize):
        # type: (int) -> ByteBuffer
        pass

    def alignmentOffset(self, index, unitSize):
        # type: (int, int) -> int
        pass

    @staticmethod
    def allocate(capacity):
        # type: (int) -> ByteBuffer
        pass

    @staticmethod
    def allocateDirect(capacity):
        # type: (int) -> ByteBuffer
        pass

    def array(self):
        # type: () -> Object
        pass

    def arrayOffset(self):
        # type: () -> int
        pass

    def asCharBuffer(self):
        # type: () -> CharBuffer
        pass

    def asDoubleBuffer(self):
        # type: () -> DoubleBuffer
        pass

    def asFloatBuffer(self):
        # type: () -> FloatBuffer
        pass

    def asIntBuffer(self):
        # type: () -> IntBuffer
        pass

    def asLongBuffer(self):
        # type: () -> LongBuffer
        pass

    def asReadOnlyBuffer(self):
        # type: () -> ByteBuffer
        pass

    def asShortBuffer(self):
        # type: () -> ShortBuffer
        pass

    def compact(self):
        # type: () -> ByteBuffer
        pass

    def compareTo(self, that):
        # type: (ByteBuffer) -> int
        pass

    def duplicate(self):
        # type: () -> Buffer
        pass

    def get(self, *args):
        # type: (Any) -> ByteBuffer
        pass

    def getChar(self, index=0):
        # type: (int) -> str
        pass

    def getDouble(self, index=0):
        # type: (int) -> float
        pass

    def getFloat(self, index=0):
        # type: (int) -> float
        pass

    def getInt(self, index=0):
        # type: (int) -> int
        pass

    def getLong(self, index=0):
        # type: (int) -> long
        pass

    def getShort(self, index=0):
        # type: (int) -> int
        pass

    def hasArray(self):
        # type: () -> bool
        pass

    def isDirect(self):
        # type: () -> bool
        pass

    def isReadOnly(self):
        # type: () -> bool
        pass

    def mismatch(self, that):
        # type: (ByteBuffer) -> int
        pass

    def order(self, bo=None):
        # type: (Optional[ByteOrder]) -> ByteOrder
        pass

    def put(self, *args):
        # type: (Any) -> ByteBuffer
        pass

    def putChar(self, *args):
        # type: (Any) -> ByteBuffer
        pass

    def putDouble(self, *args):
        # type: (Any) -> ByteBuffer
        pass

    def putFloat(self, *args):
        # type: (Any) -> ByteBuffer
        pass

    def putInt(self, *args):
        # type: (Any) -> ByteBuffer
        pass

    def putLong(self, *args):
        # type: (Any) -> ByteBuffer
        pass

    def putShort(self, *args):
        # type: (Any) -> ByteBuffer
        pass

    def slice(self):
        # type: () -> ByteBuffer
        pass

    @staticmethod
    def wrap(*arg):
        # type: (Any) -> ByteBuffer
        pass


class ByteOrder(Object):
    BIG_ENDIAN = None  # type: ByteOrder
    LITTLE_ENDIAN = None  # type: ByteOrder

    @staticmethod
    def nativeOrder():
        # type: () -> ByteOrder
        pass


class CharBuffer(Buffer, Appendable, CharSequence):
    @staticmethod
    def allocate(capacity):
        # type: (int) -> CharBuffer
        pass

    def append(self, c_csq, start=0, end=-1):
        # type: (Union[CharSequence, str], int, int) -> CharBuffer
        pass

    def array(self):
        # type: () -> Object
        pass

    def arrayOffset(self):
        # type: () -> int
        pass

    def charAt(self, index):
        # type: (int) -> str
        pass

    def compact(self):
        # type: () -> CharBuffer
        pass

    def compareTo(self, that):
        # type: (CharBuffer) -> int
        pass

    def duplicate(self):
        # type: () -> CharBuffer
        pass

    def get(self, *args):
        # type: (Any) -> CharBuffer
        pass

    def hasArray(self):
        # type: () -> bool
        pass

    def isDirect(self):
        # type: () -> bool
        pass

    def isReadOnly(self):
        # type: () -> bool
        pass

    def length(self):
        # type: () -> int
        pass

    def mismatch(self, that):
        # type: (CharBuffer) -> int
        pass

    def order(self):
        # type: () -> ByteOrder
        pass

    def put(self, *args):
        # type: (Any) -> CharBuffer
        pass

    def read(self, target):
        # type: (CharBuffer) -> int
        pass

    def slice(self):
        # type: () -> CharBuffer
        pass

    def subSequence(self, start, end):
        # type: (int, int) -> CharSequence
        pass

    @staticmethod
    def wrap(*args):
        # type: (Any) -> CharBuffer
        pass


class DoubleBuffer(Buffer):
    @staticmethod
    def allocate(capacity):
        # type: (int) -> DoubleBuffer
        pass

    def array(self):
        # type: () -> Object
        pass

    def arrayOffset(self):
        # type: () -> int
        pass

    def compact(self):
        # type: () -> DoubleBuffer
        pass

    def compareTo(self, that):
        # type: (DoubleBuffer) -> int
        pass

    def duplicate(self):
        # type: () -> DoubleBuffer
        pass

    def get(self, *args):
        # type: (Any) -> DoubleBuffer
        pass

    def hasArray(self):
        # type: () -> bool
        pass

    def isDirect(self):
        # type: () -> bool
        pass

    def isReadOnly(self):
        # type: () -> bool
        pass

    def mismatch(self, that):
        # type: (DoubleBuffer) -> int
        pass

    def order(self):
        # type: () -> ByteOrder
        pass

    def put(self, *args):
        # type: (Any) -> DoubleBuffer
        pass

    def slice(self):
        # type: () -> DoubleBuffer
        pass

    @staticmethod
    def wrap(*args):
        # type: (Any) -> DoubleBuffer
        pass


class FloatBuffer(Buffer):
    @staticmethod
    def allocate(capacity):
        # type: (int) -> FloatBuffer
        pass

    def array(self):
        # type: () -> Object
        pass

    def arrayOffset(self):
        # type: () -> int
        pass

    def compact(self):
        # type: () -> FloatBuffer
        pass

    def compareTo(self, that):
        # type: (FloatBuffer) -> int
        pass

    def duplicate(self):
        # type: () -> FloatBuffer
        pass

    def get(self, *args):
        # type: (Any) -> FloatBuffer
        pass

    def hasArray(self):
        # type: () -> bool
        pass

    def isDirect(self):
        # type: () -> bool
        pass

    def isReadOnly(self):
        # type: () -> bool
        pass

    def mismatch(self, that):
        # type: (FloatBuffer) -> int
        pass

    def order(self):
        # type: () -> ByteOrder
        pass

    def put(self, *args):
        # type: (Any) -> FloatBuffer
        pass

    def slice(self):
        # type: () -> FloatBuffer
        pass

    @staticmethod
    def wrap(*args):
        # type: (Any) -> FloatBuffer
        pass


class IntBuffer(Buffer):
    @staticmethod
    def allocate(capacity):
        # type: (int) -> IntBuffer
        pass

    def array(self):
        # type: () -> Object
        pass

    def arrayOffset(self):
        # type: () -> int
        pass

    def compact(self):
        # type: () -> IntBuffer
        pass

    def compareTo(self, that):
        # type: (IntBuffer) -> int
        pass

    def duplicate(self):
        # type: () -> IntBuffer
        pass

    def get(self, *args):
        # type: (Any) -> IntBuffer
        pass

    def hasArray(self):
        # type: () -> bool
        pass

    def isDirect(self):
        # type: () -> bool
        pass

    def isReadOnly(self):
        # type: () -> bool
        pass

    def mismatch(self, that):
        # type: (IntBuffer) -> int
        pass

    def order(self):
        # type: () -> ByteOrder
        pass

    def put(self, *args):
        # type: (Any) -> IntBuffer
        pass

    def slice(self):
        # type: () -> IntBuffer
        pass

    @staticmethod
    def wrap(*args):
        # type: (Any) -> IntBuffer
        pass


class LongBuffer(Buffer):
    @staticmethod
    def allocate(capacity):
        # type: (int) -> LongBuffer
        pass

    def array(self):
        # type: () -> Object
        pass

    def arrayOffset(self):
        # type: () -> int
        pass

    def compact(self):
        # type: () -> LongBuffer
        pass

    def compareTo(self, that):
        # type: (LongBuffer) -> int
        pass

    def duplicate(self):
        # type: () -> LongBuffer
        pass

    def get(self, *args):
        # type: (Any) -> LongBuffer
        pass

    def hasArray(self):
        # type: () -> bool
        pass

    def isDirect(self):
        # type: () -> bool
        pass

    def isReadOnly(self):
        # type: () -> bool
        pass

    def mismatch(self, that):
        # type: (LongBuffer) -> int
        pass

    def order(self):
        # type: () -> ByteOrder
        pass

    def put(self, *args):
        # type: (Any) -> LongBuffer
        pass

    def slice(self):
        # type: () -> LongBuffer
        pass

    @staticmethod
    def wrap(*args):
        # type: (Any) -> LongBuffer
        pass


class ShortBuffer(Buffer):
    @staticmethod
    def allocate(capacity):
        # type: (int) -> ShortBuffer
        pass

    def array(self):
        # type: () -> Object
        pass

    def arrayOffset(self):
        # type: () -> int
        pass

    def compact(self):
        # type: () -> ShortBuffer
        pass

    def compareTo(self, that):
        # type: (ShortBuffer) -> int
        pass

    def duplicate(self):
        # type: () -> ShortBuffer
        pass

    def get(self, *args):
        # type: (Any) -> ShortBuffer
        pass

    def hasArray(self):
        # type: () -> bool
        pass

    def isDirect(self):
        # type: () -> bool
        pass

    def isReadOnly(self):
        # type: () -> bool
        pass

    def mismatch(self, that):
        # type: (ShortBuffer) -> int
        pass

    def order(self):
        # type: () -> ByteOrder
        pass

    def put(self, *args):
        # type: (Any) -> ShortBuffer
        pass

    def slice(self):
        # type: () -> ShortBuffer
        pass

    @staticmethod
    def wrap(*args):
        # type: (Any) -> ShortBuffer
        pass


class MappedByteBuffer(ByteBuffer):
    def force(self):
        # type: () -> MappedByteBuffer
        pass

    def isLoaded(self):
        # type: () -> bool
        pass

    def load(self):
        # type: () -> MappedByteBuffer
        pass
