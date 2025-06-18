from java.lang import Class
from org.bson.codecs import Codec

class CodecRegistry:
    def get(self, clazz: Class) -> Codec: ...
