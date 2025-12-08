__all__ = ["ModuleInfo"]

from typing import List, Mapping, Optional, Union

from java.lang import Object

from com.inductiveautomation.ignition.common.licensing import LicenseState
from com.inductiveautomation.ignition.common.model import Version
from com.inductiveautomation.ignition.common.util import Platform


class ModuleInfo(Object):

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
            # type: (Union[str, unicode]) -> ModuleInfo.Builder
            pass

        def setExports(self, exports):
            # type: (List[ModuleInfo.JarInfo]) -> ModuleInfo.Builder
            pass

        def setHooks(
            self,
            hooks,  # type: Mapping[int, Union[str, unicode]]
        ):
            # type: (...) -> ModuleInfo.Builder
            pass

        def setId(self, id_):
            # type: (Union[str, unicode]) -> ModuleInfo.Builder
            pass

        def setJars(self, jars):
            # type: (List[ModuleInfo.JarInfo]) -> ModuleInfo.Builder
            pass

        def setLicenseFile(self, licenseFilename):
            # type: (Union[str, unicode]) -> ModuleInfo.Builder
            pass

        def setName(self, name):
            # type: (Union[str, unicode]) -> ModuleInfo.Builder
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

        def setVendor(
            self,
            id_,  # type: int
            name,  # type: Union[str, unicode]
            contactInfo,  # type: Union[str, unicode]
        ):
            # type: (...) -> ModuleInfo.Builder
            pass

        def setVersion(self, version):
            # type: (Version) -> ModuleInfo.Builder
            pass

    class JarInfo(Object):
        def __init__(
            self,
            scope,  # type: int
            path,  # type: Union[str, unicode]
            requiredOs="",  # type: Union[str, unicode]
            requiredArch="",  # type: Union[str, unicode]
        ):
            # type: (...) -> None
            super(ModuleInfo.JarInfo, self).__init__()
            self._scope = scope
            self._path = path
            self._requiredOs = requiredOs
            self._requiredArch = requiredArch

        def getPath(self):
            # type: () -> Union[str, unicode]
            return self._path

        def getRequiredArch(self):
            # type: () -> Union[str, unicode]
            return self._requiredArch

        def getRequiredOS(self):
            # type: () -> Union[str, unicode]
            return self._requiredOs

        def getScope(self):
            # type: () -> int
            return self._scope

        def isNativeLib(self):
            # type: () -> bool
            return True

        def isRequiredArchitecture(self, arch):
            # type: (Platform.Architecture) -> bool
            return True

        def isRequiredOS(self, os):
            # type: (Platform.OperatingSystem) -> bool
            return True

    class LibraryInfo(Object):
        def getName(self):
            # type: () -> Union[str, unicode]
            pass

        def getScope(self):
            # type: () -> int
            pass

        def setName(self, name):
            # type: (Union[str, unicode]) -> None
            pass

        def setScope(self, scope):
            # type: (int) -> None
            pass

    class ModuleDependency(Object):
        def getModuleId(self):
            # type: () -> Union[str, unicode]
            pass

        def getScope(self):
            # type: () -> int
            pass

        def getVersion(self):
            # type: () -> Version
            pass

    def getCrc(self):
        # type: () -> long
        pass

    def getDependencies(self, scope=None):
        # type: (Optional[int]) -> List[ModuleInfo.ModuleDependency]
        pass

    def getDescription(self):
        # type: () -> Union[str, unicode]
        pass

    def getDocumentationRoot(self):
        # type: () -> Union[str, unicode]
        pass

    def getExports(self):
        # type: () -> List[ModuleInfo.JarInfo]
        pass

    def getHooks(self):
        # type: () -> Mapping[int, Union[str, unicode]]
        pass

    def getId(self):
        # type: () -> Union[str, unicode]
        pass

    def getInstallPath(self):
        # type: () -> Union[str, unicode]
        pass

    def getJars(self):
        # type: () -> List[ModuleInfo.JarInfo]
        pass

    def getLibsRequired(self):
        # type: () -> List[ModuleInfo.LibraryInfo]
        pass

    def getLicenseFile(self):
        # type: () -> Union[str, unicode]
        pass

    def getLicenseState(self):
        # type: () -> LicenseState
        pass

    def getName(self):
        # type: () -> Union[str, unicode]
        pass

    def getRequiredFrameworkVersion(self):
        # type: () -> int
        pass

    def getRequiredIgnitionVersion(self):
        # type: () -> Version
        pass

    def getVendorContactInfo(self):
        # type: () -> Union[str, unicode]
        pass

    def getVendorId(self):
        # type: () -> int
        pass

    def getVendorName(self):
        # type: () -> Union[str, unicode]
        pass

    def getVersion(self):
        # type: () -> Version
        pass

    def isFree(self):
        # type: () -> bool
        return True

    def isMakerEditionCompatible(self):
        # type: () -> bool
        return True

    def isSelfSigned(self):
        # type: () -> bool
        return True

    def isTrialMode(self):
        # type: () -> bool
        return True

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
        # type: (Union[str, unicode]) -> None
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
        # type: (int, Union[str, unicode], Union[str, unicode]) -> None
        pass

    @staticmethod
    def setDependencyOrder(list_, scope, reverse):
        # type: (List[ModuleInfo], int, bool) -> List[ModuleInfo]
        pass

    def toXML(self):
        # type: () -> Union[str, unicode]
        pass
