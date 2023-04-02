from __future__ import print_function

__all__ = ["ScriptFunction", "ScriptManager"]

from copy import PyStringMap
from typing import Any, List, Mapping, Optional, Set

from com.codahale.metrics import Timer
from com.inductiveautomation.ignition.common.script.hints import ScriptFunctionHint
from dev.thecesrom.helper.types import AnyStr
from java.io import OutputStream
from java.lang import Class, Object
from java.util import UUID
from org.python.core import PyObject, PySystemState


class ScriptFunction(object):
    def invoke(self, *args):
        # type: (*Any) -> PyObject
        raise NotImplementedError


class ScriptManager(Object):
    def __init__(self, contextName, pathToExternalLibs):
        # type: (AnyStr, AnyStr) -> None
        super(ScriptManager, self).__init__()
        print(contextName, pathToExternalLibs)

    def addGlobalVariable(self, name, value):
        # type: (AnyStr, PyObject) -> None
        pass

    def addScriptModule(self, *args):
        # type: (*Any) -> None
        pass

    def addStaticFields(self, path, clazz):
        # type: (AnyStr, Class) -> None
        pass

    def addStdErrStream(self, os):
        # type: (OutputStream) -> None
        pass

    def addStdOutStream(self, os):
        # type: (OutputStream) -> None
        pass

    @staticmethod
    def asynchInit(pathToExternalLibs=None):
        # type: (Optional[AnyStr]) -> None
        pass

    def beginCompileTimer(self):
        # type: () -> Timer.Context
        pass

    def clearAppModule(self):
        # type: () -> None
        pass

    def clearModule(self, moduleName):
        # type: (AnyStr) -> None
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
        # type: () -> Mapping[AnyStr, List[ScriptFunctionHint]]
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
        # type: (*AnyStr) -> None
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
        # type: (AnyStr) -> None
        pass

    def setPaused(self, paused):
        # type: (bool) -> None
        pass

    def shutdown(self):
        # type: () -> None
        pass

    def validatePackageName(self, newName):
        # type: (AnyStr) -> None
        pass

    class ExecutionInfo(Object):
        description = None  # type: AnyStr
        startTime = None  # type: long
        threadId = None  # type: long
