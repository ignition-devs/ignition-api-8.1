__all__ = ["ModuleInfo"]

from typing import List, Mapping, Optional

from com.inductiveautomation.ignition.common.licensing import LicenseState
from com.inductiveautomation.ignition.common.model import Version
from com.inductiveautomation.ignition.common.util import Platform
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object


class ModuleInfo(Object):
    def getCrc(self):
        # type: () -> long
        pass

    def getDependencies(self, scope=None):
        # type: (Optional[int]) -> List[ModuleInfo.ModuleDependency]
        pass

    def getDescription(self):
        # type: () -> AnyStr
        pass

    def getDocumentationRoot(self):
        # type: () -> AnyStr
        pass

    def getExports(self):
        # type: () -> List[ModuleInfo.JarInfo]
        pass

    def getHooks(self):
        # type: () -> Mapping[int, AnyStr]
        pass

    def getId(self):
        # type: () -> AnyStr
        pass

    def getInstallPath(self):
        # type: () -> AnyStr
        pass

    def getJars(self):
        # type: () -> List[ModuleInfo.JarInfo]
        pass

    def getLibsRequired(self):
        # type: () -> List[ModuleInfo.LibraryInfo]
        pass

    def getLicenseFile(self):
        # type: () -> AnyStr
        pass

    def getLicenseState(self):
        # type: () -> LicenseState
        pass

    def getName(self):
        # type: () -> AnyStr
        pass

    def getRequiredFrameworkVersion(self):
        # type: () -> int
        pass

    def getRequiredIgnitionVersion(self):
        # type: () -> Version
        pass

    def getVendorContactInfo(self):
        # type: () -> AnyStr
        pass

    def getVendorId(self):
        # type: () -> int
        pass

    def getVendorName(self):
        # type: () -> AnyStr
        pass

    def getVersion(self):
        # type: () -> Version
        pass

    def isFree(self):
        # type: () -> bool
        pass

    def isMakerEditionCompatible(self):
        # type: () -> bool
        pass

    def isSelfSigned(self):
        # type: () -> bool
        pass

    def isTrialMode(self):
        # type: () -> bool
        pass

    @staticmethod
    def newBuilder():
        # type: () -> ModuleInfo.Builder
        pass

    def setCrc(self, crc):
        # type: (long) -> None
        pass

    def setFree(self):
        # type: () -> None
        pass

    def setInstallPath(self, installPath):
        # type: (AnyStr) -> None
        pass

    def setLicenseState(self, newState):
        # type: (LicenseState) -> None
        pass

    def setMakerEditionCompatible(self):
        # type: () -> None
        pass

    def setSelfSigned(self):
        # type: () -> None
        pass

    def setVendorInfo(self, vendorId, vendorName, vendorContactInfo):
        # type: (int, AnyStr, AnyStr) -> None
        pass

    @staticmethod
    def setDependencyOrder(list_, scope, reverse):
        # type: (List[ModuleInfo], int, bool) -> List[ModuleInfo]
        pass

    def toXML(self):
        # type: () -> AnyStr
        pass

    class Builder(Object):
        def __init__(self):
            # type: () -> None
            super(ModuleInfo.Builder, self).__init__()

        def addDependency(self, dependency):
            # type: (ModuleInfo.ModuleDependency) -> ModuleInfo.Builder
            pass

        def build(self):
            # type: () -> ModuleInfo
            pass

        def setDependencies(
            self,
            dependencies,  # type: List[ModuleInfo.ModuleDependency]
        ):
            # type: (...) -> ModuleInfo.Builder
            pass

        def setDescription(self, description):
            # type: (AnyStr) -> ModuleInfo.Builder
            pass

        def setExports(self, exports):
            # type: (List[ModuleInfo.JarInfo]) -> ModuleInfo.Builder
            pass

        def setHooks(self, hooks):
            # type: (Mapping[int, AnyStr]) -> ModuleInfo.Builder
            pass

        def setId(self, id_):
            # type: (AnyStr) -> ModuleInfo.Builder
            pass

        def setJars(self, jars):
            # type: (List[ModuleInfo.JarInfo]) -> ModuleInfo.Builder
            pass

        def setLicenseFile(self, licenseFilename):
            # type: (AnyStr) -> ModuleInfo.Builder
            pass

        def setName(self, name):
            # type: (AnyStr) -> ModuleInfo.Builder
            pass

        def setRequire(self, require):
            # type: (List[ModuleInfo.LibraryInfo]) -> ModuleInfo.Builder
            pass

        def setRequiredFrameworkVersion(self, requiredFrameworkVersion):
            # type: (int) -> ModuleInfo.Builder
            pass

        def setRequiredIgnitionVersion(self, requiredIgnitionVersion):
            # type: (Version) -> ModuleInfo.Builder
            pass

        def setSelfSigned(self, selfSigned):
            # type: (bool) -> ModuleInfo.Builder
            pass

        def setVendor(self, id_, name, contactInfo):
            # type: (int, AnyStr, AnyStr) -> ModuleInfo.Builder
            pass

        def setVersion(self, version):
            # type: (Version) -> ModuleInfo.Builder
            pass

    class JarInfo(Object):
        def __init__(
            self,
            scope,  # type: int
            path,  # type: AnyStr
            requiredOs="",  # type: AnyStr
            requiredArch="",  # type: AnyStr
        ):
            # type: (...) -> None
            super(ModuleInfo.JarInfo, self).__init__()
            self._scope = scope
            self._path = path
            self._requiredOs = requiredOs
            self._requiredArch = requiredArch

        def getPath(self):
            # type: () -> AnyStr
            return self._path

        def getRequiredArch(self):
            # type: () -> AnyStr
            return self._requiredArch

        def getRequiredOS(self):
            # type: () -> AnyStr
            return self._requiredOs

        def getScope(self):
            # type: () -> int
            return self._scope

        def isNativeLib(self):
            # type: () -> bool
            pass

        def isRequiredArchitecture(self, arch):
            # type: (Platform.Architecture) -> bool
            pass

        def isRequiredOS(self, os):
            # type: (Platform.OperatingSystem) -> bool
            pass

    class LibraryInfo(Object):
        def getName(self):
            # type: () -> AnyStr
            pass

        def getScope(self):
            # type: () -> int
            pass

        def setName(self, name):
            # type: (AnyStr) -> None
            pass

        def setScope(self, scope):
            # type: (int) -> None
            pass

    class ModuleDependency(Object):
        def getModuleId(self):
            # type: () -> AnyStr
            pass

        def getScope(self):
            # type: () -> int
            pass

        def getVersion(self):
            # type: () -> Version
            pass
