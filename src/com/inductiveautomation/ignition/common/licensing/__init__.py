__all__ = [
    "LicenseDetails",
    "LicenseMode",
    "LicenseRestriction",
    "LicenseState",
    "ModuleLicense",
]

from typing import Iterable, List, Union

from java.lang import Enum, Object
from java.util import Date


class LicenseDetails(object):
    def checkFlag(self, key):
        # type: (Union[str, unicode]) -> bool
        return True

    def getExpirationDate(self):
        # type: () -> Date
        pass

    def getLicenseDetail(self, key):
        # type: (Union[str, unicode]) -> Union[str, unicode]
        raise NotImplementedError

    def getLicenseDetails(self, key):
        # type: (Union[str, unicode]) -> List[LicenseRestriction]
        raise NotImplementedError

    def getModuleId(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getVersion(self):
        # type: () -> int
        raise NotImplementedError

    def isPlatformDetails(self):
        # type: () -> bool
        return True


class LicenseState(object):
    def getLicenseMode(self):
        # type: () -> LicenseMode
        raise NotImplementedError

    def getModuleLicense(self):
        # type: () -> ModuleLicense
        raise NotImplementedError

    def getPlatformLicense(self):
        # type: () -> LicenseDetails
        raise NotImplementedError

    def getTrialExpirationDate(self):
        # type: () -> Date
        raise NotImplementedError

    def isTrialExpired(self):
        # type: () -> bool
        raise NotImplementedError


class LicenseMode(Enum):
    @staticmethod
    def values():
        # type: () -> Iterable[LicenseMode]
        pass


class LicenseRestriction(Object):
    def __init__(self, restrictionName, restrictionValue):
        # type: (Union[str, unicode], Union[str, unicode]) -> None
        super(LicenseRestriction, self).__init__()
        self._restrictionName = restrictionName
        self._restrictionValue = restrictionValue

    def getrestrictionName(self):
        # type: () -> Union[str, unicode]
        return self._restrictionName

    def getrestrictionValue(self):
        # type: () -> Union[str, unicode]
        return self._restrictionValue


class ModuleLicense(LicenseDetails):
    def getLicenseDetail(self, key):
        # type: (Union[str, unicode]) -> Union[str, unicode]
        raise NotImplementedError

    def getLicenseDetails(self, key):
        # type: (Union[str, unicode]) -> List[LicenseRestriction]
        raise NotImplementedError

    def getModuleId(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getVersion(self):
        # type: () -> int
        raise NotImplementedError
