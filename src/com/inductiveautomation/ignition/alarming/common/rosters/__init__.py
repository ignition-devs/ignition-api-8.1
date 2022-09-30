from typing import List

from com.inductiveautomation.ignition.common.user import User
from com.palantir.ptoss.cinch.core import DefaultBindableModel
from java.lang import String


class RosterModel(DefaultBindableModel):
    def getName(self):
        # type: () -> String
        pass

    def getUsers(self):
        # type: () -> List[String]
        pass

    def set(self, that):
        # type: (RosterModel) -> None
        pass

    def setName(self, name):
        # type: (String) -> None
        pass

    def setUsers(self, users):
        # type: (List[User]) -> None
        pass
