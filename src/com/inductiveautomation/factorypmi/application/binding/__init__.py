__all__ = ["VisionClientContext"]

from com.inductiveautomation.factorypmi.application import VisionDesktop
from com.inductiveautomation.factorypmi.application.model import TemplateManager
from com.inductiveautomation.factorypmi.application.script.builtin import (
    ClientDatasetUtilities,
    ClientSystemUtilities,
    NavUtilities,
    WindowUtilities,
)
from com.inductiveautomation.factorypmi.application.sqltags.project import (
    ProjectTagManager,
)


class VisionClientContext(object):
    def getDatasetUtil(self):
        # type: () -> ClientDatasetUtilities
        raise NotImplementedError

    def getGuiUtil(self):
        # type: () -> WindowUtilities
        raise NotImplementedError

    def getNavUtil(self):
        # type: () -> NavUtilities
        raise NotImplementedError

    def getPrimaryDesktop(self):
        # type: () -> VisionDesktop
        raise NotImplementedError

    def getProjectTags(self):
        # type: () -> ProjectTagManager
        raise NotImplementedError

    def getSystemUtil(self):
        # type: () -> ClientSystemUtilities
        raise NotImplementedError

    def getTemplateManager(self):
        # type: () -> TemplateManager
        raise NotImplementedError

    def getUpdateBase(self):
        # type: () -> int
        raise NotImplementedError
