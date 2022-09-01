from typing import Any

from java.awt import AWTEvent, Component, Container
from java.lang import Object


class AncestorEvent(AWTEvent):
    ANCESTOR_ADDED = None  # type: int
    ANCESTOR_MOVED = None  # type: int
    ANCESTOR_REMOVED = None  # type: int

    def __init__(self, source, id, ancestor, ancestorParent):
        # type: (Component, int, Container, Container) -> None
        self._ancestor = ancestor
        self._ancestorParent = ancestorParent
        self._id = id
        self._source = source
        super(AncestorEvent, self).__init__(source, id)

    def getAncestor(self):
        # type: () -> Container
        return self._ancestor

    def getAncestorParent(self):
        # type: () -> Container
        return self._ancestorParent

    def getComponent(self):
        # type: () -> Component
        pass


class AncestorListener(object):
    def ancestorAdded(self, event):
        # type: (AncestorEvent) -> None
        raise NotImplementedError

    def ancestorMoved(self, event):
        # type: (AncestorEvent) -> None
        raise NotImplementedError

    def ancestorRemoved(self, event):
        # type: (AncestorEvent) -> None
        raise NotImplementedError
