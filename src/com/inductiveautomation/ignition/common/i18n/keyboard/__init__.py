from __future__ import print_function

from typing import Any, List, Optional

from dev.thecesrom.helper.types import AnyStr
from java.lang import Object


class KeyboardLayout(Object):
    alias = None  # type: AnyStr
    id = None  # type: Any
    labels = None  # type: Optional[Any]
    name = None  # type: AnyStr
    rows = None  # type: Optional[List[Any]]
    title = None  # type: AnyStr
    supportedLanguages = None  # type: Optional[List[AnyStr]]

    def __init__(
        self,
        id,  # type: Any
        name,  # type: AnyStr
        title,  # type: AnyStr
        alias,  # type: AnyStr
        rows=None,  # type: Optional[List[Any]]
        supportedLanguages=None,  # type: Optional[List[AnyStr]]
        labels=None,  # type: Optional[Any]
    ):
        super(KeyboardLayout, self).__init__()
        self.id = id
        self.name = name
        self.title = title
        self.alias = alias
        self.rows = rows
        self.supportedLanguages = supportedLanguages
        self.labels = labels

    def getAlias(self):
        # type: () -> AnyStr
        return self.alias

    def getId(self):
        # type: () -> Any
        return self.id

    def getLabels(self):
        # type: () -> Optional[Any]
        return self.labels

    def getName(self):
        # type: () -> AnyStr
        return self.name

    def getRows(self):
        # type: () -> Optional[List[Any]]
        return self.rows

    def getSupportedLanguages(self):
        # type: () -> Optional[List[AnyStr]]
        return self.supportedLanguages
