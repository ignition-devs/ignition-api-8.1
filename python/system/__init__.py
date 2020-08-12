# Copyright (C) 2020
# Author: Cesar Roman
# Contact: thecesrom@gmail.com

"""The Ignition scripting API, which is available under the module
name "system", is full of functions that are useful when designing
projects in Ignition. From running database queries, manipulating
components, to exporting data, scripting functions can help. Some of
these functions only work in the Gateway scope, and other only work
in the Client scope, while the rest will work in any scope.

Additional information on scripting Ignition can be found in the
Scripting section."""

from abc import ABCMeta, abstractmethod

from java.lang import Object
from javax.swing import JInternalFrame


class Aggregate(ABCMeta):
    """This interface defines an aggregation function used by the
    history query system. Different types of history providers may
    support different Aggregate functions, and may define new types of
    aggregates. The name and description are for informational
    purposes, aggregates are only identified by their id (name and
    description should not be taken into account).

    The general implementation class is AggregateInfo. Common or "well
    known" aggregates are defined in the AggregationMode enum. The
    system works like this for historical reasons, previous to 7.7
    only the AggregationMode aggregates were used. After, with the
    introduction of history providers as an extension point, new
    providers could define any aggregation function.
    """

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def getDesc(cls):
        pass

    @abstractmethod
    def getId(cls):
        pass

    @abstractmethod
    def getName(cls):
        pass


class BrowseResults(Object):
    """BrowseResults class."""

    def getContinuationPoint(self):
        pass

    def getResultQuality(self):
        pass

    def getResults(self):
        pass

    def getReturnedSize(self):
        pass

    def getTotalAvailableSize(self):
        pass

    def setContinuationPoint(self, continuationPoint):
        pass

    def setResultQuality(self, value):
        pass

    def setResults(self, results):
        pass

    def setTotalAvailableResults(self, totalAvailableResults):
        pass


class EventObject(Object):
    """EventObject object."""
    pass


class FPMIWindow(JInternalFrame):
    """FPMIWindow object."""
    # Fields.
    CACHE_ALWAYS = 2
    CACHE_AUTO = 0
    CACHE_NEVER = 1
    DOCK_EAST = 2
    DOCK_FLOAT = 0
    DOCK_NORTH = 2
    DOCK_SOUTH = 4
    DOCK_WEST = 3
    PARENT_WINDOW_NAME = '_parent'
    SHOW_ALWAYS = 0
    SHOW_NEVER = 1
    SHOW_MAXIMIZED = 2

    def getPath(self):
        print self
        return 'Path/To/Window'

    def getRootContainer(self):
        print self


class INavUtilities(ABCMeta):
    """Parent interface to coordinate the functions between
    NavUtilities and NavUtilitiesDispatcher."""

    def __new__(mcs, *args, **kwargs):
        pass

    @abstractmethod
    def centerWindow(cls, arg):
        pass

    @abstractmethod
    def closeParentWindow(cls, event):
        pass

    @abstractmethod
    def closeWindow(cls, arg):
        pass

    @abstractmethod
    def getCurrentWindow(cls):
        pass

    @abstractmethod
    def goBack(cls):
        pass

    @abstractmethod
    def goForward(cls):
        pass

    @abstractmethod
    def goHome(cls):
        pass

    @abstractmethod
    def openWindow(cls, *args):
        pass

    @abstractmethod
    def openWindowImpl(cls, path, params, openAdditional):
        pass

    @abstractmethod
    def openWindowInstance(cls, *args):
        pass

    @abstractmethod
    def swapTo(cls, *args):
        pass

    @abstractmethod
    def swapWindow(cls, *args):
        pass


class NavUtilities(INavUtilities):
    """This class contains the actual implementation for the methods
    mounted under system.nav.*, but it is not actually directly
    mounted in the script manager because there is a separate instance
    of this class for each desktop instance."""

    def centerWindow(self, arg):
        pass

    def closeParentWindow(self, event):
        pass

    def closeWindow(self, arg):
        pass

    def getCurrentWindow(self):
        pass

    def goBack(self):
        pass

    def goForward(self):
        pass

    def goHome(self):
        pass

    def openWindow(self, *args):
        pass

    def openWindowImpl(self, path, params, openAdditional):
        pass

    def openWindowInstance(self, *args):
        pass

    def swapTo(self, *args):
        pass

    def swapWindow(self, *args):
        pass


class QualifiedValue(object):
    """Represents a value with a DataQuality & timestamp attached to
    it."""

    def __init__(self,
                 value=None,
                 quality=None,
                 timestamp=None):
        self.value = value
        self.quality = quality
        self.timestamp = timestamp

    def derive(self, diagnosticMessage):
        pass

    def equals(self, value, includeTimestamp):
        pass

    def getQuality(self):
        pass

    def getTimestamp(self):
        pass

    def getValue(self):
        pass


class Quality(object):
    def getDescription(self):
        pass

    def getLevel(self):
        pass

    def getName(self):
        pass

    def getQualityCode(self):
        pass

    def isGood(self):
        pass


class ReadResult(Object):
    pass


class UIResponse(Object):
    def __init__(self, locale='en'):
        super(UIResponse, self).__init__()
        self.locale = locale

    def attempt(self, method):
        pass

    def error(self, message, args):
        pass

    def getErrors(self):
        pass

    def getInfos(self):
        pass

    def getLocale(self):
        pass

    def getWarns(self):
        pass

    def info(self, message, args):
        pass

    def warn(self, message, args):
        pass

    def wrap(self, locale, fx):
        pass
