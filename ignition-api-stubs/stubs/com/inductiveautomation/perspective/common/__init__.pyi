from typing import Optional

from com.inductiveautomation.ignition.common.gson import Gson, JsonObject
from com.inductiveautomation.ignition.common.jsonschema import JsonSchema
from com.inductiveautomation.ignition.common.util import LoggerEx
from dev.coatl.helper.types import AnyStr
from java.lang import Object
from java.util.function import Consumer

class PerspectiveModule(Object):
    LOG_PREFIX: AnyStr
    META_SCHEMA: JsonSchema
    MODULE_ID: AnyStr
    SESSION_PROPS_SCHEMA: JsonSchema
    VIEW_SCHEMA: JsonSchema
    @staticmethod
    def createPerspectiveCompatibleGson(
        customize: Optional[Consumer] = ...,
    ) -> Gson: ...
    @staticmethod
    def defaultMetaProps() -> JsonObject: ...
    @staticmethod
    def defaultSessionProps() -> JsonObject: ...
    @staticmethod
    def defaultViewProps() -> JsonObject: ...
    @staticmethod
    def getLogger(name: AnyStr) -> LoggerEx: ...
