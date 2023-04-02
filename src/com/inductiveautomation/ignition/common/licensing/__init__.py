__all__ = [
    "LicenseDetails",
    "LicenseMode",
    "LicenseRestriction",
    "LicenseState",
    "ModuleLicense",
]

from typing import Iterable, List

from dev.thecesrom.helper.types import AnyStr
from java.lang import Enum, Object
from java.util import Date


class LicenseDetails(object):
    def checkFlag(self, key):
        # type: (AnyStr) -> bool
        pass

    def getExpirationDate(self):
        # type: () -> Date
        pass

    def getLicenseDetail(self, key):
        # type: (AnyStr) -> AnyStr
        raise NotImplementedError

    def getLicenseDetails(self, key):
        # type: (AnyStr) -> List[LicenseRestriction]
        raise NotImplementedError

    def getModuleId(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getVersion(self):
        # type: () -> int
        raise NotImplementedError

    def isPlatformDetails(self):
        # type: () -> bool
        pass


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
        # type: (AnyStr, AnyStr) -> None
        super(LicenseRestriction, self).__init__()
        self._restrictionName = restrictionName
        self._restrictionValue = restrictionValue

    def getrestrictionName(self):
        # type: () -> AnyStr
        return self._restrictionName

    def getrestrictionValue(self):
        # type: () -> AnyStr
        return self._restrictionValue


class ModuleLicense(LicenseDetails):
    def getLicenseDetail(self, key):
        # type: (AnyStr) -> AnyStr
        raise NotImplementedError

    def getLicenseDetails(self, key):
        # type: (AnyStr) -> List[LicenseRestriction]
        raise NotImplementedError

    def getModuleId(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getVersion(self):
        # type: () -> int
        raise NotImplementedError
