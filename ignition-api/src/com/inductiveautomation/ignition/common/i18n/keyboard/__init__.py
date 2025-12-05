from __future__ import print_function

from typing import Any, List, Optional, Union

from java.lang import Object


class KeyboardLayout(Object):
    alias = None  # type: Union[str, unicode]
    id = None  # type: Any
    labels = None  # type: Optional[Any]
    name = None  # type: Union[str, unicode]
    rows = None  # type: Optional[List[Any]]
    title = None  # type: Union[str, unicode]
    supportedLanguages = None  # type: Optional[List[Union[str, unicode]]]

    def __init__(
        self,
        id,  # type: Any
        name,  # type: Union[str, unicode]
        title,  # type: Union[str, unicode]
        alias,  # type: Union[str, unicode]
        rows=None,  # type: Optional[List[Any]]
        supportedLanguages=None,  # type: Optional[List[Union[str, unicode]]]
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
        # type: () -> Union[str, unicode]
        return self.alias

    def getId(self):
        # type: () -> Any
        return self.id

    def getLabels(self):
        # type: () -> Optional[Any]
        return self.labels

    def getName(self):
        # type: () -> Union[str, unicode]
        return self.name

    def getRows(self):
        # type: () -> Optional[List[Any]]
        return self.rows

    def getSupportedLanguages(self):
        # type: () -> Optional[List[Union[str, unicode]]]
        return self.supportedLanguages
