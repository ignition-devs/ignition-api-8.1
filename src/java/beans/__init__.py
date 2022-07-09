from java.lang import Object, String
from java.util import EventObject


class PropertyChangeEvent(EventObject):
    def __init__(self, source, propertyName, oldValue, newValue):
        # type: (Object, String, Object, Object) -> None
        super(PropertyChangeEvent, self).__init__(source)
        self._newValue = newValue
        self._oldValue = oldValue
        self._propertyName = propertyName
        self._propagationId = Object()

    def getNewValue(self):
        # type: () -> Object
        return self._newValue

    def getOldValue(self):
        # type: () -> Object
        return self._oldValue

    def getPropagationId(self):
        # type: () -> Object
        return self._propagationId

    def setPropagationId(self, propagationId):
        # type: (Object) -> None
        self._propagationId = propagationId


class PropertyChangeListener(object):
    def propertyChange(self, evt):
        # type: (PropertyChangeEvent) -> None
        raise NotImplementedError
