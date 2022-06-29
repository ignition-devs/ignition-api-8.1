__all__ = ["ShelvedPath"]

from com.inductiveautomation.ignition.common import Path, QualifiedPath
from java.lang import Object
from java.util import Date


class ShelvedPath(Object):
    """This class provides information about a path that has been
    "shelved", such as when it was shelved, and by whom, and the actual
    path.
    """

    def __init__(self, path=None, user=None, expiration=None, shelveTime=None):
        # type: (Path, QualifiedPath, long, Date) -> None
        self._path = path
        self._user = user
        self._expiration = expiration
        self._shelveTime = shelveTime

    def getExpiration(self):
        # type: () -> Date
        pass

    def getHitCount(self):
        # type: () -> int
        pass

    def getPath(self):
        # type: () -> Path
        pass

    def getShelveTime(self):
        # type: () -> Date
        pass

    def getUser(self):
        # type: () -> QualifiedPath
        pass

    def incrementHitCount(self):
        # type: () -> None
        pass

    def isExpired(self):
        # type: () -> bool
        pass
