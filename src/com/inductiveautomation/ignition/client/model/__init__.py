class ClientContext(object):
    def addPropertyChangeListener(self, *args):
        raise NotImplementedError

    def desearilize(self, data, log):
        raise NotImplementedError

    def getAuthProfileName(self):
        raise NotImplementedError

    def getDefaultDataSourceName(self):
        raise NotImplementedError

    def getDefaultTagProviderName(self):
        raise NotImplementedError

    def getExecutionManager(self):
        raise NotImplementedError

    def getLaunchContext(self):
        raise NotImplementedError

    def getLocalizationManager(self):
        raise NotImplementedError

    def getModules(self):
        raise NotImplementedError

    def getNamedQueryManager(self):
        raise NotImplementedError

    def getProgressManager(self):
        raise NotImplementedError

    def getProject(self):
        raise NotImplementedError

    def getProjectName(self):
        raise NotImplementedError

    def getRootPaneContainer(self):
        raise NotImplementedError

    def getTagManager(self):
        raise NotImplementedError

    def getTagPollRate(self):
        raise NotImplementedError

    def getUIEventBus(self):
        raise NotImplementedError

    def removePropertyChangeListened(self, *args):
        raise NotImplementedError
