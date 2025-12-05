from typing import Union

from java.lang import Object
from java.util import EventObject

class PropertyChangeEvent(EventObject):
    def __init__(
        self,
        source: Object,
        propertyName: Union[str, unicode],
        oldValue: Object,
        newValue: Object,
    ) -> None: ...
    def getNewValue(self) -> Object: ...
    def getOldValue(self) -> Object: ...
    def getPropagationId(self) -> Object: ...
    def setPropagationId(self, propagationId: Object) -> None: ...

class PropertyChangeListener:
    def propertyChange(self, evt: PropertyChangeEvent) -> None: ...
