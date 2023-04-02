__all__ = ["PerspectiveModule"]

from typing import Optional

from com.inductiveautomation.ignition.common.gson import Gson, JsonObject
from com.inductiveautomation.ignition.common.jsonschema import JsonSchema
from com.inductiveautomation.ignition.common.util import LoggerEx
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from java.util.function import Consumer


class PerspectiveModule(Object):
    LOG_PREFIX = None  # type: AnyStr
    META_SCHEMA = None  # type: JsonSchema
    MODULE_ID = None  # type: AnyStr
    SESSION_PROPS_SCHEMA = None  # type: JsonSchema
    VIEW_SCHEMA = None  # type: JsonSchema

    @staticmethod
    def createPerspectiveCompatibleGson(customize=None):
        # type: (Optional[Consumer]) -> Gson
        pass

    @staticmethod
    def defaultMetaProps():
        # type: () -> JsonObject
        pass

    @staticmethod
    def defaultSessionProps():
        # type: () -> JsonObject
        pass

    @staticmethod
    def defaultViewProps():
        # type: () -> JsonObject
        pass

    @staticmethod
    def getLogger(name):
        # type: (AnyStr) -> LoggerEx
        pass
