__all__ = ["PerspectiveModule"]

from typing import Optional, Union

from java.lang import Object
from java.util.function import Consumer

from com.inductiveautomation.ignition.common.gson import Gson, JsonObject
from com.inductiveautomation.ignition.common.jsonschema import JsonSchema
from com.inductiveautomation.ignition.common.util import LoggerEx


class PerspectiveModule(Object):
    LOG_PREFIX = None  # type: Union[str, unicode]
    META_SCHEMA = None  # type: JsonSchema
    MODULE_ID = None  # type: Union[str, unicode]
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
        # type: (Union[str, unicode]) -> LoggerEx
        pass
