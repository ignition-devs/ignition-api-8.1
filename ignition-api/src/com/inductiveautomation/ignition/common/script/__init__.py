from __future__ import print_function

__all__ = ["ScriptFunction", "ScriptManager"]

from typing import Any, List, Mapping, Set, Union

from java.io import OutputStream
from java.lang import Class, Object
from java.util import UUID

from com.codahale.metrics import Timer
from com.inductiveautomation.ignition.common.script.hints import ScriptFunctionHint
from org.python.core import PyObject, PyStringMap, PySystemState

HintsMap = Mapping[Union[str, unicode], List[ScriptFunctionHint]]


class ScriptFunction(object):
    def invoke(self, *args):
        # type: (*Any) -> PyObject
        raise NotImplementedError


class ScriptManager(Object):

    class ExecutionInfo(Object):
        description = None  # type: Union[str, unicode]
        startTime = None  # type: long
        threadId = None  # type: long

    def __init__(self, contextName, pathToExternalLibs):
        # type: (Union[str, unicode], Union[str, unicode]) -> None
        super(ScriptManager, self).__init__()
        print(contextName, pathToExternalLibs)

    def addGlobalVariable(self, name, value):
        # type: (Union[str, unicode], PyObject) -> None
        pass

    def addScriptModule(self, *args):
        # type: (*Any) -> None
        pass

    def addStaticFields(self, path, clazz):
        # type: (Union[str, unicode], Class) -> None
        pass

    def addStdErrStream(self, os):
        # type: (OutputStream) -> None
        pass

    def addStdOutStream(self, os):
        # type: (OutputStream) -> None
        pass

    @staticmethod
    def asynchInit(pathToExternalLibs=None):
        # type: (Union[str, unicode, None]) -> None
        pass

    def beginCompileTimer(self):
        # type: () -> Timer.Context
        pass

    def clearAppModule(self):
        # type: () -> None
        pass

    def clearModule(self, moduleName):
        # type: (Union[str, unicode]) -> None
        pass

    def clearProjectScriptModules(self):
        # type: () -> None
        pass

    def clearThirdPartyModules(self):
        # type: () -> None
        pass

    def compileFunction(self, *args):
        # type: (*Any) -> ScriptFunction
        pass

    def createLocalsMap(self):
        # type: () -> PyStringMap
        pass

    @staticmethod
    def createUtf8PySystemState(stdOut, stdErr):
        # type: (OutputStream, OutputStream) -> PySystemState
        pass

    @staticmethod
    def executingScripts():
        # type: () -> Set[ScriptManager.ExecutionInfo]
        pass

    def getCompileTimer(self):
        # type: () -> Timer
        pass

    def getExecutionTimer(self):
        # type: () -> Timer
        pass

    def getGlobals(self):
        # type: () -> PyStringMap
        pass

    def getHintsMap(self):
        # type: () -> HintsMap
        pass

    def getModules(self):
        # type: () -> PyStringMap
        pass

    def getUUID(self):
        # type: () -> UUID
        pass

    @staticmethod
    def interrupt(threadId):
        # type: (long) -> None
        pass

    @staticmethod
    def main(*args):
        # type: (*Union[str, unicode]) -> None
        pass

    def removeStdErrStream(self, os):
        # type: (OutputStream) -> None
        pass

    def removeStdOutStream(self, os):
        # type: (OutputStream) -> None
        pass

    def runCode(self, *args):
        # type: (*Any) -> None
        pass

    def runFunction(self, *args):
        # type: (*Any) -> PyObject
        pass

    def setContextName(self, name):
        # type: (Union[str, unicode]) -> None
        pass

    def setPaused(self, paused):
        # type: (bool) -> None
        pass

    def shutdown(self):
        # type: () -> None
        pass

    def validatePackageName(self, newName):
        # type: (Union[str, unicode]) -> None
        pass
