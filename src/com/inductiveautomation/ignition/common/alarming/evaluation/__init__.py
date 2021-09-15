__all__ = ["ShelvedPath"]

from java.lang import Object


class ShelvedPath(Object):
    """This class provides information about a path that has been
    "shelved", such as when it was shelved, and by whom, and the actual
    path.
    """

    def __init__(self, path=None, user=None, expiration=None):
        self.path = path
        self.user = user
        self.expiration = expiration

    def getExpiration(self):
        pass

    def getHitCount(self):
        pass

    def getPath(self):
        pass

    def getShelveTime(self):
        pass

    def getUser(self):
        pass

    def incrementHitCount(self):
        pass

    def isExpired(self):
        pass
