from typing import Optional, Union

from com.inductiveautomation.ignition.common.gson import Gson, JsonObject
from com.inductiveautomation.ignition.common.jsonschema import JsonSchema
from com.inductiveautomation.ignition.common.util import LoggerEx
from java.lang import Object
from java.util.function import Consumer

class PerspectiveModule(Object):
    LOG_PREFIX: Union[str, unicode]
    META_SCHEMA: JsonSchema
    MODULE_ID: Union[str, unicode]
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
    def getLogger(name: Union[str, unicode]) -> LoggerEx: ...
