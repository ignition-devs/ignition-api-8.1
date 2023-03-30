__all__ = [
    "ClientContext",
    "ClientLocalizationManager",
    "DesktopListener",
    "LocaleListener",
]

from typing import Any, List

from com.google.common.eventbus import EventBus
from com.inductiveautomation.ignition.client.launch import LaunchContext
from com.inductiveautomation.ignition.client.util.gui.progress import (
    ClientProgressManager,
)
from com.inductiveautomation.ignition.common.db.namedquery import NamedQueryManager
from com.inductiveautomation.ignition.common.execution import ExecutionManager
from com.inductiveautomation.ignition.common.expressions import FunctionFactory
from com.inductiveautomation.ignition.common.i18n.translation import TranslationMap
from com.inductiveautomation.ignition.common.licensing import LicenseState
from com.inductiveautomation.ignition.common.logging import LogFilterSettings
from com.inductiveautomation.ignition.common.model import CommonContext, EdgeEdition
from com.inductiveautomation.ignition.common.modules import ModuleInfo
from com.inductiveautomation.ignition.common.project import Project
from com.inductiveautomation.ignition.common.script import ScriptManager
from com.inductiveautomation.ignition.common.tags.model import TagManager
from com.inductiveautomation.ignition.common.xmlserialization.deserialization import (
    XMLDeserializer,
)
from dev.thecesrom.helper.types import AnyStr
from java.beans import PropertyChangeListener
from java.lang import Object
from java.util import Locale
from javax.swing import RootPaneContainer
from org.apache.log4j import Logger


class ClientContext(CommonContext):
    def addPropertyChangeListener(self, *args):
        # type: (*Any) -> None
        raise NotImplementedError

    def createDeserializer(self):
        # type: () -> XMLDeserializer
        raise NotImplementedError

    def desearilize(self, data, log):
        # type: (bytearray, Logger) -> Object
        raise NotImplementedError

    def getAuthProfileName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getDefaultDataSourceName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getDefaultTagProviderName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getEdgeEditions(self):
        # type: () -> List[EdgeEdition]
        raise NotImplementedError

    def getEventBus(self):
        # type: () -> EventBus
        raise NotImplementedError

    def getExecutionManager(self):
        # type: () -> ExecutionManager
        raise NotImplementedError

    def getExpressionFunctionFactory(self):
        # type: () -> FunctionFactory
        raise NotImplementedError

    def getLaunchContext(self):
        # type: () -> LaunchContext
        raise NotImplementedError

    def getLicenseState(self, moduleId):
        # type: (AnyStr) -> LicenseState
        raise NotImplementedError

    def getLocalizationManager(self):
        # type: () -> ClientLocalizationManager
        raise NotImplementedError

    def getLoggingManager(self):
        # type: () -> LogFilterSettings
        raise NotImplementedError

    def getModule(self, id_):
        # type: (AnyStr) -> Object
        raise NotImplementedError

    def getModules(self):
        # type: () -> List[ModuleInfo]
        raise NotImplementedError

    def getNamedQueryManager(self):
        # type: () -> NamedQueryManager
        raise NotImplementedError

    def getProgressManager(self):
        # type: () -> ClientProgressManager
        raise NotImplementedError

    def getProject(self):
        # type: () -> Project
        raise NotImplementedError

    def getProjectName(self):
        # type: () -> AnyStr
        raise NotImplementedError

    def getRootPaneContainer(self):
        # type: () -> RootPaneContainer
        raise NotImplementedError

    def getScriptManager(self):
        # type: () -> ScriptManager
        raise NotImplementedError

    def getTagManager(self):
        # type: () -> TagManager
        raise NotImplementedError

    def getTagPollRate(self):
        # type: () -> int
        raise NotImplementedError

    def getUIEventBus(self):
        # type: () -> EventBus
        raise NotImplementedError

    def removePropertyChangeListened(self, *args):
        # type: (*Any) -> None
        raise NotImplementedError


class DesktopListener(object):
    pass


class LocaleListener(object):
    def localeChanged(self, newLocale):
        # type: (Locale) -> None
        raise NotImplementedError


class ClientLocalizationManager(Object):
    def addLocaleListener(self, listener):
        # type: (LocaleListener) -> None
        raise NotImplementedError

    def addPropertyChangeListener(self, propertyName, listener):
        # type: (AnyStr, PropertyChangeListener) -> None
        pass

    def get(self, locale, key):
        # type: (Locale, AnyStr) -> AnyStr
        raise NotImplementedError

    def getAvailableLocales(self):
        # type: () -> List[Locale]
        raise NotImplementedError

    def getCurrentLocale(self):
        # type: () -> Locale
        raise NotImplementedError

    def getPreviewLocale(self):
        # type: () -> Locale
        raise NotImplementedError

    def getStrict(self, *args):
        # type: (*Any) -> AnyStr
        raise NotImplementedError

    def getString(self, key):
        # type: (AnyStr) -> AnyStr
        raise NotImplementedError

    def getStringForBundleKey(self, bundlekey):
        # type: (AnyStr) -> AnyStr
        raise NotImplementedError

    def getTranslationsFor(self, key):
        # type: (AnyStr) -> TranslationMap
        raise NotImplementedError

    def isTranslationEnabled(self):
        # type: () -> bool
        raise NotImplementedError

    def removeLocaleListener(self, listener):
        # type: (LocaleListener) -> None
        raise NotImplementedError

    def removePropertyChangeListener(self, propertyName, listener):
        # type: (AnyStr, PropertyChangeListener) -> None
        pass

    def resetLocale(self):
        # type: () -> None
        raise NotImplementedError

    def setCurrentLocale(self, locale):
        # type: (Locale) -> None
        raise NotImplementedError
