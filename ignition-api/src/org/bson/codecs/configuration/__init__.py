from java.lang import Class
from org.bson.codecs import Codec


class CodecRegistry(object):
    def get(self, clazz):
        # type: (Class) -> Codec
        raise NotImplementedError
