from __future__ import print_function

__all__ = [
    "GatewayAddress",
    "LaunchContext",
    "LaunchContextImpl",
    "LaunchManifest",
    "LaunchParent",
    "LaunchableApp",
]

from typing import Any, Iterable, List, Mapping, Optional, Union

from dev.thecesrom.helper.types import AnyStr
from java.awt import Dimension, Image
from java.io import File, InputStream, OutputStream, PrintWriter, Writer
from java.lang import Enum, Object
from javax.swing import JComponent, JPanel, RootPaneContainer


class LaunchContext(object):
    def getAttribute(self, key, defaultValue=None):
        # type: (AnyStr, Optional[Any]) -> Any
        raise NotImplementedError

    def getAttributes(self):
        # type: () -> Mapping[AnyStr, Object]
        raise NotImplementedError

    def getCacheDir(self):
        # type: () -> File
        raise NotImplementedError

    def getEdgeFlags(self):
        # type: () -> List[AnyStr]
        raise NotImplementedError

    def getGatewayAddress(self):
        # type: () -> GatewayAddress
        raise NotImplementedError

    def getGatewayAddresses(self):
        # type: () -> List[GatewayAddress]
        raise NotImplementedError

    def getGwCacheDir(self):
        # type: () -> File
        raise NotImplementedError

    def getLaunchManifest(self):
        # type: () -> LaunchManifest
        raise NotImplementedError

    def getLog(self):
        # type: () -> PrintWriter
        raise NotImplementedError

    def getMainClass(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getParent(self):
        # type: () -> LaunchParent
        raise NotImplementedError

    def getPlatformEdition(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getProjectCacheChkFile(self):
        # type: () -> File
        raise NotImplementedError

    def getProjectCacheFile(self):
        # type: () -> File
        raise NotImplementedError

    def getProjectName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getResourceDir(self):
        # type: () -> File
        raise NotImplementedError

    def getScopeCode(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getTranslationDBLocation(self):
        # type: () -> File
        raise NotImplementedError

    def getUserObject(self):
        # type: () -> bytearray
        raise NotImplementedError

    def log(self, message, *args):
        # type: (AnyStr, *Object) -> None
        raise NotImplementedError

    def setAttribute(self, key, value):
        # type: (AnyStr, Object) -> None
        raise NotImplementedError

    def updateGatewayAddressListCache(self, addrs):
        # type: (List[GatewayAddress]) -> None
        raise NotImplementedError

    def updateProjectCache(self, project):
        # type: (LaunchContext.WritableProject) -> None
        raise NotImplementedError

    class WritableProject(object):
        def write(self, stream):
            # type: (OutputStream) -> None
            raise NotImplementedError


class LaunchParent(object):
    def getLaunchFlavor(self):
        # type: () -> LaunchParent.LaunchFlavor
        raise NotImplementedError

    def getRootPaneContainer(self):
        # type: () -> RootPaneContainer
        raise NotImplementedError

    def isFullScreen(self):
        # type: () -> bool
        raise NotImplementedError

    def restart(
        self,
        addresses,  # type: List[GatewayAddress]
        projectName,  # type: AnyStr
        scope,  # type: AnyStr
        userObj,  # type: bytearray
    ):
        # type: (...) -> None
        raise NotImplementedError

    def setContent(self, context, app):
        # type: (LaunchContext, LaunchableApp) -> None
        raise NotImplementedError

    class LaunchFlavor(Enum):
        @staticmethod
        def values():
            # type: () -> Iterable[LaunchParent.LaunchFlavor]
            pass


class GatewayAddress(Object):
    def __init__(self, protocol, address, port, path):
        # type: (AnyStr, AnyStr, int, AnyStr) -> None
        super(GatewayAddress, self).__init__()
        self._protocol = protocol
        self._address = address
        self._port = port
        self._path = path

    def getAddress(self):
        # type: () -> AnyStr
        return self._address

    def getPath(self):
        # type: () -> AnyStr
        return self._path

    def getPort(self):
        # type: () -> int
        return self._port

    def getProcotol(self):
        # type: () -> AnyStr
        return self._protocol

    @staticmethod
    def parse(addr):
        # type: (AnyStr) -> GatewayAddress
        pass

    def toParseableString(self):
        # type: () -> AnyStr
        pass


class LaunchContextImpl(Object, LaunchContext):
    def getAttribute(self, key, defaultValue=None):
        # type: (AnyStr, Optional[Any]) -> Any
        pass

    def getAttributes(self):
        # type: () -> Mapping[AnyStr, Object]
        pass

    def getCacheDir(self):
        # type: () -> File
        pass

    def getEdgeFlags(self):
        # type: () -> List[AnyStr]
        pass

    def getGatewayAddress(self):
        # type: () -> GatewayAddress
        pass

    def getGatewayAddresses(self):
        # type: () -> List[GatewayAddress]
        pass

    def getGwCacheDir(self):
        # type: () -> File
        pass

    def getLaunchManifest(self):
        # type: () -> LaunchManifest
        pass

    def getLog(self):
        # type: () -> PrintWriter
        pass

    def getMainClass(self):
        # type: () -> AnyStr
        pass

    def getParent(self):
        # type: () -> LaunchParent
        pass

    def getPlatformEdition(self):
        # type: () -> AnyStr
        pass

    def getProjectCacheChkFile(self):
        # type: () -> File
        pass

    def getProjectCacheFile(self):
        # type: () -> File
        pass

    def getProjectName(self):
        # type: () -> AnyStr
        pass

    def getResourceDir(self):
        # type: () -> File
        pass

    def getScopeCode(self):
        # type: () -> AnyStr
        pass

    def getTranslationDBLocation(self):
        # type: () -> File
        pass

    def getUserObject(self):
        # type: () -> bytearray
        pass

    def log(self, message, *args):
        # type: (AnyStr, *Object) -> None
        pass

    def setAttribute(self, key, value):
        # type: (AnyStr, Object) -> None
        pass

    def updateGatewayAddressListCache(self, addrs):
        # type: (List[GatewayAddress]) -> None
        pass

    def updateProjectCache(self, project):
        # type: (LaunchContext.WritableProject) -> None
        pass


class LaunchManifest(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(LaunchManifest, self).__init__()
        print(args)

    def addModule(self, module):
        # type: (LaunchManifest.Module) -> None
        pass

    def getFrameworkVersion(self):
        # type: () -> int
        pass

    def getJavaExecutable(self):
        # type: () -> AnyStr
        pass

    def getJreVersion(self):
        # type: () -> AnyStr
        pass

    def getModules(self):
        # type: () -> Iterable[LaunchManifest.Module]
        pass

    def getPort(self):
        # type: () -> int
        pass

    def getScope(self):
        # type: () -> AnyStr
        pass

    def getThirdPartyScriptModulesHash(self):
        # type: () -> AnyStr
        pass

    def isEmpty(self):
        # type: () -> bool
        pass

    def isUseSsl(self):
        # type: () -> bool
        pass

    def newDiffAction(self, context):
        # type: (LaunchContextImpl) -> Any
        pass

    @staticmethod
    def readFrom(is_):
        # type: (InputStream) -> LaunchManifest
        pass

    def setJavaExecutable(self, javaExecutable):
        # type: (AnyStr) -> None
        pass

    def setUseCondensedDialogFont(self, useCondensedDialogFont):
        # type: (bool) -> None
        pass

    def storeTo(self, arg):
        # type: (Union[OutputStream, Writer]) -> None
        pass

    def useCondensedDialogFont(self):
        # type: () -> bool
        pass

    class Jar(Object):
        def __init__(self, name, crc32, length):
            # type: (AnyStr, long, long) -> None
            super(LaunchManifest.Jar, self).__init__()
            self._name = name
            self._crc32 = crc32
            self._length = length

        def getCrc32(self):
            # type: () -> long
            return self._crc32

        def getLength(self):
            # type: () -> long
            return self._length

        def getName(self):
            # type: () -> AnyStr
            return self._name

    class Module(Object):
        def __init__(self, name, build):
            # type: (AnyStr, int) -> None
            super(LaunchManifest.Module, self).__init__()
            self._name = name
            self._build = build

        def addJar(self, file):
            # type: (LaunchManifest.Jar) -> None
            pass

        def getBuild(self):
            # type: () -> int
            return self._build

        def getJarFiles(self):
            # type: () -> List[LaunchManifest.Jar]
            pass

        def getName(self):
            # type: () -> AnyStr
            return self._name


class LaunchableApp(JPanel):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(LaunchableApp, self).__init__()
        print(args)

    def canShutdown(self):
        # type: () -> bool
        raise NotImplementedError

    def getFrameIcon(self):
        # type: () -> Image
        pass

    def getFrameTitle(self):
        # type: () -> AnyStr
        pass

    def getGlassPane(self):
        # type: () -> JComponent
        pass

    def getInitialFrameSize(self):
        # type: () -> Dimension
        raise NotImplementedError

    def getScreenIndex(self):
        # type: () -> int
        pass

    def isStartCentered(self):
        # type: () -> bool
        raise NotImplementedError

    def isStartMaximized(self):
        # type: () -> bool
        raise NotImplementedError

    def setFrameIcon(self, frameIcon):
        # type: (Image) -> None
        pass

    def setFrameTitle(self, frameTitle):
        # type: (AnyStr) -> None
        pass

    def setGlassPane(self, frameIcon):
        # type: (JComponent) -> None
        pass

    def shutdown(self):
        # type: () -> None
        raise NotImplementedError
