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

from java.awt import Dimension, Image
from java.io import File, InputStream, OutputStream, PrintWriter, Writer
from java.lang import Enum, Object
from javax.swing import JComponent, JPanel, RootPaneContainer


class LaunchContext(object):

    class WritableProject(object):
        def write(self, stream):
            # type: (OutputStream) -> None
            raise NotImplementedError

    def getAttribute(self, key, defaultValue=None):
        # type: (Union[str, unicode], Optional[Any]) -> Any
        raise NotImplementedError

    def getAttributes(self):
        # type: () -> Mapping[Union[str, unicode], Object]
        raise NotImplementedError

    def getCacheDir(self):
        # type: () -> File
        raise NotImplementedError

    def getEdgeFlags(self):
        # type: () -> List[Union[str, unicode]]
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
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getParent(self):
        # type: () -> LaunchParent
        raise NotImplementedError

    def getPlatformEdition(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getProjectCacheChkFile(self):
        # type: () -> File
        raise NotImplementedError

    def getProjectCacheFile(self):
        # type: () -> File
        raise NotImplementedError

    def getProjectName(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getResourceDir(self):
        # type: () -> File
        raise NotImplementedError

    def getScopeCode(self):
        # type: () -> Union[str, unicode]
        raise NotImplementedError

    def getTranslationDBLocation(self):
        # type: () -> File
        raise NotImplementedError

    def getUserObject(self):
        # type: () -> bytearray
        raise NotImplementedError

    def log(self, message, *args):
        # type: (Union[str, unicode], *Object) -> None
        raise NotImplementedError

    def setAttribute(self, key, value):
        # type: (Union[str, unicode], Object) -> None
        raise NotImplementedError

    def updateGatewayAddressListCache(self, addrs):
        # type: (List[GatewayAddress]) -> None
        raise NotImplementedError

    def updateProjectCache(self, project):
        # type: (LaunchContext.WritableProject) -> None
        raise NotImplementedError


class LaunchParent(object):

    class LaunchFlavor(Enum):
        @staticmethod
        def values():
            # type: () -> Iterable[LaunchParent.LaunchFlavor]
            pass

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
        projectName,  # type: Union[str, unicode]
        scope,  # type: Union[str, unicode]
        userObj,  # type: bytearray
    ):
        # type: (...) -> None
        raise NotImplementedError

    def setContent(self, context, app):
        # type: (LaunchContext, LaunchableApp) -> None
        raise NotImplementedError


class GatewayAddress(Object):
    def __init__(
        self,
        protocol,  # type: Union[str, unicode]
        address,  # type: Union[str, unicode]
        port,  # type: int
        path,  # type: Union[str, unicode]
    ):
        # type: (...) -> None
        super(GatewayAddress, self).__init__()
        self._protocol = protocol
        self._address = address
        self._port = port
        self._path = path

    def getAddress(self):
        # type: () -> Union[str, unicode]
        return self._address

    def getPath(self):
        # type: () -> Union[str, unicode]
        return self._path

    def getPort(self):
        # type: () -> int
        return self._port

    def getProcotol(self):
        # type: () -> Union[str, unicode]
        return self._protocol

    @staticmethod
    def parse(addr):
        # type: (Union[str, unicode]) -> GatewayAddress
        pass

    def toParseableString(self):
        # type: () -> Union[str, unicode]
        pass


class LaunchContextImpl(Object, LaunchContext):
    def getAttribute(self, key, defaultValue=None):
        # type: (Union[str, unicode], Optional[Any]) -> Any
        pass

    def getAttributes(self):
        # type: () -> Mapping[Union[str, unicode], Object]
        pass

    def getCacheDir(self):
        # type: () -> File
        pass

    def getEdgeFlags(self):
        # type: () -> List[Union[str, unicode]]
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
        # type: () -> Union[str, unicode]
        pass

    def getParent(self):
        # type: () -> LaunchParent
        pass

    def getPlatformEdition(self):
        # type: () -> Union[str, unicode]
        pass

    def getProjectCacheChkFile(self):
        # type: () -> File
        pass

    def getProjectCacheFile(self):
        # type: () -> File
        pass

    def getProjectName(self):
        # type: () -> Union[str, unicode]
        pass

    def getResourceDir(self):
        # type: () -> File
        pass

    def getScopeCode(self):
        # type: () -> Union[str, unicode]
        pass

    def getTranslationDBLocation(self):
        # type: () -> File
        pass

    def getUserObject(self):
        # type: () -> bytearray
        pass

    def log(self, message, *args):
        # type: (Union[str, unicode], *Object) -> None
        pass

    def setAttribute(self, key, value):
        # type: (Union[str, unicode], Object) -> None
        pass

    def updateGatewayAddressListCache(self, addrs):
        # type: (List[GatewayAddress]) -> None
        pass

    def updateProjectCache(self, project):
        # type: (LaunchContext.WritableProject) -> None
        pass


class LaunchManifest(Object):

    class Jar(Object):
        def __init__(self, name, crc32, length):
            # type: (Union[str, unicode], long, long) -> None
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
            # type: () -> Union[str, unicode]
            return self._name

    class Module(Object):
        def __init__(self, name, build):
            # type: (Union[str, unicode], int) -> None
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
            # type: () -> Union[str, unicode]
            return self._name

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
        # type: () -> Union[str, unicode]
        pass

    def getJreVersion(self):
        # type: () -> Union[str, unicode]
        pass

    def getModules(self):
        # type: () -> Iterable[LaunchManifest.Module]
        pass

    def getPort(self):
        # type: () -> int
        pass

    def getScope(self):
        # type: () -> Union[str, unicode]
        pass

    def getThirdPartyScriptModulesHash(self):
        # type: () -> Union[str, unicode]
        pass

    def isEmpty(self):
        # type: () -> bool
        return True

    def isUseSsl(self):
        # type: () -> bool
        return True

    def newDiffAction(self, context):
        # type: (LaunchContextImpl) -> Any
        pass

    @staticmethod
    def readFrom(is_):
        # type: (InputStream) -> LaunchManifest
        pass

    def setJavaExecutable(self, javaExecutable):
        # type: (Union[str, unicode]) -> None
        pass

    def setUseCondensedDialogFont(self, useCondensedDialogFont):
        # type: (bool) -> None
        pass

    def storeTo(self, arg):
        # type: (Union[OutputStream, Writer]) -> None
        pass

    def useCondensedDialogFont(self):
        # type: () -> bool
        return True


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
        # type: () -> Union[str, unicode]
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
        # type: (Union[str, unicode]) -> None
        pass

    def setGlassPane(self, frameIcon):
        # type: (JComponent) -> None
        pass

    def shutdown(self):
        # type: () -> None
        raise NotImplementedError
