from dev.coatl.helper.types import AnyStr


class LittleEndianInput(object):
    def available(self):
        # type: () -> int
        pass

    def readByte(self):
        # type: () -> int
        pass

    def readDouble(self):
        # type: () -> float
        pass

    def readFully(self, buf, off=0, len=0):
        # type: (bytearray, int, int) -> None
        pass

    def readInt(self):
        # type: () -> int
        pass

    def readLong(self):
        # type: () -> long
        pass

    def readPlain(self, buf, offset=0, length=0):
        # type: (bytearray, int, int) -> None
        pass

    def readShort(self):
        # type: () -> int
        pass

    def readUByte(self):
        # type: () -> int
        pass

    def readUShort(self):
        # type: () -> int
        pass


class LittleEndianOutput(object):
    def write(self, b, offset=0, length=0):
        # type: (bytearray, int, int) -> None
        pass

    def writeByte(self, value):
        # type: (int) -> None
        pass

    def writeDouble(self, value):
        # type: (float) -> None
        pass

    def writeInt(self, value):
        # type: (int) -> None
        pass

    def writeShort(self, value):
        # type: (int) -> None
        pass

    def writeUTF(self, value):
        # type: (AnyStr) -> None
        pass
