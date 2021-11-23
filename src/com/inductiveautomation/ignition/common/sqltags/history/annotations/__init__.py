__all__ = ["Annotation"]

from java.lang import Object


class Annotation(Object):
    def delete(self):
        pass

    @staticmethod
    def fromJson(json):
        pass

    def getData(self):
        pass

    def getPath(self):
        pass

    def getRangeEnd(self):
        pass

    def getRangeStart(self):
        pass

    def getStorageId(self):
        pass

    def getType(self):
        pass

    def isDeleted(self):
        pass

    @staticmethod
    def newBuilder():
        pass

    @staticmethod
    def newDelete(storageId):
        pass

    def toJson(self):
        pass

    def updatePath(self, path):
        pass
