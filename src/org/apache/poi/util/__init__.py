from dev.coatl.helper.types import AnyStr


class LittleEndianInput(object):
    def available(self):
        # type: () -> int
        raise NotImplementedError

    def readByte(self):
        # type: () -> int
        raise NotImplementedError

    def readDouble(self):
        # type: () -> float
        raise NotImplementedError

    def readFully(self, buf, off=0, len=0):
        # type: (bytearray, int, int) -> None
        raise NotImplementedError

    def readInt(self):
        # type: () -> int
        raise NotImplementedError

    def readLong(self):
        # type: () -> long
        raise NotImplementedError

    def readPlain(self, buf, offset=0, length=0):
        # type: (bytearray, int, int) -> None
        raise NotImplementedError

    def readShort(self):
        # type: () -> int
        raise NotImplementedError

    def readUByte(self):
        # type: () -> int
        raise NotImplementedError

    def readUShort(self):
        # type: () -> int
        raise NotImplementedError


class LittleEndianOutput(object):
    def write(self, b, offset=0, length=0):
        # type: (bytearray, int, int) -> None
        raise NotImplementedError

    def writeByte(self, value):
        # type: (int) -> None
        raise NotImplementedError

    def writeDouble(self, value):
        # type: (float) -> None
        raise NotImplementedError

    def writeInt(self, value):
        # type: (int) -> None
        raise NotImplementedError

    def writeShort(self, value):
        # type: (int) -> None
        raise NotImplementedError

    def writeUTF(self, value):
        # type: (AnyStr) -> None
        raise NotImplementedError
