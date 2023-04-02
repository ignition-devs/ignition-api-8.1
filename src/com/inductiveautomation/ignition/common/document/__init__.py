__all__ = ["Document", "DocumentElement"]

from typing import Any

from java.lang import Object


class DocumentElement(Object):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(DocumentElement, self).__init__()


class Document(DocumentElement):
    def __init__(self, *args):
        # type: (*Any) -> None
        super(Document, self).__init__(*args)
