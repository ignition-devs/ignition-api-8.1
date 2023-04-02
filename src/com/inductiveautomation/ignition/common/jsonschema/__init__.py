from __future__ import print_function

__all__ = [
    "BaseJsonValidator",
    "ItemsValidator",
    "JsonSchema",
    "JsonType",
    "JsonValidator",
    "TypeValidator",
    "ValidationMessage",
]

from typing import Any, Dict, List, Optional, Set, Tuple

from com.inductiveautomation.ignition.common import JsonPath
from com.inductiveautomation.ignition.common.gson import JsonArray, JsonElement
from dev.thecesrom.helper.types import AnyStr
from java.io import InputStream
from java.lang import Enum, Object
from java.util.regex import Pattern


class JsonValidator(object):
    AT_ROOT = None  # type: AnyStr

    def validate(self, *args):
        # type: (Any) -> Set[ValidationMessage]
        raise NotImplementedError


class BaseJsonValidator(Object, JsonValidator):
    def __init__(self, *args):
        # type: (Any) -> None
        super(BaseJsonValidator, self).__init__()

    def asInt(self, element):
        # type: (JsonElement) -> int
        pass

    def validate(self, *args):
        # type: (Any) -> Set[ValidationMessage]
        pass


class ItemsValidator(BaseJsonValidator):
    PROPERTY = None  # type: AnyStr

    def __init__(self, *args):
        # type: (Any) -> None
        super(ItemsValidator, self).__init__(*args)

    def deriveDefaultArray(self, includeExample=None):
        # type: (Optional[bool]) -> JsonArray
        pass

    def findSchemaForIndex(self, index):
        # type: (int) -> Optional[JsonSchema]
        pass

    def getDefaultItem(
        self,
    ):
        # type: () -> Optional[JsonElement]
        pass

    def getSchemas(self):
        # type: () -> List[JsonSchema]
        pass

    def isBoundedSchema(self):
        # type: () -> Set[ValidationMessage]
        pass


class JsonSchema(BaseJsonValidator):
    IGNITION_SCHEMA_PATTERN = None  # type: Pattern
    IGNITION_SCHEMA_URN = None  # type: AnyStr

    def __init__(self, *args):
        # type: (Any) -> None
        super(JsonSchema, self).__init__(*args)

    def acceptsType(self, type):
        # type: (JsonType) -> bool
        return True

    def findAncestor(self):
        # type: () -> JsonSchema
        pass

    def findAncestorMatchingPath(self, matchingPath):
        # type: (AnyStr) -> Optional[JsonSchema]
        pass

    def findSchemaForPath(self, path):
        # type: (JsonPath) -> Optional[JsonSchema]
        pass

    def getChildDefaultValue(self, type):
        # type: (JsonType) -> Optional[JsonElement]
        pass

    def getDeclaredProperties(self):
        # type: () -> List[AnyStr]
        pass

    def getDefaultValue(self, includeExamples=None):
        # type: (Optional[bool]) -> JsonElement
        pass

    def getDescription(self):
        # type: () -> AnyStr
        pass

    def getDynamicSuggestionPath(self):
        # type: () -> AnyStr
        pass

    def getEnumChoices(self):
        # type: () -> Dict[AnyStr, JsonElement]
        pass

    def getExamples(self):
        # type: () -> List[JsonElement]
        pass

    def getExampleValue(self):
        # type: () -> Optional[JsonElement]
        pass

    def getExtension(self, key):
        # type: (AnyStr) -> Optional[JsonElement]
        pass

    def getFormat(self):
        # type: () -> AnyStr
        pass

    def getItemsValidator(self):
        # type: () -> ItemsValidator
        pass

    def getRefSchemaNode(self, ref=None):
        # type: (Optional[AnyStr]) -> JsonElement
        pass

    def getSchemasForItems(self):
        # type: () -> List[JsonSchema]
        pass

    def getSchemasForProperties(self):
        # type: () -> Dict[AnyStr, JsonSchema]
        pass

    def getSuggestions(self):
        # type: () -> Dict[AnyStr, JsonElement]
        pass

    def getTitle(self):
        # type: () -> AnyStr
        pass

    def getTypeValidator(self):
        # type: () -> TypeValidator
        pass

    def getVisibleWhenCondition(self):
        # type: () -> Optional[Tuple[AnyStr, List[JsonElement]]]
        pass

    def hasChildren(self):
        # type: () -> bool
        return True

    def isDeprecated(self):
        # type: () -> bool
        return True

    def isType(self, type):
        # type: (JsonType) -> bool
        return True

    @staticmethod
    def parse(stream):
        # type: (InputStream) -> JsonSchema
        pass


class JsonType(Enum):
    OBJECT = "object"
    ARRAY = "array"
    STRING = "string"
    NUMBER = "number"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    NULL = "null"
    DATASET = "dataset"
    DATE = "date"
    UNKNOWN = "unknown"

    @staticmethod
    def typeOf(element):
        # type: (JsonElement) -> JsonType
        pass

    @staticmethod
    def values():
        # type: () -> List[JsonType]
        pass


class ValidationMessage(Object):
    def getCode(self):
        # type: () -> AnyStr
        pass

    def getMessage(self):
        # type: () -> AnyStr
        pass

    def getPath(self):
        # type: () -> AnyStr
        pass

    def getType(self):
        # type: () -> AnyStr
        pass

    def setArguments(self, *args):
        # type: (AnyStr) -> None
        pass

    def setType(self, type):
        # type: (AnyStr) -> None
        pass

    class Builder(Object):
        def arguments(self, *args):
            # type: (AnyStr) -> ValidationMessage.Builder
            pass

        def build(self):
            # type: () -> ValidationMessage
            pass

        def code(self, code):
            # type: (AnyStr) -> ValidationMessage.Builder
            pass

        def format(self, format):
            # type: (AnyStr) -> ValidationMessage.Builder
            pass

        def path(self, path):
            # type: (AnyStr) -> ValidationMessage.Builder
            pass

        def type(self, type):
            # type: (AnyStr) -> ValidationMessage.Builder
            pass


class TypeValidator(BaseJsonValidator):
    def __init__(self, *args):
        # type: (Any) -> None
        super(TypeValidator, self).__init__(*args)

    def getAcceptedTypes(self):
        # type: () -> Set[JsonType]
        pass
