__all__ = ["RosterModel"]

from typing import List, Union

from com.inductiveautomation.ignition.common.user import User
from com.palantir.ptoss.cinch.core import DefaultBindableModel


class RosterModel(DefaultBindableModel):
    def __init__(self):
        # type: () -> None
        super(RosterModel, self).__init__()

    def getDescription(self):
        # type: () -> Union[str, unicode]
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        pass

    def getUsers(self):
        # type: () -> List[User]
        pass

    def set(self, that):
        # type: (RosterModel) -> None
        pass

    def setDescription(self, description):
        # type: (Union[str, unicode]) -> None
        pass

    def setName(self, name):
        # type: (Union[str, unicode]) -> None
        pass

    def setUsers(self, users):
        # type: (List[User]) -> None
        pass
